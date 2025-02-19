#!/usr/bin/env python3

import os
import sys
import logging
import copy

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication


from logger import logger


from global_config import DIR_PATH


app = QApplication(sys.argv)
app.setApplicationName("OneDriveGUI")
app.setWindowIcon(QIcon(DIR_PATH + "/resources/images/icons8-clouds-80-dark-edge.png"))


from options import gui_settings, global_config, version
from global_config import save_global_config
from main_window import MainWindow


def main_window_start_state():
    # Determine if OneDriveGUI should start maximized, minimized to tray or minimized to taskbar/dock.
    # This should help ensure the GUI does not just disappear on Gnome without system tray extension.

    if gui_settings.get("start_minimized") == "True" or len(global_config) == 0:
        try:
            if main_window.tray.isSystemTrayAvailable():
                main_window.hide()
                logging.info("[GUI] Starting OneDriveGUI minimized to system tray")
        except:
            main_window.show()
            main_window.setWindowState(Qt.WindowMinimized)
            logging.info("[GUI] Starting OneDriveGUI minimized to taskbar/dock")
    else:
        main_window.show()
        logging.info("[GUI] Starting OneDriveGUI maximized")


workers = {}


if __name__ == "__main__":
    # gui_settings = GuiSettings(GUI_SETTINGS_FILE)

    logging.info(f"Starting OneDriveGUI v{version}")

    if len(global_config) > 0:
        save_global_config(global_config)

    # setup_wizard = SetupWizard(profile_settings_window=profile_settings_window)

    main_window = MainWindow()
    main_window_start_state()

    app.exec()
