from PySide6.QtCore import QThread, Signal, QFileInfo

from PySide6.QtWidgets import QWidget, QFileIconProvider


# Imports for main window.
from ui.ui_list_item_widget import Ui_list_item_widget


import re
import time
import subprocess

from global_config import save_global_config
from options import (
    # main_window,
    global_config,
    temp_global_config,
    # profile_settings_window,
    client_bin_path,
    gui_settings,
    version,
)

from utils.utils import humanize_file_size, shorten_path


import logging

# from logger import logger
from global_config import DIR_PATH, PROFILES_FILE


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

    def __init__(self, profile, options=""):
        super(WorkerThread, self).__init__()
        logging.info(f"[GUI] Starting worker for profile {profile}")

        self.config_file = global_config[profile]["config_file"]
        self.config_dir = re.search(r"(.+)/.+$", self.config_file)
        logging.debug(f"[GUI] OneDrive config file: {self.config_file}")
        logging.debug(f"[GUI] OneDrive config dir: {self.config_dir}")
        self._command = f"exec {client_bin_path} --confdir='{self.config_dir.group(1)}' --monitor -v {options}"
        logging.debug(f"[GUI] Monitoring command: '{self._command}'")
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

    def read_stdout(self):
        stdout = self.onedrive_process.stdout.readline().strip()
        if stdout != "":
            logging.info(f"[{self.profile_name}] " + stdout)

            if "Calling Function: testNetwork()" in stdout:
                self.profile_status["status_message"] = "Cannot connect to Microsoft OneDrive Service"
                self.update_profile_status.emit(self.profile_status, self.profile_name)

            elif "authorise this application by" in stdout.lower() or "--reauth and re-authorise this client" in stdout:
                self.onedrive_process.kill()
                self.profile_status["status_message"] = "OneDrive login is required"
                self.update_profile_status.emit(self.profile_status, self.profile_name)
                self.update_credentials.emit(self.profile_name)

            elif "Sync with Microsoft OneDrive is complete" in stdout or "Total number of local file(s) added or changed" in stdout:
                self.profile_status["status_message"] = "OneDrive sync is complete"
                self.update_profile_status.emit(self.profile_status, self.profile_name)

            elif "Sync with Microsoft OneDrive has completed, however there are items that failed to sync" in stdout:
                self.profile_status["status_message"] = "Sync completed with errors. Check the log file."
                self.update_profile_status.emit(self.profile_status, self.profile_name)

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
                self.profile_status["status_message"] = "Initializing the OneDrive API"
                self.update_profile_status.emit(self.profile_status, self.profile_name)

            elif "Processing" in stdout:
                items_left = re.match(r"^Processing\s([0-9]+)\sOneDrive\sitems", stdout)
                if items_left != None:
                    self.profile_status["status_message"] = f"OneDrive is processing {items_left.group(1)} items..."
                else:
                    self.profile_status["status_message"] = "OneDrive is processing items..."
                self.update_profile_status.emit(self.profile_status, self.profile_name)

            elif "--resync is required" in stdout:
                # Ask user for resync authorization and stop the worker.
                logging.warning(f"[{self.profile_name}] {str(stdout)}  - Asking for resync authorization.")
                self.trigger_resync.emit(self.profile_name)

            elif "To delete a large volume of data use" in stdout:
                # Ask user for big delete authorization and stop the worker.
                logging.warning(f"[{self.profile_name}] {str(stdout)}  - Asking for big delete authorization.")
                self.update_profile_status.emit(self.profile_status, self.profile_name)
                self.profile_status["status_message"] = "Sync stopped due to big delete detected."
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
                progress = "0"

                transfer_progress_new = {
                    "file_operation": file_operation,
                    "file_path": "unknown file name" if self.file_path is None else self.file_path.group(1),
                    "progress": progress,
                    "transfer_complete": transfer_complete,
                }

                # Update file transfer list
                logging.info(transfer_progress_new)
                self.update_progress_new.emit(transfer_progress_new, self.profile_name)

                # Update profile status message.
                if transfer_complete:
                    pass
                    # self.profile_status["status_message"] = "OneDrive sync is complete"
                else:
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
                        }

                        logging.info(transfer_progress_new)
                        self.update_progress_new.emit(transfer_progress_new, self.profile_name)

                        if transfer_complete:
                            pass
                            # self.profile_status["status_message"] = "OneDrive sync is complete"
                        else:
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

            elif "onedrive application is already running" in stdout:
                self.profile_status["status_message"] = "OneDrive is already running outside OneDriveGUI !"
                self.update_profile_status.emit(self.profile_status, self.profile_name)

            elif "command not found" in stdout:
                logging.error(
                    """Onedrive does not seem to be installed. Please install it as per instruction at 
                https://github.com/abraunegg/onedrive/blob/master/docs/install.md """
                )

                self.profile_status["status_message"] = (
                    'OneDrive Client not found! Please <a href="https://github.com/abraunegg/onedrive/blob/master/docs/install.md" style="color:#FFFFFF;">install</a> it.'
                )
                self.update_profile_status.emit(self.profile_status, self.profile_name)

            elif "/dlang/" in stdout:
                self.profile_status["status_message"] = "OneDrive client crashed. Please check logs."
                self.update_profile_status.emit(self.profile_status, self.profile_name)

            elif " refresh_token " in stdout or "'refresh_token'" in stdout:
                self.profile_status["status_message"] = "Logon details expired. Please re-authenticate."
                self.update_profile_status.emit(self.profile_status, self.profile_name)
                self.update_credentials.emit(self.profile_name)

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
        logging.debug(f"[GUI] OneDrive config file: {self.config_file}")
        logging.debug(f"[GUI] OneDrive config dir: {self.config_dir}")

        self._command = f"exec {client_bin_path} --confdir='{self.config_dir}' {options}"
        logging.debug(f"[GUI] Maintenance command: '{self._command}'")

    def run(self):
        logging.debug(f"[GUI] Starting Maintenance Worker")
        self.onedrive_maintainer = subprocess.Popen(
            self._command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
            universal_newlines=True,
        )

        if "--auth-response" in self.options:
            # exec onedrive --confdir="{config_dir}" --auth-response "{response_url}"
            logging.info(f"[GUI] Trying login...")
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
                logging.info(f"[MaintenanceWorker][{self.profile}] Library Name: {library_name}")

                self.library_ids_dict[library_name] = ""

            elif "drive_id:" in stdout:
                last_key = list(self.library_ids_dict.keys())[-1]

                library_id = re.match(r"^.+\:\s+(.+)$", stdout).group(1)
                logging.info(f"[MaintenanceWorker][{self.profile}] Library ID: {library_id}")

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
                logging.info(f"[MaintenanceWorker][{self.profile}] Retrieved Business Shared Folder: {folder_name}")
            else:
                logging.info(f"[MaintenanceWorker][{self.profile}] " + stdout.strip())

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
                logging.info(f"[MaintenanceWorker][{self.profile}] Retrieved SharePoint Site: {site_name}")
            else:
                logging.info(f"[MaintenanceWorker][{self.profile}] " + stdout.strip())

        if self.onedrive_maintainer.stderr:
            stderr = self.onedrive_maintainer.stderr.readline()
            if stderr != "":
                logging.error("@ERROR " + stderr)


class TaskList(QWidget, Ui_list_item_widget):
    def __init__(self):
        super(TaskList, self).__init__()

        # Set up the user interface from Designer.
        self.setupUi(self)

    def set_icon(self, file_path):
        self.fileInfo = QFileInfo(file_path)
        self.iconProvider = QFileIconProvider()
        self.icon = self.iconProvider.icon(self.fileInfo)

        self.toolButton.setIcon(self.icon)

    def set_file_name(self, file_path):
        self.ls_label_file_name.setText(file_path)

    def get_file_name(self):
        return self.ls_label_file_name.text()

    def set_progress(self, percentage):
        self.ls_progressBar.setValue(percentage)

    def set_label_1(self, text):
        self.ls_label_1.setOpenExternalLinks(True)
        self.ls_label_1.setText(text)

    def set_label_2(self, text):
        self.ls_label_2.setText(text)

    def hide_progress_bar(self, transfer_status: bool):
        if transfer_status:
            self.ls_progressBar.hide()
        else:
            self.ls_progressBar.show()


workers = {}
