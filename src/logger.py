import os
import sys
import re
import logging
import logging.handlers as handlers
from settings.gui_settings import gui_settings


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
    else:
        return logging.DEBUG


def config_logging_handlers():
    # Allow stdout logging and logging into rotating log file based on user settings.
    show_debug = gui_settings.get("show_debug")
    save_debug = gui_settings.get("save_debug")
    log_rotation_interval = int(gui_settings.get("log_rotation_interval"))
    log_backup_count = int(gui_settings.get("log_backup_count"))
    log_file = os.path.expanduser(gui_settings.get("log_file"))
    _log_dir = re.search(r"(.+)/.+$", log_file).group(1)
    log_dir = os.path.expanduser(_log_dir)

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    stdout_handler = logging.StreamHandler(sys.stdout)
    timed_handler = handlers.TimedRotatingFileHandler(
        filename=log_file,
        when="H",
        interval=log_rotation_interval,
        backupCount=log_backup_count,
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
