# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(420, 800)
        MainWindow.setMinimumSize(QSize(420, 0))
        MainWindow.setMaximumSize(QSize(420, 16777215))
        icon = QIcon()
        icon.addFile(u"../../../OneDriveGUI_POC_recovered-multi/icons8-clouds-48.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionfghgfh = QAction(MainWindow)
        self.actionfghgfh.setObjectName(u"actionfghgfh")
        self.actionStart_Service = QAction(MainWindow)
        self.actionStart_Service.setObjectName(u"actionStart_Service")
        self.actionStop_Service = QAction(MainWindow)
        self.actionStop_Service.setObjectName(u"actionStop_Service")
        self.actionRestart_Service = QAction(MainWindow)
        self.actionRestart_Service.setObjectName(u"actionRestart_Service")
        self.actionStart_Monitor = QAction(MainWindow)
        self.actionStart_Monitor.setObjectName(u"actionStart_Monitor")
        self.actionStop_Monitor = QAction(MainWindow)
        self.actionStop_Monitor.setObjectName(u"actionStop_Monitor")
        self.actionForce_Resync = QAction(MainWindow)
        self.actionForce_Resync.setObjectName(u"actionForce_Resync")
        self.actionRefresh_Service_Status = QAction(MainWindow)
        self.actionRefresh_Service_Status.setObjectName(u"actionRefresh_Service_Status")
        self.actionObtain_Sync_Status = QAction(MainWindow)
        self.actionObtain_Sync_Status.setObjectName(u"actionObtain_Sync_Status")
        self.actionTest_Service = QAction(MainWindow)
        self.actionTest_Service.setObjectName(u"actionTest_Service")
        self.actionstart = QAction(MainWindow)
        self.actionstart.setObjectName(u"actionstart")
        self.actionStart_Minimized = QAction(MainWindow)
        self.actionStart_Minimized.setObjectName(u"actionStart_Minimized")
        self.actionStart_Minimized.setCheckable(True)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.comboBox.setFont(font)
        self.comboBox.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox.setStyleSheet(u"")
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setFrame(False)

        self.verticalLayout_2.addWidget(self.comboBox)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_new_profile = QPushButton(self.centralwidget)
        self.pushButton_new_profile.setObjectName(u"pushButton_new_profile")
        self.pushButton_new_profile.setMaximumSize(QSize(9999, 9999))
        self.pushButton_new_profile.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_new_profile.setStyleSheet(u"alignment=Qt.AlignCenter\n"
"")
        self.pushButton_new_profile.setFlat(True)

        self.verticalLayout_3.addWidget(self.pushButton_new_profile)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 420, 22))
        self.menuAdvanced = QMenu(self.menubar)
        self.menuAdvanced.setObjectName(u"menuAdvanced")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuAdvanced.menuAction())
        self.menuAdvanced.addSeparator()
        self.menuAdvanced.addAction(self.actionQuit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"OneDriveGUI", None))
        self.actionfghgfh.setText(QCoreApplication.translate("MainWindow", u"fghgfh", None))
        self.actionStart_Service.setText(QCoreApplication.translate("MainWindow", u"Start Service", None))
        self.actionStop_Service.setText(QCoreApplication.translate("MainWindow", u"Stop Service", None))
        self.actionRestart_Service.setText(QCoreApplication.translate("MainWindow", u"Restart Service", None))
        self.actionStart_Monitor.setText(QCoreApplication.translate("MainWindow", u"Start Monitor", None))
        self.actionStop_Monitor.setText(QCoreApplication.translate("MainWindow", u"Stop Monitor", None))
        self.actionForce_Resync.setText(QCoreApplication.translate("MainWindow", u"Force Resync", None))
        self.actionRefresh_Service_Status.setText(QCoreApplication.translate("MainWindow", u"Refresh Service Status", None))
        self.actionObtain_Sync_Status.setText(QCoreApplication.translate("MainWindow", u"Obtain Sync Status", None))
        self.actionTest_Service.setText(QCoreApplication.translate("MainWindow", u"Test Service", None))
        self.actionstart.setText(QCoreApplication.translate("MainWindow", u"start", None))
        self.actionStart_Minimized.setText(QCoreApplication.translate("MainWindow", u"Start Minimized", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.pushButton_new_profile.setText(QCoreApplication.translate("MainWindow", u"Create/ Import OneDrive profile", None))
        self.menuAdvanced.setTitle(QCoreApplication.translate("MainWindow", u"Advanced", None))
    # retranslateUi

