# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OneDriveGUIAnUifJ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1115, 781)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(10, 70, 401, 531))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 623, 101, 81))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(150, 620, 101, 81))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(290, 620, 101, 81))
        self.toolButton = QToolButton(self.centralwidget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(240, 640, 32, 33))
        self.toolButton_2 = QToolButton(self.centralwidget)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setGeometry(QRect(20, 20, 32, 33))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 20, 191, 31))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(440, 10, 661, 721))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.tabWidget = QTabWidget(self.frame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(20, 40, 621, 631))
        self.exemptions_tab = QWidget()
        self.exemptions_tab.setObjectName(u"exemptions_tab")
        self.textEdit = QTextEdit(self.exemptions_tab)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(40, 340, 501, 231))
        self.textEdit_2 = QTextEdit(self.exemptions_tab)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(40, 50, 501, 241))
        self.label_4 = QLabel(self.exemptions_tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 20, 58, 18))
        self.label_5 = QLabel(self.exemptions_tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 310, 111, 18))
        self.tabWidget.addTab(self.exemptions_tab, "")
        self.logging_tab = QWidget()
        self.logging_tab.setObjectName(u"logging_tab")
        self.checkBox = QCheckBox(self.logging_tab)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(150, 30, 88, 22))
        self.label_2 = QLabel(self.logging_tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 30, 101, 18))
        self.lineEdit = QLineEdit(self.logging_tab)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(150, 60, 421, 32))
        self.label_3 = QLabel(self.logging_tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 70, 101, 18))
        self.tabWidget.addTab(self.logging_tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(540, 680, 88, 34))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1115, 30))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open Folder", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Sync", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Skip files:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Skip directories:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.exemptions_tab), QCoreApplication.translate("MainWindow", u"Exemptions", None))
        self.checkBox.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Enable logging:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Log location:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.logging_tab), QCoreApplication.translate("MainWindow", u"Logging", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Page", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Page", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi

