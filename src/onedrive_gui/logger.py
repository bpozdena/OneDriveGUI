import os
import sys
import re
import logging
import logging.handlers as handlers
from .settings.gui_settings import gui_settings


def config_debug_level():
    debug_level = gui_settings.get("debug_level").upper()

    if debug_level == "DEBUG":
        return logging.DEBUG
    elif debug_level == "INFO":
        return logging.INFO
    elif debug_level == "WARNING":
        return logging.WARNING
    elif debug_level == "ERROR":
        return logging.ERROR
    elif debug_level == "CRITICAL":
        return logging.CRITICAL
    else:
        return logging.DEBUG


class SizeCappedTimedRotatingFileHandler(handlers.TimedRotatingFileHandler):
    """
    TimedRotatingFileHandler that also rotates when the current file reaches
    max_bytes.

    With the default DEBUG level every line of client output is logged, and a
    busy initial sync can grow the log by gigabytes per day - far more between
    two scheduled time rotations, filling up /tmp (or wherever the log lives)
    after a few days. The size cap bounds every file, and together with
    backupCount it bounds the total space used by the logs.

    Size-triggered rollovers rotate numbered backups (log.1, log.2, ...),
    because the parent class skips the rollover when the time-based backup
    name (e.g. log.2026-10-18_11) already exists - all size rollovers within
    one rotation interval would silently do nothing and the file would keep
    growing.
    """

    def __init__(self, *args, max_bytes=0, **kwargs):
        self.max_bytes = max_bytes
        self._size_rollover_due = False
        super().__init__(*args, **kwargs)

    def shouldRollover(self, record):
        self._size_rollover_due = False
        if super().shouldRollover(record):
            return True
        if self.max_bytes > 0:
            if self.stream is None:
                self.stream = self._open()
            msg = self.format(record) + "\n"
            if self.stream.tell() + len(msg.encode()) >= self.max_bytes:
                self._size_rollover_due = True
                return True
        return False

    def doRollover(self):
        if not self._size_rollover_due:
            super().doRollover()
            return
        self._size_rollover_due = False

        if self.stream:
            self.stream.close()
            self.stream = None

        for index in range(self.backupCount - 1, 0, -1):
            source = f"{self.baseFilename}.{index}"
            destination = f"{self.baseFilename}.{index + 1}"
            if os.path.exists(source):
                if os.path.exists(destination):
                    os.remove(destination)
                os.rename(source, destination)

        first_backup = f"{self.baseFilename}.1"
        if os.path.exists(first_backup):
            os.remove(first_backup)
        if os.path.exists(self.baseFilename):
            os.rename(self.baseFilename, first_backup)

        if not self.delay:
            self.stream = self._open()


def config_logging_handlers():
    # Allow stdout logging and logging into rotating log file based on user settings.
    show_debug = gui_settings.get("show_debug")
    save_debug = gui_settings.get("save_debug")
    log_rotation_interval = int(gui_settings.get("log_rotation_interval"))
    log_backup_count = int(gui_settings.get("log_backup_count"))
    log_max_file_size = int(gui_settings.get("log_max_file_size")) * 1024 * 1024
    log_file = os.path.expanduser(gui_settings.get("log_file"))
    _log_dir = re.search(r"(.+)/.+$", log_file).group(1)
    log_dir = os.path.expanduser(_log_dir)

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    stdout_handler = logging.StreamHandler(sys.stdout)
    timed_handler = SizeCappedTimedRotatingFileHandler(
        filename=log_file,
        when="H",
        interval=log_rotation_interval,
        backupCount=log_backup_count,
        max_bytes=log_max_file_size,
    )

    log_handlers = []

    if show_debug == "True":
        log_handlers.append(stdout_handler)
    if save_debug == "True":
        log_handlers.append(timed_handler)

    return log_handlers


logging.basicConfig(
    format="%(asctime)s [%(filename)s:%(lineno)s][fn=%(funcName)s][%(levelname)s] - %(message)s",
    handlers=config_logging_handlers(),
    level=config_debug_level(),
)

logger = logging.getLogger(__name__)
