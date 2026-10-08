from PySide6.QtCore import QThread, Signal, QFileInfo, Qt

from PySide6.QtWidgets import QWidget, QFileIconProvider, QStyle
from PySide6.QtGui import QFontMetrics, QIcon


# Imports for main window.
from .ui.ui_list_item_widget import Ui_list_item_widget


import re
import time
import subprocess
from datetime import datetime

from .global_config import save_global_config
from .options import (
    # main_window,
    global_config,
    temp_global_config,
    # profile_settings_window,
    client_bin_path,
    gui_settings,
    version,
)

from .utils.utils import humanize_file_size, shorten_path


import logging

# from logger import logger
from .global_config import DIR_PATH, PROFILES_FILE


class WorkerThread(QThread):
    """
    Constructs a thread, which can start, monitor and stop OneDrive process.
    """

    update_credentials = Signal(str)
    update_progress_new = Signal(dict, str)
    update_profile_status = Signal(dict, str)
    trigger_resync = Signal(str)
    trigger_big_delete = Signal(str)
    remove_worker = Signal(str)
    clear_warning = Signal(str)
    browser_login_required = Signal(str)
    finalize_stalled_tasks = Signal(str)
    notify_failed_sync = Signal(str, int)

    def __init__(self, profile, options=""):
        super(WorkerThread, self).__init__()
        logging.info(f"[GUI] Starting worker for profile {profile}")

        self.config_file = global_config[profile]["config_file"]
        self.config_dir = re.search(r"(.+)/.+$", self.config_file)
        logging.info(f"[GUI] OneDrive config file: {self.config_file}")
        logging.info(f"[GUI] OneDrive config dir: {self.config_dir}")
        self._command = f"exec {client_bin_path} --confdir='{self.config_dir.group(1)}' --monitor -v {options}"
        logging.info(f"[GUI] Monitoring command: '{self._command}'")
        self.profile_name = profile

    def stop_worker(self):
        logging.info(f"[{self.profile_name}] Waiting for worker to finish...")
        while self.onedrive_process.poll() is None:
            self.onedrive_process.kill()

        logging.info(f"[{self.profile_name}] Quitting thread")
        self.quit()
        self.wait()

        self.remove_worker.emit(self.profile_name)

    def run(self, resync=False):
        """
        Starts OneDrive and sends signals to GUI based on parsed information.
        """

        self.file_name = None
        self.file_path = None

        self.tasks = [
            "Downloading file",
            "Downloading new file",
            "Uploading file",
            "Uploading new file",
            "Uploading modified file",
            "Downloading modified file",
            "Deleting item",  # File deleted locally and then removed in the cloud
            "Deleting local file",  # File deleted in the cloud and then removed locally
            "Moving this local file",  # File deleted in the cloud and then moved to recycling bin locally
        ]

        self.profile_status = {
            "status_message": "",
            "free_space": "",
            "account_type": "",
        }

        # Track pending error for multi-line error messages
        self.pending_error = None
        self.pending_error_path = None

        # Track per-file error messages so the GUI can show why each file failed
        self.file_errors = {}
        self.last_unattributed_error = None
        self.last_error_time = 0.0

        # Signature of the last notified failure list, to avoid repeating
        # identical tray notifications on every sync cycle
        self._last_notified_failures = None

        # Track failed files for detailed error reporting
        self.failed_files = []
        self.failed_files_count = 0
        self.collecting_failed_files = False  # Flag to indicate we're collecting failed file lines

        # Track whether we're waiting for the user to complete login in their browser
        self.awaiting_browser_login = False

        self.msg = ""
        self.profile_status["status_message"] = "OneDrive sync is starting..."
        self.update_profile_status.emit(self.profile_status, self.profile_name)

        self.onedrive_process = subprocess.Popen(
            self._command + "--resync" if resync else self._command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            shell=True,
            universal_newlines=True,
            encoding="utf-8",
            errors="replace",
        )

        while self.onedrive_process.poll() is None:
            if self.onedrive_process.stdout:
                # Capture stdout and stderr from OneDrive process.
                self.read_stdout()

        # This helps monitor stdout and stderr for extra second after onedrive process stops. I could not find a smarter way.
        timeout = time.time() + 1
        while True:
            if self.onedrive_process.stderr:
                self.read_stderr()

            if time.time() > timeout:
                break

    def _emit_error_status(self, full_error_message):
        """Emit a short, categorized status message. The full error message is kept
        for the warning icon tooltip, and per-file details are shown when hovering
        the failed files in the file operation list."""
        lower = full_error_message.lower()

        if "name is too long" in lower:
            short_error = "File or folder name too long"
        elif "case-insensitive match" in lower:
            short_error = "File name conflicts with an existing file on OneDrive"
        elif "permission denied" in lower:
            short_error = "File cannot be read (permission denied)"
        elif "no space left" in lower or "insufficient space" in lower:
            short_error = "Not enough disk space"
        else:
            # Unknown error: keep the beginning of the message on a single line
            short_error = full_error_message if len(full_error_message) <= 90 else full_error_message[:87] + "..."

        self.profile_status["status_message"] = f"Error: {short_error}"
        self.profile_status["error_message"] = full_error_message  # Full error for tooltip
        self.update_profile_status.emit(self.profile_status, self.profile_name)

    def _emit_failed_files_status(self):
        """Format and emit status for failed file uploads/downloads."""
        if not self.failed_files and self.failed_files_count == 0:
            return

        # Use the actual count from the summary line if available, otherwise use list length
        count = self.failed_files_count if self.failed_files_count > 0 else len(self.failed_files)

        # Status message (truncated for main UI)
        status_msg = f"Sync completed with {count} failed file(s)"

        # Tooltip message (detailed list)
        tooltip_lines = [f"Failed items to upload to/from Microsoft OneDrive: {count}"]
        tooltip_lines.extend(self.failed_files)

        # If there are more failures than we captured, add indicator
        if count > len(self.failed_files):
            remaining = count - len(self.failed_files)
            tooltip_lines.append(f"... and {remaining} more")

        full_tooltip = "\n".join(tooltip_lines)

        self.profile_status["status_message"] = status_msg
        self.profile_status["error_message"] = full_tooltip
        self.update_profile_status.emit(self.profile_status, self.profile_name)

        # Raise a tray notification so the user learns about the failures even
        # when the GUI window is minimized - but only when the set of failing
        # files changed, so persistent failures do not spam on every cycle.
        if full_tooltip != self._last_notified_failures:
            self._last_notified_failures = full_tooltip
            self.notify_failed_sync.emit(self.profile_name, count)

    def read_stdout(self):
        stdout = self.onedrive_process.stdout.readline().strip()
        if stdout != "":
            logging.debug(f"[{self.profile_name}] " + stdout)

            # Check if we have a pending error from previous line that wasn't followed by "Error Message:"
            # The onedrive client emits multi-line error blocks like:
            #   ERROR: <summary>
            #   Calling Function:  <...>
            #   Path:              <...>
            #   Error Message:     <...>
            #   Disk Space (CWD):  <...>
            # so known continuation lines must not trigger an early flush of the pending error.
            error_continuation_markers = ("Calling Function:", "Path:", "Disk Space")
            if (
                self.pending_error
                and "Error Message:" not in stdout
                and not any(marker in stdout for marker in error_continuation_markers)
            ):
                # Emit the pending error since the next line didn't continue it
                self._emit_error_status(self.pending_error)
                self.pending_error = None
                self.pending_error_path = None

            # Check if we were collecting failed files and this line is not a "Failed to" line
            if self.collecting_failed_files and "Failed to upload:" not in stdout and "Failed to download:" not in stdout:
                # We're done collecting, emit the status
                self._emit_failed_files_status()
                self.collecting_failed_files = False

            if "Calling Function: testNetwork()" in stdout:
                self.msg = "Testing network connection to Microsoft OneDrive Service..."
                logging.warning(f"[{self.profile_name}] {self.msg}")
                self.profile_status["status_message"] = self.msg
                self.update_profile_status.emit(self.profile_status, self.profile_name)

            elif "authorise this application by" in stdout.lower() or "--reauth and re-authorise this client" in stdout:
                self.onedrive_process.kill()
                self.msg = "OneDrive login is required."
                logging.warning(f"[{self.profile_name}] {self.msg}")
                self.profile_status["status_message"] = self.msg
                self.update_profile_status.emit(self.profile_status, self.profile_name)
                self.update_credentials.emit(self.profile_name)

            elif "Opening the Microsoft authorisation URL in your default browser" in stdout:
                # New default auth method (client v2.5.11+): the client itself opens the
                # system browser and runs a local loopback listener for the OAuth response,
                # so the browser window may open in the background and go unnoticed.
                self.awaiting_browser_login = True
                self.msg = "Action required: please complete the OneDrive login\nthat just opened in your web browser."
                logging.warning(f"[{self.profile_name}] {self.msg}")
                self.profile_status["status_message"] = self.msg
                self.update_profile_status.emit(self.profile_status, self.profile_name)
                self.browser_login_required.emit(self.profile_name)

            elif self.awaiting_browser_login and "The OneDrive API was initialised successfully" in stdout:
                self.awaiting_browser_login = False
                self.msg = "OneDrive login successful."
                logging.info(f"[{self.profile_name}] {self.msg}")
                self.profile_status["status_message"] = self.msg
                self.update_profile_status.emit(self.profile_status, self.profile_name)

            elif any(
                msg in stdout
                for msg in [
                    "Sync with Microsoft OneDrive is complete",
                    "Total number of local file(s) added or changed",
                    "No changes or items that can be applied were discovered",
                ]
            ):
                if self.failed_files or self.failed_files_count:
                    # This sync cycle had files that failed to sync - keep the
                    # "completed with errors" state (status message, warning icon
                    # and tray) until a cycle completes without any failures, so
                    # the user stays aware of the background failures.
                    count = self.failed_files_count if self.failed_files_count > 0 else len(self.failed_files)
                    logging.warning(f"[{self.profile_name}] Sync finished with {count} failed item(s) - keeping error state")
                else:
                    # Clear warnings when sync completes without errors
                    self.profile_status.pop("error_message", None)
                    self.clear_warning.emit(self.profile_name)
                    self.msg = "OneDrive sync is complete."
                    logging.info(f"[{self.profile_name}] {self.msg}")
                    self.profile_status["status_message"] = self.msg
                    self.update_profile_status.emit(self.profile_status, self.profile_name)
                # Finalize any transfers that never reported completion during the cycle.
                self.finalize_stalled_tasks.emit(self.profile_name)

            elif "Sync with Microsoft OneDrive has completed, however there are items that failed to sync" in stdout:
                self.msg = "OneDrive sync completed with errors."
                logging.warning(f"[{self.profile_name}] {self.msg}")
                self.profile_status["status_message"] = self.msg
                self.update_profile_status.emit(self.profile_status, self.profile_name)
                # Finalize any transfers that never reported completion during the cycle.
                self.finalize_stalled_tasks.emit(self.profile_name)

            elif "Remaining Free Space" in stdout:
                try:
                    self.free_space_bytes = re.search(r"([0-9]+)\sbytes", stdout).group(1)
                    self.free_space_human = str(humanize_file_size(int(self.free_space_bytes)))
                except:
                    self.free_space_human = "Not Available"

                logging.info(f"[{self.profile_name}] Free Space: {self.free_space_human}")
                self.profile_status["free_space"] = f"{self.free_space_human}"
                self.update_profile_status.emit(self.profile_status, self.profile_name)

                # Update profile file with Free Space
                global_config[self.profile_name]["free_space"] = self.free_space_human
                temp_global_config[self.profile_name]["free_space"] = self.free_space_human
                # save_global_config()

            elif "Account Type" in stdout:
                self.account_type = re.search(r"\s(\w+)$", stdout).group(1)
                self.profile_status["account_type"] = self.account_type.capitalize()
                logging.info(f"[{self.profile_name}] Account type: {self.account_type}")
                self.update_profile_status.emit(self.profile_status, self.profile_name)

                # Update profile file with account type
                global_config[self.profile_name]["account_type"] = self.account_type.capitalize()
                temp_global_config[self.profile_name]["account_type"] = self.account_type.capitalize()
                # save_global_config()

            elif "Initializing the OneDrive API" in stdout:
                # Clear failed files list at start of new sync cycle
                self.failed_files = []
                self.failed_files_count = 0
                self.collecting_failed_files = False
                self.file_errors = {}
                self.last_unattributed_error = None
                self._last_notified_failures = None
                self.msg = "Initializing the OneDrive API"
                logging.info(f"[{self.profile_name}] {self.msg}")
                self.profile_status["status_message"] = self.msg
                self.update_profile_status.emit(self.profile_status, self.profile_name)

            elif "Starting a sync with Microsoft OneDrive" in stdout:
                # A new sync cycle starts. Reset the failed-files list of the
                # previous cycle, but keep its warning (if any) visible until
                # this cycle completes, so the user stays informed that files
                # failed to sync.
                previous_cycle_had_failures = bool(self.failed_files or self.failed_files_count)
                self.failed_files = []
                self.failed_files_count = 0
                self.collecting_failed_files = False
                if not previous_cycle_had_failures:
                    self.profile_status.pop("error_message", None)
                    self.clear_warning.emit(self.profile_name)
                self.msg = "Starting a sync with Microsoft OneDrive"
                logging.info(f"[{self.profile_name}] {self.msg}")
                self.profile_status["status_message"] = self.msg
                self.update_profile_status.emit(self.profile_status, self.profile_name)
                # Finalize transfers left over from a previous cycle that never
                # reported completion (e.g. the client was killed mid-sync).
                self.finalize_stalled_tasks.emit(self.profile_name)

            elif "Processing:" in stdout or "Number of items to download from Microsoft OneDrive" in stdout or "OneDrive Client requested to create" in stdout:
                items_left = re.match(r"^Processing\s([0-9]+)\sOneDrive\sitems", stdout)
                if items_left != None:
                    if self.profile_status["status_message"].startswith(f"OneDrive is processing"):
                        logging.info(f"[{self.profile_name}] OneDrive is processing {items_left.group(1)} items...")
                    self.profile_status["status_message"] = f"OneDrive is processing {items_left.group(1)} items..."
                else:
                    if self.profile_status["status_message"] != "OneDrive is processing items...":
                        logging.info(f"[{self.profile_name}] OneDrive is processing items...")
                    self.profile_status["status_message"] = "OneDrive is processing items..."
                self.update_profile_status.emit(self.profile_status, self.profile_name)

            elif "--resync is required" in stdout or "before using --resync" in stdout:
                # Ask user for resync authorization and stop the worker.
                self.msg = "OneDrive resync authorization is required."
                logging.warning(f"[{self.profile_name}] {stdout!s} - {self.msg}")
                self.trigger_resync.emit(self.profile_name)

            elif "To delete a large volume of data use" in stdout:
                # Ask user for big delete authorization and stop the worker.
                self.msg = "OneDrive big delete authorization is required."
                logging.warning(f"[{self.profile_name}] {stdout!s}  - {self.msg}")
                self.update_profile_status.emit(self.profile_status, self.profile_name)
                self.profile_status["status_message"] = self.msg
                self.trigger_big_delete.emit(self.profile_name)

            elif any(_ in stdout for _ in self.tasks):
                # Capture information about file that is being uploaded/downloaded/deleted by OneDrive.
                file_operation = re.search(r"\b([Uploading|Downloading|Deleting|Moving]+)*", stdout).group(1)

                if file_operation in {"Deleting", "Moving"}:
                    self.file_name = re.search(r".*/(.+)$", stdout)
                    self.file_path = re.search(r".+\:\s(.+)$", stdout)

                else:
                    self.file_name = re.search(r".*/(.+)\s+\.+", stdout)
                    self.file_path = re.search(r"\b[file:]+\s(.+)\s+\.\.\.", stdout)

                transfer_complete = any(["done" in stdout, "Deleting" in stdout, "Moving" in stdout])
                transfer_failed = "failed!" in stdout
                progress = "0"

                transfer_progress_new = {
                    "file_operation": file_operation,
                    "file_path": "unknown file name" if self.file_path is None else self.file_path.group(1),
                    "progress": progress,
                    "transfer_complete": transfer_complete,
                    "transfer_failed": transfer_failed,
                    "timestamp": datetime.now() if transfer_complete else None,
                }

                if transfer_failed:
                    # Attach the reason why this file failed, if we know it.
                    error_message = self.file_errors.get(transfer_progress_new["file_path"])
                    if error_message is None and self.last_unattributed_error and (time.time() - self.last_error_time) < 10:
                        # API error blocks (e.g. HTTP 400) carry no path - they are
                        # printed just before the client retries the same file and
                        # reports the failed transfer, so attribute them here.
                        error_message = self.last_unattributed_error
                        self.last_unattributed_error = None
                        self.file_errors[transfer_progress_new["file_path"]] = error_message
                    transfer_progress_new["error_message"] = error_message

                # Update file transfer list
                logging.debug(transfer_progress_new)
                self.update_progress_new.emit(transfer_progress_new, self.profile_name)

                # Update profile status message.
                if transfer_complete:
                    pass
                    # self.profile_status["status_message"] = "OneDrive sync is complete"
                else:
                    if self.profile_status["status_message"] != "OneDrive sync in progress...":
                        logging.info(f"[{self.profile_name}] OneDrive sync in progress...")
                    self.profile_status["status_message"] = "OneDrive sync in progress..."

            elif "% " in stdout:
                # Capture download progress status
                """
                # Line Example for regex:
                # Uploading: dir1/another dir 2 - 123/dir3/50MBa.zip ... 80%  |  ETA    00:00:04
                """
                match = re.search(r"(\w[Downloading|Uploading]+)\:\s+(.+?)[\.]*\s(\d{1,3})\%", stdout)
                if match:
                    file_operation = match.group(1)
                    file_path = match.group(2).strip()
                    progress = match.group(3)

                    if progress != "100":
                        transfer_complete = progress == "100"

                        transfer_progress_new = {
                            "file_operation": file_operation,
                            "file_path": file_path,
                            "progress": progress,
                            "transfer_complete": transfer_complete,
                            "timestamp": datetime.now() if transfer_complete else None,
                        }

                        logging.debug(transfer_progress_new)
                        self.update_progress_new.emit(transfer_progress_new, self.profile_name)

                        if transfer_complete:
                            pass
                            # self.profile_status["status_message"] = "OneDrive sync is complete"
                        else:
                            if self.profile_status["status_message"] != "OneDrive sync in progress...":
                                logging.info(f"[{self.profile_name}] OneDrive sync in progress...")
                            self.profile_status["status_message"] = "OneDrive sync in progress..."

                        self.update_profile_status.emit(self.profile_status, self.profile_name)
                    elif progress == "100":
                        # Ignore progress 100% message to prevent duplicate entries.
                        # It will always be followed by another confirmation.
                        # Example: "Downloading file ./200MB.zip ... done"
                        pass

            elif "sync_business_shared_folders" in stdout:
                self.profile_status["status_message"] = (
                    'Business Shared Folder <a href="https://github.com/abraunegg/onedrive/blob/master/docs/business-shared-items.md"> has been deprecated</a>.'
                )
                self.update_profile_status.emit(self.profile_status, self.profile_name)

            elif "Network Connection Issue" in stdout:
                self.profile_status["status_message"] = "Cannot connect to Microsoft OneDrive Service."
                self.update_profile_status.emit(self.profile_status, self.profile_name)

            # elif "application is already running" in stdout:
            #     self.profile_status["status_message"] = """OneDrive is already running outside OneDriveGUI!\nPlease stop it first."""
            #     self.update_profile_status.emit(self.profile_status, self.profile_name)

            elif "command not found" in stdout:
                self.msg = "Onedrive does not seem to be installed. Please install it as per instruction at https://github.com/abraunegg/onedrive/blob/master/docs/install.md"
                logging.error(f"[{self.profile_name}] {self.msg}")

                self.profile_status["status_message"] = self.msg
                self.update_profile_status.emit(self.profile_status, self.profile_name)

            elif "/dlang/" in stdout:
                self.msg = "OneDrive client crashed. Please check logs."
                logging.critical(f"[{self.profile_name}] {self.msg}")
                self.profile_status["status_message"] = self.msg
                self.update_profile_status.emit(self.profile_status, self.profile_name)

            elif " refresh_token " in stdout or "'refresh_token'" in stdout:
                self.msg = "Logon details expired. Please re-authenticate."
                self.profile_status["status_message"] = self.msg
                self.update_profile_status.emit(self.profile_status, self.profile_name)
                self.update_credentials.emit(self.profile_name)

            elif "Error Message:" in stdout:
                # Check if this is a continuation of a previous ERROR: line
                if self.pending_error:
                    error_parts = stdout.split("Error Message:", 1)
                    if len(error_parts) > 1:
                        additional_error = error_parts[1].strip()
                        # Combine with pending error, including the affected path if we captured one
                        if self.pending_error_path:
                            full_error_message = f"{self.pending_error} Path: {self.pending_error_path} - {additional_error}"
                        else:
                            full_error_message = f"{self.pending_error} {additional_error}"
                    else:
                        full_error_message = self.pending_error
                    # Remember the error for the file it refers to (local file system
                    # error blocks include a "Path:" line), or as the most recent
                    # error to be attributed to the next transfer that fails.
                    if self.pending_error_path:
                        self.file_errors[self.pending_error_path] = full_error_message
                    self.last_unattributed_error = full_error_message
                    self.last_error_time = time.time()
                    self.pending_error = None  # Clear pending error
                    self.pending_error_path = None
                    logging.error(f"[{self.profile_name}] {full_error_message}")
                    self._emit_error_status(full_error_message)

            elif "Error Reason:" in stdout:
                # API error blocks print the human-readable reason on the line after
                # "Error Message:" - append it to the last error so the per-file
                # tooltip explains the actual cause (e.g. file name too long), and
                # re-emit the status so it can be categorized into a short message.
                if self.last_unattributed_error and "Error Reason" not in self.last_unattributed_error:
                    reason = stdout.split("Error Reason:", 1)[1].strip()
                    self.last_unattributed_error = f"{self.last_unattributed_error} - {reason}"
                    self.last_error_time = time.time()
                    self._emit_error_status(self.last_unattributed_error)

            elif self.pending_error and "Path:" in stdout:
                # Capture the affected file/folder path from a multi-line ERROR block
                path_parts = stdout.split("Path:", 1)
                if len(path_parts) > 1:
                    path_value = path_parts[1].strip()
                    if path_value and path_value != "(not available)":
                        self.pending_error_path = path_value

            elif "ERROR:" in stdout:
                # Extract error message after "ERROR:" prefix
                error_parts = stdout.split("ERROR:", 1)
                if len(error_parts) > 1:
                    error_text = error_parts[1].strip()
                    # Store as pending error to check if next line has "Error Message:"
                    self.pending_error = error_text
                    self.pending_error_path = None

            elif stdout.startswith("Skipping uploading this"):
                # Examples:
                #   Skipping uploading this new file due to 'case-insensitive match': ./file
                #   Skipping uploading this file as it cannot be read (file permissions or file corruption): ./file
                match = re.match(r"Skipping uploading this (?:new )?file (.*?): (.+)$", stdout)
                if match:
                    self.file_errors[match.group(2).strip()] = f"Skipped uploading {match.group(1)}"

            elif "Failed items to upload to/from Microsoft OneDrive:" in stdout:
                # Extract the count of failed items
                match = re.search(r"Failed items .+?: (\d+)", stdout)
                if match:
                    self.failed_files_count = int(match.group(1))
                    # Start collecting failed file lines (they come after this summary line)
                    self.collecting_failed_files = True

            elif "Failed to upload:" in stdout or "Failed to download:" in stdout:
                # Extract the operation and file path
                match = re.search(r"Failed to (upload|download): (.+)$", stdout)
                if match:
                    operation = match.group(1)
                    file_path = match.group(2).strip()
                    failed_entry = f"Failed to {operation}: {file_path}"

                    # Add to list, limiting to 25 entries
                    if len(self.failed_files) < 25:
                        self.failed_files.append(failed_entry)

                    # Mark the matching entry in the file operation list as failed,
                    # or create one for files that failed before a transfer was shown
                    # (e.g. skipped due to permission errors or name conflicts).
                    transfer_progress_new = {
                        "file_operation": "Uploading" if operation == "upload" else "Downloading",
                        "file_path": file_path,
                        "progress": "0",
                        "transfer_complete": False,
                        "transfer_failed": True,
                        "error_message": self.file_errors.get(file_path),
                        "timestamp": None,
                    }
                    logging.debug(transfer_progress_new)
                    self.update_progress_new.emit(transfer_progress_new, self.profile_name)

            elif "Unknown key in config file:" in stdout:
                # Extract the invalid config key
                match = re.search(r"Unknown key in config file:\s*(.+)$", stdout)
                if match:
                    invalid_key = match.group(1).strip()
                    error_message = f"Configuration error: Unknown key '{invalid_key}'. Please check your config file and remove invalid options."
                else:
                    error_message = "Configuration error: Unknown key in config file. Please check your configuration."
                logging.error(f"[{self.profile_name}] {error_message}")
                self._emit_error_status(error_message)

            else:
                # logging.debug(f"No rule matched: {stdout}")
                pass


class MaintenanceWorker(QThread):
    """
    Performs various onedrive tasks asynchronously.
    """

    update_sharepoint_site_list = Signal(list)
    update_library_list = Signal(dict)
    update_business_folder_list = Signal(list)
    update_login_response = Signal(dict)

    def __init__(self, profile, options=""):
        super(MaintenanceWorker, self).__init__()

        self.options = options
        self.profile = profile

        logging.info(f"[GUI] Starting maintenance worker for profile {self.profile} {self.options}")

        self.config_file = global_config[self.profile]["config_file"]
        self.config_dir = re.search(r"(.+)/.+$", self.config_file).group(1)
        logging.info(f"[GUI] OneDrive config file: {self.config_file}")
        logging.info(f"[GUI] OneDrive config dir: {self.config_dir}")

        self._command = f"exec {client_bin_path} --confdir='{self.config_dir}' {options}"
        logging.info(f"[GUI] Maintenance command: '{self._command}'")

    def run(self):
        logging.info(f"[GUI] Starting Maintenance Worker")
        self.onedrive_maintainer = subprocess.Popen(
            self._command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
            universal_newlines=True,
        )

        if "--auth-response" in self.options:
            # exec onedrive --confdir="{config_dir}" --auth-response "{response_url}"
            logging.debug(f"[GUI] Trying login...")
            self.login_response = "success"

            while self.onedrive_maintainer.poll() is None:
                self.perform_login()

            timeout = time.time() + 1
            while True:
                # This helps monitor stdout for extra second after onedrive process stops. I could not find a smarter way.
                self.perform_login()
                if time.time() > timeout:
                    break

            logging.info(f"[GUI] - Login response: {self.login_response}")
            self.update_login_response.emit({"profile_name": self.profile, "response": self.login_response})

        elif "--get-sharepoint-drive-id 'non-existent-library'" in self.options:
            # Trying to obtain Sharepoint Site list by searching a non-existent library name.
            logging.info(f"[GUI] Trying to get list of SharePoint Sites...")
            self.sharepoint_site_list = []

            while self.onedrive_maintainer.poll() is None:
                self.read_sharepoint_sites()

            timeout = time.time() + 1
            while True:
                # This helps monitor stdout for extra second after onedrive process stops. I could not find a smarter way.
                self.read_sharepoint_sites()
                if time.time() > timeout:
                    break

            logging.info(f"[GUI] - Number of retrieved Shared libraries: {len(self.sharepoint_site_list)}")
            self.update_sharepoint_site_list.emit(self.sharepoint_site_list)

        elif "--get-sharepoint-drive-id '" in self.options:
            self.library_ids_dict = {}

            # Obtain Drive ID of a specific Shared Library.
            logging.info(f"[GUI] Trying to get Drive ID of shared library...")

            while self.onedrive_maintainer.poll() is None:
                self.read_library_drive_ids()

            timeout = time.time() + 5
            while True:
                # This helps monitor stdout for extra second after onedrive process stops. I could not find a smarter way.
                self.read_library_drive_ids()
                if time.time() > timeout:
                    break

            self.update_library_list.emit(self.library_ids_dict)

        elif "--list-shared-items" in self.options:
            self.business_folder_list = []

            while self.onedrive_maintainer.poll() is None:
                self.read_shared_business_folders()

            timeout = time.time() + 1
            while True:
                # This helps monitor stdout for extra second after onedrive process stops. I could not find a smarter way.
                self.read_shared_business_folders()
                if time.time() > timeout:
                    break

            self.update_business_folder_list.emit(self.business_folder_list)

    def perform_login(self):
        """
        Performs OneDrive Login based on provided --auth-response url .
        Validates if login was successful.
        """
        if self.onedrive_maintainer.stdout:
            stdout = self.onedrive_maintainer.stdout.readline().strip()

            if stdout == "":
                pass
            elif "error reason" in stdout.lower():
                self.login_response = stdout
                logging.error(stdout)

            if self.onedrive_maintainer.stderr:
                stderr = self.onedrive_maintainer.stderr.readline().strip()
                if stderr != "":
                    logging.error("@ERROR " + stderr)

                if "error reason" in stderr.lower():
                    self.login_response = stderr
                    logging.error(stderr)

    def read_library_drive_ids(self):
        """
        Reads returned Drive IDs of SharePoint Shared Libraries and emits them to GUI wizard.
        """

        if self.onedrive_maintainer.stdout:
            stdout = self.onedrive_maintainer.stdout.readline()

            if stdout.strip() == "":
                pass
            elif "Library Name:" in stdout:
                library_name = re.match(r"^.+\:\s+(.+)$", stdout).group(1)
                logging.debug(f"[MaintenanceWorker][{self.profile}] Library Name: {library_name}")

                self.library_ids_dict[library_name] = ""

            elif "drive_id:" in stdout:
                last_key = list(self.library_ids_dict.keys())[-1]

                library_id = re.match(r"^.+\:\s+(.+)$", stdout).group(1)
                logging.debug(f"[MaintenanceWorker][{self.profile}] Library ID: {library_id}")

                self.library_ids_dict[last_key] = library_id

            if self.onedrive_maintainer.stderr:
                stderr = self.onedrive_maintainer.stderr.readline()
                if stderr != "":
                    logging.error("@ERROR " + stderr)

    def read_shared_business_folders(self):
        """
        Reads list of returned Shared Business Folders and emits them to GUI.
        """
        if self.onedrive_maintainer.stdout:
            stdout = self.onedrive_maintainer.stdout.readline()

            if stdout.strip() == "":
                pass
            elif "Shared Folder:" in stdout:
                folder_name = re.match(r"^.+:\s+(.+)$", stdout).group(1)
                self.business_folder_list.append(folder_name)
                logging.debug(f"[MaintenanceWorker][{self.profile}] Retrieved Business Shared Folder: {folder_name}")
            else:
                logging.debug(f"[MaintenanceWorker][{self.profile}] " + stdout.strip())

        if self.onedrive_maintainer.stderr:
            stderr = self.onedrive_maintainer.stderr.readline()
            if stderr != "":
                logging.error("@ERROR " + stderr)

    def read_sharepoint_sites(self):
        """
        Reads list of returned SharePoint Sites and emits them to GUI wizard.
        """
        if self.onedrive_maintainer.stdout:
            stdout = self.onedrive_maintainer.stdout.readline()

            if stdout.strip() == "":
                pass
            elif " * " in stdout:
                site_name = re.match(r"^\s\*\s(.+)", stdout).group(1)
                self.sharepoint_site_list.append(site_name)
                logging.debug(f"[MaintenanceWorker][{self.profile}] Retrieved SharePoint Site: {site_name}")
            else:
                logging.debug(f"[MaintenanceWorker][{self.profile}] " + stdout.strip())

        if self.onedrive_maintainer.stderr:
            stderr = self.onedrive_maintainer.stderr.readline()
            if stderr != "":
                logging.error("@ERROR " + stderr)


class TaskList(QWidget, Ui_list_item_widget):
    def __init__(self):
        super(TaskList, self).__init__()

        # Set up the user interface from Designer.
        self.setupUi(self)

        # Store completion timestamp for relative time display
        self.completion_timestamp = None
        self._original_file_name = ""
        self._file_path = ""
        self.transfer_state = "Uploading"

        # Enable text eliding for ls_label_2 to prevent horizontal overflow
        self.ls_label_2.setWordWrap(False)
        self.ls_label_2.setSizePolicy(self.ls_label_2.sizePolicy().horizontalPolicy(), self.ls_label_2.sizePolicy().verticalPolicy())
        self.ls_label_2_max_width = 170  # Store max width for eliding

    def set_icon(self, file_path):
        self.fileInfo = QFileInfo(file_path)
        self.iconProvider = QFileIconProvider()
        self.icon = self.iconProvider.icon(self.fileInfo)

        self.toolButton.setIcon(self.icon)

    def set_custom_icon(self, icon):
        """Set a custom QIcon for the toolButton."""
        self.toolButton.setIcon(icon)

    def set_file_name(self, file_path):
        self._original_file_name = file_path
        # Use font metrics to elide long filenames
        font_metrics = QFontMetrics(self.ls_label_file_name.font())
        elided_text = font_metrics.elidedText(file_path, Qt.ElideMiddle, 270)
        self.ls_label_file_name.setText(elided_text)

    def get_file_name(self):
        return self._original_file_name

    def set_file_path(self, file_path):
        """Store the absolute path of the file this row refers to, so rows for
        identically-named files in different folders can be told apart."""
        self._file_path = file_path

    def get_file_path(self):
        return self._file_path

    def set_state(self, state):
        """Set transfer state: 'Uploading', 'Downloading', 'Complete' or 'Failed'."""
        self.transfer_state = state

    def get_state(self):
        return self.transfer_state

    def clone(self):
        """Create a new widget displaying the same row.

        Needed when moving a row within the list: Qt deletes a row's widget when
        the row is taken out of a QListWidget, so a moved row must be given a
        fresh widget instead of reusing the old one."""
        new_widget = TaskList()
        new_widget.set_file_name(self._original_file_name)
        new_widget.set_file_path(self._file_path)
        new_widget.set_state(self.transfer_state)
        new_widget.set_progress(self.ls_progressBar.value())
        new_widget.set_custom_icon(self.toolButton.icon())
        new_widget.set_label_1(self.ls_label_1.text())
        new_widget.set_label_2(self.ls_label_2.text())
        new_widget.set_completion_timestamp(self.completion_timestamp)
        new_widget.set_timestamp(self.ls_label_timestamp.text())
        new_widget.set_tooltip(self.toolTip())
        new_widget.hide_progress_bar(self.ls_progressBar.isHidden())
        return new_widget

    def set_progress(self, percentage):
        self.ls_progressBar.setValue(percentage)

    def set_label_1(self, text):
        self.ls_label_1.setOpenExternalLinks(True)
        self.ls_label_1.setText(text)

    def set_label_2(self, text):
        # Use font metrics to elide text if it exceeds maximum width
        font_metrics = QFontMetrics(self.ls_label_2.font())
        elided_text = font_metrics.elidedText(text, Qt.ElideRight, self.ls_label_2_max_width)
        self.ls_label_2.setText(elided_text)

    def set_tooltip(self, text):
        """Show text on hover anywhere on the row, e.g. the full path of a failed
        file and the error message explaining why it failed."""
        self.setToolTip(text)

    def set_timestamp(self, text):
        """Set the timestamp label text"""
        self.ls_label_timestamp.setText(text)

    def get_timestamp_text(self):
        """Get current timestamp label text"""
        return self.ls_label_timestamp.text()

    def hide_progress_bar(self, transfer_status: bool):
        if transfer_status:
            self.ls_progressBar.hide()
        else:
            self.ls_progressBar.show()

    def set_completion_timestamp(self, timestamp):
        """Store the completion timestamp for this transfer"""
        self.completion_timestamp = timestamp

    def get_completion_timestamp(self):
        """Get the completion timestamp for this transfer"""
        return self.completion_timestamp


workers = {}
