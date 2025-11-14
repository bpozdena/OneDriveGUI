from PySide6.QtCore import QTimer, QUrl, QFileInfo, Qt, Signal, Slot, QTimer
from PySide6.QtGui import QIcon, QPixmap, QDesktopServices
from PySide6.QtWidgets import (
    QWidget,
    QMainWindow,
    QMenu,
    QSystemTrayIcon,
    QListWidgetItem,
    QStackedLayout,
    QMessageBox,
    QStyledItemDelegate,
)


# Imports for main window.
from ui.ui_mainwindow import Ui_MainWindow
from ui.ui_process_status_page import Ui_status_page


# Import for login windows.
from ui.ui_external_login import Ui_ExternalLoginWindow


import re
import os
import sys

import requests
import subprocess


from wizard import setup_wizard
from profile_settings_window import profile_settings_window

from options import (
    global_config,
    client_bin_path,
    gui_settings,
    version,
)

from utils.utils import humanize_file_size, shorten_path
from workers import WorkerThread, MaintenanceWorker, TaskList, workers
from gui_settings_window import gui_settings_window

import logging

# from logger import logger
from global_config import DIR_PATH, PROFILES_FILE

try:
    from ui.ui_login import Ui_LoginWindow
except ImportError:
    logging.warning("Failed to import ui_login. This is expected if you are running AppImage version.")

    # Define a dummy class to avoid errors when this UI component isn't available
    class Ui_LoginWindow:
        def setupUi(self, window):
            logging.error("LoginWindow UI is not available in this environment")
            window.hide()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Access setup_wizard from wizard module to avoid circular imports
        import wizard

        wizard.setup_wizard.show_main_window_signal.connect(self.show)
        wizard.setup_wizard.add_profile_signal.connect(self.add_profile)

        profile_settings_window.remove_profile_signal.connect(self.remove_profile)
        profile_settings_window.rename_profile_signal.connect(self.rename_profile_in_main_window)

        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(f"OneDriveGUI v{version}")
        self.setWindowIcon(QIcon(DIR_PATH + "/resources/images/icons8-clouds-80-dark-edge.png"))

        if gui_settings.get("frameless_window") == "True":
            self.setWindowFlags(Qt.FramelessWindowHint)

        if len(global_config) == 0:
            self.show_setup_wizard()

        self.pushButton_new_profile.hide()
        self.menubar.hide()

        self.comboBox.activated.connect(self.switch_account_status_page)
        self.comboBox.setStyleSheet(
            f"""
        QComboBox {{
            border : 0px black;
            border-radius : 0px;
            background-color: rgb(0, 120, 212);
            color: rgb(255, 255, 255);
        }}

        QComboBox::drop-down {{
            border : 0px black;
            background-color: rgb(0, 120, 212);
            text-transform: uppercase;
            color: rgb(255, 255, 255);
        }}

        QComboBox QAbstractItemView::item {{ 
            min-height: 20px;
            background-color: rgb(0, 120, 212);
            text-transform: uppercase;
            color: rgb(255, 255, 255);
        }}

        QComboBox::down-arrow {{
            image: url({DIR_PATH}/resources/images/user-account.png);
            width: 20px;
            height: 20px;
        }}

        background-color: rgb(0, 120, 212);
        color: rgb(255, 255, 255);
        
        """
        )
        self.stackedLayout = QStackedLayout()

        self.profile_status_pages = {}
        for profile in global_config:
            self.comboBox.addItem(profile)
            self.profile_status_pages[profile] = ProfileStatusPage(profile)
            self.profile_status_pages[profile].start_sync_signal.connect(self.start_onedrive_monitor)
            self.profile_status_pages[profile].stop_sync_signal.connect(self.stop_onedrive_monitor)
            self.profile_status_pages[profile].quit_gui_signal.connect(self.graceful_shutdown)
            self.stackedLayout.addWidget(self.profile_status_pages[profile])

        self.verticalLayout_2.addLayout(self.stackedLayout)

        # Ensure all profiles in comboBox are aligned to center
        delegate = AlignDelegate(self.comboBox)
        self.comboBox.setItemDelegate(delegate)

        # Making comboBox editable, which allows for center alignment.
        self.comboBox.setEditable(True)
        line_edit = self.comboBox.lineEdit()
        line_edit.setAlignment(Qt.AlignRight)
        line_edit.setReadOnly(True)

        # Hide comboBox if only one profile exists
        if len(self.profile_status_pages) < 2:
            self.comboBox.hide()

        # System Tray
        self.tray = QSystemTrayIcon()
        if self.tray.isSystemTrayAvailable():
            icon = QIcon(DIR_PATH + "/resources/images/icons8-clouds-80-dark-edge.png")
            menu = QMenu()

            show_action = menu.addAction("Show/Hide")
            show_action.triggered.connect(lambda: self.hide() if self.isVisible() else self.show())
            setting_action = menu.addAction("Settings")
            setting_action.triggered.connect(self.show_settings_window)
            quit_action = menu.addAction("Quit")
            quit_action.triggered.connect(lambda: self.graceful_shutdown())

            self.tray.activated.connect(self.tray_icon_clicked)

            self.tray.setIcon(icon)
            self.tray.setContextMenu(menu)
            self.tray.show()
            self.tray.setToolTip("OneDriveGUI")

        else:
            self.tray = None

        self.refresh_process_status = QTimer()
        self.refresh_process_status.setSingleShot(False)
        self.refresh_process_status.timeout.connect(self.onedrive_process_status)
        self.refresh_process_status.start(500)

        self.check_client_version = QTimer()
        self.check_client_version.setSingleShot(True)
        self.check_client_version.timeout.connect(self.client_version_check)
        self.check_client_version.start(500)

        self.auto_sync = QTimer()
        self.auto_sync.setSingleShot(True)
        self.auto_sync.timeout.connect(self.autostart_monitor)
        self.auto_sync.start(1000)

    def mousePressEvent(self, event):
        if gui_settings.get("frameless_window") == "True":
            self.dragPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if gui_settings.get("frameless_window") == "True":
            self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
            self.dragPos = event.globalPosition().toPoint()
            event.accept()

    def tray_icon_clicked(self, reason):
        if reason == QSystemTrayIcon.Unknown:
            pass
        elif reason == QSystemTrayIcon.Context:
            logging.debug("[GUI] Right clicked on tray icon")
        elif reason == QSystemTrayIcon.DoubleClick:
            pass
        elif reason == QSystemTrayIcon.Trigger:
            logging.debug("[GUI] Left clicked on tray icon")
            self.hide() if self.isVisible() else self.show()
        elif reason == QSystemTrayIcon.MiddleClick:
            pass
        else:
            pass

    def graceful_shutdown(self):
        close_question = QMessageBox.question(
            self,
            "Quit OneDriveGUI ?",
            f"Would you like to stop all sync operations and quit OneDriveGUI ?",
            buttons=QMessageBox.Yes | QMessageBox.No,
            defaultButton=QMessageBox.No,
        )

        if close_question == QMessageBox.Yes:
            logging.info("Quitting OneDriveGUI")
            workers_to_stop = []

            for worker in workers:
                workers_to_stop.append(worker)

            for worker in workers_to_stop:
                workers[worker].stop_worker()

            sys.exit()

        elif close_question == QMessageBox.No:
            logging.debug("[GUI] Keeping OneDriveGUI running.")

    def stop_onedrive_monitor(self, profile_name):
        if profile_name in workers:
            workers[profile_name].stop_worker()
            self.profile_status_pages[profile_name].label_onedrive_status.setText("OneDrive sync has been stopped")
            logging.info(f"OneDrive sync for profile {profile_name} has been stopped.")
        else:
            logging.info(f"OneDrive for profile {profile_name} is not running.")

    def closeEvent(self, event):
        # Minimize main window to system tray if it is available. Otherwise minimize to taskbar.
        event.ignore()
        try:
            if self.tray.isSystemTrayAvailable():
                self.hide()
                logging.info("[GUI] Minimizing main window to tray")
            else:
                self.setWindowState(Qt.WindowMinimized)
                logging.info("[GUI] Minimizing main window to taskbar/dock")
        except:
            self.setWindowState(Qt.WindowMinimized)
            logging.info("[GUI] Minimizing main window to taskbar/dock")

    def show_setup_wizard(self):
        setup_wizard.show()

    def show_settings_window(self):
        profile_settings_window.show()

        # Start checking for unsaved changes.
        profile_settings_window.start_unsaved_changes_timer()

    def switch_account_status_page(self):
        self.stackedLayout.setCurrentIndex(self.comboBox.currentIndex())

    def client_version_check(self):
        """
        Compare installed version of OneDrive client with the latest version on Github releases.
        Show workings or prevent sync when installed version is too old.
        """
        pixmap_warning = QPixmap(DIR_PATH + "/resources/images/warning.png").scaled(20, 20, Qt.KeepAspectRatio)
        s = requests.Session()
        version_label_text = ""
        version_tooltip_text = ""
        min_requirements_met = True
        min_supported_version = 2500

        def get_latest_client_version():
            latest_url = "https://api.github.com/repos/abraunegg/onedrive/releases/latest"
            try:
                latest_client_version = s.get(latest_url, timeout=1).json()["tag_name"]
                return latest_client_version

            except Exception as e:
                logging.error(e)
                return None

        def get_installed_client_version():
            try:
                client_version_check = subprocess.check_output([client_bin_path, "--version"], stderr=subprocess.STDOUT)
                installed_client_version = re.search(r"(v[0-9.]+)", str(client_version_check)).group(1)

                installed_client_version_num = int(installed_client_version.replace("v", "").replace(".", ""))
                installed_client_version_num = installed_client_version_num if len(str(installed_client_version_num)) > 3 else installed_client_version_num * 10

                return installed_client_version, installed_client_version_num

            except Exception as e:
                logging.error(e)
                return None

        try:
            latest_client_version = get_latest_client_version()
            installed_client_version = get_installed_client_version()

            logging.debug(f"[GUI] Client version check: Installed: {installed_client_version[0]} | Latest: {latest_client_version}")

            if not installed_client_version:
                version_label_text = "OneDrive client not found!"
                version_tooltip_text = "OneDrive client not found!"
                min_requirements_met = False

            elif not latest_client_version:
                version_label_text = "Unable to check for latest OneDrive client version!"
                version_tooltip_text = "Unable to check for latest OneDrive client version!"

            elif installed_client_version[1] < min_supported_version:
                version_label_text = (
                    'Unsupported OneDrive client! Please <a href="https://github.com/abraunegg/onedrive/blob/master/docs/install.md" style="color:#FFFFFF;">upgrade</a> it.'
                )
                version_tooltip_text = (
                    f"Your OneDrive Client version not supported! Please upgrade it. \n Installed: {installed_client_version[0]} \n Latest: {latest_client_version}"
                )
                min_requirements_met = False

            elif latest_client_version not in installed_client_version[0]:
                version_label_text = "OneDrive client is out of date!"
                version_tooltip_text = f"OneDrive client is out of date! \n Installed: {installed_client_version[0]} \n Latest: {latest_client_version}"

            for profile_name in global_config:
                self.profile_status_pages[profile_name].label_onedrive_status.setOpenExternalLinks(True)

                if version_label_text:
                    self.profile_status_pages[profile_name].label_onedrive_status.setText(version_label_text)

                if not min_requirements_met:
                    # Disable Start Sync button if OneDrive client is too old (smaller then min_supported_version_num).
                    self.profile_status_pages[profile_name].pushButton_start.setEnabled(False)
                    self.profile_status_pages[profile_name].pushButton_start_stop.setEnabled(False)
                    self.profile_status_pages[profile_name].pushButton_profiles.setEnabled(False)
                    self.profile_status_pages[profile_name].label_version_check.setToolTip(version_tooltip_text)
                    self.profile_status_pages[profile_name].label_version_check.setPixmap(pixmap_warning)

                elif latest_client_version not in installed_client_version:
                    # Display warning in GUI when installed OneDrive client is not up to date.
                    self.profile_status_pages[profile_name].label_version_check.setToolTip(version_tooltip_text)
                    self.profile_status_pages[profile_name].label_version_check.setPixmap(pixmap_warning)

        except Exception as e:
            logging.error(f"Client version check failed: {e}")

    def onedrive_process_status(self):
        # Check OneDrive status and start/stop sync button.
        pixmap_running = QPixmap(DIR_PATH + "/resources/images/icons8-green-circle-48.png").scaled(24, 24, Qt.KeepAspectRatio)
        pixmap_stopped = QPixmap(DIR_PATH + "/resources/images/icons8-red-circle-48.png").scaled(24, 24, Qt.KeepAspectRatio)

        for profile_name in global_config:
            # Check if profile exists in profile_status_pages, if not add it
            if profile_name not in self.profile_status_pages:
                logging.info(f"Profile {profile_name} found in global_config but not in UI, adding it now")
                self.add_profile(profile_name)

            profile_status_page = self.profile_status_pages[profile_name]

            if profile_name not in workers:
                profile_status_page.label_status.setText("stopped")
                profile_status_page.label_status.setToolTip("Sync is stopped")
                profile_status_page.label_status.setPixmap(pixmap_stopped)

                # Show Play icon when sync is stopped.
                profile_status_page.pushButton_start_stop.setIcon(profile_status_page.start_icon)
                profile_status_page.pushButton_start_stop.setToolTip("Start Sync")
                profile_status_page.pushButton_start_stop.clicked.disconnect()
                profile_status_page.pushButton_start_stop.clicked.connect(profile_status_page.start_monitor)

            else:
                if workers[profile_name].isRunning():
                    profile_status_page.label_status.setText("running")
                    profile_status_page.label_status.setToolTip("Sync is running")
                    profile_status_page.label_status.setPixmap(pixmap_running)

                    # Show Stop icon when sync is running.
                    profile_status_page.pushButton_start_stop.setIcon(profile_status_page.stop_icon)
                    profile_status_page.pushButton_start_stop.setToolTip("Stop Sync")
                    profile_status_page.pushButton_start_stop.clicked.disconnect()
                    profile_status_page.pushButton_start_stop.clicked.connect(profile_status_page.stop_monitor)

    def autostart_monitor(self):
        # Auto-start sync if compatible version of OneDrive client is installed.
        for profile_name in global_config:
            logging.debug(f"[{profile_name}] Compatible client version found: {self.profile_status_pages[profile_name].pushButton_start.isEnabled()}")
            logging.debug(f"[{profile_name}] Auto-sync enabled for profile: {global_config[profile_name]['auto_sync']}")

            if self.profile_status_pages[profile_name].pushButton_start.isEnabled() and global_config[profile_name]["auto_sync"] == "True":
                self.start_onedrive_monitor(profile_name)

    def start_onedrive_monitor(self, profile_name, options=""):
        if profile_name not in workers:
            workers[profile_name] = WorkerThread(profile_name, options)
            workers[profile_name].start()
        else:
            logging.info(f"Worker for profile {profile_name} is already running. Please stop it first.")
            logging.info(f"Running workers: {workers}")

        if "True" not in gui_settings.get("QWebEngine_login"):
            # Assume GUI runs as AppImage. Force login in external browser as a workaround for #37 .
            logging.info(f"[GUI] Opening external login window")
            workers[profile_name].update_credentials.connect(self.show_external_login)
        else:
            # Use QT WebEngine for a more convenient login.
            logging.info(f"[GUI] Opening WebEngine login window")
            workers[profile_name].update_credentials.connect(self.show_login)

        workers[profile_name].trigger_resync.connect(self.resync_auth_dialog)
        workers[profile_name].trigger_big_delete.connect(self.big_delete_auth_dialog)
        workers[profile_name].update_progress_new.connect(self.event_update_progress)
        workers[profile_name].update_profile_status.connect(self.event_update_profile_status)
        workers[profile_name].started.connect(lambda: logging.info(f"started worker {profile_name}"))
        workers[profile_name].finished.connect(lambda: logging.info(f"finished worker {profile_name}"))
        try:
            workers[profile_name].finished.connect(lambda: self.remove_worker(profile_name))
        except KeyError:
            logging.debug(f"[GUI] The worker for profile {profile_name} is already stopped.")

    def resync_auth_dialog(self, profile_name):
        resync_question = QMessageBox(
            QMessageBox.Question,
            f"Resync required for profile {profile_name}",
            "An application configuration change has been detected where a resync is required. <br><br>"
            "The use of resync will remove your local 'onedrive' client state, thus no record will exist regarding your current 'sync status'. <br><br>"
            "This has the potential to overwrite local versions of files with potentially older versions downloaded from OneDrive which can lead to <b>data loss</b>. <br><br>"
            "If in-doubt, backup your local data first before proceeding with resync.<br><br><br>"
            f"Would you like to perform resync for profile <b>{profile_name}</b>?",
            QMessageBox.Yes | QMessageBox.No,
        )
        yes_button = resync_question.button(QMessageBox.Yes)
        yes_button.setEnabled(False)
        self.countdown_timer = QTimer(self)
        self.countdown_value = 5

        def update_button_text():
            yes_button.setText(f"Yes ({self.countdown_value})")
            self.countdown_value -= 1
            if self.countdown_value < 0:
                self.countdown_timer.stop()
                yes_button.setText("Yes")
                yes_button.setEnabled(True)

        self.countdown_timer.timeout.connect(update_button_text)
        self.countdown_timer.start(1000)  # Update every 1 second

        resync_question.setDefaultButton(QMessageBox.No)
        result = resync_question.exec()

        if result == QMessageBox.Yes:
            logging.info("Authorize sync: Yes")
            self.profile_status_pages[profile_name].stop_monitor()
            self.start_onedrive_monitor(profile_name, "--resync --resync-auth")

        elif result == QMessageBox.No:
            logging.info("Authorize sync: No")
            self.countdown_timer.stop()
            self.profile_status_pages[profile_name].stop_monitor()

    def big_delete_auth_dialog(self, profile_name):
        big_delete_question = QMessageBox.question(
            self,
            f"Big Delete detected for profile {profile_name}",
            "An attempt to remove a large volume of data from OneDrive has been detected. <br><br>"
            "This has the potential to delete a large volume of data from your OneDrive which can lead to <b>data loss</b>. <br><br>"
            "If in-doubt, backup your OneDrive data first before proceeding with big delete.<br><br><br>"
            f"Would you like to proceed with big delete for profile <b>{profile_name}</b>?",
            buttons=QMessageBox.Yes | QMessageBox.No,
            defaultButton=QMessageBox.No,
        )

        if big_delete_question == QMessageBox.Yes:
            logging.info("Authorize big delete: Yes")
            self.profile_status_pages[profile_name].stop_monitor()
            self.remove_worker(profile_name)
            self.start_onedrive_monitor(profile_name, "--force")
            self.profile_status_pages[profile_name].label_onedrive_status.setText("Big delete approved")

        elif big_delete_question == QMessageBox.No:
            logging.info("Authorize big delete: No")
            self.profile_status_pages[profile_name].stop_monitor()
            self.profile_status_pages[profile_name].label_onedrive_status.setText("Big delete denied")

    def event_update_profile_status(self, data, profile):
        self.profile_status_pages[profile].label_onedrive_status.setText(data["status_message"])
        self.profile_status_pages[profile].label_free_space.setText(data["free_space"])
        self.profile_status_pages[profile].label_account_type.setText(data["account_type"])

    def event_update_progress(self, data, profile):
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

        logging.info(data)
        file_path = f"{_sync_dir}" + "/" + data["file_path"]
        absolute_path = QFileInfo(file_path).absolutePath().replace(" ", "%20")
        relative_path_display = os.path.relpath(QFileInfo(file_path).absolutePath(), _sync_dir + os.path.sep)
        parent_dir = re.search(r".+/([^/]+)/.+$", file_path).group(1)
        file_size = QFileInfo(file_path + ".partial").size() if QFileInfo(file_path).size() == 0 else QFileInfo(file_path).size()
        file_size_human = humanize_file_size(file_size)
        file_name = QFileInfo(file_path).fileName()
        progress = data["progress"]
        progress_data = file_size / 100 * int(progress)
        progress_data_human = humanize_file_size(progress_data)
        file_operation = data["file_operation"]
        transfer_complete = data["transfer_complete"]
        move_scrollbar = True
        new_list_item = True

        for row in range(50):
            # Check last 50 entries to see if the file is already in the list.
            if self.profile_status_pages[profile].listWidget.item(row) != None:
                item = self.profile_status_pages[profile].listWidget.item(row)
                item_widget = self.profile_status_pages[profile].listWidget.itemWidget(item)
                item_file_name = item_widget.get_file_name()
                item_incomplete = item_widget.ls_progressBar.isVisible()

                if file_name == item_file_name and item_incomplete:
                    # If current file is already in the list and progress bar is not complete, update the existing item.
                    # Otherwise skip and create a new item.
                    logging.info("Updating list item")

                    item_widget.set_progress(int(progress))
                    # item_widget.set_icon(file_path)
                    item_widget.hide_progress_bar(transfer_complete)

                    if file_operation == "Deleting":
                        item_widget.set_label_1(f"Deleted from {parent_dir}")
                        item_widget.set_label_2(f"")

                    elif file_operation == "Moving":
                        item_widget.set_label_1(f"Trashed from {parent_dir}")
                        item_widget.set_label_2(f"")

                    elif transfer_complete and file_operation == "Uploading":
                        shortened_path = shorten_path(relative_path_display, 32)
                        item_widget.set_label_1(f"Uploaded from <a href=file:///{absolute_path}>{shortened_path}</a>")
                        item_widget.set_label_2(f"{file_size_human}")

                    elif transfer_complete and file_operation == "Downloading":
                        shortened_path = shorten_path(relative_path_display, 32)
                        item_widget.set_label_1(f"Downloaded from <a href=file:///{absolute_path}>{shortened_path}</a>")
                        item_widget.set_label_2(f"{file_size_human}")

                    elif file_operation == "Downloading":
                        # Estimate final size of file before download completes
                        # Adding 5% to progress as the OD client report status 5% behind.
                        item_widget.set_label_1(file_operation)
                        item_widget.set_label_2(f"{humanize_file_size(file_size)} of ~{humanize_file_size(int(file_size) / (int(progress) + 5) * 100)}")
                    else:
                        item_widget.set_label_1(file_operation)
                        item_widget.set_label_2(f"{progress_data_human} of {file_size_human}")

                    self.profile_status_pages[profile].listWidget.setItemWidget(item, item_widget)
                    new_list_item = False
                    logging.info(f"List item updated for file {item_file_name}")
                    break

        if new_list_item:
            logging.info(f"Adding new list item for file {file_name}")
            myQCustomQWidget = TaskList()
            myQCustomQWidget.set_file_name(file_name)
            myQCustomQWidget.set_progress(int(progress))
            myQCustomQWidget.set_icon(file_path)
            myQCustomQWidget.hide_progress_bar(transfer_complete)

            if file_operation == "Deleting":
                myQCustomQWidget.set_label_1(f"Deleted from {parent_dir}")
                myQCustomQWidget.set_label_2(f"")

            elif file_operation == "Moving":
                myQCustomQWidget.set_label_1(f"Trashed from {parent_dir}")
                myQCustomQWidget.set_label_2(f"")

            elif transfer_complete and file_operation == "Uploading":
                shortened_path = shorten_path(relative_path_display, 32)
                myQCustomQWidget.set_label_1(f"Uploaded from <a href=file:///{absolute_path}>{shortened_path}</a>")
                myQCustomQWidget.set_label_2(f"{file_size_human}")

            elif transfer_complete and file_operation == "Downloading":
                shortened_path = shorten_path(relative_path_display, 32)
                myQCustomQWidget.set_label_1(f"Downloaded from <a href=file:///{absolute_path}>{shortened_path}</a>")
                myQCustomQWidget.set_label_2(f"{file_size_human}")

            elif file_operation == "Downloading":
                # Estimate final size of file before download completes
                # Adding 5% to progress as the OD client report status 5% behind.
                myQCustomQWidget.set_label_1(file_operation)
                myQCustomQWidget.set_label_2(f"{humanize_file_size(file_size)} of ~{humanize_file_size(int(file_size) / (int(progress) + 5) * 100)}")
            else:
                myQCustomQWidget.set_label_1(file_operation)
                myQCustomQWidget.set_label_2(f"{progress_data_human} of {file_size_human}")

            # Create QListWidgetItem
            myQListWidgetItem = QListWidgetItem()

            # Set size hint
            myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())

            # Add QListWidgetItem into QListWidget
            listWidget = self.profile_status_pages[profile].listWidget
            listWidget.insertItem(0, myQListWidgetItem)
            listWidget.setItemWidget(myQListWidgetItem, myQCustomQWidget)

            # If the list is not scrolled all the way to the top, increment the scroll value so that the list stays in the same spot when new items are added.
            scroll = listWidget.verticalScrollBar()
            currentScrollValue = scroll.value()
            if move_scrollbar and (currentScrollValue > 0):
                scroll.setValue(currentScrollValue + 1)

            # Limit list to 10k items to fix #208.
            if listWidget.count() > 10_000:
                listWidget.takeItem(listWidget.count() - 1)

    def show_login(self, profile):
        # Show login window with QT WebEngine
        self.window1 = QWidget()
        self.window1.setWindowIcon(QIcon(DIR_PATH + "/resources/images/icons8-clouds-80-dark-edge.png"))
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
        self.lw.loginFrame.urlChanged.connect(lambda: self.get_response_url(self.lw.loginFrame.url().toString(), profile))

    def show_external_login(self, profile):
        # Show external login window
        self.window2 = QWidget()
        self.window2.setWindowIcon(QIcon(DIR_PATH + "/resources/images/icons8-clouds-80-dark-edge.png"))
        self.lw2 = Ui_ExternalLoginWindow()
        self.lw2.setupUi(self.window2)
        self.window2.show()
        self.window2.setWindowTitle(f"OneDrive login for profile {profile}")

        self.config_file = global_config[profile]["config_file"].strip('"')
        self.config_dir = re.search(r"(.+)/.+$", self.config_file).group(1)

        self.lw2.label_2.setOpenExternalLinks(True)
        self.lw2.pushButton_login.setEnabled(False)

        self.lw2.lineEdit_response_url.textChanged.connect(self.enable_login_button)

        self.lw2.pushButton_login.clicked.connect(lambda: self.get_response_url(self.lw2.lineEdit_response_url.text(), profile))

    def enable_login_button(self):
        # Enable 'Save' button only when valid URL with login response code is provided.
        if "nativeclient?code=" in self.lw2.lineEdit_response_url.text():
            logging.debug(f"[GUI] Valid login response code provided. Enabling Save button.")
            self.lw2.pushButton_login.setEnabled(True)
        else:
            logging.debug(f"[GUI] Invalid login response code provided. Disabling Save button.")
            self.lw2.pushButton_login.setEnabled(False)

    def get_response_url(self, response_url, profile):
        # Get response URL from OneDrive OAuth2
        if "nativeclient?code=" in response_url:
            logging.info("Login performed")

            options = f'--reauth --auth-response "{response_url}"'
            self.login = MaintenanceWorker(profile, options)
            self.login.start()
            self.login.update_login_response.connect(self.login_failed_dialog)
        else:
            pass

    def login_failed_dialog(self, response: dict):
        profile_name = response["profile_name"]
        response_reason = response["response"]

        if response_reason == "success":
            self.profile_status_pages[profile_name].label_onedrive_status.setText("Login successful. Please, start sync manually.")

            response_dialog = QMessageBox.information(
                self,
                "Login successful",
                f"Login successful!  Please start sync manually.",
                buttons=QMessageBox.Ok,
                defaultButton=QMessageBox.Ok,
            )
        else:
            self.profile_status_pages[profile_name].label_onedrive_status.setText("Login failed.")

            response_dialog = QMessageBox.critical(
                self,
                "Login failed",
                f"Login failed!  Please verify your response URL and try again.<br><br> {response_reason}",
                buttons=QMessageBox.Ok,
                defaultButton=QMessageBox.Ok,
            )

        if response_dialog == QMessageBox.Ok:
            logging.info("[GUI] Login response message acknowledged.")

            if "True " not in gui_settings.get("QWebEngine_login") and response_reason == "success":
                self.window2.hide()
            elif response_reason == "success":
                self.window1.hide()

            else:
                self.window2.activateWindow()
                self.window2.raise_()

    def remove_worker(self, profile_name):
        logging.info(f"[{profile_name}] Removing thread info")
        workers.pop(profile_name, None)
        logging.info(f"[GUI] Remaining running workers: {workers}")

    def add_profile(self, profile_name):
        """
        Adds a new profile to the main window UI.
        Called when a new profile is created through the wizard.
        """
        logging.info(f"[MAIN_WINDOW] Adding profile {profile_name} to main window UI")

        # Check if profile already exists in UI
        if profile_name in self.profile_status_pages:
            logging.info(f"[MAIN_WINDOW] Profile {profile_name} already exists in UI, skipping add")
            return

        # Create a profile status page and add it to the UI
        self.comboBox.addItem(profile_name)
        self.profile_status_pages[profile_name] = ProfileStatusPage(profile_name)
        self.profile_status_pages[profile_name].start_sync_signal.connect(self.start_onedrive_monitor)
        self.profile_status_pages[profile_name].stop_sync_signal.connect(self.stop_onedrive_monitor)
        self.profile_status_pages[profile_name].quit_gui_signal.connect(self.graceful_shutdown)
        self.stackedLayout.addWidget(self.profile_status_pages[profile_name])

        # Select the newly added profile
        index = self.comboBox.findText(profile_name)
        if index >= 0:
            self.comboBox.setCurrentIndex(index)
            self.stackedLayout.setCurrentIndex(index)
            logging.info(f"[MAIN_WINDOW] Selected profile {profile_name} at index {index}")

        # Show comboBox if more than one profile exists
        if len(self.profile_status_pages) > 1:
            self.comboBox.show()

        # Force update the UI
        self.comboBox.update()
        self.update()

        # Make the profile visible and force a layout refresh
        self.comboBox.show()
        self.stackedLayout.update()
        self.verticalLayout_2.update()

        # Process events to ensure UI updates immediately
        from PySide6.QtCore import QCoreApplication

        QCoreApplication.processEvents()

    @Slot(str, str)
    def rename_profile_in_main_window(self, old_name, new_name):
        """
        Updates the profile name in the main window UI elements.
        """
        logging.info(f"[MAIN_WINDOW] Renaming profile '{old_name}' to '{new_name}' in main window UI.")

        # 1. Update the item text in the comboBox.
        index = self.comboBox.findText(old_name)
        if index >= 0:
            self.comboBox.setItemText(index, new_name)
            logging.debug(f"[MAIN_WINDOW] Updated comboBox item at index {index} from '{old_name}' to '{new_name}'.")
        else:
            logging.warning(f"[MAIN_WINDOW] Profile '{old_name}' not found in comboBox.")

        # 2. Update the key in the self.profile_status_pages dictionary.
        if old_name in self.profile_status_pages:
            self.profile_status_pages[new_name] = self.profile_status_pages.pop(old_name)
            # Also update the profile_name attribute within the ProfileStatusPage instance
            self.profile_status_pages[new_name].profile_name = new_name
            logging.debug(f"[MAIN_WINDOW] Updated profile_status_pages key from '{old_name}' to '{new_name}'.")
        else:
            logging.warning(f"[MAIN_WINDOW] Profile '{old_name}' not found in profile_status_pages.")

        # 3. Update the key in the workers dictionary if a worker exists.
        if old_name in workers:
            workers[new_name] = workers.pop(old_name)
            # Also update the profile_name attribute within the WorkerThread instance
            workers[new_name].profile_name = new_name
            logging.debug(f"[MAIN_WINDOW] Updated workers key from '{old_name}' to '{new_name}'.")
        else:
            logging.debug(f"[MAIN_WINDOW] No worker found for profile '{old_name}'.")

        # Force update the UI
        self.comboBox.update()
        self.update()

        # Process events to ensure UI updates immediately
        from PySide6.QtCore import QCoreApplication

        QCoreApplication.processEvents()

    def remove_profile(self, profile_name):
        """
        Removes onedrive profile from the GUI.
        """
        combo_box_index = self.comboBox.findText(profile_name)
        self.comboBox.removeItem(combo_box_index)
        self.stackedLayout.setCurrentIndex(0)
        self.profile_status_pages.pop(profile_name, None)
        global_config.pop(profile_name, None)
        logging.info(global_config)

        if len(global_config) < 2:
            self.comboBox.hide()

    def show_main_window(self):
        self.show()

    def hide_main_window(self):
        self.hide()


class ProfileStatusPage(QWidget, Ui_status_page):
    start_sync_signal = Signal(str)
    stop_sync_signal = Signal(str)
    quit_gui_signal = Signal()

    def __init__(self, profile_name):
        super(ProfileStatusPage, self).__init__()

        self.profile_name = profile_name

        # Set up the user interface from Designer.
        self.setupUi(self)

        # Configure Icons
        self.start_icon = QIcon(DIR_PATH + "/resources/images/play.png")
        self.stop_icon = QIcon(DIR_PATH + "/resources/images/stop.png")
        self.storage_icon = QPixmap(DIR_PATH + "/resources/images/storage.png").scaled(26, 26, Qt.KeepAspectRatio)
        self.quit_icon = QIcon(DIR_PATH + "/resources/images/quit.png")
        self.close_icon = QIcon(DIR_PATH + "/resources/images/close-filled.png")

        self.folder_icon = QIcon(DIR_PATH + "/resources/images/folder.png")
        self.profile_icon = QIcon(DIR_PATH + "/resources/images/account.png")
        self.settings_icon = QIcon(DIR_PATH + "/resources/images/gear.png")

        # Show Start/Stop buttons
        if gui_settings.get("combined_start_stop_button") == "True":
            self.pushButton_start_stop.show()
            self.pushButton_start.hide()
            self.pushButton_stop.hide()
        else:
            self.pushButton_start_stop.hide()
            self.pushButton_start.show()
            self.pushButton_stop.show()

        # Combined Start/Stop button
        self.pushButton_start_stop.setIcon(self.start_icon)
        self.pushButton_start_stop.setText("")
        self.pushButton_start_stop.clicked.connect(self.start_monitor)

        # Separate start/stop buttons
        self.pushButton_start.setIcon(self.start_icon)
        self.pushButton_start.setText("")
        self.pushButton_start.clicked.connect(self.start_monitor)

        self.pushButton_stop.setIcon(self.stop_icon)
        self.pushButton_stop.setText("")
        self.pushButton_stop.clicked.connect(self.stop_monitor)

        # Temp Quit button
        self.pushButton_quit.setIcon(self.quit_icon)
        self.pushButton_quit.setText("")
        self.pushButton_quit.clicked.connect(self.quit_gui)

        # Close Button
        if gui_settings.get("frameless_window") == "True":
            self.pushButton_close.setIcon(self.close_icon)
            self.pushButton_close.setText("")
            self.pushButton_close.clicked.connect(lambda: self.close())
        else:
            self.pushButton_close.hide()

        # Free Space Icon
        self.label_free_space_icon.setPixmap(self.storage_icon)
        self.label_free_space_icon.hide()

        # Open Sync Dir
        self.pushButton_open_dir.setText("")
        self.pushButton_open_dir.setIcon(self.folder_icon)
        self.pushButton_open_dir.clicked.connect(self.open_sync_dir)

        # Open Profiles window
        self.pushButton_profiles.setText("")
        self.pushButton_profiles.setIcon(self.profile_icon)
        self.pushButton_profiles.clicked.connect(lambda: profile_settings_window.show())
        self.pushButton_profiles.clicked.connect(lambda: profile_settings_window.start_unsaved_changes_timer())

        # Open GUI Settings window
        self.pushButton_gui_settings.setText("")
        self.pushButton_gui_settings.setIcon(self.settings_icon)
        self.pushButton_gui_settings.clicked.connect(self.show_gui_settings_window)

        # Show Account Type on GUI startup (when sync is not running)
        self.label_account_type.setText(global_config[self.profile_name]["account_type"])

        # Allow hyperlinks in status messages
        self.label_onedrive_status.setOpenExternalLinks(True)

        # Show last known Free Space on GUI startup (when sync is not running)
        _free_space = global_config[self.profile_name]["free_space"]

        if _free_space == "0":
            self.label_free_space.setText("")
            # self.label_free_space_icon.hide()
        else:
            self.label_free_space.setText(global_config[self.profile_name]["free_space"])

    def open_sync_dir(self):
        sync_dir = global_config[self.profile_name]["onedrive"]["sync_dir"].strip('"')
        url = QUrl(os.path.expanduser(sync_dir))
        QDesktopServices.openUrl(url)

    def show_gui_settings_window(self):
        # self.gui_settings_window = GuiSettingsWindow()
        gui_settings_window.show()

    def stop_monitor(self):
        self.stop_sync_signal.emit(self.profile_name)

    def start_monitor(self):
        # self.start_onedrive_monitor(self.profile_name)
        self.start_sync_signal.emit(self.profile_name)

    def quit_gui(self):
        self.quit_gui_signal.emit()


class AlignDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = Qt.AlignRight
