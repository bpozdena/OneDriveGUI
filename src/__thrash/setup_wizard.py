import subprocess
import re
import os
from configparser import ConfigParser

from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import Property, Qt
from PySide6.QtWidgets import (
    QWizard,
    QGridLayout,
    QLineEdit,
    QWizardPage,
    QLabel,
    QVBoxLayout,
    QComboBox,
    QApplication,
    QCheckBox,
    QPushButton,
)

from OneDriveGUI import read_config


class SetupWizard(QWizard):
    def __init__(self, parent=None):
        super(SetupWizard, self).__init__(parent)
        self.setWindowIcon(QIcon("resources/images/icons8-clouds-48.png"))
        self.setPage(1, WizardPage_welcome(self))
        self.setPage(2, wizardPage_version_check(self))
        self.setPage(3, wizardPage_create_import(self))
        self.setPage(4, wizardPage_import(self))

        self.setWindowTitle("OneDriveGUI Setup Wizard")
        self.resize(640, 480)

        self.currentIdChanged.connect(self.on_page_change)

    def on_page_change(self):
        if self.currentId() == 2:
            print("Checking installed OneDrive version")
            self.page(2).check_onedrive_version()        

  
class WizardPage_welcome(QWizardPage):
    def __init__(self, parent=None):
        super(WizardPage_welcome, self).__init__(parent)

        self.setTitle("Welcome to OneDriveGUI")
        # self.setSubTitle("SubTitle")

        # self.label1 = QLabel()
        # self.label1.setText("Welcome to OneDriveGUI")

        self.label_2 = QLabel()
        self.label_2.setText("This wizard will help you with initial OneDrive profile creation/import.")

        layout = QVBoxLayout()
        # layout.addWidget(self.label1)
        layout.addWidget(self.label_2)
        self.setLayout(layout)



class wizardPage_version_check(QWizardPage):
    def __init__(self, parent=None):
        super(wizardPage_version_check, self).__init__(parent)
        self.setTitle("OneDrive version check")

        # self.label_3 = QLabel()
        # self.label_3.setText("Installed OneDrive version:")

        self.label_4 = QLabel()
        self.label_4.setText("Installed/Not Installed/ version")

        self.label_5 = QLabel()
        self.label_5.setWordWrap(True)
        self.label_5.setText(
            "OneDrive Client for Linux does not seem to be installed. Please install it by following " \
            "<a href='https://github.com/abraunegg/onedrive/blob/master/docs/INSTALL.md'>instructions</a> for your distro. "
        )

        layout = QVBoxLayout()
        # layout.addWidget(self.label_3)
        layout.addWidget(self.label_4)
        layout.addWidget(self.label_5)
        self.setLayout(layout)

    def check_onedrive_version(self):
        # Check if OneDrive is installed
        od_version_check = subprocess.check_output(["onedrive", "--version"])
        if "onedrive v" in str(od_version_check):
            self.od_version = re.search(r".\s(v[0-9.]+)", str(od_version_check)).group(1)
            print(f"OneDrive {self.od_version} detected.")
            self.label_4.setText(f"OneDrive {self.od_version} detected.")
            self.label_5.hide()
            return True
        else:
            self.label_4.setText("OneDrive not detected.")
            return False      


     
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
            print(f"Create new profile is checked")
            self.checkBox_import.setDisabled(True)
            # self.wizardPage_create_import.completeChanged()

        elif self.checkBox_import.isChecked():
            print(f"Import profile is checked")
            self.checkBox_create.setDisabled(True)
            # self.wizardPage_create_import.completeChanged()

        else:
            print(f"No option is unchecked")
            self.checkBox_import.setDisabled(False)
            self.checkBox_create.setDisabled(False)


class wizardPage_import(QWizardPage):
    def __init__(self, parent=None):
        super(wizardPage_import, self).__init__(parent)
        self.setTitle("Create/Import OneDrive profile")

        self.label_profile_name = QLabel()
        self.label_profile_name.setText("Profile name")

        self.label_config_path = QLabel()
        self.label_config_path.setText("Config fil path")


        self.lineEdit_profile_name = QLineEdit()
        self.lineEdit_profile_name.setPlaceholderText("E.g. john@live.com")

        self.lineEdit_config_path = QLineEdit()
        self.lineEdit_config_path.setPlaceholderText("E.g. ~/.config/onedrive/config")


        self.pushButton_import = QPushButton()


        layout = QVBoxLayout()
        layout.addWidget(self.label_profile_name)
        layout.addWidget(self.label_config_path)
        layout.addWidget(self.lineEdit_profile_name)
        layout.addWidget(self.lineEdit_config_path)
        layout.addWidget(self.pushButton_import)
        self.setLayout(layout)        
   
    def import_profile(self):
        """
        Imports pre-existing OneDrive profile.
        Loads default values firt, then overwrite them with user settings.
        This is to handle cases where imported config contains only some properties.
        """

        profile_name = self.lineEdit_profile_name.text()
        config_path = os.path.expanduser(self.lineEdit_config_path.text())

        # Load all default values.
        _default_od_config = read_config("resources/default_config")
        default_od_config = _default_od_config._sections

        # Load user's settings.
        _new_od_config = read_config(config_path)
        new_od_config = _new_od_config._sections

        # Construct dict with user profile settings.
        new_profile = {profile_name: {"config_file": config_path, "enable_debug": False, "mode": "monitor"}}

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
        # print(new_profile)
        # print(global_config)

        self.settings_window.listWidget_profiles.addItem(profile_name)
        self.setting_page = ProfileSettingsPage(profile_name)
        self.settings_window.stackedLayout.addWidget(self.setting_page)

        # Add status page widget for new profile
        main_window.comboBox.addItem(profile_name)
        main_window.profile_status_pages[profile_name] = ProfileStatusPage(profile_name)
        main_window.stackedLayout.addWidget(main_window.profile_status_pages[profile_name])

        # Hide "Create profile" push button from main windows.
        main_window.pushButton_new_profile.hide()

        print(f"Account {profile_name} has been imported")
        self.pushButton_import.setText("Done")
        self.pushButton_import.setDisabled(True)





