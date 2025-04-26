from PySide6.QtCore import Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QVBoxLayout,
    QLabel,
    QWizard,
    QWizardPage,
    QLineEdit,
    QCheckBox,
    QPushButton,
    QFormLayout,
    QGridLayout,
    QFileDialog,
    QComboBox,
)

import re
import os
import sys
import copy
import requests
import subprocess
from configparser import ConfigParser

from global_config import save_global_config, read_config
from options import (
    global_config,
    temp_global_config,
    client_bin_path,
    gui_settings,
    version,
)

from workers import MaintenanceWorker
import logging
from global_config import DIR_PATH, PROFILES_FILE


class SetupWizard(QWizard):
    show_main_window_signal = Signal()
    add_profile_signal = Signal(str)

    def __init__(self, parent=None):
        super(SetupWizard, self).__init__(parent)
        self.setWindowIcon(QIcon(DIR_PATH + "/resources/images/icons8-clouds-80-dark-edge.png"))

        self.setPage(1, WizardPage_welcome(self))
        self.setPage(2, wizardPage_version_check(self))
        self.setPage(3, wizardPage_create_import(self))
        self.setPage(4, wizardPage_create(self))
        self.setPage(5, wizardPage_import(self))
        self.setPage(6, wizardPage_create_shared_library(self))
        self.setPage(10, wizardPage_finish(self))

        self.setWindowTitle("OneDriveGUI Setup Wizard")
        self.resize(640, 480)

        self.currentIdChanged.connect(self.on_page_change)
        # self.profile_settings_window = profile_settings_window

    def showEvent(self, event):
        """Reset form fields when wizard is shown"""
        super(SetupWizard, self).showEvent(event)

        # Always restart at the first page (Welcome)
        self.restart()

        # Reset the create profile page
        create_page = self.page(4)
        if hasattr(create_page, "lineEdit_new_profile_name"):
            create_page.lineEdit_new_profile_name.setText("")
            create_page.lineEdit_sync_dir.setText("")
            create_page.pushButton_create.setText("Create new profile")
            create_page.pushButton_create.setEnabled(False)
            create_page.lineEdit_new_profile_name.setEnabled(True)
            create_page.lineEdit_sync_dir.setEnabled(True)
            create_page.pushButton_browse.setEnabled(True)

        # Reset the import profile page
        import_page = self.page(5)
        if hasattr(import_page, "lineEdit_profile_name"):
            import_page.lineEdit_profile_name.setText("")
            import_page.lineEdit_config_path.setText("")
            import_page.pushButton_import.setText("Import")
            import_page.pushButton_import.setEnabled(False)
            import_page.lineEdit_profile_name.setEnabled(True)
            import_page.lineEdit_config_path.setEnabled(True)
            import_page.pushButton_browse.setEnabled(True)

        # Reset the create/import selection page
        selection_page = self.page(3)
        if hasattr(selection_page, "checkBox_create"):
            selection_page.checkBox_create.setChecked(False)
            selection_page.checkBox_import.setChecked(False)
            selection_page.checkBox_sharepoint_library.setChecked(False)
            selection_page.checkBox_create.setEnabled(True)
            selection_page.checkBox_import.setEnabled(True)
            selection_page.checkBox_sharepoint_library.setEnabled(True)

    def on_page_change(self):
        if self.currentId() == 2:
            logging.info("Checking installed OneDrive version")
            self.page(2).check_onedrive_version()

    def nextId(self):
        """
        Defines order of wizard pages based on selected options.
        """
        if self.currentPage() == self.page(1):
            return 2
        if self.currentPage() == self.page(2):
            return 3
        if self.currentPage() == self.page(3):
            if self.page(3).checkBox_create.isChecked():
                return 4
            elif self.page(3).checkBox_import.isChecked():
                return 5
            elif self.page(3).checkBox_sharepoint_library.isChecked():
                return 6
        if self.currentPage() == self.page(4):
            return 10
        if self.currentPage() == self.page(5):
            return 10
        if self.currentPage() == self.page(6):
            return 10
        if self.currentPage() == self.page(10):
            self.show_main_window_signal.emit()
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
        try:
            client_version_check = subprocess.check_output([client_bin_path, "--version"], stderr=subprocess.STDOUT)
            installed_client_version = re.search(r"(v[0-9.]+)", str(client_version_check)).group(1)
            installed_client_version_num = int(installed_client_version.replace("v", "").replace(".", ""))
            installed_client_version_num = (
                installed_client_version_num
                if len(str(installed_client_version_num)) > 3
                else installed_client_version_num * 10
            )
            min_supported_version_num = 2500

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
        return True
        # if "not" in self.label_4.text().lower():
        #     return False
        # else:
        #     return True


class wizardPage_create_import(QWizardPage):
    def __init__(self, parent=None):
        super(wizardPage_create_import, self).__init__(parent)
        self.setTitle("Add OneDrive profile")

        self.checkBox_create = QCheckBox()
        self.checkBox_create.setText("Create new OneDrive profile")
        self.checkBox_create.stateChanged.connect(self.on_checkbox_change)

        self.checkBox_import = QCheckBox()
        self.checkBox_import.setText("Import existing OneDrive profile/config")
        self.checkBox_import.stateChanged.connect(self.on_checkbox_change)

        self.checkBox_sharepoint_library = QCheckBox()
        self.checkBox_sharepoint_library.setText("Add SharePoint Shared Library")
        self.checkBox_sharepoint_library.stateChanged.connect(self.on_checkbox_change)

        layout = QVBoxLayout()
        layout.addWidget(self.checkBox_create)
        layout.addWidget(self.checkBox_import)
        layout.addWidget(self.checkBox_sharepoint_library)
        self.setLayout(layout)

    def on_checkbox_change(self):
        if self.checkBox_create.isChecked():
            logging.info(f"Create new profile is checked")
            self.checkBox_import.setDisabled(True)
            self.checkBox_sharepoint_library.setDisabled(True)
            self.completeChanged.emit()

        elif self.checkBox_import.isChecked():
            logging.info(f"Import profile is checked")
            self.checkBox_create.setDisabled(True)
            self.checkBox_sharepoint_library.setDisabled(True)
            self.completeChanged.emit()

        elif self.checkBox_sharepoint_library.isChecked():
            logging.info(f"SharePoint Shared Library is checked")
            self.checkBox_create.setDisabled(True)
            self.checkBox_import.setDisabled(True)
            self.completeChanged.emit()

        else:
            logging.info(f"No option is checked")
            self.checkBox_import.setDisabled(False)
            self.checkBox_create.setDisabled(False)
            self.checkBox_sharepoint_library.setDisabled(False)
            self.completeChanged.emit()

    def isComplete(self):
        if any(
            [
                self.checkBox_create.isChecked(),
                self.checkBox_import.isChecked(),
                self.checkBox_sharepoint_library.isChecked(),
            ]
        ):
            logging.info("Wizard page is complete.")
            return True
        else:
            logging.info("Wizard page is not complete.")
            return False


class wizardPage_create_shared_library(QWizardPage):
    def __init__(self, parent=None):
        self.library_dict = {}

        super(wizardPage_create_shared_library, self).__init__(parent)
        self.setTitle("Add SharePoint Shared Library")

        self.label_1 = QLabel()
        self.label_1.setText("1. Select profile with access to SharePoint Library.")

        self.label_2 = QLabel()
        self.label_2.setText("2. Obtain list of SharePoint Sites")

        self.label_3 = QLabel()
        self.label_3.setText("3. Select a SharePoint Site")

        self.label_4 = QLabel()
        self.label_4.setText("4. Obtain list of Shared Libraries")

        self.label_5 = QLabel()
        self.label_5.setText("4. Select a SharePoint Shared Library")

        self.label_6 = QLabel()
        self.label_6.setText("6. Create profile")

        self.comboBox_profile_list = QComboBox()
        self.comboBox_profile_list.setPlaceholderText("No Business accounts detected.")

        self.pushButton_get_sites = QPushButton()
        self.pushButton_get_sites.setText("Get SharePoint Sites")
        self.pushButton_get_sites.setDisabled(True)
        self.pushButton_get_sites.clicked.connect(self.get_sharepoint_site_list)

        self.comboBox_sharepoint_site_list = QComboBox()
        self.comboBox_sharepoint_site_list.setDisabled(True)

        self.pushButton_get_libraries = QPushButton()
        self.pushButton_get_libraries.setText("Get Shared Libraries")
        self.pushButton_get_libraries.setDisabled(True)
        self.pushButton_get_libraries.clicked.connect(self.get_library_drive_ids)

        self.comboBox_sharepoint_library_list = QComboBox()
        self.comboBox_sharepoint_library_list.setDisabled(True)

        self.pushButton_create_profile = QPushButton()
        self.pushButton_create_profile.clicked.connect(self.create_library_profile)
        self.pushButton_create_profile.setText("Create Profile")
        self.pushButton_create_profile.setDisabled(True)

        for profile in global_config:
            if global_config[profile]["account_type"] == "Business":
                self.comboBox_profile_list.addItem(profile)
                self.comboBox_profile_list.setPlaceholderText("")
                self.pushButton_get_sites.setDisabled(False)

        layout = QGridLayout()
        layout.addWidget(self.label_1, 0, 0)
        layout.addWidget(self.comboBox_profile_list, 0, 1)
        layout.addWidget(self.label_2, 1, 0)
        layout.addWidget(self.pushButton_get_sites, 1, 1)
        layout.addWidget(self.label_3, 2, 0)
        layout.addWidget(self.comboBox_sharepoint_site_list, 2, 1)
        layout.addWidget(self.label_4, 3, 0)
        layout.addWidget(self.pushButton_get_libraries, 3, 1)
        layout.addWidget(self.label_5, 4, 0)
        layout.addWidget(self.comboBox_sharepoint_library_list, 4, 1)
        layout.addWidget(self.label_6, 5, 0)
        layout.addWidget(self.pushButton_create_profile, 5, 1)

        self.setLayout(layout)

    def isComplete(self):
        if self.pushButton_create_profile.text() == "Done":
            return True
        return False

    def get_sharepoint_site_list(self):
        """
        Starts OneDrive with --get-sharepoint-drive-id argument and populates comboBox list of SharePoint Sites emitted by MaintenanceWorker.
        """
        profile_name = self.comboBox_profile_list.currentText()
        options = "--get-sharepoint-drive-id 'non-existent-library'"

        self.pushButton_get_sites.setDisabled(True)
        self.pushButton_get_sites.setText("Please wait...")

        logging.info(f"[GUI] Starting maintenance worker to obtain SharePoint Library List for profile {profile_name}.")

        # Create and configure the worker before connecting signals
        self.obtain_sharepoint_site_list = MaintenanceWorker(profile_name, options)

        # Connect signals before starting the worker
        self.obtain_sharepoint_site_list.update_sharepoint_site_list.connect(
            self.populate_comboBox_sharepoint_site_list
        )

        # Process events to ensure UI stays responsive
        from PySide6.QtCore import QCoreApplication

        QCoreApplication.processEvents()

        # Start the worker after all connections are set up
        self.obtain_sharepoint_site_list.start()

    def populate_comboBox_sharepoint_site_list(self, sharepoint_site_list):
        """
        Populates comboBox_sharepoint_site_list with a list of emitted SharePoint Sites.
        """
        if len(sharepoint_site_list) == 0:
            self.comboBox_sharepoint_site_list.setPlaceholderText("Failed to fetch SharePoint Site list.")
            self.comboBox_sharepoint_site_list.setDisabled(True)

            self.pushButton_get_sites.setDisabled(False)
            self.pushButton_get_sites.setText("Get SharePoint Sites")

        else:
            self.comboBox_sharepoint_site_list.setPlaceholderText("")
            self.comboBox_sharepoint_site_list.addItems(sorted(sharepoint_site_list, key=str.casefold))
            self.comboBox_sharepoint_site_list.setDisabled(False)

            self.comboBox_profile_list.setDisabled(True)

            self.pushButton_get_sites.setDisabled(True)
            self.pushButton_get_sites.setText("Done")

            self.comboBox_sharepoint_site_list.setDisabled(False)
            self.pushButton_get_libraries.setDisabled(False)

    def get_library_drive_ids(self):
        """
        Starts OneDrive with --get-sharepoint-drive-id argument to obtain names and drive_ids
        of available SharePoint Shared Libraries within selected SharePoint Site.

        Once libraries are obtained, the worker emits dict {'Documents': 'b!SeGaP5QU4UWy...', 'test': 'b!SeGaP5QU4UWySy...'}
        """
        profile_name = self.comboBox_profile_list.currentText()
        library_name = self.comboBox_sharepoint_site_list.currentText()
        options = f"--get-sharepoint-drive-id '{library_name}'"

        self.pushButton_get_libraries.setText("Please wait...")
        self.pushButton_get_libraries.setDisabled(True)
        self.comboBox_sharepoint_site_list.setDisabled(True)

        logging.info(
            f"[GUI] Starting maintenance worker to obtain SharePoint Library Drive ID for library {library_name} from profile {profile_name}."
        )

        self.obtain_library_drive_ids = MaintenanceWorker(profile_name, options)
        self.obtain_library_drive_ids.start()
        self.obtain_library_drive_ids.update_library_list.connect(self.populate_comboBox_sharepoint_library_list)

    def populate_comboBox_sharepoint_library_list(self, library_dict):
        """
        Populates comboBox_sharepoint_library_list with keys from emitted
        SharePoint library dict {'Documents': 'b!SeGaP5QU4UWy...', 'test': 'b!SeGaP5QU4UWySy...'}
        """

        self.library_dict = library_dict  # Make dictionary available for create_library_profile()

        if len(library_dict) == 0:
            self.comboBox_sharepoint_library_list.setPlaceholderText("Failed to fetch Shared Libraries.")
            self.comboBox_sharepoint_library_list.setDisabled(True)

            self.pushButton_get_libraries.setDisabled(False)
            self.pushButton_get_libraries.setText("Get Shared Libraries")

        else:
            self.list_of_libraries = sorted(library_dict.keys(), key=str.casefold)

            self.comboBox_sharepoint_library_list.setPlaceholderText("")
            self.comboBox_sharepoint_library_list.addItems(self.list_of_libraries)
            self.comboBox_sharepoint_library_list.setDisabled(False)

            self.pushButton_get_libraries.setDisabled(True)
            self.pushButton_get_libraries.setText("Done")

            self.comboBox_sharepoint_site_list.setDisabled(True)
            self.pushButton_create_profile.setDisabled(False)

    def create_library_profile(self):
        """
        1 - Create new profile for SharePoint Library
        2 - Load default settings
        3 - Set 'sync_dir' based on Site and Library name
        4 - Set 'drive_id'
        """
        # Stop checking for unsaved changes while new profile is being created.
        # self.profile_settings_window.stop_unsaved_changes_timer()

        logging.info(f"[GUI] Available Libraries:  {self.library_dict}")
        _site_name = self.comboBox_sharepoint_site_list.currentText()
        _library_name = self.comboBox_sharepoint_library_list.currentText()
        _library_id = self.library_dict[_library_name]
        profile_name = f"SharePoint_{_site_name.replace(' ', '_')}_{_library_name.replace(' ', '_')}"

        sync_dir = os.path.expanduser(f"~/{profile_name}")
        config_path = os.path.expanduser(f"~/.config/onedrive/accounts/{profile_name}/config")

        # Load all default values.
        _default_od_config = read_config(DIR_PATH + "/resources/default_config")
        default_od_config = _default_od_config._sections

        # Construct dict with user profile settings.
        new_profile = {
            profile_name: {
                "config_file": config_path,
                "auto_sync": False,
                "account_type": "",
                "free_space": "",
            }
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

        # Set SharePoint Library Drive ID
        new_profile[profile_name]["onedrive"]["drive_id"] = f'"{_library_id}"'

        # Append new profile into running global profile
        _global_config = copy.deepcopy(new_profile)
        _temp_global_config = copy.deepcopy(new_profile)

        global_config.update(_global_config)
        temp_global_config.update(_temp_global_config)

        # Automatically save global config to prevent loss if user does not press 'Save' button.
        save_global_config(global_config)

        # Add Setting page widget for new profile
        # self.profile_settings_window.listWidget_profiles.addItem(profile_name)
        # # self.setting_page = ProfileSettingsPage(profile_name)
        # self.profile_settings_window.stackedLayout.addWidget(self.setting_page)

        # # Add status page widget for new profile
        # main_window.comboBox.addItem(profile_name)
        # main_window.profile_status_pages[profile_name] = ProfileStatusPage(profile_name)
        # main_window.stackedLayout.addWidget(main_window.profile_status_pages[profile_name])

        # # Show comboBox with profile list if more than one profiles exist
        # if len(global_config) > 1:
        #     main_window.comboBox.show()

        # Start checking for unsaved changes again after a new profile has been created.
        # self.profile_settings_window.start_unsaved_changes_timer()

        logging.info(f"Account {profile_name} has been created")
        self.pushButton_create_profile.setText("Done")
        self.pushButton_create_profile.setDisabled(True)
        self.comboBox_sharepoint_library_list.setDisabled(True)

        # Emit signal to add the profile to profile settings window and main window
        logging.info(f"[WIZARD] Emitting add_profile_signal for {profile_name}")
        wizard_instance = self.wizard()
        logging.info(f"[WIZARD] wizard_instance: {wizard_instance}")
        if wizard_instance:
            wizard_instance.add_profile_signal.emit(profile_name)
            logging.info(f"[WIZARD] Signal emitted successfully")
        else:
            logging.error(f"[WIZARD] Failed to get wizard instance!")

        self.completeChanged.emit()


class wizardPage_create(QWizardPage):
    add_profile_signal = Signal(str)

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
        """Enables wizard 'Create' button only when below conditions are met."""
        _used_sync_dirs = []  # List of used sync directories.
        _used_profile_names = []  # List of used profile names.

        for profile in global_config:
            _used_sync_dirs.append(global_config[profile]["onedrive"]["sync_dir"].strip('"'))
            _used_profile_names.append(profile)

        if self.lineEdit_new_profile_name.text().strip() == "" or self.lineEdit_sync_dir.text().strip() == "":
            # Do not allow profile creation when input fields are empty.
            self.pushButton_create.setEnabled(False)

        elif self.lineEdit_new_profile_name.text().strip() in _used_profile_names:
            # Do not allow profile creation when profile name is already used.
            self.pushButton_create.setEnabled(False)
            logging.warning(f"[GUI] Profile name '{self.lineEdit_new_profile_name.text()}' is already used!")

        elif self.lineEdit_sync_dir.text().strip() in _used_sync_dirs:
            # Do not allow profile creation when sync_dir is already used for different profile.
            self.pushButton_create.setEnabled(False)
            logging.warning(f"[GUI] Sync dir '{self.lineEdit_sync_dir.text()}' is already used by different profile!")

        else:
            self.pushButton_create.setEnabled(True)

    def create_profile(self):
        """
        Creates new profile and loads default settings.
        TODO: Consolidate with import_profile()
        """
        # Stop checking for unsaved changes while new profile is being created.
        # self.profile_settings_window.stop_unsaved_changes_timer()

        profile_name = self.lineEdit_new_profile_name.text()
        sync_dir = self.lineEdit_sync_dir.text()
        config_path = os.path.expanduser(f"~/.config/onedrive/accounts/{profile_name}/config")

        # Load all default values.
        _default_od_config = read_config(DIR_PATH + "/resources/default_config")
        default_od_config = _default_od_config._sections

        # Construct dict with user profile settings.
        new_profile = {
            profile_name: {
                "config_file": config_path,
                "auto_sync": False,
                "account_type": "",
                "free_space": "",
            }
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
        _global_config = copy.deepcopy(new_profile)
        _temp_global_config = copy.deepcopy(new_profile)

        global_config.update(_global_config)
        temp_global_config.update(_temp_global_config)

        # Automatically save global config to prevent loss if user does not press 'Save' button.
        save_global_config(global_config)

        # Add Setting page widget for new profile
        # Emit signal to add the profile to profile settings window and main window
        logging.info(f"[WIZARD] Emitting add_profile_signal for {profile_name}")
        wizard_instance = self.wizard()
        logging.info(f"[WIZARD] wizard_instance: {wizard_instance}")
        if wizard_instance:
            wizard_instance.add_profile_signal.emit(profile_name)
            logging.info(f"[WIZARD] Signal emitted successfully")
        else:
            logging.error(f"[WIZARD] Failed to get wizard instance!")
        # self.profile_settings_window.listWidget_profiles.addItem(profile_name)
        # # self.setting_page = ProfileSettingsPage(profile_name)
        # self.profile_settings_window.stackedLayout.addWidget(self.setting_page)

        # # Add status page widget for new profile
        # main_window.comboBox.addItem(profile_name)
        # main_window.profile_status_pages[profile_name] = ProfileStatusPage(profile_name)
        # main_window.stackedLayout.addWidget(main_window.profile_status_pages[profile_name])

        # # Show comboBox with profile list if more than one profiles exist
        # if len(global_config) > 1:
        #     main_window.comboBox.show()

        # # Hide "Create profile" push button from main windows.
        # main_window.pushButton_new_profile.hide()

        # Start checking for unsaved changes again after new profile has been created.
        # self.profile_settings_window.start_unsaved_changes_timer()

        logging.info(f"Account {profile_name} has been created")
        self.pushButton_create.setText("Done")
        self.pushButton_create.setDisabled(True)
        self.lineEdit_new_profile_name.setDisabled(True)
        self.lineEdit_sync_dir.setDisabled(True)
        self.pushButton_browse.setDisabled(True)

        # Force UI update immediately
        from PySide6.QtCore import QCoreApplication

        QCoreApplication.processEvents()

        # Signal that this page is complete so the wizard can move to the next page
        self.completeChanged.emit()
        # Force the wizard to advance to the next page
        self.wizard().next()


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
        profile_name_filled = self.lineEdit_profile_name.text().strip() != ""

        config_specified = re.search(r"/config$", self.lineEdit_config_path.text().strip()) != None
        config_path = os.path.expanduser(self.lineEdit_config_path.text().strip())
        config_exists = os.path.exists(config_path)
        unique_profile_name = self.lineEdit_profile_name.text() not in global_config.keys()

        if all([profile_name_filled, config_specified, config_exists, unique_profile_name]):
            self.pushButton_import.setEnabled(True)
        else:
            self.pushButton_import.setEnabled(False)
            if not unique_profile_name:
                logging.warning(f"[GUI] Profile name {self.lineEdit_profile_name.text()} is already used!")
            if not config_specified:
                logging.warning(f"[GUI] Path to config file not specified.")
            if not config_exists:
                logging.warning(f"[GUI] Specified config file '{self.lineEdit_config_path.text().strip()}' not found!")

    def get_config_name(self):
        self.file_dialog = QFileDialog.getOpenFileName(self, dir=os.path.expanduser("~/.config/onedrive"))

        file_name = self.file_dialog[0]

        logging.info(file_name)
        self.lineEdit_config_path.setText(file_name)

    def import_profile(self):
        """
        Imports pre-existing OneDrive profile.
        Loads default values first, then overwrite them with user settings.
        This is to handle cases where imported config contains only some properties.
        """

        # Stop checking for unsaved changes while new profile is being imported.
        # self.profile_settings_window.stop_unsaved_changes_timer()

        profile_name = self.lineEdit_profile_name.text().strip()
        config_path = os.path.expanduser(self.lineEdit_config_path.text())

        # Load all default values.
        _default_od_config = read_config(DIR_PATH + "/resources/default_config")
        default_od_config = _default_od_config._sections
        logging.debug("[GUI] default_od_config: " + str(default_od_config))

        # Load user's settings.
        _new_od_config = read_config(config_path)
        new_od_config = _new_od_config._sections
        logging.debug("[GUI] new_od_config: " + str(new_od_config))

        # Construct dict with user profile settings.
        new_profile = {
            profile_name: {
                "config_file": config_path,
                "auto_sync": False,
                "account_type": "",
                "free_space": "",
            }
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

        # Append new profile into running global profile
        _global_config = copy.deepcopy(new_profile)
        _temp_global_config = copy.deepcopy(new_profile)

        global_config.update(_global_config)
        temp_global_config.update(_temp_global_config)

        # Update GUI with new profile
        # self.profile_settings_window.listWidget_profiles.addItem(profile_name)
        # # self.setting_page = ProfileSettingsPage(profile_name)
        # self.profile_settings_window.stackedLayout.addWidget(self.setting_page)

        # # Add status page widget for new profile
        # main_window.comboBox.addItem(profile_name)
        # main_window.profile_status_pages[profile_name] = ProfileStatusPage(profile_name)
        # main_window.stackedLayout.addWidget(main_window.profile_status_pages[profile_name])

        # # Show comboBox with profile list if more than one profiles exist
        # if len(global_config) > 1:
        #     main_window.comboBox.show()

        # # Hide "Create profile" push button from main window.
        # main_window.pushButton_new_profile.hide()

        # Automatically save global config to prevent loss if user does not press 'Save' button.
        save_global_config(global_config)

        # Emit signal to add the profile to main window and profile settings window
        logging.info(f"[WIZARD] Emitting add_profile_signal for imported profile {profile_name}")
        wizard_instance = self.wizard()
        if wizard_instance:
            wizard_instance.add_profile_signal.emit(profile_name)
            logging.info(f"[WIZARD] Signal emitted successfully for imported profile")
        else:
            logging.error(f"[WIZARD] Failed to get wizard instance!")

        # Start checking for unsaved changes again after new profile has being created.
        # self.profile_settings_window.start_unsaved_changes_timer()

        logging.info(f"Account {profile_name} has been imported")
        self.pushButton_import.setText("Done")
        self.pushButton_import.setDisabled(True)
        self.lineEdit_profile_name.setDisabled(True)
        self.lineEdit_config_path.setDisabled(True)
        self.pushButton_browse.setDisabled(True)
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


# Create a single instance of the wizard
setup_wizard = SetupWizard()
