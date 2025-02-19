from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QFileDialog


# Imports for GUI settings window
from ui.ui_gui_settings_window import Ui_gui_settings_window


import re
import os

from settings.gui_settings import gui_settings


import logging

# from logger import logger
from global_config import DIR_PATH, PROFILES_FILE


class GuiSettingsWindow(QWidget, Ui_gui_settings_window):
    def __init__(self):
        super(GuiSettingsWindow, self).__init__()

        self.setupUi(self)
        self.setWindowIcon(QIcon(DIR_PATH + "/resources/images/icons8-clouds-80-dark-edge.png"))

        self.checkBox_start_minimized.setChecked(self.get_check_box_state("start_minimized"))
        self.checkBox_start_minimized.stateChanged.connect(self.set_check_box_state)

        self.lineEdit_client_bin_path.setText(gui_settings.get("client_bin_path"))
        self.lineEdit_client_bin_path.textChanged.connect(self.set_client_bin_path)
        self.pushButton_client_bin_path.clicked.connect(self.get_bin_path)

        self.checkBox_frameless_window.setChecked(self.get_check_box_state("frameless_window"))
        self.checkBox_frameless_window.stateChanged.connect(self.set_check_box_state)

        self.checkBox_combined_start_stop_button.setChecked(self.get_check_box_state("combined_start_stop_button"))
        self.checkBox_combined_start_stop_button.stateChanged.connect(self.set_check_box_state)

        self.checkBox_QWebEngine_login.setChecked(self.get_check_box_state("QWebEngine_login"))
        self.checkBox_QWebEngine_login.stateChanged.connect(self.set_check_box_state)

        self.checkBox_show_debug.setChecked(self.get_check_box_state("show_debug"))
        self.checkBox_show_debug.stateChanged.connect(self.set_check_box_state)

        self.checkBox_save_debug.setChecked(self.get_check_box_state("save_debug"))
        self.checkBox_save_debug.stateChanged.connect(self.set_check_box_state)

        self.spinBox_log_rotation_interval.setValue(int(gui_settings.get("log_rotation_interval")))
        self.spinBox_log_rotation_interval.valueChanged.connect(self.set_spin_box_value)

        self.spinBox_log_backup_count.setValue(int(gui_settings.get("log_backup_count")))
        self.spinBox_log_backup_count.valueChanged.connect(self.set_spin_box_value)

        self.comboBox_debug_level.setCurrentText(gui_settings.get("debug_level").upper())
        self.comboBox_debug_level.activated.connect(self.set_debug_level)

        self.lineEdit_log_file.setText(gui_settings.get("log_file"))
        self.lineEdit_log_file.textChanged.connect(self.set_log_file)

        self.pushButton_log_file.clicked.connect(self.get_log_dir_name)

        self.pushButton_save.clicked.connect(self.save_settings)

    def get_bin_path(self):
        self.file_dialog = QFileDialog()
        self.file_dialog.setFileMode(QFileDialog.ExistingFile)
        self.file_dialog.setNameFilter("onedrive")

        if self.file_dialog.exec():
            file_path = self.file_dialog.selectedFiles()[0]
            logging.info(file_path)
            self.lineEdit_client_bin_path.setText(file_path)

    def get_log_dir_name(self):
        self.file_dialog = QFileDialog.getExistingDirectory(dir=os.path.expanduser("~/"))

        dir_name = self.file_dialog
        logging.info(dir_name)
        self.lineEdit_client_bin_path.setText(dir_name)

    def set_client_bin_path(self):
        file_path = str(self.lineEdit_client_bin_path.text())
        if file_path == "":
            file_path = "onedrive"
        gui_settings.set("client_bin_path", file_path)

    def set_log_file(self):
        gui_settings.set("log_file", str(self.lineEdit_log_file.text()))

    def set_debug_level(self):
        gui_settings.set("debug_level", self.comboBox_debug_level.currentText())

    def set_spin_box_value(self, value):
        _property = self.sender().objectName()
        property = re.search(r"spinBox_(.+)", _property).group(1)
        gui_settings.set(property, str(value))

    def get_check_box_state(self, property):
        return "True" in gui_settings.get(property)

    def set_check_box_state(self):
        _property = self.sender().objectName()
        property = re.search(r"checkBox_(.+)", _property).group(1)

        if self.sender().isChecked():
            logging.info(f"[GUI][SETTINGS] {property} is checked")
            gui_settings.set(property, "True")
        else:
            logging.info(f"[GUI][SETTINGS] {property} is unchecked")
            gui_settings.set(property, "False")

    def save_settings(self):
        gui_settings.save()


gui_settings_window = GuiSettingsWindow()
