from PySide6.QtCore import QTimer, Qt, Signal
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import (
    QWidget,
    QStackedLayout,
    QAbstractItemView,
    QFileDialog,
    QMessageBox,
    QStyledItemDelegate,
    QStyleOptionViewItem,
    QInputDialog,
)

# Imports for Profiles windows.
from ui.ui_profile_settings_window import Ui_profile_settings_window
from ui.ui_profile_settings_page import Ui_profile_settings

import re
import os
import copy
from configparser import ConfigParser

# Import setup_wizard after importing wizard, keeping it at the bottom to avoid circular imports
import wizard
from global_config import save_global_config

# Import main_window (lazy import to avoid circular references)
import main_window
from options import client_bin_path, global_config
from options import temp_global_config

from workers import workers

import logging

# from logger import logger
from global_config import DIR_PATH, PROFILES_FILE


class ProfileSettingsWindow(QWidget, Ui_profile_settings_window):
    remove_profile_signal = Signal(str)
    rename_profile_signal = Signal(str, str)  # Signal to emit old_name, new_name

    def __init__(self):
        super(ProfileSettingsWindow, self).__init__()

        # Listen for Signals from wizard
        # Access setup_wizard through the wizard module to avoid circular imports
        wizard.setup_wizard.add_profile_signal.connect(self.add_profile)

        self.unsaved_profiles = []

        self.setupUi(self)
        self.setWindowIcon(QIcon(DIR_PATH + "/resources/images/icons8-clouds-80-dark-edge.png"))
        self.delegate = ListItemDelegate()
        self.listWidget_profiles.setItemDelegate(self.delegate)

        self.stackedLayout = QStackedLayout()

        for profile in global_config:
            logging.info(profile)
            self.listWidget_profiles.addItem(profile)
            self.page = ProfileSettingsPage(profile)
            self.stackedLayout.addWidget(self.page)

        self.horizontalLayout.addLayout(self.stackedLayout)

        self.listWidget_profiles.setCurrentRow(0)
        self.listWidget_profiles.itemSelectionChanged.connect(self.switch_account_settings_page)

        self.pushButton_remove.clicked.connect(self.remove_profile)
        self.pushButton_rename.clicked.connect(self.rename_profile)
        self.pushButton_create_import.clicked.connect(self.show_setup_wizard)

    def add_profile(self, profile):
        self.stop_unsaved_changes_timer()
        self.listWidget_profiles.addItem(profile)
        self.page = ProfileSettingsPage(profile)
        self.stackedLayout.addWidget(self.page)
        self.start_unsaved_changes_timer()

    def closeEvent(self, event):
        event.ignore()
        if len(self.unsaved_profiles) != 0:
            self.close_window_dialog()
        else:
            self.hide()
            self.stop_unsaved_changes_timer()
            logging.debug("[GUI] Closing Profiles window.")

    def close_window_dialog(self):
        close_question = QMessageBox.question(
            self,
            "Discard changes?",
            f"You have unsaved changes in profile(s) <b>{', '.join(self.unsaved_profiles)}</b>.<br><br> Discard changes and close Profiles window?",
            buttons=QMessageBox.Yes | QMessageBox.No,
            defaultButton=QMessageBox.No,
        )

        if close_question == QMessageBox.Yes:
            logging.debug("[GUI] Discarding changes and closing Profiles window.")
            self.hide()
            self.stop_unsaved_changes_timer()
            for widget_num in range(self.stackedLayout.count()):
                self.stackedLayout.widget(widget_num).discard_changes()

        elif close_question == QMessageBox.No:
            logging.debug("[GUI] Keeping Profiles window open.")

    def stop_unsaved_changes_timer(self):
        """Stops checking for unsaved changes when Profile Settings Window is closed to save CPU resources."""

        logging.debug("[GUI] Stopping timer for unsaved changes checker")
        for widget_num in range(self.stackedLayout.count()):
            self.stackedLayout.widget(widget_num).timer_unsaved_changes.stop()

    def start_unsaved_changes_timer(self):
        """Start checking for unsaved changes when Profile Settings Window is opened."""

        logging.debug("[GUI] Starting timer for unsaved changes checker")
        for widget_num in range(self.stackedLayout.count()):
            self.stackedLayout.widget(widget_num).timer_unsaved_changes.start(500)

    def switch_account_settings_page(self):
        self.stackedLayout.setCurrentIndex(self.listWidget_profiles.currentRow())

    def show_setup_wizard(self):
        # Access setup_wizard through the wizard module to avoid circular imports
        wizard.setup_wizard.setStartId(3)
        wizard.setup_wizard.show()

    def remove_profile(self):
        # Stop checking for unsaved changes while new profile is being removed.
        self.stop_unsaved_changes_timer()

        selected_profile_name = self.listWidget_profiles.currentItem().text()

        # Add confirmation dialog
        confirm_removal = QMessageBox.question(
            self,
            "Confirm Profile Removal",
            f"Are you sure you want to remove the profile <b>{selected_profile_name}</b>?",
            buttons=QMessageBox.Yes | QMessageBox.No,
            defaultButton=QMessageBox.No,
        )

        if confirm_removal == QMessageBox.Yes:
            logging.info(f"[GUI] Removing profile: {selected_profile_name}")
            # Remove profile from settings window.
            selected_profile_index = self.listWidget_profiles.currentRow()
            selected_profile_widget = self.stackedLayout.currentWidget()
            self.listWidget_profiles.takeItem(selected_profile_index)
            self.stackedLayout.removeWidget(selected_profile_widget)

            # Remove profile from main window.
            print(f"emit removal of profile {selected_profile_name}")
            self.remove_profile_signal.emit(selected_profile_name)

            # Load existing user profiles and remove the new profile.
            _profiles = ConfigParser()
            _profiles.read(PROFILES_FILE)
            _profiles.remove_section(selected_profile_name)

            # Save the new profiles file.
            with open(PROFILES_FILE, "w") as profilefile:
                _profiles.write(profilefile)

            # Start checking for unsaved changes again after profile has been removed.
            self.start_unsaved_changes_timer()
        else:
            logging.info(f"[GUI] Profile removal cancelled for: {selected_profile_name}")
            # If removal is cancelled, restart the timer as no changes were made
            self.start_unsaved_changes_timer()

    def rename_profile(self):
        selected_item = self.listWidget_profiles.currentItem()
        if not selected_item:
            QMessageBox.warning(self, "Rename Profile", "Please select a profile to rename.")
            return

        old_name = selected_item.text()

        new_name, ok = QInputDialog.getText(self, "Rename Profile", f"Enter new name for profile '{old_name}':", text=old_name)

        if ok and new_name:
            new_name = new_name.strip()
            if not new_name:
                QMessageBox.warning(self, "Rename Profile", "Profile name cannot be empty.")
                return
            if new_name == old_name:
                logging.info("[GUI] Rename cancelled: New name is the same as the old name.")
                return
            if new_name in global_config:
                QMessageBox.warning(self, "Rename Profile", f"Profile '{new_name}' already exists.")
                return

            logging.info(f"[GUI] Renaming profile '{old_name}' to '{new_name}'.")

            # Stop checking for unsaved changes during rename
            self.stop_unsaved_changes_timer()

            # 4. Update global_config and temp_global_config.
            global_config[new_name] = global_config.pop(old_name)
            temp_global_config[new_name] = temp_global_config.pop(old_name)

            # 5. Rename section in PROFILES_FILE.
            _profiles = ConfigParser()
            _profiles.read(PROFILES_FILE)
            if _profiles.has_section(old_name):
                items = _profiles.items(old_name)
                _profiles.add_section(new_name)
                for key, value in items:
                    _profiles.set(new_name, key, value)
                _profiles.remove_section(old_name)
                with open(PROFILES_FILE, "w") as profilefile:
                    _profiles.write(profilefile)
            else:
                logging.warning(f"[GUI] Section '{old_name}' not found in {PROFILES_FILE}.")

            # 6. Update listWidget_profiles item.
            selected_item.setText(new_name)

            # 7. Update label_profile_name in the corresponding ProfileSettingsPage.
            current_index = self.listWidget_profiles.currentRow()
            page_widget = self.stackedLayout.widget(current_index)
            if isinstance(page_widget, ProfileSettingsPage):
                page_widget.profile = new_name  # Update the profile name stored in the page widget
                page_widget.label_profile_name.setText(new_name)
                # Update the temp_profile_config reference in the page widget
                page_widget.temp_profile_config = temp_global_config[new_name]

            # 8. Signal main_window to update profile name display.
            self.rename_profile_signal.emit(old_name, new_name)

            # Save the updated global config
            save_global_config(global_config)

            # Restart checking for unsaved changes
            self.start_unsaved_changes_timer()

        elif not ok:
            logging.info("[GUI] Rename profile dialog cancelled.")
        # If ok is True but new_name is empty, the validation message box is shown.


class ListItemDelegate(QStyledItemDelegate):
    """
    Ensures a warning icon for unsaved profile changes is shown right of the profile name.
    """

    def paint(self, painter, option, index):
        option.decorationPosition = QStyleOptionViewItem.Right
        super(ListItemDelegate, self).paint(painter, option, index)


class ProfileSettingsPage(QWidget, Ui_profile_settings):
    def __init__(self, profile):
        super(ProfileSettingsPage, self).__init__()

        self.profile = profile

        # Set up the user interface from Designer.
        self.setupUi(self)

        self.temp_profile_config = temp_global_config[self.profile]

        self.label_profile_name.setText(self.profile)
        self.tabWidget.setCurrentIndex(0)

        # Configures widget values
        self.configure_profile_settings_page()

        # Configures widget connect actions
        self.configure_connect_actions()

        # Buttons
        self.pushButton_discard.clicked.connect(self.discard_changes)
        self.pushButton_save.clicked.connect(self.save_profile_settings)
        self.pushButton_save.clicked.connect(self.save_sync_list)

        # Time which periodically checks for unsaved changes.
        self.timer_unsaved_changes = QTimer()
        self.timer_unsaved_changes.setSingleShot(False)
        self.timer_unsaved_changes.timeout.connect(self.check_for_unsaved_changes)
        self.timer_unsaved_changes.stop()

    def check_for_unsaved_changes(self):
        """
        Compare saved profile configuration with 'running' temporary configuration.
        Show a warning icon next to unsaved profile name.
        Remove the warning icon when profile changes are reverted, discarded or saved.
        """

        config_changed = False
        sync_list_changed = False
        pixmap_warning = QPixmap(DIR_PATH + "/resources/images/warning.png").scaled(20, 20, Qt.KeepAspectRatio)

        # Check if profile exists in listWidget
        matching_items = profile_settings_window.listWidget_profiles.findItems(self.profile, Qt.MatchExactly)
        if not matching_items:
            logging.warning(f"[PROFILE_SETTINGS] Profile {self.profile} not found in UI list, skipping check")
            return

        unsaved_profile = matching_items[0]

        # Check if profile exists in global_config
        if self.profile not in global_config:
            logging.warning(f"[PROFILE_SETTINGS] Profile {self.profile} not found in global_config, skipping check")
            return

        # Unsaved changes to config file?
        if global_config[self.profile] != self.temp_profile_config:
            # Unsaved changes to OneDrive config file detected.
            config_changed = True
        else:
            # No changes to OneDrive config file detected.
            config_changed = False

        # Unsaved changes to sync_list file?
        if self.read_sync_list() != self.textEdit_sync_list.toPlainText():
            # Unsaved changes to OneDrive sync_list file detected.
            sync_list_changed = True
        else:
            # No changes to OneDrive sync_list file detected.
            sync_list_changed = False

        # Show warning if any configuration change was detected.
        if any([config_changed, sync_list_changed]):
            unsaved_profile.setIcon(pixmap_warning)
            unsaved_profile.setToolTip("This profile has unsaved configuration changes.")

            # Show messageBox when closing window with unsaved changes.
            if self.profile not in profile_settings_window.unsaved_profiles:
                profile_settings_window.unsaved_profiles.append(self.profile)
        else:
            pixmap_warning = QPixmap().isNull()
            unsaved_profile.setIcon(QIcon())
            unsaved_profile.setToolTip("")

            # Don't show messageBox when closing window without unsaved changes.
            if self.profile in profile_settings_window.unsaved_profiles:
                profile_settings_window.unsaved_profiles.remove(self.profile)

    def configure_connect_actions(self):
        # Monitored files tab
        self.lineEdit_sync_dir.textChanged.connect(self.set_sync_dir)
        self.checkBox_sync_root_files.stateChanged.connect(self.set_check_box_state)
        self.pushButton_sync_dir_browse.clicked.connect(self.get_sync_dir_name)
        self.checkBox_sync_business_shared_items.stateChanged.connect(self.set_check_box_state)

        # Disable Business Shared Folder tab when account type is not Business
        if global_config[self.profile]["account_type"] == "Business":
            self.checkBox_sync_business_shared_items.setEnabled(True)
        elif global_config[self.profile]["onedrive"]["sync_business_shared_items"].strip('"') == "true":
            self.checkBox_sync_business_shared_items.setEnabled(True)
        else:
            self.checkBox_sync_business_shared_items.setEnabled(False)

        # Skip_file section
        self.pushButton_add_skip_file.clicked.connect(self.add_skip_file)
        self.pushButton_add_skip_file.clicked.connect(self.lineEdit_skip_file.clear)
        self.pushButton_rm_skip_file.clicked.connect(self.remove_skip_file)

        # Skip_dir section
        self.pushButton_add_skip_dir.clicked.connect(self.add_skip_dir)
        self.pushButton_add_skip_dir.clicked.connect(self.lineEdit_skip_dir.clear)
        self.pushButton_rm_skip_dir.clicked.connect(self.remove_skip_dir)
        self.checkBox_skip_dir_strict_match.stateChanged.connect(self.set_check_box_state)
        self.checkBox_check_nosync.stateChanged.connect(self.set_check_box_state)
        self.checkBox_skip_symlinks.stateChanged.connect(self.set_check_box_state)
        self.checkBox_skip_dotfiles.stateChanged.connect(self.set_check_box_state)

        # Sync Options tab
        self.spinBox_monitor_interval.valueChanged.connect(self.set_spin_box_value)
        self.spinBox_monitor_fullscan_frequency.valueChanged.connect(self.set_spin_box_value)
        self.spinBox_classify_as_big_delete.valueChanged.connect(self.set_spin_box_value)
        self.spinBox_sync_dir_permissions.valueChanged.connect(self.set_spin_box_value)
        self.spinBox_sync_file_permissions.valueChanged.connect(self.set_spin_box_value)
        self.spinBox_operation_timeout.valueChanged.connect(self.set_spin_box_value)
        self.spinBox_connect_timeout.valueChanged.connect(self.set_spin_box_value)
        self.spinBox_data_timeout.valueChanged.connect(self.set_spin_box_value)
        self.spinBox_ip_protocol_version.valueChanged.connect(self.set_spin_box_value)
        self.spinBox_threads.valueChanged.connect(self.set_spin_box_value)
        self.spinBox_inotify_delay.valueChanged.connect(self.set_spin_box_value)
        self.checkBox_download_only.stateChanged.connect(self.set_check_box_state)
        self.checkBox_download_only.stateChanged.connect(self.validate_checkbox_input)
        self.checkBox_upload_only.stateChanged.connect(self.set_check_box_state)
        self.checkBox_upload_only.stateChanged.connect(self.validate_checkbox_input)
        self.checkBox_force_http_11.stateChanged.connect(self.set_check_box_state)
        self.checkBox_disable_upload_validation.stateChanged.connect(self.set_check_box_state)
        self.checkBox_disable_download_validation.stateChanged.connect(self.set_check_box_state)
        self.checkBox_display_running_config.stateChanged.connect(self.set_check_box_state)
        self.checkBox_check_nomount.stateChanged.connect(self.set_check_box_state)
        self.checkBox_local_first.stateChanged.connect(self.set_check_box_state)
        self.checkBox_no_remote_delete.stateChanged.connect(self.set_check_box_state)
        self.checkBox_dry_run.stateChanged.connect(self.set_check_box_state)
        self.checkBox_remove_source_files.stateChanged.connect(self.set_check_box_state)
        self.checkBox_resync.stateChanged.connect(self.set_check_box_state)
        self.checkBox_bypass_data_preservation.stateChanged.connect(self.set_check_box_state)
        self.checkBox_delay_inotify_processing.stateChanged.connect(self.set_check_box_state)
        self.checkBox_force_session_upload.stateChanged.connect(self.set_check_box_state)
        self.lineEdit_user_agent.textChanged.connect(self.set_line_edit_value)
        self.lineEdit_azure_ad_endpoint.textChanged.connect(self.set_line_edit_value)
        self.lineEdit_azure_tenant_id.textChanged.connect(self.set_line_edit_value)
        self.lineEdit_drive_id.textChanged.connect(self.set_line_edit_value)

        # Rate limit
        self.spinBox_rate_limit.valueChanged.connect(self.set_spin_box_value)
        self.spinBox_rate_limit.valueChanged.connect(self.horizontalSlider_rate_limit.setValue)
        self.spinBox_rate_limit.valueChanged.connect(lambda: self.label_rate_limit_mbps.setText(str(round(self.spinBox_rate_limit.value() * 8 / 1000 / 1000, 2)) + " Mbit/s"))
        self.horizontalSlider_rate_limit.valueChanged.connect(self.spinBox_rate_limit.setValue)

        # Webhooks tab
        self.checkBox_webhook_enabled.stateChanged.connect(self.set_check_box_state)
        self.checkBox_webhook_enabled.stateChanged.connect(self.validate_checkbox_input)
        self.spinBox_webhook_expiration_interval.valueChanged.connect(self.set_spin_box_value)
        self.spinBox_webhook_renewal_interval.valueChanged.connect(self.set_spin_box_value)
        self.spinBox_webhook_listening_port.valueChanged.connect(self.set_spin_box_value)
        self.lineEdit_webhook_public_url.textChanged.connect(self.set_line_edit_value)
        self.lineEdit_webhook_listening_host.textChanged.connect(self.set_line_edit_value)

        # Logging tab
        self.checkBox_enable_logging.stateChanged.connect(self.set_check_box_state)
        self.checkBox_enable_logging.stateChanged.connect(self.validate_checkbox_input)
        self.lineEdit_log_dir.textChanged.connect(self.set_log_dir)
        self.pushButton_log_dir_browse.clicked.connect(self.get_log_dir_name)
        self.checkBox_debug_https.stateChanged.connect(self.set_check_box_state)
        self.spinBox_monitor_log_frequency.valueChanged.connect(self.set_spin_box_value)
        self.checkBox_disable_notifications.stateChanged.connect(self.set_check_box_state)
        self.checkBox_disable_notifications.stateChanged.connect(self.validate_checkbox_input)

        # Account tab
        self.pushButton_login.clicked.connect(lambda: main_window.main_window_instance.show_login(self.profile))
        self.pushButton_logout.clicked.connect(self.logout)
        self.checkBox_auto_sync.stateChanged.connect(self.set_check_box_state_profile)
        self.checkBox_display_manager_integration.stateChanged.connect(self.set_check_box_state)

        ## Recycle Bin group box
        self.checkBox_use_recycle_bin.stateChanged.connect(self.set_check_box_state)
        self.checkBox_use_recycle_bin.stateChanged.connect(self.validate_checkbox_input)
        self.lineEdit_recycle_bin_path.textChanged.connect(self.set_recycle_bin_path)
        self.pushButton_recycle_bin_path_browse.clicked.connect(self.get_recycle_bin_path)

    def configure_profile_settings_page(self):
        """Sets all widgets values with values from profile config files"""

        # Monitored files tab
        self.lineEdit_sync_dir.setText(self.temp_profile_config["onedrive"]["sync_dir"].strip('"'))
        self.checkBox_sync_root_files.setChecked(self.get_check_box_state("sync_root_files"))
        self.checkBox_sync_business_shared_items.setChecked(self.get_check_box_state("sync_business_shared_items"))

        # Excluded files tab

        # Skip_file section
        self.skip_files = self.temp_profile_config["onedrive"]["skip_file"].strip('"').split("|")
        self.listWidget_skip_file.clear()
        self.listWidget_skip_file.addItems(self.skip_files)
        self.listWidget_skip_file.setSelectionMode(QAbstractItemView.ExtendedSelection)

        # Skip_dir section
        self.skip_dirs = self.temp_profile_config["onedrive"]["skip_dir"].strip('"').split("|")
        self.listWidget_skip_dir.clear()
        self.listWidget_skip_dir.addItems(self.skip_dirs)
        self.listWidget_skip_dir.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.checkBox_skip_dir_strict_match.setChecked(self.get_check_box_state("skip_dir_strict_match"))
        self.checkBox_check_nosync.setChecked(self.get_check_box_state("check_nosync"))
        self.checkBox_skip_symlinks.setChecked(self.get_check_box_state("skip_symlinks"))
        self.checkBox_skip_dotfiles.setChecked(self.get_check_box_state("skip_dotfiles"))

        # Sync Options tab
        self.checkBox_force_http_11.setChecked(self.get_check_box_state("force_http_11"))
        self.spinBox_monitor_interval.setValue(int(self.temp_profile_config["onedrive"]["monitor_interval"].strip('"')))
        self.spinBox_monitor_fullscan_frequency.setValue(int(self.temp_profile_config["onedrive"]["monitor_fullscan_frequency"].strip('"')))
        self.spinBox_classify_as_big_delete.setValue(int(self.temp_profile_config["onedrive"]["classify_as_big_delete"].strip('"')))
        self.spinBox_sync_dir_permissions.setValue(int(self.temp_profile_config["onedrive"]["sync_dir_permissions"].strip('"')))
        self.spinBox_sync_file_permissions.setValue(int(self.temp_profile_config["onedrive"]["sync_file_permissions"].strip('"')))
        self.spinBox_operation_timeout.setValue(int(self.temp_profile_config["onedrive"]["operation_timeout"].strip('"')))
        self.spinBox_connect_timeout.setValue(int(self.temp_profile_config["onedrive"]["connect_timeout"].strip('"')))
        self.spinBox_data_timeout.setValue(int(self.temp_profile_config["onedrive"]["data_timeout"].strip('"')))
        self.spinBox_ip_protocol_version.setValue(int(self.temp_profile_config["onedrive"]["ip_protocol_version"].strip('"')))
        self.spinBox_threads.setValue(int(self.temp_profile_config["onedrive"]["threads"].strip('"')))
        self.spinBox_inotify_delay.setValue(int(self.temp_profile_config["onedrive"]["inotify_delay"].strip('"')))
        self.checkBox_download_only.setChecked(self.get_check_box_state("download_only"))
        self.checkBox_download_only.setDisabled(self.get_check_box_state("upload_only"))
        self.checkBox_upload_only.setChecked(self.get_check_box_state("upload_only"))
        self.checkBox_upload_only.setDisabled(self.get_check_box_state("download_only"))
        self.checkBox_disable_upload_validation.setChecked(self.get_check_box_state("disable_upload_validation"))
        self.checkBox_disable_download_validation.setChecked(self.get_check_box_state("disable_download_validation"))
        self.checkBox_display_running_config.setChecked(self.get_check_box_state("display_running_config"))
        self.checkBox_check_nomount.setChecked(self.get_check_box_state("check_nomount"))
        self.checkBox_local_first.setChecked(self.get_check_box_state("local_first"))
        self.checkBox_no_remote_delete.setChecked(self.get_check_box_state("no_remote_delete"))
        self.checkBox_no_remote_delete.setEnabled(self.checkBox_upload_only.isChecked())
        self.checkBox_dry_run.setChecked(self.get_check_box_state("dry_run"))
        self.checkBox_remove_source_files.setChecked(self.get_check_box_state("remove_source_files"))
        self.checkBox_resync.setChecked(self.get_check_box_state("resync"))
        self.checkBox_bypass_data_preservation.setChecked(self.get_check_box_state("bypass_data_preservation"))
        self.checkBox_delay_inotify_processing.setChecked(self.get_check_box_state("delay_inotify_processing"))
        self.checkBox_force_session_upload.setChecked(self.get_check_box_state("force_session_upload"))
        self.lineEdit_user_agent.setText(self.temp_profile_config["onedrive"]["user_agent"].strip('"'))
        self.lineEdit_azure_ad_endpoint.setText(self.temp_profile_config["onedrive"]["azure_ad_endpoint"].strip('"'))
        self.lineEdit_azure_tenant_id.setText(self.temp_profile_config["onedrive"]["azure_tenant_id"].strip('"'))
        self.lineEdit_drive_id.setText(self.temp_profile_config["onedrive"]["drive_id"].strip('"'))

        # Rate limit
        self.spinBox_rate_limit.setValue(int(self.temp_profile_config["onedrive"]["rate_limit"].strip('"')))
        self.horizontalSlider_rate_limit.setValue(int(self.temp_profile_config["onedrive"]["rate_limit"].strip('"')))
        self.label_rate_limit_mbps.setText(str(round(self.spinBox_rate_limit.value() * 8 / 1000 / 1000, 2)) + " Mbit/s")

        # Webhooks tab
        self.checkBox_webhook_enabled.setChecked(self.get_check_box_state("webhook_enabled"))
        self.spinBox_webhook_expiration_interval.setValue(int(self.temp_profile_config["onedrive"]["webhook_expiration_interval"].strip('"')))
        self.spinBox_webhook_expiration_interval.setEnabled(self.checkBox_webhook_enabled.isChecked())
        self.spinBox_webhook_renewal_interval.setValue(int(self.temp_profile_config["onedrive"]["webhook_renewal_interval"].strip('"')))
        self.spinBox_webhook_renewal_interval.setEnabled(self.checkBox_webhook_enabled.isChecked())
        self.spinBox_webhook_listening_port.setValue(int(self.temp_profile_config["onedrive"]["webhook_listening_port"].strip('"')))
        self.spinBox_webhook_listening_port.setEnabled(self.checkBox_webhook_enabled.isChecked())
        self.lineEdit_webhook_public_url.setText(self.temp_profile_config["onedrive"]["webhook_public_url"].strip('"'))
        self.lineEdit_webhook_public_url.setEnabled(self.checkBox_webhook_enabled.isChecked())
        self.lineEdit_webhook_listening_host.setText(self.temp_profile_config["onedrive"]["webhook_listening_host"].strip('"'))
        self.lineEdit_webhook_listening_host.setEnabled(self.checkBox_webhook_enabled.isChecked())

        # Logging tab
        self.checkBox_enable_logging.setChecked(self.get_check_box_state("enable_logging"))
        self.lineEdit_log_dir.setText(self.temp_profile_config["onedrive"]["log_dir"].strip('"'))
        self.lineEdit_log_dir.setEnabled(self.checkBox_enable_logging.isChecked())
        self.pushButton_log_dir_browse.setEnabled(self.checkBox_enable_logging.isChecked())
        self.checkBox_debug_https.setChecked(self.get_check_box_state("debug_https"))
        self.spinBox_monitor_log_frequency.setValue(int(self.temp_profile_config["onedrive"]["monitor_log_frequency"].strip('"')))
        self.spinBox_monitor_log_frequency.setEnabled(self.checkBox_enable_logging.isChecked())
        self.checkBox_disable_notifications.setChecked(self.get_check_box_state("disable_notifications"))

        # Account tab
        self.config_file = global_config[self.profile]["config_file"].strip('"')
        self.config_dir = re.search(r"(.+)/.+$", self.config_file).group(1)
        self.pushButton_login.hide()
        self.checkBox_auto_sync.setChecked(self.get_check_box_state_profile("auto_sync"))
        self.checkBox_display_manager_integration.setChecked(self.get_check_box_state("display_manager_integration"))

        # Sync List tab
        self.textEdit_sync_list.setText(self.read_sync_list())

        ## Recycle Bin group box
        self.checkBox_use_recycle_bin.setChecked(self.get_check_box_state("use_recycle_bin"))
        self.lineEdit_recycle_bin_path.setText(self.temp_profile_config["onedrive"]["recycle_bin_path"].strip('"'))
        self.lineEdit_recycle_bin_path.setEnabled(self.checkBox_use_recycle_bin.isChecked())
        self.label_recycle_bin_path.setEnabled(self.checkBox_use_recycle_bin.isChecked())
        self.pushButton_recycle_bin_path_browse.setEnabled(self.checkBox_use_recycle_bin.isChecked())

    def read_sync_list(self):
        self.sync_list_file = re.search(r"(.+)/.+$", self.config_file).group(1) + "/sync_list"

        try:
            with open(self.sync_list_file, "r") as f:
                self.sync_list = f.read()
        except:
            self.sync_list = ""

        return self.sync_list

    def save_sync_list(self):
        self.sync_list_new = self.textEdit_sync_list.toPlainText()

        with open(self.sync_list_file, "w") as f:
            f.write(self.sync_list_new)

    def validate_checkbox_input(self):
        """Disables incompatible settings"""

        if self.sender().objectName() == "checkBox_download_only" or "checkBox_upload_only":
            if self.checkBox_download_only.isChecked():
                self.checkBox_upload_only.setChecked(False)
                self.checkBox_upload_only.setDisabled(True)
            else:
                self.checkBox_upload_only.setDisabled(False)

            if self.checkBox_upload_only.isChecked():
                self.checkBox_download_only.setChecked(False)
                self.checkBox_download_only.setDisabled(True)
                self.checkBox_no_remote_delete.setDisabled(False)
            else:
                self.checkBox_download_only.setDisabled(False)
                self.checkBox_no_remote_delete.setDisabled(True)
                self.checkBox_no_remote_delete.setChecked(False)

        if self.sender().objectName() == "checkBox_enable_logging":
            if self.checkBox_enable_logging.isChecked():
                self.lineEdit_log_dir.setEnabled(True)
                self.spinBox_monitor_log_frequency.setEnabled(True)
                self.pushButton_log_dir_browse.setEnabled(True)
            else:
                self.lineEdit_log_dir.setEnabled(False)
                self.spinBox_monitor_log_frequency.setEnabled(False)
                self.pushButton_log_dir_browse.setEnabled(False)

        if self.sender().objectName() == "checkBox_webhook_enabled":
            if self.checkBox_webhook_enabled.isChecked():
                self.spinBox_webhook_expiration_interval.setEnabled(True)
                self.spinBox_webhook_renewal_interval.setEnabled(True)
                self.spinBox_webhook_listening_port.setEnabled(True)
                self.lineEdit_webhook_public_url.setEnabled(True)
                self.lineEdit_webhook_listening_host.setEnabled(True)
            else:
                self.spinBox_webhook_expiration_interval.setEnabled(False)
                self.spinBox_webhook_renewal_interval.setEnabled(False)
                self.spinBox_webhook_listening_port.setEnabled(False)
                self.lineEdit_webhook_public_url.setEnabled(False)
                self.lineEdit_webhook_listening_host.setEnabled(False)

        if self.sender().objectName() == "checkBox_use_recycle_bin":
            if self.checkBox_use_recycle_bin.isChecked():
                self.lineEdit_recycle_bin_path.setEnabled(True)
                self.label_recycle_bin_path.setEnabled(True)
                self.pushButton_recycle_bin_path_browse.setEnabled(True)
            else:
                self.lineEdit_recycle_bin_path.setEnabled(False)
                self.label_recycle_bin_path.setEnabled(False)
                self.pushButton_recycle_bin_path_browse.setEnabled(False)

    def str2bool(self, value):
        return value.lower() in "true"

    def logout(self):
        os.system(f"{client_bin_path} --confdir='{self.config_dir}' --logout")
        logging.info(f"Profile {self.profile} has been logged out.")

        main_window.main_window_instance.profile_status_pages[self.profile].stop_monitor()
        if self.profile in workers:
            workers[self.profile].stop_worker()
            main_window.main_window_instance.profile_status_pages[self.profile].label_onedrive_status.setText("OneDrive sync has been stopped")
            logging.info(f"OneDrive sync for profile {self.profile} has been stopped.")
        else:
            logging.info(f"OneDrive for profile {self.profile} is not running.")

        main_window.main_window_instance.profile_status_pages[self.profile].label_onedrive_status.setText("You have been logged out")

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

    def get_recycle_bin_path(self):
        self.file_dialog = QFileDialog.getExistingDirectory(dir=os.path.expanduser("~/"))

        recycle_bin_path = self.file_dialog
        logging.info(recycle_bin_path)
        self.lineEdit_recycle_bin_path.setText(recycle_bin_path)

    def set_line_edit_value(self, value):
        _property = self.sender().objectName()
        property = re.search(r"lineEdit_(.+)", _property).group(1)
        self.temp_profile_config["onedrive"][f"{property}"] = f'"{value}"'

    def set_spin_box_value(self, value):
        _property = self.sender().objectName()
        property = re.search(r"spinBox_(.+)", _property).group(1)
        self.temp_profile_config["onedrive"][f"{property}"] = f'"{value}"'

    def set_check_box_state(self):
        sender = self.sender()
        _property = self.sender().objectName()
        print("test " + _property)
        try:
            property = re.search(r"checkBox_(.+)", _property).group(1)
        except:
            property = re.search(r"groupBox_(.+)", _property).group(1)

        if self.sender().isChecked():
            logging.info(f"[GUI] [{self.profile}] {property} is checked.")
            self.temp_profile_config["onedrive"][f"{property}"] = '"true"'
        else:
            logging.info(f"[GUI] [{self.profile}] {property} is unchecked.")
            self.temp_profile_config["onedrive"][f"{property}"] = '"false"'

    def set_check_box_state_profile(self):
        _property = self.sender().objectName()
        property = re.search(r"checkBox_(.+)", _property).group(1)

        if self.sender().isChecked():
            logging.info(f"[GUI] [{self.profile}] {property} is checked.")
            self.temp_profile_config[f"{property}"] = "True"
        else:
            logging.info(f"[GUI] [{self.profile}] {property} is unchecked.")
            self.temp_profile_config[f"{property}"] = "False"

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
        self.label_rate_limit_mbps.setText(str(round(int(self.lineEdit_rate_limit.text()) * 8 / 1000 / 1000, 2)) + " Mbit/s")

    def set_sync_dir(self):
        self.temp_profile_config["onedrive"]["sync_dir"] = f'"{self.lineEdit_sync_dir.text()}"'

    def set_log_dir(self):
        self.temp_profile_config["onedrive"]["log_dir"] = f'"{self.lineEdit_log_dir.text()}"'

    def set_recycle_bin_path(self):
        self.temp_profile_config["onedrive"]["recycle_bin_path"] = f'"{self.lineEdit_recycle_bin_path.text()}"'
        logging.info(f"[GUI] [{self.profile}] Recycle bin path set to: {self.temp_profile_config['onedrive']['recycle_bin_path']}")

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
            qlistwidget_name.takeItem(qlistwidget_name.row(item))
            logging.info(list)
            list.remove(item.text())

    def save_profile_settings(self):
        global_config[self.profile] = copy.deepcopy(self.temp_profile_config)
        logging.debug("save_profile_settings" + "self.temp_profile_config" + str(self.temp_profile_config))
        logging.debug("save_profile_settings" + "global_config" + str(global_config))
        save_global_config(global_config)

    def discard_changes(self):
        self.temp_profile_config = copy.deepcopy(global_config[self.profile])
        self.configure_profile_settings_page()


profile_settings_window = ProfileSettingsWindow()
