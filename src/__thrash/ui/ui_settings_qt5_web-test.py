# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_qt5_web-testdOxRon.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2.QtWebEngineWidgets import QWebEngineView



class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(697, 846)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.exemptions_tab = QWidget()
        self.exemptions_tab.setObjectName(u"exemptions_tab")
        self.verticalLayout_3 = QVBoxLayout(self.exemptions_tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.checkBox_2 = QCheckBox(self.exemptions_tab)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout_3.addWidget(self.checkBox_2, 1, 0, 1, 2)

        self.label = QLabel(self.exemptions_tab)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.exemptions_tab)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_3.addWidget(self.lineEdit_4, 0, 1, 1, 1)

        self.pushButton = QPushButton(self.exemptions_tab)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_3.addWidget(self.pushButton, 0, 2, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_3)

        self.label_4 = QLabel(self.exemptions_tab)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit_2 = QLineEdit(self.exemptions_tab)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.exemptions_tab)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_2.addWidget(self.pushButton_6, 1, 1, 1, 1)

        self.pushButton_5 = QPushButton(self.exemptions_tab)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.pushButton_5, 0, 1, 1, 1)

        self.listWidget = QListWidget(self.exemptions_tab)
        self.listWidget.setObjectName(u"listWidget")

        self.gridLayout_2.addWidget(self.listWidget, 0, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_2)

        self.label_5 = QLabel(self.exemptions_tab)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_3.addWidget(self.label_5)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_8 = QPushButton(self.exemptions_tab)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.pushButton_8, 0, 1, 1, 1)

        self.listWidget_2 = QListWidget(self.exemptions_tab)
        self.listWidget_2.setObjectName(u"listWidget_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.listWidget_2.sizePolicy().hasHeightForWidth())
        self.listWidget_2.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.listWidget_2, 0, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.exemptions_tab)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 1, 0, 1, 1)

        self.pushButton_7 = QPushButton(self.exemptions_tab)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.pushButton_7, 1, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)

        self.tabWidget.addTab(self.exemptions_tab, "")
        self.logging_tab = QWidget()
        self.logging_tab.setObjectName(u"logging_tab")
        self.verticalLayout_4 = QVBoxLayout(self.logging_tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.checkBox = QCheckBox(self.logging_tab)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_4.addWidget(self.checkBox, 0, 0, 1, 2)

        self.label_3 = QLabel(self.logging_tab)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 1, 0, 1, 1)

        self.lineEdit = QLineEdit(self.logging_tab)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_4.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.logging_tab)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_4.addWidget(self.pushButton_2, 1, 2, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.logging_tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.webEngineView = QWebEngineView(self.tab_4)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setGeometry(QRect(30, 150, 611, 461))
        self.webEngineView.setUrl(QUrl(u"https://www.seznam.cz/"))
        self.tabWidget.addTab(self.tab_4, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout.addWidget(self.pushButton_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"Skip Hidden Files", None))
        self.label.setText(QCoreApplication.translate("Form", u"Sync Folder:", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Browse", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Skip files:", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"Add", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"Remove", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Skip directories:", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"Remove", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"Add", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.exemptions_tab), QCoreApplication.translate("Form", u"Monitored Files", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"Enable Logging", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Log location:", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Browse", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.logging_tab), QCoreApplication.translate("Form", u"Logging", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"Page", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Form", u"Page", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"Save", None))
    # retranslateUi

