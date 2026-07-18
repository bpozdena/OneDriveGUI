#!/usr/bin/env python3

import os
import sys
import logging
import copy

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication


from .logger import logger


from .global_config import DIR_PATH


app = QApplication(sys.argv)
app.setApplicationName("OneDriveGUI")
app.setDesktopFileName("OneDriveGUI")
app.setWindowIcon(QIcon(DIR_PATH + "/resources/images/icons8-cloud-80.png"))


from .options import gui_settings, global_config, version
from .global_config import save_global_config
from .main_window import MainWindow

workers = {}

def main():
    logging.info(f"Starting OneDriveGUI v{version}")

    if len(global_config) > 0:
        save_global_config(global_config)

    main_window = MainWindow()
    
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


    app.exec()

