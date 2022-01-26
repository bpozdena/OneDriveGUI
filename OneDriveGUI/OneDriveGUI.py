import os
import psutil
import re
import subprocess
import sys
from configparser import ConfigParser


from PySide6.QtCore import QThread, QTimer, QUrl, Signal, QFileInfo
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QWidget, QApplication, QMainWindow, QMenu, QSystemTrayIcon, QListWidget, QListWidgetItem, QFileIconProvider, QStackedLayout, QVBoxLayout, QLabel)

from ui.ui_login import Ui_LoginWindow
from ui.ui_settings import Ui_settings_window
from ui.ui_list_item_widget import Ui_list_item_widget

from ui.ui_mainwindow import Ui_MainWindow
from ui.ui_process_status_page import Ui_status_page

from ui.ui_profile_settings_page import Ui_profile_settings

CONFIG_FILE = os.path.expanduser('/home/bob/.config/onedrive/accounts/boris@pozdena.eu/config')
PROFILES_FILE = os.path.expanduser('~/.config/onedrive-gui/profiles')


class SettingsWindow(QWidget, Ui_settings_window):
    def __init__(self):
        super(SettingsWindow, self).__init__()

        # Set up the user interface from Designer.
        self.setupUi(self)
        


        self.stackedLayout = QStackedLayout()

        for account in global_config:
            print(account)
            self.listWidget.addItem(account)
            self.page = ProfileSettingsPage(account)
            self.stackedLayout.addWidget(self.page)

        self.horizontalLayout.addLayout(self.stackedLayout)
        self.listWidget.itemSelectionChanged.connect(self.switch_account_settings_page)
        self.show()
        
    def switch_account_settings_page(self):
        self.stackedLayout.setCurrentIndex(self.listWidget.currentRow())


    def add_item_to_qlist(self, source_widget, destination_widget, list):
        if source_widget.text() == "":
            print("Inoring empty value.")
        elif source_widget.text() in list:
            print("Item already in exemption list.")
        else:
            list.append(source_widget.text())
            destination_widget.addItem(source_widget.text())

    def remove_item_from_qlist(self, qlistwidget_name):
        for item in qlistwidget_name.selectedItems():
            print("Removing: " + item.text())
            # items.remove(item.text())
            qlistwidget_name.takeItem(qlistwidget_name.row(item))


class ProfileStatusPage(QWidget, Ui_status_page):
    def __init__(self, profile):
        super(ProfileStatusPage, self).__init__()

        # Set up the user interface from Designer.
        self.setupUi(self)

        # Show selected profile name
        self.label_4.setText(profile)

        # # Open Settings window
        self.pushButton_settings.clicked.connect(self.show_settings_window)     

        # Open login form TODO: testing
        # self.pushButton_2.setText("login")
        # self.pushButton_2.clicked.connect(lambda: self.show_login())    

    def show_settings_window(self):
        self.settings_window = SettingsWindow()
        self.settings_window.show()


class ProfileSettingsPage(QWidget, Ui_profile_settings):
    def __init__(self, profile):
        super(ProfileSettingsPage, self).__init__()

        # Set up the user interface from Designer.
        self.setupUi(self)

        self.lineEdit_6.setText(global_config[profile]['onedrive']['sync_dir'].strip('"'))
        # self.ui.lineEdit_4.textChanged.connect(
        #     lambda: settings.set('onedrive', 'sync_dir', f'"{self.ui.lineEdit_4.text()}"'))

        # self.ui.lineEdit.setText(settings['onedrive']['log_dir'].strip('"'))
        # self.ui.lineEdit.textChanged.connect(
        #     lambda: settings.set('onedrive', 'log_dir', f'"{self.ui.lineEdit.text()}"'))

        # skip_files = settings['onedrive']['skip_file'].strip('"').split('|')
        # self.ui.listWidget.addItems(skip_files)
        # self.ui.pushButton_6.clicked.connect(
        #     lambda: self.add_item_to_qlist(self.ui.lineEdit_2, self.ui.listWidget, skip_files))
        # self.ui.pushButton_6.clicked.connect(
        #     lambda: settings.set('onedrive', 'skip_file', '"' + '|'.join(skip_files) + '"'))
        # self.ui.pushButton_6.clicked.connect(self.ui.lineEdit_2.clear)

        # skip_dirs = settings['onedrive']['skip_dir'].strip('"').split('|')
        # self.ui.listWidget_2.addItems(skip_dirs)
        # self.ui.pushButton_7.clicked.connect(
        #     lambda: self.add_item_to_qlist(self.ui.lineEdit_3, self.ui.listWidget_2, skip_dirs))
        # self.ui.pushButton_7.clicked.connect(
        #     lambda: settings.set('onedrive', 'skip_dir', '"' + '|'.join(skip_dirs) + '"'))
        # self.ui.pushButton_7.clicked.connect(self.ui.lineEdit_3.clear)

        # self.ui.pushButton_4.clicked.connect(lambda: save_config(settings))

        # # Rate limit
        # self.ui.lineEdit_5.setText(settings['onedrive']['rate_limit'].strip('"'))
        # self.ui.label_6.setText(str(round(int(self.ui.lineEdit_5.text()) * 8 / 1000 / 1000, 2)) + " Mbit/s")
        # self.ui.lineEdit_5.textChanged.connect(lambda: settings.set('onedrive', 'rate_limit', f'"{self.ui.lineEdit_5.text()}"'))
        # self.ui.lineEdit_5.textChanged.connect(lambda: self.ui.label_6.setText(str(round(int(self.ui.lineEdit_5.text()) * 8 / 1000 / 1000, 2)) + " Mbit/s"))




class TaskList(QWidget, Ui_list_item_widget):
    def __init__(self):
        super(TaskList, self).__init__()

        # Set up the user interface from Designer.
        self.setupUi(self)



    def set_icon (self, file_path):
        self.fileInfo = QFileInfo(file_path)
        self.iconProvider = QFileIconProvider()
        self.icon = self.iconProvider.icon(self.fileInfo)    

        # icon = QIcon(icon_file)
        self.toolButton.setIcon(self.icon)

    def set_file_name(self, file_path):
        self.ls_label_file_name.setText(file_path)

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
        #     self.ls_label_task.hide()
        #     self.ls_label_status.hide()
        #     self.ls_label_dir.show()
        else:
            self.ls_progressBar.show()
        #     self.ls_label_task.show()
        #     self.ls_label_status.show()
        #     self.ls_label_dir.hide()  


class WorkerThread(QThread):
    update_credentials = Signal()
    update_progress = Signal(dict)
    update_progress_new = Signal(dict, str)
    trigger_resync = Signal()

    def __init__(self, profile):
        super(WorkerThread, self).__init__()
        print(f"starting worker for profile {profile}")
        print(global_config[profile])
        self.config_file = global_config[profile]['config_file']
        self.config_folder = re.search(r"(.+)/.+$", self.config_file)
        print(self.config_file)
        self._command = f"onedrive --confdir='{self.config_folder.group(1)}' --monitor -v"
        print(f"command is: {self._command}")
        self._profile_name = profile

    def run(self, resync=False):
        matches = ['Downloading file', 'Downloading new file', 'Uploading file', 'Uploading new file',
                   'Uploading modified file', 'Downloading modified file']
        file_name = None

    

        self.onedrive_process = subprocess.Popen(self._command + '--resync' if resync else self._command,
                                                 stdout=subprocess.PIPE,
                                                 stderr=subprocess.PIPE,
                                                 shell=True,
                                                 universal_newlines=True)

        # TODO: De-monster once all possible situations are handled correctly. 
        while self.onedrive_process.poll() is None:
            if self.onedrive_process.stdout:
                stdout = self.onedrive_process.stdout.readline()
                # print(f"worker: {stdout.strip()}")
                print(f'[{self._profile_name}] ' + stdout.strip())

                if 'Authorize this app visiting' in stdout:
                    self.onedrive_process.kill()
                    self.update_credentials.emit()

                elif any(x in stdout for x in matches):  # capture file uploads and downloads
                    # self.tray.setIcon(QIcon("resources/images/icons8-cloud-sync-40_2.png")) 
                    print('# ' + stdout)
                    file_operation = re.search(r'\b([Uploading|Downloading]+)*', stdout)
                    file_name = re.search(r".*/(.+)\s+\.+", stdout)
                    file_path = re.search(r"\b[file]+\s(.+)\s+\.\.\.", stdout)
                    transfer_complete = 'done' in stdout
                    progress = '0' # if transfer_complete else '0'

                    transfer_progress = {
                        "file_operation": file_operation.group(1),
                        "file_name": 'unknown file name' if file_name is None else file_name.group(1),
                        "progress": progress,
                        "transfer_complete": transfer_complete}

                    transfer_progress_new = {
                        "file_operation": file_operation.group(1),
                        "file_path": 'unknown file name' if file_path is None else file_path.group(1),
                        "progress": progress,
                        "transfer_complete": transfer_complete}                        
    
                    if transfer_complete:
                        self.update_progress.emit(transfer_progress)
                        self.update_progress_new.emit(transfer_progress_new, self._profile_name)

                elif '% |' in stdout and file_name is not None:  # capture upload/download progress
                    file_operation = re.search(r'\b([Uploading|Downloading]+)*', stdout)
                    progress = re.search(r'\s([0-9]+)%', stdout)
                    transfer_complete = progress.group(1) == '100'

                    transfer_progress = {
                        "file_operation": file_operation.group(1),
                        "file_name": 'Resuming last file...' if file_name is None else file_name.group(1),
                        "progress": progress.group(1),
                        "transfer_complete": transfer_complete}

                    transfer_progress_new = {
                        "file_operation": file_operation.group(1),
                        "file_path": 'unknown file name' if file_path is None else file_path.group(1),
                        "progress": progress.group(1),
                        "transfer_complete": transfer_complete}                         

                    self.update_progress.emit(transfer_progress)
                    self.update_progress_new.emit(transfer_progress_new, self._profile_name)

                elif 'Sync with OneDrive is complete' in stdout:
                    pass
                    # self.tray.setIcon(QIcon("resources/images/icons8-cloud-done-40_2.png"))        

                elif 'Remaining free space on OneDrive' in stdout:
                    pass

                elif 'Processing' in stdout:
                    pass
                    # self.tray.setIcon(QIcon("resources/images/icons8-cloud-sync-40_2.png")) 

                else:
                    pass
                    # print('@@ no match')

        if self.onedrive_process.stderr:
            stderr = self.onedrive_process.stderr.readline()
            if stderr != '':
                if 'command not found' in stderr:
                    print("""Onedrive does not seem to be installed. Please install it as per instruction at 
                    https://github.com/abraunegg/onedrive/blob/master/docs/INSTALL.md """)

                elif '--resync is required' in stderr:
                    print(str(stderr) + " Starting resync.")
                    self.trigger_resync.emit()

                    self.run(resync=True)
                else:
                    print('@@ERROR' + stderr)


class MainWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        self.workers= {}

        super(MainWindow, self).__init__()
        self.setupUi(self)
        #
        # Menu
        # 

        # Update OneDrive Status
        self.actionRefresh_Service_Status.triggered.connect(lambda: self.onedrive_process_status())

        # Start OneDrive service
        self.actionStart_Service.triggered.connect(lambda: os.system('systemctl --user start onedrive'))


        # Stop OneDrive service
        self.actionStop_Service.triggered.connect(lambda: os.system('systemctl --user stop onedrive'))


        # Restart OneDrive service
        self.actionRestart_Service.triggered.connect(lambda: os.system('systemctl --user restart onedrive'))


        # Start OneDrive monitoring
        self.actionStart_Monitor.triggered.connect(lambda: self.start_onedrive_monitor('boris@pozdena.eu'))


        # Stop OneDrive monitoring
        self.actionStop_Monitor.triggered.connect(lambda: os.system('pkill onedrive'))


        # Refresh Sync Status
        self.actionObtain_Sync_Status.triggered.connect(lambda: self.label_4.setText("Retreiving status..."))
        self.actionObtain_Sync_Status.triggered.connect(lambda: self.onedrive_sync_status())

        # Start second account
        self.actionstart.triggered.connect(lambda: self.start_onedrive_monitor('bpozdena@gmail.com'))


        self.comboBox.activated.connect(self.switch_account_status_page)
        self.stackedLayout = QStackedLayout()

        self.profile_status_pages = {}
        for profile in global_config:
            self.comboBox.addItem(profile)
            self.profile_status_pages[profile] = ProfileStatusPage(profile)
            self.stackedLayout.addWidget(self.profile_status_pages[profile])
        
        self.verticalLayout_2.addLayout(self.stackedLayout)



        # self.label_5.hide()
        # self.progressBar.hide()
        # self.progressBar.setValue(0)

        # self.refresh_process_status = QTimer()
        # self.refresh_process_status.setSingleShot(False)
        # self.refresh_process_status.timeout.connect(lambda: self.onedrive_process_status())
        # self.refresh_process_status.start(1000)


        # System Tray
        self.tray = QSystemTrayIcon()
        if self.tray.isSystemTrayAvailable():

            icon = QIcon("resources/images/icons8-clouds-48.png")
            menu = QMenu()

            actionshow = menu.addAction("Show/Hide")
            actionshow.triggered.connect(lambda: self.hide() if self.isVisible() else self.show())
            setting_action = menu.addAction("Settings")
            # setting_action.triggered.connect(self.show_settings)
            quit_action = menu.addAction("Quit")
            quit_action.triggered.connect(sys.exit)

            self.tray.setIcon(icon)
            self.tray.setContextMenu(menu)
            self.tray.show()
            self.tray.setToolTip("This is OneDriveGUI")

        else:
            self.tray = None

    def switch_account_status_page(self):
        self.stackedLayout.setCurrentIndex(self.comboBox.currentIndex())

    def onedrive_process_status(self):
        # Check OneDrive status
        for onedrive_process in psutil.process_iter():
            if onedrive_process.name().lower() == 'onedrive' and onedrive_process.status() != 'zombie':
                self.label_3.setText("running")
                return True

        self.label_3.setText("not running")
        self.tray.setIcon(QIcon("resources/images/icons8-cloud-cross-40_2.png"))
        self.progressBar.hide()
        self.label_5.hide()
        return False

    def onedrive_sync_status(self):
        # Check OneDrive sync status
        status = subprocess.check_output(['onedrive', '--display-sync-status'])
        if 'in sync' in str(status):
            self.label_4.setText("In Sync")
            self.tray.setIcon(QIcon("resources/images/icons8-cloud-done-40_2.png"))
            return True
        else:
            self.label_4.setText("Out of Sync")
            self.tray.setIcon(QIcon("resources/images/icons8-cloud-sync-40_2.png"))
            return False



    def start_onedrive_monitor(self, profile_name):


        # for profile in global_config:
        self.workers[profile_name] = WorkerThread(profile_name)
        self.workers[profile_name].start()

        # self.worker = WorkerThread()
        # self.worker.start()
        # self.worker.update_credentials.connect(self.show_login)
        # self.worker.update_progress.connect(self.event_update_progress)
        # self.worker.trigger_resync.connect(self.show_login)
        self.workers[profile_name].update_progress_new.connect(self.event_update_progress_new)

    def event_update_progress(self, data):
        """
        data:
        transfer_progress = {
            "file_operation": file_operation.group(1),
            "file_name": file_name.group(1),
            "progress": progress.group(1),
            "transfer_complete": transfer_complete
        }
        """

        print(data)
        if self.label_5.isHidden():
            self.label_5.show()
            self.progressBar.show()
        self.label_5.setText(data['file_operation'] + ' ' + data['file_name'])
        self.progressBar.setValue(int(data['progress']))

        if data["transfer_complete"]:
            self.listWidget.insertItem(0, data['file_operation'] + ' of ' + data['file_name'] + ' completed.')
            if not self.label_5.isHidden():
                self.label_5.hide()
                self.progressBar.hide()


    def event_update_progress_new(self, data, profile):
        """
        data:
        transfer_progress = {
            "file_operation": file_operation.group(1),
            "file_path": file_path.group(1),
            "progress": progress.group(1),
            "transfer_complete": transfer_complete
        }

        TODO: De-monster once all possible situations are handled correctly. 
        """
        _sync_dir = os.path.expanduser(global_config[profile]['onedrive']['sync_dir'].strip('"'))
        # profile_status_page = self.profile_status_pages[profile]

        print(data)        
        file_path = f'{_sync_dir}' + "/" + data['file_path']
        absolute_path = QFileInfo(file_path).absolutePath()
        parent_dir = re.search(r".+/([^/]+)/.+$", file_path)
        file_size = QFileInfo(file_path).size()
        file_size_human = humanize_file_size(file_size)
        file_name = QFileInfo(file_path).fileName()
        file_path2 = QFileInfo(file_path).filePath()
        progress = data['progress']
        progress_data = file_size / 100 * int(progress)
        progress_data_human = humanize_file_size(progress_data)

        print("absolute path " + absolute_path)

        print("parent dir " + parent_dir.group(1))
        print("progress: " + progress)
        print("progress data: " + humanize_file_size(progress_data))
        print("file path: " + file_path)
        print("file size: " + humanize_file_size(file_size))
        print("file name: " + file_name)
        print("file path2: " + file_path2)

        if int(data['progress']) == 0 and data['transfer_complete'] == True:
            myQCustomQWidget = TaskList()
            myQCustomQWidget.set_file_name(file_name)
            myQCustomQWidget.set_progress(100)
            myQCustomQWidget.set_icon(file_path)
            myQCustomQWidget.hide_progress_bar(data['transfer_complete'])
            myQCustomQWidget.set_label_1(f"Available in <a href=file:///{absolute_path}>{parent_dir.group(1)}</a>") 
            myQCustomQWidget.set_label_2(f'{file_size_human}')
            # Create QListWidgetItem
            myQListWidgetItem = QListWidgetItem()
            # Set size hint
            myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
            # Add QListWidgetItem into QListWidget
            self.profile_status_pages[profile].listWidget.insertItem(0, myQListWidgetItem)
            self.profile_status_pages[profile].listWidget.setItemWidget(myQListWidgetItem, myQCustomQWidget)
            

        elif int(data['progress']) == 0 and data['transfer_complete'] == False:
            myQCustomQWidget = TaskList()
            myQCustomQWidget.set_file_name(file_name)
            myQCustomQWidget.set_progress(0)
            myQCustomQWidget.set_icon(file_path)
            myQCustomQWidget.hide_progress_bar(data['transfer_complete'])
            myQCustomQWidget.set_label_1(data['file_operation'])
            myQCustomQWidget.set_label_2(f'{progress_data_human} of {file_size_human}')

            # Create QListWidgetItem
            myQListWidgetItem = QListWidgetItem()
            # Set size hint
            myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
            # Add QListWidgetItem into QListWidget
            self.profile_status_pages[profile].listWidget.insertItem(0, myQListWidgetItem)
            self.profile_status_pages[profile].listWidget.setItemWidget(myQListWidgetItem, myQCustomQWidget)

        elif int(data['progress']) == 100 and data['transfer_complete'] == True:
            self.profile_status_pages[profile].listWidget.takeItem(0)

            myQCustomQWidget = TaskList()
            myQCustomQWidget.set_file_name(file_name)
            myQCustomQWidget.set_progress(int(data['progress']))
            myQCustomQWidget.set_icon(file_path)
            myQCustomQWidget.hide_progress_bar(data['transfer_complete'])
            myQCustomQWidget.set_label_1(f"Available in <a href=file:///{absolute_path}>{parent_dir.group(1)}</a>") 
            myQCustomQWidget.set_label_2(f'{file_size_human}')

            # Create QListWidgetItem
            myQListWidgetItem = QListWidgetItem()
            # Set size hint
            myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
            # Add QListWidgetItem into QListWidget
            self.profile_status_pages[profile].listWidget.insertItem(0, myQListWidgetItem)
            self.profile_status_pages[profile].listWidget.setItemWidget(myQListWidgetItem, myQCustomQWidget)


        else:
            self.profile_status_pages[profile].listWidget.takeItem(0)

            myQCustomQWidget = TaskList()
            myQCustomQWidget.set_file_name(file_name)
            myQCustomQWidget.set_progress(int(data['progress']))
            myQCustomQWidget.set_icon(file_path)
            myQCustomQWidget.hide_progress_bar(data['transfer_complete'])
            myQCustomQWidget.set_label_1(data['file_operation'])
            myQCustomQWidget.set_label_2(f'{progress_data_human} of {file_size_human}')

            # Create QListWidgetItem
            myQListWidgetItem = QListWidgetItem()
            # Set size hint
            myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
            # Add QListWidgetItem into QListWidget
            self.profile_status_pages[profile].listWidget.insertItem(0, myQListWidgetItem)
            self.profile_status_pages[profile].listWidget.setItemWidget(myQListWidgetItem, myQCustomQWidget)




    def show_login(self):
        # Show login window
        self.window1 = QWidget()
        self.lw = Ui_LoginWindow()
        self.lw.setupUi(self.window1)
        self.window1.show()

        # use static URL for now. TODO: use auth files in the future
        url = 'https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=d50ca740-c83f-4d1b-b616' \
              '-12c519384f0c&scope=Files.ReadWrite%20Files.ReadWrite.all%20Sites.Read.All%20Sites.ReadWrite.All' \
              '%20offline_access&response_type=code&prompt=login&redirect_uri=https://login.microsoftonline.com' \
              '/common/oauth2/nativeclient '
        self.lw.loginFrame.setUrl(QUrl(url))

        # Wait for user to login and obtain response URL
        self.lw.loginFrame.urlChanged.connect(lambda: self.get_response_url(self.lw.loginFrame.url().toString()))

    def get_response_url(self, response_url):
        # Get response URL from OneDrive OAuth2
        if 'nativeclient?code=' in response_url:
            os.system(f'onedrive --auth-response "{response_url}"')
            print("Login performed")
            self.window1.hide()
        else:
            pass



def read_config(config_file):
    with open(config_file, 'r') as f:
        config_string = '[onedrive]\n' + f.read()

    config = ConfigParser()
    config.read_string(config_string)

    return config


def profile_reader():
    _profiles = ConfigParser()
    _profiles.read(PROFILES_FILE)
    profiles = _profiles._sections 

    for profile in profiles:
        profile_name = profile
        profile_config_file = profiles[profile]['config_file']
        _od_config = read_config(profile_config_file)
        od_config = _od_config._sections

        profiles[profile].update(od_config)


    return profiles





def save_config(new_settings):
    # Save OneDrive config after configuration change.
    # new_settings.write
    print(new_settings)
    print(new_settings['onedrive']['sync_dir'])
    print('saved')

    with open(CONFIG_FILE, 'w') as configfile:
        new_settings.write(configfile)

    # remove first line (section) from config file
    with open(CONFIG_FILE, 'r') as fin:
        data = fin.read().splitlines(True)
    with open(CONFIG_FILE, 'w') as fout:
        fout.writelines(data[1:])

    config = ConfigParser()
    config.read(new_settings)


def humanize_file_size(num, suffix="B"):
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"


if __name__ == "__main__":
    settings = read_config(CONFIG_FILE)
    global_config = profile_reader()

    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    app.exec()
