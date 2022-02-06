import sys, psutil, os, subprocess, signal
from configparser import ConfigParser

from PySide6.QtWidgets import (QWidget, QApplication, QMainWindow, QMenu, QSystemTrayIcon, QDialog)
from PySide6.QtGui import QIcon
from PySide6.QtCore import QTimer, QUrl

from ui.ui_mainwindow import Ui_MainWindow
from ui.ui_settings import Ui_Form
from ui.ui_login import Ui_LoginWindow

CONFIG_FILE = os.path.expanduser('~/.config/onedrive/config')

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # Open Settings window
        self.pushButton_3.clicked.connect(lambda: self.show_settings())

        # Update OneDrive Status
        self.pushButton_10.clicked.connect(lambda: self.oneDriveProcessStatus())

        # Start OneDrive service
        self.pushButton_4.clicked.connect(lambda: os.system('systemctl --user start onedrive'))

        # Stop OneDrive service
        self.pushButton_7.clicked.connect(lambda: os.system('systemctl --user stop onedrive'))

        # Restart OneDrive service
        self.pushButton_9.clicked.connect(lambda: os.system('systemctl --user restart onedrive'))     

        # Start OneDrive monitoring
        self.pushButton_5.clicked.connect(lambda: self.oneDriveMonitor('onedrive --monitor'))       

        # Stop OneDrive monitoring
        self.pushButton_6.clicked.connect(lambda: os.system('pkill onedrive'))  

        # Force OneDrive resync
        # self.pushButton_6.clicked.connect(lambda: os.system('pkill onedrive'))     
        # 

        # Open login form TODO: testing
        self.pushButton_2.setText("login")
        self.pushButton_2.clicked.connect(lambda: self.show_login())    


        # Refresh Sync Status
        self.pushButton_11.clicked.connect(lambda: self.label_4.setText("Retreiving status...")) 
        self.pushButton_11.clicked.connect(lambda: self.oneDriveSyncStatus())          

        self.text_timer = QTimer()
        self.text_timer.setSingleShot(False)
        self.text_timer.timeout.connect(lambda: self.oneDriveProcessStatus())
        self.text_timer.start(1000) 



        # System Tray
      
        self.tray = QSystemTrayIcon()
        if self.tray.isSystemTrayAvailable():

            icon = QIcon("icons8-clouds-48.png")
            menu = QMenu()

            actionshow = menu.addAction("Show/Hide")
            actionshow.triggered.connect(lambda: self.hide() if self.isVisible() else self.show())
            settingAction = menu.addAction("Settings")
            settingAction.triggered.connect(self.show_settings)
            quitAction = menu.addAction("Quit")
            quitAction.triggered.connect(sys.exit)

            self.tray.setIcon(icon)
            self.tray.setContextMenu(menu)
            self.tray.show()
            self.tray.setToolTip("This is OneDriveGUI")
            # self.tray.showMessage("OneDriveGUI", "OneDriveGUI started sucessfully.")
        else:
            self.tray = None

    # Check OneDrive status
    def oneDriveProcessStatus(self):
        for onedrive_process in psutil.process_iter():
            if onedrive_process.name().lower() == 'onedrive' and onedrive_process.status() != 'zombie':
                # print("OneDrive is running.")
                self.label_3.setText("running")
                return True
        # print("OneDrive is NOT running.")
        self.label_3.setText("not running")
        return False        

    def oneDriveSyncStatus(self):
        
        status = subprocess.check_output(['onedrive', '--display-sync-status'])
        if 'in sync' in str(status):
            self.label_4.setText("In Sync")
            return True
        else:
            self.label_4.setText("Out of Sync")
            return False

    # def oneDriveMonitor(self, state):
        # if state == 'start':
        #     self.onedrive_process = subprocess.Popen('onedrive --monitor -v', stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
        #     while True:
        #         onedrive_output = self.onedrive_process.communicate()
        #         print(onedrive_output)
        # elif state == 'stop':
        #     os.killpg(os.getpgid(self.onedrive_process.pid), signal.SIGTERM)



        # # def status_checker():
        # #     timer = QTimer()
        # #     timer.setSingleShot(True)
        # #     timer.timeout.connect(status_checker)
        # #     timer.start(1000)

        # # status_checker()        

    async def oneDriveMonitor(self, command):
        self.onedrive_process = subprocess.Popen(command, 
                                            stdout=subprocess.PIPE, 
                                            stderr=subprocess.PIPE, 
                                            shell=True, 
                                            universal_newlines=True)


        while self.onedrive_process.poll() == None:

            if self.onedrive_process.stdout:
                stdout = self.onedrive_process.stdout.readline()        

                if 'Authorize this app visiting' in stdout:
                    # os.killpg(os.getpgid(self.onedrive_process.pid), signal.SIGTERM)
                    self.onedrive_process.kill()
                    self.show_login()
                if 'time' in stdout:
                    print('# ' + stdout)
                else:
                    print('@@ ' + stdout.strip())


        if self.onedrive_process.stderr:
            stderr = self.onedrive_process.stderr.readline()
            print('!!!!ERROR ' + stderr)

            if 'command not found' in stderr:
                print("Onedrive does not seem to be installed. Please install it as per instruction at https://github.com/abraunegg/onedrive/blob/master/docs/INSTALL.md ")
            elif '--resync is required' in stderr:
                print(stderr.decode() + " Starting resync.")
                self.oneDriveMonitor("onedrive --monitor --resync")
            else:
                print('@@ERROR' + stderr)



    def show_login(self):
        self.window1 = QWidget()
        self.lw = Ui_LoginWindow()
        self.lw.setupUi(self.window1)
        self.window1.show()

        # use static URL for now. TODO: use auth files in the future
        url = 'https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=d50ca740-c83f-4d1b-b616-12c519384f0c&scope=Files.ReadWrite%20Files.ReadWrite.all%20Sites.Read.All%20Sites.ReadWrite.All%20offline_access&response_type=code&prompt=login&redirect_uri=https://login.microsoftonline.com/common/oauth2/nativeclient'
        self.lw.loginFrame.setUrl(QUrl(url))

        # Wait for user to login and obtain response URL
        self.lw.loginFrame.urlChanged.connect(lambda: self.getResponseUrl(self.lw.loginFrame.url().toString()))

    
    def getResponseUrl(self, response_url):
        if 'nativeclient?code=' in response_url:
            os.system(f'onedrive --auth-response "{response_url}"')
            print("Login performed")
        else:
            pass
        




    def show_settings(self):
        self.window2 = QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window2)
        
        self.window2.show()

        self.ui.lineEdit_4.setText(settings['onedrive']['sync_dir'].strip('"'))
        self.ui.lineEdit_4.textChanged.connect(lambda: settings.set('onedrive', 'sync_dir', f'"{self.ui.lineEdit_4.text()}"'))  

        self.ui.lineEdit.setText(settings['onedrive']['log_dir'].strip('"'))
        self.ui.lineEdit.textChanged.connect(lambda: settings.set('onedrive', 'log_dir', f'"{self.ui.lineEdit.text()}"'))  


        skip_files = settings['onedrive']['skip_file'].strip('"').split('|')
        self.ui.listWidget.addItems(skip_files)
        self.ui.pushButton_6.clicked.connect(lambda: self.add_item_to_Qlist(self.ui.lineEdit_2, self.ui.listWidget, skip_files))
        self.ui.pushButton_6.clicked.connect(lambda: settings.set('onedrive', 'skip_file',  '"' + '|'.join(skip_files) + '"' ))
        self.ui.pushButton_6.clicked.connect(self.ui.lineEdit_2.clear)

        # self.ui.listWidget.itemChanged.connect(lambda: print("something changed"))
        # self.ui.listWidget.itemChanged.connect(lambda: settings.set('onedrive', 'skip_file', "|".join(skip_files)))


        skip_dirs = settings['onedrive']['skip_dir'].strip('"').split('|')
        self.ui.listWidget_2.addItems(skip_dirs)        
        self.ui.pushButton_7.clicked.connect(lambda: self.add_item_to_Qlist(self.ui.lineEdit_3, self.ui.listWidget_2, skip_dirs))
        self.ui.pushButton_7.clicked.connect(lambda: settings.set('onedrive', 'skip_dir', '"' + '|'.join(skip_dirs) + '"' ))
        self.ui.pushButton_7.clicked.connect(self.ui.lineEdit_3.clear)

        # self.button2 = QtWidgets.QPushButton("save")
        # self.pushButton_4.setText("save")
        # self.button2.clicked.connect(lambda: settings.set('onedrive', 'skip_dir', f'"{self.input.text()}"')) 
        self.ui.pushButton_4.clicked.connect(lambda: save_config(settings))

        # url = 'https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=d50ca740-c83f-4d1b-b616-12c519384f0c&scope=Files.ReadWrite%20Files.ReadWrite.all%20Sites.Read.All%20Sites.ReadWrite.All%20offline_access&response_type=code&prompt=login&redirect_uri=https://login.microsoftonline.com/common/oauth2/nativeclient'
        # self.ui.webEngineView.setUrl(QUrl(url))
        # self.ui.webEngineView.urlChanged.connect(lambda: print("the url is"))
        # self.ui.webEngineView.urlChanged.connect(lambda: print(str(self.ui.webEngineView.url().toString())))

        # Rate limit
        self.ui.lineEdit_5.setText(settings['onedrive']['rate_limit'].strip('"'))
        self.ui.label_6.setText(str(round(int(self.ui.lineEdit_5.text()) * 8 / 1024 / 1024, 2)) + " MiB/s")
        self.ui.lineEdit_5.textChanged.connect(lambda: settings.set('onedrive', 'rate_limit', f'"{self.ui.lineEdit_5.text()}"'))  
        self.ui.lineEdit_5.textChanged.connect(lambda: self.ui.label_6.setText(str(round(int(self.ui.lineEdit_5.text()) * 8 / 1024 / 1024, 2)) + " MiB/s")) 




    def add_item_to_Qlist(self, source_widget, destination_widget, list):
        if source_widget.text() == "":
            print("Inoring empty value.") 
        elif source_widget.text() in list:
            print("Item already in exemption list.")
        else: 
            list.append(source_widget.text())
            destination_widget.addItem(source_widget.text())                



    def remove_item_from_Qlist(self, QListWidget_name):
        for item in QListWidget_name.selectedItems():
            print("Removing: " + item.text())
            items.remove(item.text())
            QListWidget_name.takeItem(QListWidget_name.row(item))







def read_config(config_file):
    with open(config_file, 'r') as f:
        config_string = '[onedrive]\n' + f.read()

    config = ConfigParser()
    config.read_string(config_string)

    return config


def save_config(new_settings):
    # config = ConfigParser()
    # config.read_dict

    new_settings.write
    print(new_settings)
    print(new_settings['onedrive']['sync_dir'])
    print('saved')

    # new_settings.set('onedrive', 'testoption', '"QQQQQ"')
    
    with open(CONFIG_FILE, 'w') as configfile:
        new_settings.write(configfile)

    # remove first line (section) from config file
    with open(CONFIG_FILE, 'r') as fin:
        data = fin.read().splitlines(True)
    with open(CONFIG_FILE, 'w') as fout:
        fout.writelines(data[1:])


    config = ConfigParser()
    config.read(new_settings)
    # print(config['onedrive']['skip_dir'])







if __name__ == "__main__":
    settings = read_config(CONFIG_FILE)

    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    app.exec()

    
