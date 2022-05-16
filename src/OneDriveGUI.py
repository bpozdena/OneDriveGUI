#!/usr/bin/env python3

import os
import re
import subprocess
import sys
import logging
import requests
import copy
import logging.handlers as handlers
from configparser import ConfigParser

from PySide6.QtCore import QThread, QTimer, QUrl, Signal, QFileInfo, Qt, QDir
from PySide6.QtGui import QIcon, QPixmap, QDesktopServices
from PySide6.QtWidgets import (
    QWidget,
    QApplication,
    QMainWindow,
    QMenu,
    QSystemTrayIcon,
    QListWidget,
    QListWidgetItem,
    QFileIconProvider,
    QStackedLayout,
    QVBoxLayout,
    QLabel,
    QAbstractItemView,
    QWizard,
    QWizardPage,
    QLineEdit,
    QCheckBox,
    QPushButton,
    QFormLayout,
    QGridLayout,
    QFileDialog,
)
from urllib3 import HTTPSConnectionPool

# TODO: Split into multiple files once all main features are implemented.
# Import for login window.
from ui.ui_login import Ui_LoginWindow

# Imports for main window.
from ui.ui_mainwindow import Ui_MainWindow
from ui.ui_list_item_widget import Ui_list_item_widget
from ui.ui_process_status_page import Ui_status_page


# Imports for Setting windows.
from ui.ui_settings import Ui_settings_window
from ui.ui_profile_settings_page import Ui_profile_settings
from ui.ui_import_existing_profile import Ui_import_profile
from ui.ui_create_new_profile import Ui_create_new_profile


PROFILES_FILE = os.path.expanduser("~/.config/onedrive-gui/profiles")
dir_path = os.path.dirname(os.path.realpath(__file__))

# Logging
# TODO: Implement logging configuration into the GUI.
log_dir = os.path.expanduser("~/.config/onedrive-gui/")
log_file = f"{log_dir}onedrivegui.log"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
timed_handler = handlers.TimedRotatingFileHandler(filename=log_file, when="D", interval=1, backupCount=2)
stdout_handler = logging.StreamHandler(sys.stdout)
handlers = [timed_handler, stdout_handler]

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=handlers,
    level=logging.DEBUG,
)


class SetupWizard(QWizard):
    def __init__(self, parent=None):
        super(SetupWizard, self).__init__(parent)
        self.setWindowIcon(QIcon(dir_path + "/resources/images/icons8-clouds-48.png"))

        self.setPage(1, WizardPage_welcome(self))
        self.setPage(2, wizardPage_version_check(self))
        self.setPage(3, wizardPage_create_import(self))
        self.setPage(4, wizardPage_create(self))
        self.setPage(5, wizardPage_import(self))
        self.setPage(6, wizardPage_finish(self))

        self.setWindowTitle("OneDriveGUI Setup Wizard")
        self.resize(640, 480)

        self.currentIdChanged.connect(self.on_page_change)

    def on_page_change(self):
        if self.currentId() == 2:
            logging.info("Checking installed OneDrive version")
            self.page(2).check_onedrive_version()

    def nextId(self):
        if self.currentPage() == self.page(1):
            return 2
        if self.currentPage() == self.page(2):
            return 3
        if self.currentPage() == self.page(3):
            if self.page(3).checkBox_create.isChecked():
                return 4
            elif self.page(3).checkBox_import.isChecked():
                return 5
        if self.currentPage() == self.page(4):
            return 6
        if self.currentPage() == self.page(5):
            return 6
        if self.currentPage() == self.page(6):
            return -1


class WizardPage_welcome(QWizardPage):
    def __init__(self, parent=None):
        super(WizardPage_welcome, self).__init__(parent)

        self.setTitle("Welcome to OneDriveGUI")

        self.label_2 = QLabel()
        self.label_2.setText("This wizard will help you with initial OneDrive profile creation/import.")

        layout = QVBoxLayout()
        layout.addWidget(self.label_2)
        self.setLayout(layout)


class wizardPage_version_check(QWizardPage):
    def __init__(self, parent=None):
        super(wizardPage_version_check, self).__init__(parent)
        self.setTitle("OneDrive version check")

        self.label_4 = QLabel()
        self.label_4.setText("Installed/Not Installed/ version")

        self.label_5 = QLabel()
        self.label_5.setWordWrap(True)
        self.label_5.setStyleSheet("color: red;")
        self.label_5.setOpenExternalLinks(True)
        self.label_5.setText(
            "OneDrive Client for Linux does not seem to be installed. Please install it by following "
            "<a href='https://github.com/abraunegg/onedrive/blob/master/docs/INSTALL.md'>instructions</a> for your distro. "
        )

        layout = QVBoxLayout()
        # layout.addWidget(self.label_3)
        layout.addWidget(self.label_4)
        layout.addWidget(self.label_5)
        self.setLayout(layout)

    def check_onedrive_version(self):
        # Check if OneDrive is installed
        # TODO: Minimim version check not yet enforced
        try:
            client_version_check = subprocess.check_output(["onedrive", "--version"], stderr=subprocess.STDOUT)
            installed_client_version = re.search(r".\s(v[0-9.]+)", str(client_version_check)).group(1)
            installed_client_version_num = int(installed_client_version.replace("v", "").replace(".", ""))
            min_supported_version_num = 2415

            if installed_client_version_num < min_supported_version_num:
                logging.info(f"Unsupported OneDrive {installed_client_version} detected.")
                self.label_4.setOpenExternalLinks(True)
                self.label_4.setText(
                    f'OneDrive {installed_client_version} is not supported. Please <a href="https://github.com/abraunegg/onedrive/blob/master/docs/INSTALL.md">upgrade</a> it.'
                )
                self.label_4.setStyleSheet("color: red;")
                self.label_5.hide()
                self.completeChanged.emit()

                return False

            if "onedrive v" in str(client_version_check):
                logging.info(f"OneDrive {installed_client_version} detected.")
                self.label_4.setText(f"OneDrive {installed_client_version} detected.")
                self.label_4.setStyleSheet("color: green;")
                self.label_5.hide()
                self.completeChanged.emit()

                return True

            else:
                self.label_4.setText("OneDrive not detected.")
                self.label_4.setStyleSheet("color: red;")
                self.completeChanged.emit()
                return False

        except FileNotFoundError:
            self.label_4.setText("OneDrive not detected.")
            self.label_4.setStyleSheet("color: red;")
            self.completeChanged.emit()
            return False

    def isComplete(self):
        if "not" in self.label_4.text().lower():
            return False
        else:
            return True


class wizardPage_create_import(QWizardPage):
    def __init__(self, parent=None):
        super(wizardPage_create_import, self).__init__(parent)
        self.setTitle("Create/Import OneDrive profile")

        self.checkBox_create = QCheckBox()
        self.checkBox_create.setText("Create new OneDrive profile")
        self.checkBox_create.stateChanged.connect(self.on_checkbox_change)

        self.checkBox_import = QCheckBox()
        self.checkBox_import.setText("Import existing OneDrive profile/config")
        self.checkBox_import.stateChanged.connect(self.on_checkbox_change)

        layout = QVBoxLayout()
        layout.addWidget(self.checkBox_create)
        layout.addWidget(self.checkBox_import)
        self.setLayout(layout)

    def on_checkbox_change(self):
        if self.checkBox_create.isChecked():
            logging.info(f"Create new profile is checked")
            self.checkBox_import.setDisabled(True)
            self.completeChanged.emit()

        elif self.checkBox_import.isChecked():
            logging.info(f"Import profile is checked")
            self.checkBox_create.setDisabled(True)
            self.completeChanged.emit()

        else:
            logging.info(f"No option is unchecked")
            self.checkBox_import.setDisabled(False)
            self.checkBox_create.setDisabled(False)
            self.completeChanged.emit()

    def isComplete(self):
        if self.checkBox_create.isChecked() == False and self.checkBox_import.isChecked() == False:
            logging.info("not complete")
            return False
        else:
            logging.info("complete")
            return True


class wizardPage_create(QWizardPage):
    def __init__(self, parent=None):
        super(wizardPage_create, self).__init__(parent)
        self.setTitle("Create OneDrive profile")

        self.label_new_profile_name = QLabel()
        self.label_new_profile_name.setText("New profile name")

        self.lineEdit_new_profile_name = QLineEdit()
        self.lineEdit_new_profile_name.setPlaceholderText("E.g. john@live.com")
        self.lineEdit_new_profile_name.textChanged.connect(self.update_sync_dir)
        self.lineEdit_new_profile_name.textChanged.connect(self.enable_create_button)

        self.label_sync_dir = QLabel()
        self.label_sync_dir.setText("Sync directory")

        self.lineEdit_sync_dir = QLineEdit()
        self.lineEdit_sync_dir.setPlaceholderText("E.g. ~/OneDrive_john@live.com/")
        self.lineEdit_sync_dir.textChanged.connect(self.enable_create_button)

        self.pushButton_browse = QPushButton()
        self.pushButton_browse.setText("Browse")
        self.pushButton_browse.clicked.connect(self.get_dir_name)

        self.pushButton_create = QPushButton()
        self.pushButton_create.setText("Create new profile")
        self.pushButton_create.setEnabled(False)
        self.pushButton_create.clicked.connect(self.create_profile)

        layout = QGridLayout()
        layout.addWidget(self.label_new_profile_name, 0, 0)
        layout.addWidget(self.lineEdit_new_profile_name, 0, 1)
        layout.addWidget(self.label_sync_dir, 1, 0)
        layout.addWidget(self.lineEdit_sync_dir, 1, 1)
        layout.addWidget(self.pushButton_browse, 1, 2)
        layout.addWidget(self.pushButton_create, 2, 0, 1, 3)
        self.setLayout(layout)

    def isComplete(self):
        if self.pushButton_create.text() == "Done":
            return True
        return False

    def get_dir_name(self):
        self.file_dialog = QFileDialog.getExistingDirectory(dir=os.path.expanduser("~/"))

        dir_name = self.file_dialog
        logging.info(dir_name)
        self.lineEdit_sync_dir.setText(dir_name)

    def update_sync_dir(self, text):
        self.lineEdit_sync_dir.setText(f"~/OneDrive_{text}")

    def enable_create_button(self):
        # Enable 'Import' button only when profile name and path to config file are not empty.
        if self.lineEdit_new_profile_name.text() == "".strip() or self.lineEdit_sync_dir == "".strip():
            self.pushButton_create.setEnabled(False)
        else:
            self.pushButton_create.setEnabled(True)

    def create_profile(self):
        """
        Creates new profile and loads default settings.
        TODO: Consolidate with import_profile()
        """
        profile_name = self.lineEdit_new_profile_name.text()
        sync_dir = self.lineEdit_sync_dir.text()
        config_path = os.path.expanduser(f"~/.config/onedrive/accounts/{profile_name}/config")

        # Load all default values.
        _default_od_config = read_config(dir_path + "/resources/default_config")
        default_od_config = _default_od_config._sections

        # Construct dict with user profile settings.
        new_profile = {
            profile_name: {"config_file": config_path, "enable_debug": False, "mode": "monitor", "auto_sync": False}
        }

        # Load existing user profiles and add the new profile.
        _profiles = ConfigParser()
        _profiles.read(PROFILES_FILE)
        _profiles[profile_name] = new_profile[profile_name]

        # Create profile config file if it does not exist.
        profiles_dir = re.search(r"(.+)/profiles$", PROFILES_FILE).group(1)
        if not os.path.exists(profiles_dir):
            os.makedirs(profiles_dir)

        # Save the new profile.
        with open(PROFILES_FILE, "w") as profilefile:
            _profiles.write(profilefile)

        # Append default OD config
        new_profile[profile_name].update(default_od_config)

        # Configure sync directory
        new_profile[profile_name]["onedrive"]["sync_dir"] = f'"{sync_dir}"'

        # Append new profile into running global profile
        global_config.update(new_profile)

        # Automatically save global config to prevent loss if user does not press 'Save' button.
        save_global_config()

        # Add Setting page widget for new profile
        settings_window.listWidget_profiles.addItem(profile_name)
        self.setting_page = ProfileSettingsPage(profile_name)
        settings_window.stackedLayout.addWidget(self.setting_page)

        # Add status page widget for new profile
        main_window.comboBox.addItem(profile_name)
        main_window.profile_status_pages[profile_name] = ProfileStatusPage(profile_name)
        main_window.stackedLayout.addWidget(main_window.profile_status_pages[profile_name])

        # Hide "Create profile" push button from main windows.
        main_window.pushButton_new_profile.hide()

        logging.info(f"Account {profile_name} has been created")
        self.pushButton_create.setText("Done")
        self.pushButton_create.setDisabled(True)
        self.completeChanged.emit()


class wizardPage_import(QWizardPage):
    def __init__(self, parent=None):
        super(wizardPage_import, self).__init__(parent)
        self.setTitle("Import OneDrive profile")

        self.label_profile_name = QLabel()
        self.label_profile_name.setText("Profile name")

        self.label_config_path = QLabel()
        self.label_config_path.setText("Config file path")

        self.lineEdit_profile_name = QLineEdit()
        self.lineEdit_profile_name.setPlaceholderText("E.g. john@live.com")
        self.lineEdit_profile_name.textChanged.connect(self.enable_import_button)

        self.lineEdit_config_path = QLineEdit()
        self.lineEdit_config_path.setPlaceholderText("E.g. ~/.config/onedrive/config")
        self.lineEdit_config_path.textChanged.connect(self.enable_import_button)

        self.pushButton_browse = QPushButton()
        self.pushButton_browse.setText("Browse")
        self.pushButton_browse.clicked.connect(self.get_config_name)

        self.pushButton_import = QPushButton()
        self.pushButton_import.setText("Import")
        self.pushButton_import.setEnabled(False)
        self.pushButton_import.clicked.connect(self.import_profile)

        # self.registerField("label_profile_name*",self.label_profile_name)

        layout = QGridLayout()
        layout.addWidget(self.label_profile_name, 0, 0)
        layout.addWidget(self.label_config_path, 1, 0)
        layout.addWidget(self.lineEdit_profile_name, 0, 1)
        layout.addWidget(self.lineEdit_config_path, 1, 1)
        layout.addWidget(self.pushButton_browse, 1, 2)
        layout.addWidget(self.pushButton_import, 2, 0, 2, 3)
        self.setLayout(layout)

    def isComplete(self):
        # Enable 'Next' button only when profile config was successfully imported
        if self.pushButton_import.text() == "Done":
            return True
        return False

    def enable_import_button(self):
        # Enable 'Import' button only when profile name and path to config file are valid.
        profile_name_filled = self.lineEdit_profile_name.text() != "".strip()

        config_specified = re.search(r"/config$", self.lineEdit_config_path.text().strip()) != None
        config_path = os.path.expanduser(self.lineEdit_config_path.text().strip())
        config_exists = os.path.exists(config_path)

        if all([profile_name_filled, config_specified, config_exists]):
            self.pushButton_import.setEnabled(True)
        else:
            self.pushButton_import.setEnabled(False)

    def get_config_name(self):
        self.file_dialog = QFileDialog.getOpenFileName(self, dir=os.path.expanduser("~/.config/"))

        file_name = self.file_dialog[0]

        logging.info(file_name)
        self.lineEdit_config_path.setText(file_name)

    def import_profile(self):
        """
        Imports pre-existing OneDrive profile.
        Loads default values first, then overwrite them with user settings.
        This is to handle cases where imported config contains only some properties.
        """

        profile_name = self.lineEdit_profile_name.text().strip()
        config_path = os.path.expanduser(self.lineEdit_config_path.text())

        # Load all default values.
        _default_od_config = read_config(dir_path + "/resources/default_config")
        default_od_config = _default_od_config._sections
        logging.debug("[GUI] default_od_config: " + str(default_od_config))

        # Load user's settings.
        _new_od_config = read_config(config_path)
        new_od_config = _new_od_config._sections
        logging.debug("[GUI] new_od_config: " + str(new_od_config))

        # Construct dict with user profile settings.
        new_profile = {
            profile_name: {"config_file": config_path, "enable_debug": False, "mode": "monitor", "auto_sync": False}
        }

        # Load existing user profiles and add the new profile.
        _profiles = ConfigParser()
        _profiles.read(PROFILES_FILE)
        _profiles[profile_name] = new_profile[profile_name]

        # Create profile config file if it does not exist.
        profiles_dir = re.search(r"(.+)/profiles$", PROFILES_FILE).group(1)
        if not os.path.exists(profiles_dir):
            os.makedirs(profiles_dir)

        # Save the new profile.
        with open(PROFILES_FILE, "w") as profilefile:
            _profiles.write(profilefile)

        # Append OD config
        new_profile[profile_name].update(default_od_config)
        for key, value in new_od_config["onedrive"].items():
            new_profile[profile_name]["onedrive"][key] = value

        # new_profile[profile_name].update(new_od_config)

        # Append new profile into running global profile
        global_config.update(new_profile)
        logging.debug("[GUI] new_profile: " + str(new_profile))
        logging.debug("[GUI] global_config: " + str(global_config))

        settings_window.listWidget_profiles.addItem(profile_name)
        self.setting_page = ProfileSettingsPage(profile_name)
        settings_window.stackedLayout.addWidget(self.setting_page)

        # Add status page widget for new profile
        main_window.comboBox.addItem(profile_name)
        main_window.profile_status_pages[profile_name] = ProfileStatusPage(profile_name)
        main_window.stackedLayout.addWidget(main_window.profile_status_pages[profile_name])

        # Hide "Create profile" push button from main window.
        main_window.pushButton_new_profile.hide()

        # Automatically save global config to prevent loss if user does not press 'Save' button.
        save_global_config()

        logging.info(f"Account {profile_name} has been imported")
        self.pushButton_import.setText("Done")
        self.pushButton_import.setDisabled(True)
        self.completeChanged.emit()


class wizardPage_finish(QWizardPage):
    def __init__(self, parent=None):
        super(wizardPage_finish, self).__init__(parent)
        self.setTitle("Finished")
        self.label_13 = QLabel()
        self.label_13.setWordWrap(True)
        self.label_13.setText(
            "<html><head/><body><p>Your OneDrive profile has been created. "
            "</p><p><br/></p><p>You can adjust advanced profile options if needed. "
            "Once you are happy with the profile settings, start sync with OneDrive. "
            "You will be automatically presented with a OneDrive login page if you have not logged on previously.</p></body></html>"
        )

        layout = QFormLayout()
        layout.addWidget(self.label_13)
        self.setLayout(layout)


class SettingsWindow(QWidget, Ui_settings_window):
    def __init__(self):
        super(SettingsWindow, self).__init__()

        self.setupUi(self)
        self.setWindowIcon(QIcon(dir_path + "/resources/images/icons8-clouds-48.png"))

        self.stackedLayout = QStackedLayout()

        for profile in global_config:
            logging.info(profile)
            self.listWidget_profiles.addItem(profile)
            self.page = ProfileSettingsPage(profile)
            self.stackedLayout.addWidget(self.page)

        self.horizontalLayout.addLayout(self.stackedLayout)
        self.listWidget_profiles.itemSelectionChanged.connect(self.switch_account_settings_page)

        self.pushButton_open_create.clicked.connect(self.create_new_profile_window)
        self.pushButton_open_create.hide()
        self.pushButton_open_import.clicked.connect(self.import_profile_window)
        self.pushButton_open_import.hide()

        self.pushButton_remove.clicked.connect(self.remove_profile)
        self.pushButton_create_import.clicked.connect(self.show_setup_wizard)
        self.show()

    def closeEvent(self, event):
        event.ignore()
        self.hide()

    def switch_account_settings_page(self):
        self.stackedLayout.setCurrentIndex(self.listWidget_profiles.currentRow())

    def show_setup_wizard(self):
        self.setup_wizard = SetupWizard()
        self.setup_wizard.setStartId(3)
        self.setup_wizard.show()

    def create_new_profile_window(self):
        # Show profile creation window
        self.create_window = QWidget()
        self.create_window.setWindowIcon(QIcon(dir_path + "/resources/images/icons8-clouds-48.png"))
        self.create_ui = Ui_create_new_profile()
        self.create_ui.setupUi(self.create_window)
        self.create_window.show()

        self.create_ui.pushButton_create.clicked.connect(self.create_profile)

        # Hide window once account is created.
        self.create_ui.pushButton_create.clicked.connect(self.create_window.hide)

    def import_profile_window(self):
        # Show profile import window
        self.import_window = QWidget()
        self.import_window.setWindowIcon(QIcon(dir_path + "/resources/images/icons8-clouds-48.png"))
        self.import_ui = Ui_import_profile()
        self.import_ui.setupUi(self.import_window)
        self.import_window.show()

        self.import_ui.pushButton_import.clicked.connect(self.import_profile)

        # Hide window once account is created
        self.import_ui.pushButton_import.clicked.connect(self.import_window.hide)

    def remove_profile(self):
        # Remove profile from settings window.
        selected_profile_name = self.listWidget_profiles.currentItem().text()
        selected_profile_index = self.listWidget_profiles.currentRow()
        selected_profile_widget = self.stackedLayout.currentWidget()
        self.listWidget_profiles.takeItem(selected_profile_index)
        self.stackedLayout.removeWidget(selected_profile_widget)

        # Remove profile from main window.
        combo_box_index = main_window.comboBox.findText(selected_profile_name)
        main_window.comboBox.removeItem(combo_box_index)
        main_window.profile_status_pages.pop(selected_profile_name, None)
        global_config.pop(selected_profile_name, None)
        logging.info(global_config)

        # Load existing user profiles and remove the new profile.
        _profiles = ConfigParser()
        _profiles.read(PROFILES_FILE)
        _profiles.remove_section(selected_profile_name)

        # Save the new profile.
        with open(PROFILES_FILE, "w") as profilefile:
            _profiles.write(profilefile)

    def create_profile(self):
        """
        Creates new profile and loads default settings.
        TODO: Consolidate with import_profile()
        """
        profile_name = self.create_ui.lineEdit_new_profile_name.text()
        sync_dir = self.create_ui.lineEdit_sync_dir.text()
        config_path = os.path.expanduser(f"~/.config/onedrive/accounts/{profile_name}/config")

        # Load all default values.
        _default_od_config = read_config(dir_path + "/resources/default_config")
        default_od_config = _default_od_config._sections

        # Construct dict with user profile settings.
        new_profile = {
            profile_name: {"config_file": config_path, "enable_debug": False, "mode": "monitor", "auto_sync": False}
        }

        # Load existing user profiles and add the new profile.
        _profiles = ConfigParser()
        _profiles.read(PROFILES_FILE)
        _profiles[profile_name] = new_profile[profile_name]

        # Create profile config file if it does not exist.
        profiles_dir = re.search(r"(.+)/profiles$", PROFILES_FILE).group(1)
        if not os.path.exists(profiles_dir):
            os.makedirs(profiles_dir)

        # Save the new profile.
        with open(PROFILES_FILE, "w") as profilefile:
            _profiles.write(profilefile)

        # Append default OD config
        new_profile[profile_name].update(default_od_config)

        # Configure sync directory
        new_profile[profile_name]["onedrive"]["sync_dir"] = f'"{sync_dir}"'

        # Append new profile into running global profile
        global_config.update(new_profile)

        # Automatically save global config to prevent loss if user does not press 'Save' button.
        save_global_config()

        # Add Setting page widget for new profile
        self.listWidget_profiles.addItem(profile_name)
        self.page = ProfileSettingsPage(profile_name)
        self.stackedLayout.addWidget(self.page)

        # Add status page widget for new profile
        main_window.comboBox.addItem(profile_name)
        main_window.profile_status_pages[profile_name] = ProfileStatusPage(profile_name)
        main_window.stackedLayout.addWidget(main_window.profile_status_pages[profile_name])

        # Hide "Create profile" push button from main windows.
        main_window.pushButton_new_profile.hide()

    def import_profile(self):
        """
        Imports pre-existing OneDrive profile.
        Loads default values first, then overwrite them with user settings.
        This is to handle cases where imported config contains only some properties.
        """

        profile_name = self.import_ui.lineEdit_profile_name.text()
        config_path = os.path.expanduser(self.import_ui.lineEdit_config_path.text())

        # Load all default values.
        _default_od_config = read_config(dir_path + "/resources/default_config")
        default_od_config = _default_od_config._sections

        # Load user's settings.
        _new_od_config = read_config(config_path)
        new_od_config = _new_od_config._sections

        # Construct dict with user profile settings.
        new_profile = {
            profile_name: {"config_file": config_path, "enable_debug": False, "mode": "monitor", "auto_sync": False}
        }

        # Load existing user profiles and add the new profile.
        _profiles = ConfigParser()
        _profiles.read(PROFILES_FILE)
        _profiles[profile_name] = new_profile[profile_name]

        # Create profile config file if it does not exist.
        profiles_dir = re.search(r"(.+)/profiles$", PROFILES_FILE).group(1)
        if not os.path.exists(profiles_dir):
            os.makedirs(profiles_dir)

        # Save the new profile.
        with open(PROFILES_FILE, "w") as configfile:
            _profiles.write(configfile)

        # Append OD config
        new_profile[profile_name].update(default_od_config)
        new_profile[profile_name].update(new_od_config)

        # Append new profile into running global profile
        global_config.update(new_profile)
        # logging.info(new_profile)
        # logging.info(global_config)

        self.listWidget_profiles.addItem(profile_name)
        self.page = ProfileSettingsPage(profile_name)
        self.stackedLayout.addWidget(self.page)

        # Hide "Create profile" push button from main windows.
        main_window.pushButton_new_profile.hide()


class ProfileStatusPage(QWidget, Ui_status_page):
    def __init__(self, profile_name):
        super(ProfileStatusPage, self).__init__()

        self.profile_name = profile_name

        # Set up the user interface from Designer.
        self.setupUi(self)

        # Temporary start/stop buttons
        self.toolButton_start.clicked.connect(self.start_monitor)
        self.toolButton_stop.clicked.connect(self.stop_monitor)

        # Open Sync Dir
        self.pushButton_open_dir.clicked.connect(self.open_sync_dir)

        # Open Settings window
        self.pushButton_settings.clicked.connect(lambda: settings_window.show())

        self.pushButton_2.setText("Wizard")
        self.pushButton_2.clicked.connect(self.show_setup_wizard)
        self.pushButton_2.hide()

    def open_sync_dir(self):
        sync_dir = global_config[self.profile_name]["onedrive"]["sync_dir"].strip('"')
        url = QUrl(os.path.expanduser(sync_dir))
        QDesktopServices.openUrl(url)

    def show_setup_wizard(self):
        self.setup_wizard = SetupWizard()
        self.setup_wizard.show()
        # self.currentIdChanged.connect(logging.info("print test"))

    def stop_monitor(self):
        if self.profile_name in main_window.workers:
            main_window.workers[self.profile_name].stop_worker()
            self.label_onedrive_status.setText("OneDrive sync has been stopped")
            logging.info(f"OneDrive sync for profile {self.profile_name} has been stopped.")
        else:
            logging.info(f"OneDrive for profile {self.profile_name} is not running.")

    def start_monitor(self):
        main_window.start_onedrive_monitor(self.profile_name)


class ProfileSettingsPage(QWidget, Ui_profile_settings):
    def __init__(self, profile):
        super(ProfileSettingsPage, self).__init__()

        self.profile = profile

        # Set up the user interface from Designer.
        self.setupUi(self)

        temp_global_config = global_config
        self.temp_profile_config = temp_global_config[self.profile]

        self.label_profile_name.setText(self.profile)
        self.tabWidget.setCurrentIndex(0)

        #
        # Monitored files tab
        #
        self.lineEdit_sync_dir.setText(self.temp_profile_config["onedrive"]["sync_dir"].strip('"'))
        self.lineEdit_sync_dir.textChanged.connect(self.set_sync_dir)

        self.checkBox_sync_root_files.setChecked(self.get_check_box_state("sync_root_files"))
        self.checkBox_sync_root_files.stateChanged.connect(self.set_check_box_state)

        self.pushButton_sync_dir_browse.clicked.connect(self.get_sync_dir_name)

        #
        # Excluded files tab
        #

        # Skip_file section
        self.skip_files = self.temp_profile_config["onedrive"]["skip_file"].strip('"').split("|")
        self.listWidget_skip_file.addItems(self.skip_files)
        self.listWidget_skip_file.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.pushButton_add_skip_file.clicked.connect(self.add_skip_file)
        self.pushButton_add_skip_file.clicked.connect(self.lineEdit_skip_file.clear)
        self.pushButton_rm_skip_file.clicked.connect(self.remove_skip_file)

        # Skip_dir section
        self.skip_dirs = self.temp_profile_config["onedrive"]["skip_dir"].strip('"').split("|")
        self.listWidget_skip_dir.addItems(self.skip_dirs)
        self.listWidget_skip_dir.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.pushButton_add_skip_dir.clicked.connect(self.add_skip_dir)
        self.pushButton_add_skip_dir.clicked.connect(self.lineEdit_skip_dir.clear)
        self.pushButton_rm_skip_dir.clicked.connect(self.remove_skip_dir)

        self.checkBox_skip_dir_strict_match.setChecked(self.get_check_box_state("skip_dir_strict_match"))
        self.checkBox_skip_dir_strict_match.stateChanged.connect(self.set_check_box_state)

        self.checkBox_check_nosync.setChecked(self.get_check_box_state("check_nosync"))
        self.checkBox_check_nosync.stateChanged.connect(self.set_check_box_state)

        self.checkBox_skip_symlinks.setChecked(self.get_check_box_state("skip_symlinks"))
        self.checkBox_skip_symlinks.stateChanged.connect(self.set_check_box_state)

        self.checkBox_skip_dotfiles.setChecked(self.get_check_box_state("skip_dotfiles"))
        self.checkBox_skip_dotfiles.stateChanged.connect(self.set_check_box_state)

        #
        # Sync Options tab
        #
        self.spinBox_monitor_interval.setValue(
            int(self.temp_profile_config["onedrive"]["monitor_interval"].strip('"'))
        )
        self.spinBox_monitor_interval.valueChanged.connect(self.set_spin_box_value)

        self.spinBox_monitor_fullscan_frequency.setValue(
            int(self.temp_profile_config["onedrive"]["monitor_fullscan_frequency"].strip('"'))
        )
        self.spinBox_monitor_fullscan_frequency.valueChanged.connect(self.set_spin_box_value)

        self.spinBox_classify_as_big_delete.setValue(
            int(self.temp_profile_config["onedrive"]["classify_as_big_delete"].strip('"'))
        )
        self.spinBox_classify_as_big_delete.valueChanged.connect(self.set_spin_box_value)

        self.spinBox_sync_dir_permissions.setValue(
            int(self.temp_profile_config["onedrive"]["sync_dir_permissions"].strip('"'))
        )
        self.spinBox_sync_dir_permissions.valueChanged.connect(self.set_spin_box_value)

        self.spinBox_sync_file_permissions.setValue(
            int(self.temp_profile_config["onedrive"]["sync_file_permissions"].strip('"'))
        )
        self.spinBox_sync_file_permissions.valueChanged.connect(self.set_spin_box_value)

        self.spinBox_operation_timeout.setValue(
            int(self.temp_profile_config["onedrive"]["operation_timeout"].strip('"'))
        )
        self.spinBox_operation_timeout.valueChanged.connect(self.set_spin_box_value)

        self.checkBox_download_only.setChecked(self.get_check_box_state("download_only"))
        self.checkBox_download_only.stateChanged.connect(self.set_check_box_state)

        self.checkBox_upload_only.setChecked(self.get_check_box_state("upload_only"))
        self.checkBox_upload_only.stateChanged.connect(self.set_check_box_state)

        self.checkBox_force_http_2.setChecked(self.get_check_box_state("force_http_2"))
        self.checkBox_force_http_2.stateChanged.connect(self.set_check_box_state)

        self.checkBox_disable_upload_validation.setChecked(self.get_check_box_state("disable_upload_validation"))
        self.checkBox_disable_upload_validation.stateChanged.connect(self.set_check_box_state)

        self.checkBox_check_nomount.setChecked(self.get_check_box_state("check_nomount"))
        self.checkBox_check_nomount.stateChanged.connect(self.set_check_box_state)

        self.checkBox_local_first.setChecked(self.get_check_box_state("local_first"))
        self.checkBox_local_first.stateChanged.connect(self.set_check_box_state)

        self.checkBox_no_remote_delete.setChecked(self.get_check_box_state("no_remote_delete"))
        self.checkBox_no_remote_delete.stateChanged.connect(self.set_check_box_state)

        self.checkBox_sync_business_shared_folders.setChecked(self.get_check_box_state("sync_business_shared_folders"))
        self.checkBox_sync_business_shared_folders.stateChanged.connect(self.set_check_box_state)

        self.checkBox_dry_run.setChecked(self.get_check_box_state("dry_run"))
        self.checkBox_dry_run.stateChanged.connect(self.set_check_box_state)

        self.checkBox_remove_source_files.setChecked(self.get_check_box_state("remove_source_files"))
        self.checkBox_remove_source_files.stateChanged.connect(self.set_check_box_state)

        self.checkBox_resync.setChecked(self.get_check_box_state("resync"))
        self.checkBox_resync.stateChanged.connect(self.set_check_box_state)

        self.checkBox_bypass_data_preservation.setChecked(self.get_check_box_state("bypass_data_preservation"))
        self.checkBox_bypass_data_preservation.stateChanged.connect(self.set_check_box_state)

        self.lineEdit_user_agent.setText(self.temp_profile_config["onedrive"]["user_agent"].strip('"'))
        self.lineEdit_user_agent.textChanged.connect(self.set_line_edit_value)

        self.lineEdit_azure_ad_endpoint.setText(self.temp_profile_config["onedrive"]["azure_ad_endpoint"].strip('"'))
        self.lineEdit_azure_ad_endpoint.textChanged.connect(self.set_line_edit_value)

        self.lineEdit_azure_tenant_id.setText(self.temp_profile_config["onedrive"]["azure_tenant_id"].strip('"'))
        self.lineEdit_azure_tenant_id.textChanged.connect(self.set_line_edit_value)

        # Rate limit
        self.spinBox_rate_limit.setValue(int(self.temp_profile_config["onedrive"]["rate_limit"].strip('"')))
        self.horizontalSlider_rate_limit.setValue(int(self.temp_profile_config["onedrive"]["rate_limit"].strip('"')))
        self.label_rate_limit_mbps.setText(
            str(round(self.spinBox_rate_limit.value() * 8 / 1000 / 1000, 2)) + " Mbit/s"
        )
        self.spinBox_rate_limit.valueChanged.connect(self.set_spin_box_value)
        self.spinBox_rate_limit.valueChanged.connect(self.horizontalSlider_rate_limit.setValue)
        self.spinBox_rate_limit.valueChanged.connect(
            lambda: self.label_rate_limit_mbps.setText(
                str(round(self.spinBox_rate_limit.value() * 8 / 1000 / 1000, 2)) + " Mbit/s"
            )
        )
        self.horizontalSlider_rate_limit.valueChanged.connect(self.spinBox_rate_limit.setValue)

        #
        # Webhooks tab
        #
        self.checkBox_webhook_enabled.setChecked(self.get_check_box_state("webhook_enabled"))
        self.checkBox_webhook_enabled.stateChanged.connect(self.set_check_box_state)

        self.spinBox_webhook_expiration_interval.setValue(
            int(self.temp_profile_config["onedrive"]["webhook_expiration_interval"].strip('"'))
        )
        self.spinBox_webhook_expiration_interval.valueChanged.connect(self.set_spin_box_value)

        self.spinBox_webhook_renewal_interval.setValue(
            int(self.temp_profile_config["onedrive"]["webhook_renewal_interval"].strip('"'))
        )
        self.spinBox_webhook_renewal_interval.valueChanged.connect(self.set_spin_box_value)

        self.spinBox_webhook_listening_port.setValue(
            int(self.temp_profile_config["onedrive"]["webhook_listening_port"].strip('"'))
        )
        self.spinBox_webhook_listening_port.valueChanged.connect(self.set_spin_box_value)

        self.lineEdit_webhook_public_url.setText(self.temp_profile_config["onedrive"]["webhook_public_url"].strip('"'))
        self.lineEdit_webhook_public_url.textChanged.connect(self.set_line_edit_value)

        self.lineEdit_webhook_listening_host.setText(
            self.temp_profile_config["onedrive"]["webhook_listening_host"].strip('"')
        )
        self.lineEdit_webhook_listening_host.textChanged.connect(self.set_line_edit_value)

        #
        # Logging tab
        #
        self.lineEdit_log_dir.setText(self.temp_profile_config["onedrive"]["log_dir"].strip('"'))
        self.lineEdit_log_dir.textChanged.connect(self.set_log_dir)

        self.pushButton_log_dir_browse.clicked.connect(self.get_log_dir_name)

        self.checkBox_enable_logging.setChecked(self.get_check_box_state("enable_logging"))
        self.checkBox_enable_logging.stateChanged.connect(self.set_check_box_state)

        self.checkBox_debug_https.setChecked(self.get_check_box_state("debug_https"))
        self.checkBox_debug_https.stateChanged.connect(self.set_check_box_state)

        self.checkBox_disable_notifications.setChecked(self.get_check_box_state("disable_notifications"))
        self.checkBox_disable_notifications.stateChanged.connect(self.set_check_box_state)

        self.spinBox_monitor_log_frequency.setValue(
            int(self.temp_profile_config["onedrive"]["monitor_log_frequency"].strip('"'))
        )
        self.spinBox_monitor_log_frequency.valueChanged.connect(self.set_spin_box_value)

        self.spinBox_min_notify_changes.setValue(
            int(self.temp_profile_config["onedrive"]["min_notify_changes"].strip('"'))
        )
        self.spinBox_min_notify_changes.valueChanged.connect(self.set_spin_box_value)

        #
        # Account tab
        #
        self.config_file = global_config[self.profile]["config_file"].strip('"')
        self.config_dir = re.search(r"(.+)/.+$", self.config_file).group(1)

        self.pushButton_login.clicked.connect(lambda: main_window.show_login(self.profile))
        self.pushButton_login.hide()
        self.pushButton_logout.clicked.connect(self.logout)

        self.checkBox_auto_sync.setChecked(self.get_check_box_state_profile("auto_sync"))
        self.checkBox_auto_sync.stateChanged.connect(self.set_check_box_state_profile)

        #
        # Buttons
        #
        self.pushButton_discart.hide()
        # TODO: How to discart unsaved changes and refresh the widgets or close window?
        # self.pushButton_discart.clicked.connect(self.discart_changes)
        self.pushButton_save.clicked.connect(self.save_profile_settings)

    def str2bool(self, value):
        return value.lower() in "true"

    def logout(self):
        os.system(f"onedrive --confdir='{self.config_dir}' --logout")
        logging.info(f"Profile {self.profile} has been logged out.")
        # self.profile_status["status_message"] = "You have been logged out"

        main_window.profile_status_pages[self.profile].stop_monitor()
        # main_window.profile_status_pages[self.profile]["status_message"] = "You have been logged out"
        if self.profile in main_window.workers:
            main_window.workers[self.profile].stop_worker()
            main_window.profile_status_pages[self.profile].label_onedrive_status.setText(
                "OneDrive sync has been stopped"
            )
            logging.info(f"OneDrive sync for profile {self.profile} has been stopped.")
        else:
            logging.info(f"OneDrive for profile {self.profile} is not running.")

        main_window.profile_status_pages[self.profile].label_onedrive_status.setText("You have been logged out")

    def get_sync_dir_name(self):
        self.file_dialog = QFileDialog.getExistingDirectory(dir=os.path.expanduser("~/"))

        sync_dir = self.file_dialog
        logging.info(sync_dir)
        self.lineEdit_sync_dir.setText(sync_dir)

    def get_log_dir_name(self):
        self.file_dialog = QFileDialog.getExistingDirectory(dir=os.path.expanduser("~/"))

        log_dir = self.file_dialog
        logging.info(log_dir)
        self.lineEdit_log_dir.setText(log_dir)

    def set_line_edit_value(self, value):
        _property = self.sender().objectName()
        property = re.search(r"lineEdit_(.+)", _property).group(1)
        self.temp_profile_config["onedrive"][f"{property}"] = f'"{value}"'

    def set_spin_box_value(self, value):
        _property = self.sender().objectName()
        property = re.search(r"spinBox_(.+)", _property).group(1)
        self.temp_profile_config["onedrive"][f"{property}"] = f'"{value}"'

    def set_check_box_state(self, state):
        _property = self.sender().objectName()
        property = re.search(r"checkBox_(.+)", _property).group(1)
        logging.info(property)
        if state == Qt.Checked:
            logging.info("is checked")
            self.temp_profile_config["onedrive"][f"{property}"] = '"true"'
        else:
            logging.info("is unchecked")
            self.temp_profile_config["onedrive"][f"{property}"] = '"false"'

    def set_check_box_state_profile(self, state):
        _property = self.sender().objectName()
        property = re.search(r"checkBox_(.+)", _property).group(1)
        logging.info(property)
        if state == Qt.Checked:
            logging.info("is checked")
            self.temp_profile_config[f"{property}"] = True
        else:
            logging.info("is unchecked")
            self.temp_profile_config[f"{property}"] = False

    def get_check_box_state(self, property):
        return self.temp_profile_config["onedrive"][f"{property}"].strip('"') in "true"

    def get_check_box_state_profile(self, property):
        return self.temp_profile_config[f"{property}"] == "True"

    def add_skip_file(self):
        self.add_item_to_qlist(self.lineEdit_skip_file, self.listWidget_skip_file, self.skip_files)
        self.temp_profile_config["onedrive"]["skip_file"] = '"' + "|".join(self.skip_files) + '"'

    def remove_skip_file(self):
        self.remove_item_from_qlist(self.listWidget_skip_file, self.skip_files)
        self.temp_profile_config["onedrive"]["skip_file"] = '"' + "|".join(self.skip_files) + '"'

    def add_skip_dir(self):
        self.add_item_to_qlist(self.lineEdit_skip_dir, self.listWidget_skip_dir, self.skip_dirs)
        self.temp_profile_config["onedrive"]["skip_dir"] = '"' + "|".join(self.skip_dirs) + '"'

    def remove_skip_dir(self):
        self.remove_item_from_qlist(self.listWidget_skip_dir, self.skip_dirs)
        self.temp_profile_config["onedrive"]["skip_dir"] = '"' + "|".join(self.skip_dirs) + '"'

    def set_rate_limit(self):
        self.temp_profile_config["onedrive"]["rate_limit"] = f'"{self.lineEdit_rate_limit.text()}"'
        self.label_rate_limit_mbps.setText(
            str(round(int(self.lineEdit_rate_limit.text()) * 8 / 1000 / 1000, 2)) + " Mbit/s"
        )

    def set_sync_dir(self):
        self.temp_profile_config["onedrive"]["sync_dir"] = f'"{self.lineEdit_sync_dir.text()}"'

    def set_log_dir(self):
        self.temp_profile_config["onedrive"]["log_dir"] = f'"{self.lineEdit_log_dir.text()}"'

    def add_item_to_qlist(self, source_widget, destination_widget, list):
        if source_widget.text() == "":
            logging.info("Ignoring empty value.")
        elif source_widget.text() in list:
            logging.info("Item already in exemption list.")
        else:
            list.append(source_widget.text())
            destination_widget.addItem(source_widget.text())

    def remove_item_from_qlist(self, qlistwidget_name, list):
        for item in qlistwidget_name.selectedItems():
            logging.info("Removing: " + item.text())
            # items.remove(item.text())
            qlistwidget_name.takeItem(qlistwidget_name.row(item))
            logging.info(list)
            list.remove(item.text())

    def save_profile_settings(self):
        global_config[self.profile].update(self.temp_profile_config)
        logging.debug("save_profile_settings" + "self.temp_profile_config" + str(self.temp_profile_config))
        logging.debug("save_profile_settings" + "global_config" + str(global_config))
        save_global_config()

    def discart_changes(self):
        self.temp_profile_config = None
        self.close()


class TaskList(QWidget, Ui_list_item_widget):
    def __init__(self):
        super(TaskList, self).__init__()

        # Set up the user interface from Designer.
        self.setupUi(self)

    def set_icon(self, file_path):
        self.fileInfo = QFileInfo(file_path)
        self.iconProvider = QFileIconProvider()
        self.icon = self.iconProvider.icon(self.fileInfo)

        # icon = QIcon(icon_file)
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
        # pass
        if transfer_status:
            self.ls_progressBar.hide()
        else:
            self.ls_progressBar.show()


class WorkerThread(QThread):
    """
    Constructs a thread, which can start, monitor and stop OneDrive process.
    """

    update_credentials = Signal(str)
    update_progress_new = Signal(dict, str)
    update_profile_status = Signal(dict, str)
    trigger_resync = Signal()

    def __init__(self, profile):
        super(WorkerThread, self).__init__()
        logging.info(f"[GUI] Starting worker for profile {profile}")

        self.config_file = global_config[profile]["config_file"]
        self.config_dir = re.search(r"(.+)/.+$", self.config_file)
        logging.debug(f"[GUI] OneDrive config file: {self.config_file}")
        logging.debug(f"[GUI] OneDrive config dir: {self.config_dir}")
        self._command = f"onedrive --confdir='{self.config_dir.group(1)}' --monitor -v"
        logging.debug(f"[GUI] Monitoring command: '{self._command}'")
        self.profile_name = profile

    def stop_worker(self):
        logging.info(f"[{self.profile_name}] Waiting for worker to finish...")
        while self.onedrive_process.poll() is None:
            self.onedrive_process.kill()

        logging.info(f"[{self.profile_name}] Quiting thread")
        self.quit()
        self.wait()
        logging.info(f"[{self.profile_name}] Removing thread info")

        main_window.workers.pop(self.profile_name, None)
        logging.info(f"[GUI] Remaining running workers: {main_window.workers}")

    def run(self, resync=False):
        """
        Starts OneDrive and sends signals to GUI based on parsed information.
        """

        file_name = None

        tasks = [
            "Downloading file",
            "Downloading new file",
            "Uploading file",
            "Uploading new file",
            "Uploading modified file",
            "Downloading modified file",
            "Deleting item",
        ]

        self.profile_status = {"status_message": "", "free_space": "", "account_type": ""}

        self.onedrive_process = subprocess.Popen(
            self._command + "--resync" if resync else self._command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
            universal_newlines=True,
        )

        while self.onedrive_process.poll() is None:
            if self.onedrive_process.stdout:
                stdout = self.onedrive_process.stdout.readline()
                if stdout == "":
                    continue

                # logging.info(bytes(stdout, 'utf-8'))
                logging.info(f"[{self.profile_name}] " + stdout.strip())

                if "Authorize this app visiting" in stdout:
                    self.onedrive_process.kill()
                    self.profile_status["status_message"] = "OneDrive login is required"
                    self.update_profile_status.emit(self.profile_status, self.profile_name)
                    self.update_credentials.emit(self.profile_name)

                elif "Sync with OneDrive is complete" in stdout:
                    self.profile_status["status_message"] = "OneDrive sync is complete"
                    self.update_profile_status.emit(self.profile_status, self.profile_name)

                elif "Remaining Free Space" in stdout:
                    self.free_space_bytes = re.search(r"([0-9]+)", stdout).group(1)
                    self.free_space_human = str(humanize_file_size(int(self.free_space_bytes)))

                    logging.info(f"[{self.profile_name}] Free Space: {self.free_space_human}")
                    self.profile_status["free_space"] = f"Free Space: {self.free_space_human}"
                    # self.profile_status["account_type"] = f"{self.account_type.capitalize()} [{self.free_space_human}]"
                    self.update_profile_status.emit(self.profile_status, self.profile_name)

                elif "Account Type" in stdout:
                    self.account_type = re.search(r"\s(\w+)$", stdout).group(1)
                    self.profile_status["account_type"] = self.account_type.capitalize()
                    logging.info(f"[{self.profile_name}] Account type: {self.account_type}")
                    self.update_profile_status.emit(self.profile_status, self.profile_name)

                elif "Initializing the OneDrive API" in stdout:
                    self.profile_status["status_message"] = "Initializing the OneDrive API"
                    self.update_profile_status.emit(self.profile_status, self.profile_name)

                elif "Processing" in stdout:
                    items_left = re.match(r"^Processing\s([0-9]+)", stdout)
                    if items_left != None:
                        self.profile_status[
                            "status_message"
                        ] = f"OneDrive is processing {items_left.group(1)} items..."
                    else:
                        self.profile_status["status_message"] = "OneDrive is processing items..."
                    self.update_profile_status.emit(self.profile_status, self.profile_name)

                elif any(_ in stdout for _ in tasks):
                    # Capture information about file that is being uploaded/downloaded/deleted by OneDrive.
                    file_operation = re.search(r"\b([Uploading|Downloading|Deleting]+)*", stdout).group(1)

                    if file_operation == "Deleting":
                        file_name = re.search(r".*/(.+)$", stdout)
                        file_path = re.search(r"\b[item|OneDrive:]+\s(.+)$", stdout)

                    else:
                        file_name = re.search(r".*/(.+)\s+\.+", stdout)
                        file_path = re.search(r"\b[file]+\s(.+)\s+\.\.\.", stdout)

                    transfer_complete = any(["done" in stdout, "Deleting" in stdout])
                    progress = "0"

                    transfer_progress_new = {
                        "file_operation": file_operation,
                        "file_path": "unknown file name" if file_path is None else file_path.group(1),
                        "progress": progress,
                        "transfer_complete": transfer_complete,
                    }

                    # Update file transfer list
                    logging.info(transfer_progress_new)
                    self.update_progress_new.emit(transfer_progress_new, self.profile_name)

                    # Update profile status message.
                    if transfer_complete:
                        self.profile_status["status_message"] = "OneDrive sync is complete"

                elif "% |" in stdout and file_name is not None:
                    # Capture upload/download progress status

                    file_operation = re.search(r"\b([Uploading|Downloading]+)*", stdout).group(1)
                    progress = re.search(r"\s([0-9]+)%", stdout).group(1)
                    transfer_complete = progress == "100"

                    transfer_progress_new = {
                        "file_operation": file_operation,
                        "file_path": "unknown file name" if file_path is None else file_path.group(1),
                        "progress": progress,
                        "transfer_complete": transfer_complete,
                    }

                    logging.info(transfer_progress_new)
                    self.update_progress_new.emit(transfer_progress_new, self.profile_name)

                    if transfer_complete:
                        self.profile_status["status_message"] = "OneDrive sync is complete"
                    else:
                        self.profile_status["status_message"] = "OneDrive sync in progress..."
                    self.update_profile_status.emit(self.profile_status, self.profile_name)

                else:
                    pass

        if self.onedrive_process.stderr:
            # Capture stderr from OneDrive process.

            stderr = self.onedrive_process.stderr.readline()
            if stderr != "":
                if "command not found" in stderr:
                    logging.info(
                        """Onedrive does not seem to be installed. Please install it as per instruction at 
                    https://github.com/abraunegg/onedrive/blob/master/docs/INSTALL.md """
                    )

                elif "--resync is required" in stderr:
                    logging.info(f"[{self.profile_name}] {str(stderr)} Starting resync.")
                    self.trigger_resync.emit()

                    self.run(resync=True)
                else:
                    logging.info("@ERROR " + stderr)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.workers = {}

        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(dir_path + "/resources/images/icons8-clouds-48.png"))

        if len(global_config) == 0:
            # self.pushButton_new_profile.clicked.connect(self.show_settings_window)
            # self.pushButton_new_profile.show()
            # self.show_settings_window()
            self.show_setup_wizard()

        # else:
        self.pushButton_new_profile.hide()

        #
        # Menu
        self.menubar.hide()
        # Update OneDrive Status
        self.actionRefresh_Service_Status.triggered.connect(lambda: self.onedrive_process_status())

        # Start OneDrive service
        self.actionStart_Service.triggered.connect(lambda: os.system("systemctl --user start onedrive"))

        # Stop OneDrive service
        self.actionStop_Service.triggered.connect(lambda: os.system("systemctl --user stop onedrive"))

        # Restart OneDrive service
        self.actionRestart_Service.triggered.connect(lambda: os.system("systemctl --user restart onedrive"))

        # Start OneDrive monitoring
        self.actionStart_Monitor.triggered.connect(lambda: self.start_onedrive_monitor(""))

        # Stop OneDrive monitoring
        self.actionStop_Monitor.triggered.connect(lambda: os.system("pkill onedrive"))

        # Refresh Sync Status
        # self.actionObtain_Sync_Status.triggered.connect(lambda: self.label_4.setText("Retreiving status..."))
        # self.actionObtain_Sync_Status.triggered.connect(lambda: self.onedrive_sync_status())

        # Start second account
        self.actionstart.triggered.connect(lambda: self.start_onedrive_monitor(""))

        self.comboBox.activated.connect(self.switch_account_status_page)
        self.stackedLayout = QStackedLayout()

        self.profile_status_pages = {}
        for profile in global_config:
            self.comboBox.addItem(profile)
            self.profile_status_pages[profile] = ProfileStatusPage(profile)
            self.stackedLayout.addWidget(self.profile_status_pages[profile])

        self.verticalLayout_2.addLayout(self.stackedLayout)

        # System Tray
        self.tray = QSystemTrayIcon()
        if self.tray.isSystemTrayAvailable():

            icon = QIcon(dir_path + "/resources/images/icons8-clouds-48.png")
            menu = QMenu()

            actionshow = menu.addAction("Show/Hide")
            actionshow.triggered.connect(lambda: self.hide() if self.isVisible() else self.show())
            setting_action = menu.addAction("Settings")
            setting_action.triggered.connect(self.show_settings_window)
            quit_action = menu.addAction("Quit")
            quit_action.triggered.connect(sys.exit)

            self.tray.activated.connect(lambda: self.hide() if self.isVisible() else self.show())
            self.tray.setIcon(icon)
            self.tray.setContextMenu(menu)
            self.tray.show()
            self.tray.setToolTip("OneDriveGUI")

        else:
            self.tray = None

        self.refresh_process_status = QTimer()
        self.refresh_process_status.setSingleShot(False)
        self.refresh_process_status.timeout.connect(lambda: self.onedrive_process_status())
        self.refresh_process_status.start(500)

        self.check_client_version = QTimer()
        self.check_client_version.setSingleShot(True)
        self.check_client_version.timeout.connect(self.client_version_check)
        self.check_client_version.start(500)

        self.auto_sync = QTimer()
        self.auto_sync.setSingleShot(True)
        self.auto_sync.timeout.connect(self.autostart_monitor)
        self.auto_sync.start(1000)

    def closeEvent(self, event):
        event.ignore()
        self.hide()

    def show_setup_wizard(self):
        self.setup_wizard = SetupWizard()
        self.setup_wizard.show()

    def show_settings_window(self):
        # self.settings_window = SettingsWindow()
        settings_window.show()

    def switch_account_status_page(self):
        self.stackedLayout.setCurrentIndex(self.comboBox.currentIndex())

    def client_version_check(self):
        pixmap_warning = QPixmap(dir_path + "/resources/images/warning.png").scaled(20, 20, Qt.KeepAspectRatio)
        s = requests.Session()
        version_label_text = ""
        version_tooltip_text = ""

        try:
            latest_url = "https://api.github.com/repos/abraunegg/onedrive/releases/latest"
            latest_client_version = s.get(latest_url).json()["tag_name"]
            client_version_check = subprocess.check_output(["onedrive", "--version"], stderr=subprocess.STDOUT)
            installed_client_version = re.search(r".\s(v[0-9.]+)", str(client_version_check)).group(1)
            installed_client_version_num = int(installed_client_version.replace("v", "").replace(".", ""))
            min_supported_version_num = 2415
            min_requirements_met = True

            result = {
                "latest_client_version": latest_client_version,
                "installed_client_version": installed_client_version,
            }
            logging.debug(f"[GUI] Client version check: {result}")

            if latest_client_version not in installed_client_version:
                version_label_text = "OneDrive client is out of date!"
                version_tooltip_text = f"OneDrive client is out of date! \n Installed: {installed_client_version} \n Latest: {latest_client_version}"

            if installed_client_version_num < min_supported_version_num:
                version_label_text = 'Unsupported OneDrive client! Please <a href="https://github.com/abraunegg/onedrive/blob/master/docs/INSTALL.md" style="color:#FFFFFF;">upgrade</a> it.'
                version_tooltip_text = f"OneDrive Client version not supported! Please upgrade it. \n Installed: {installed_client_version} \n Latest: {latest_client_version}"
                min_requirements_met = False

        except FileNotFoundError as e:
            logging.error(f"OneDrive Client not found: {e}")
            version_label_text = 'OneDrive Client not found! Please <a href="https://github.com/abraunegg/onedrive/blob/master/docs/INSTALL.md" style="color:#FFFFFF;">install</a> it.'
            version_tooltip_text = f"OneDrive Client not found! Please install it."
            min_requirements_met = False

        except Exception as e:
            logging.error(f"Client version check failed: {e}")

        finally:
            for profile_name in global_config:
                self.profile_status_pages[profile_name].label_onedrive_status.setOpenExternalLinks(True)
                self.profile_status_pages[profile_name].label_onedrive_status.setText(version_label_text)

                if not min_requirements_met:
                    self.profile_status_pages[profile_name].toolButton_start.setEnabled(False)
                    self.profile_status_pages[profile_name].pushButton_settings.setEnabled(False)
                    self.profile_status_pages[profile_name].label_version_check.setToolTip(version_tooltip_text)
                    self.profile_status_pages[profile_name].label_version_check.setPixmap(pixmap_warning)

    def onedrive_process_status(self):
        # Check OneDrive status
        # logging.info(self.workers)
        pixmap_running = QPixmap(dir_path + "/resources/images/icons8-green-circle-48.png").scaled(
            20, 20, Qt.KeepAspectRatio
        )
        pixmap_stopped = QPixmap(dir_path + "/resources/images/icons8-red-circle-48.png").scaled(
            20, 20, Qt.KeepAspectRatio
        )

        for profile_name in global_config:
            # logging.info(profile_name)
            if profile_name not in self.workers:
                self.profile_status_pages[profile_name].label_status.setText("stopped")
                self.profile_status_pages[profile_name].label_status.setPixmap(pixmap_stopped)
                # logging.info(f"not running {profile_name}")

            else:
                if self.workers[profile_name].isRunning():
                    self.profile_status_pages[profile_name].label_status.setText("running")
                    self.profile_status_pages[profile_name].label_status.setPixmap(pixmap_running)
                    # logging.info(f"running worker {profile_name}")

    def autostart_monitor(self):
        # Auto-start sync if compatible version of OneDrive client is installed.

        for profile_name in global_config:
            logging.debug(
                f"[{profile_name}] Compatible client version found: {self.profile_status_pages[profile_name].toolButton_start.isEnabled()}"
            )
            logging.debug(
                f"[{profile_name}] Auto-sync enabled for profile: {global_config[profile_name]['auto_sync']}"
            )

            if (
                self.profile_status_pages[profile_name].toolButton_start.isEnabled()
                and global_config[profile_name]["auto_sync"] == "True"
            ):
                self.start_onedrive_monitor(profile_name)

    def start_onedrive_monitor(self, profile_name):
        # for profile in global_config:

        if profile_name not in self.workers:
            self.workers[profile_name] = WorkerThread(profile_name)
            self.workers[profile_name].start()
        else:
            logging.info(f"Worker for profile {profile_name} is already running. Please stop it first.")
            logging.info(f"Running workers: {main_window.workers}")

        # self.worker = WorkerThread()
        # self.worker.start()
        self.workers[profile_name].update_credentials.connect(self.show_login)
        # self.worker.update_progress.connect(self.event_update_progress)
        # self.worker.trigger_resync.connect(self.show_login)
        self.workers[profile_name].update_progress_new.connect(self.event_update_progress_new)
        self.workers[profile_name].update_profile_status.connect(self.event_update_profile_status)
        self.workers[profile_name].started.connect(lambda: logging.info(f"started worker {profile_name}"))
        self.workers[profile_name].finished.connect(lambda: logging.info(f"finished worker {profile_name}"))

    def event_update_profile_status(self, data, profile):
        self.profile_status_pages[profile].label_onedrive_status.setText(data["status_message"])
        self.profile_status_pages[profile].label_free_space.setText(data["free_space"])
        self.profile_status_pages[profile].label_account_type.setText(data["account_type"])

    def event_update_progress_new(self, data, profile):
        """
        data:
        transfer_progress = {
            "file_operation": file_operation.group(1),
            "file_path": file_path.group(1),
            "progress": progress.group(1),
            "transfer_complete": transfer_complete
        }
        """
        _sync_dir = os.path.expanduser(global_config[profile]["onedrive"]["sync_dir"].strip('"'))
        # profile_status_page = self.profile_status_pages[profile]

        logging.info(data)
        file_path = f"{_sync_dir}" + "/" + data["file_path"]
        absolute_path = QFileInfo(file_path).absolutePath().replace(" ", "%20")
        parent_dir = re.search(r".+/([^/]+)/.+$", file_path).group(1)
        file_size = QFileInfo(file_path).size()
        file_size_human = humanize_file_size(file_size)
        file_name = QFileInfo(file_path).fileName()
        file_path2 = QFileInfo(file_path).filePath()
        progress = data["progress"]
        progress_data = file_size / 100 * int(progress)
        progress_data_human = humanize_file_size(progress_data)
        file_operation = data["file_operation"]
        transfer_complete = data["transfer_complete"]

        logging.info("absolute path " + absolute_path)

        logging.info("parent dir " + parent_dir)
        logging.info("progress: " + progress)
        logging.info("progress data: " + humanize_file_size(progress_data))
        logging.info("file path: " + file_path)
        logging.info("file size: " + humanize_file_size(file_size))
        logging.info("file name: " + file_name)
        logging.info("file path2: " + file_path2)

        # Delete last item list if it has the same file name.
        if self.profile_status_pages[profile].listWidget.item(0) != None:
            last_item = self.profile_status_pages[profile].listWidget.item(0)
            last_item_widget = self.profile_status_pages[profile].listWidget.itemWidget(last_item)
            last_file_name = last_item_widget.get_file_name()
            logging.info(f"The last list item's file name is : {last_file_name}")

            if file_name == last_file_name:
                logging.info("Deleting last list item")
                self.profile_status_pages[profile].listWidget.takeItem(0)

        myQCustomQWidget = TaskList()
        myQCustomQWidget.set_file_name(file_name)
        myQCustomQWidget.set_progress(int(progress))
        myQCustomQWidget.set_icon(file_path)
        myQCustomQWidget.hide_progress_bar(transfer_complete)

        if file_operation == "Deleting":
            myQCustomQWidget.set_label_1(f"Deleted from {parent_dir}")
            myQCustomQWidget.set_label_2(f"")

        elif transfer_complete:
            myQCustomQWidget.set_label_1(f"Available in <a href=file:///{absolute_path}>{parent_dir}</a>")
            myQCustomQWidget.set_label_2(f"{file_size_human}")
        else:
            myQCustomQWidget.set_label_1(file_operation)
            myQCustomQWidget.set_label_2(f"{progress_data_human} of {file_size_human}")

        # Create QListWidgetItem
        myQListWidgetItem = QListWidgetItem()

        # Set size hint
        myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())

        # Add QListWidgetItem into QListWidget
        self.profile_status_pages[profile].listWidget.insertItem(0, myQListWidgetItem)
        self.profile_status_pages[profile].listWidget.setItemWidget(myQListWidgetItem, myQCustomQWidget)

    def show_login(self, profile):
        # Show login window
        self.window1 = QWidget()
        self.window1.setWindowIcon(QIcon(dir_path + "/resources/images/icons8-clouds-48.png"))
        self.lw = Ui_LoginWindow()
        self.lw.setupUi(self.window1)
        self.window1.show()
        self.window1.setWindowTitle(f"OneDrive login for profile {profile}")

        self.config_file = global_config[profile]["config_file"].strip('"')
        self.config_dir = re.search(r"(.+)/.+$", self.config_file).group(1)

        # use static URL for now. TODO: use auth files in the future
        url = (
            "https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=d50ca740-c83f-4d1b-b616"
            "-12c519384f0c&scope=Files.ReadWrite%20Files.ReadWrite.all%20Sites.Read.All%20Sites.ReadWrite.All"
            "%20offline_access&response_type=code&prompt=login&redirect_uri=https://login.microsoftonline.com"
            "/common/oauth2/nativeclient"
        )
        self.lw.loginFrame.setUrl(QUrl(url))

        # Wait for user to login and obtain response URL
        self.lw.loginFrame.urlChanged.connect(
            lambda: self.get_response_url(self.lw.loginFrame.url().toString(), self.config_dir, profile)
        )

    def get_response_url(self, response_url, config_dir, profile):
        # Get response URL from OneDrive OAuth2
        if "nativeclient?code=" in response_url:
            logging.info(f'onedrive --confdir="{config_dir}" --auth-response "{response_url}"')
            os.system(f'onedrive --confdir="{config_dir}" --auth-response "{response_url}"')
            logging.info("Login performed")
            self.window1.hide()
            main_window.workers[profile].stop_worker()
            main_window.profile_status_pages[profile].label_onedrive_status.setText(
                "You have been logged in. Start sync manually."
            )
        else:
            pass


def humanize_file_size(num, suffix="B"):
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"


def read_config(config_file):
    with open(config_file, "r") as f:
        config_string = "[onedrive]\n" + f.read()

    config = ConfigParser()
    config.read_string(config_string)

    return config


def create_global_config():
    """
    Creates dict which is used as running global config.
    EXAMPLE:

    {
    "bob@live.com": {
        "config_file": "/home/bob/.config/onedrive/accounts/bob@live.com/config",
        "enable_debug": "True",
        "mode": "monitor",
        "auto_sync": False,
        "onedrive": {
            "sync_dir": '"~/OneDrive"',
            "skip_file": '"~*|.~*|*.tmp|*.txt|*.exe|.testfile"',
            "monitor_interval": '"15"',
            ...},
    "john@live.com": {
        "config_file": "/home/bob/.config/onedrive/accounts/john@live.com/config",
        "enable_debug": "True",
        "mode": "monitor",
        "auto_sync": False,
        "onedrive": {
            "sync_dir": '"~/OneDrive2"',
            "skip_file": '"~*|.~*|*.tmp|*.txt|*.exe"',
            "monitor_interval": '"15"', ...}
    """

    # Load all default values. Needed for cases when imported config does not contain all properties.
    _default_od_config = read_config(dir_path + "/resources/default_config")
    _default_profile_config = {"auto_sync": False}
    default_od_config = _default_od_config._sections

    # Load existing user profiles.
    _profiles = ConfigParser()
    _profiles.read(PROFILES_FILE)
    profiles = _profiles._sections

    for profile in profiles:
        profile_config_file = profiles[profile]["config_file"]
        _od_config = read_config(profile_config_file)
        od_config = _od_config._sections

        if "auto_sync" not in profiles[profile]:  # add 'auto_sync' value if from older versions
            profiles[profile].update(_default_profile_config)
        profiles[profile].update(default_od_config)
        profiles[profile].update(od_config)

    logging.debug(profiles)
    return profiles


def save_global_config():
    # Save all OneDrive config files after configuration change.
    #
    # Save GUI profile file changes
    #
    _profile_config = copy.deepcopy(global_config)
    logging.debug(f"[save_global_config]:[1]{_profile_config}")

    for profile in _profile_config:
        _profile_config[profile].pop("onedrive", None)

    logging.debug(f"[save_global_config]:[2]{_profile_config}")
    logging.debug(f"[save_global_config]:[3]{global_config}")

    profile_config = ConfigParser()
    profile_config.read_dict(_profile_config)

    # Create profile config file if it does not exist.
    profiles_dir = re.search(r"(.+)/profiles$", PROFILES_FILE).group(1)
    if not os.path.exists(profiles_dir):
        os.makedirs(profiles_dir)

    # Save the new profile.
    with open(PROFILES_FILE, "w") as profilefile:
        profile_config.write(profilefile)

    for profile in global_config:

        #
        # Save OneDrive config changes
        #
        od_config_file = os.path.expanduser(global_config[profile]["config_file"].strip('"'))

        _od_config = {}
        _od_config["onedrive"] = global_config[profile]["onedrive"]

        od_config = ConfigParser()
        od_config.read_dict(_od_config)

        # Backup last config
        os.system(f"cp {od_config_file} {od_config_file}_backup")

        # Save OD config changes.
        directory = re.search(r"(.+)/.+$", od_config_file).group(1)
        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(od_config_file, "w") as f:
            od_config.write(f)

        # Remove first line (section) from config file so that OneDrive can read it.
        with open(od_config_file, "r") as input:
            data = input.read().splitlines(True)
        with open(od_config_file, "w") as output:
            output.writelines(data[1:])

        logging.info(f"{profile} config saved")

    logging.info("All configs saved")
    logging.debug(global_config)


if __name__ == "__main__":
    global_config = create_global_config()

    app = QApplication(sys.argv)
    app.setApplicationName("OneDriveGUI")
    app.setWindowIcon(QIcon(dir_path + "/resources/images/icons8-clouds-48.png"))

    main_window = MainWindow()
    settings_window = SettingsWindow()
    settings_window.hide()

    app.exec()
