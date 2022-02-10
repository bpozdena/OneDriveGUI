# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings2DclElV.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_settings_new(object):
    def setupUi(self, settings_new):
        if not settings_new.objectName():
            settings_new.setObjectName(u"settings_new")
        settings_new.resize(619, 892)
        self.centralwidget = QWidget(settings_new)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout.addWidget(self.pushButton_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
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
        self.tabWidget.addTab(self.tab_4, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        settings_new.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(settings_new)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 619, 19))
        settings_new.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(settings_new)
        self.statusbar.setObjectName(u"statusbar")
        settings_new.setStatusBar(self.statusbar)

        self.retranslateUi(settings_new)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(settings_new)
    # setupUi

    def retranslateUi(self, settings_new):
        settings_new.setWindowTitle(QCoreApplication.translate("settings_new", u"MainWindow", None))
        self.pushButton_4.setText(QCoreApplication.translate("settings_new", u"Save", None))
        self.checkBox_2.setText(QCoreApplication.translate("settings_new", u"Skip Hidden Files", None))
        self.label.setText(QCoreApplication.translate("settings_new", u"Sync Folder:", None))
        self.pushButton.setText(QCoreApplication.translate("settings_new", u"Browse", None))
        self.label_4.setText(QCoreApplication.translate("settings_new", u"Skip files:", None))
        self.pushButton_6.setText(QCoreApplication.translate("settings_new", u"Add", None))
        self.pushButton_5.setText(QCoreApplication.translate("settings_new", u"Remove", None))
        self.label_5.setText(QCoreApplication.translate("settings_new", u"Skip directories:", None))
        self.pushButton_8.setText(QCoreApplication.translate("settings_new", u"Remove", None))
        self.pushButton_7.setText(QCoreApplication.translate("settings_new", u"Add", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.exemptions_tab), QCoreApplication.translate("settings_new", u"Monitored Files", None))
        self.checkBox.setText(QCoreApplication.translate("settings_new", u"Enable Logging", None))
        self.label_3.setText(QCoreApplication.translate("settings_new", u"Log location:", None))
        self.pushButton_2.setText(QCoreApplication.translate("settings_new", u"Browse", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.logging_tab), QCoreApplication.translate("settings_new", u"Logging", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("settings_new", u"Page", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("settings_new", u"Page", None))
    # retranslateUi

