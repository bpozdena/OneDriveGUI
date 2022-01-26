# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profile_settings_page.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_profile_settings(object):
    def setupUi(self, profile_settings):
        if not profile_settings.objectName():
            profile_settings.setObjectName(u"profile_settings")
        profile_settings.resize(588, 785)
        self.verticalLayout_2 = QVBoxLayout(profile_settings)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(profile_settings)
        self.tabWidget.setObjectName(u"tabWidget")
        self.exemptions_tab_2 = QWidget()
        self.exemptions_tab_2.setObjectName(u"exemptions_tab_2")
        self.verticalLayout_5 = QVBoxLayout(self.exemptions_tab_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.checkBox_3 = QCheckBox(self.exemptions_tab_2)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout_5.addWidget(self.checkBox_3, 1, 0, 1, 2)

        self.label_7 = QLabel(self.exemptions_tab_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.exemptions_tab_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_5.addWidget(self.lineEdit_6, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.exemptions_tab_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_5.addWidget(self.pushButton_3, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_5)

        self.label_8 = QLabel(self.exemptions_tab_2)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_5.addWidget(self.label_8)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.lineEdit_7 = QLineEdit(self.exemptions_tab_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_6.addWidget(self.lineEdit_7, 1, 0, 1, 1)

        self.pushButton_9 = QPushButton(self.exemptions_tab_2)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout_6.addWidget(self.pushButton_9, 1, 1, 1, 1)

        self.pushButton_10 = QPushButton(self.exemptions_tab_2)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)

        self.gridLayout_6.addWidget(self.pushButton_10, 0, 1, 1, 1)

        self.listWidget_3 = QListWidget(self.exemptions_tab_2)
        self.listWidget_3.setObjectName(u"listWidget_3")

        self.gridLayout_6.addWidget(self.listWidget_3, 0, 0, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_6)

        self.label_9 = QLabel(self.exemptions_tab_2)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_5.addWidget(self.label_9)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.pushButton_11 = QPushButton(self.exemptions_tab_2)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy1)

        self.gridLayout_7.addWidget(self.pushButton_11, 0, 1, 1, 1)

        self.listWidget_4 = QListWidget(self.exemptions_tab_2)
        self.listWidget_4.setObjectName(u"listWidget_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.listWidget_4.sizePolicy().hasHeightForWidth())
        self.listWidget_4.setSizePolicy(sizePolicy2)

        self.gridLayout_7.addWidget(self.listWidget_4, 0, 0, 1, 1)

        self.lineEdit_8 = QLineEdit(self.exemptions_tab_2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout_7.addWidget(self.lineEdit_8, 1, 0, 1, 1)

        self.pushButton_12 = QPushButton(self.exemptions_tab_2)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy3)

        self.gridLayout_7.addWidget(self.pushButton_12, 1, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_7)

        self.tabWidget.addTab(self.exemptions_tab_2, "")
        self.logging_tab_2 = QWidget()
        self.logging_tab_2.setObjectName(u"logging_tab_2")
        self.verticalLayout_6 = QVBoxLayout(self.logging_tab_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.checkBox_4 = QCheckBox(self.logging_tab_2)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.gridLayout_8.addWidget(self.checkBox_4, 0, 0, 1, 2)

        self.label_10 = QLabel(self.logging_tab_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_8.addWidget(self.label_10, 1, 0, 1, 1)

        self.lineEdit_9 = QLineEdit(self.logging_tab_2)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout_8.addWidget(self.lineEdit_9, 1, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.logging_tab_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_8.addWidget(self.pushButton_4, 1, 2, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_8)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.tabWidget.addTab(self.logging_tab_2, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.lineEdit_10 = QLineEdit(self.tab_5)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setGeometry(QRect(110, 50, 113, 22))
        self.lineEdit_10.setInputMethodHints(Qt.ImhDigitsOnly)
        self.label_11 = QLabel(self.tab_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 50, 101, 16))
        self.label_12 = QLabel(self.tab_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(250, 50, 71, 16))
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.tabWidget.addTab(self.tab_6, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.pushButton_13 = QPushButton(profile_settings)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.verticalLayout_2.addWidget(self.pushButton_13)


        self.retranslateUi(profile_settings)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(profile_settings)
    # setupUi

    def retranslateUi(self, profile_settings):
        profile_settings.setWindowTitle(QCoreApplication.translate("profile_settings", u"Form", None))
        self.checkBox_3.setText(QCoreApplication.translate("profile_settings", u"Skip Hidden Files", None))
        self.label_7.setText(QCoreApplication.translate("profile_settings", u"Sync Folder:", None))
        self.pushButton_3.setText(QCoreApplication.translate("profile_settings", u"Browse", None))
        self.label_8.setText(QCoreApplication.translate("profile_settings", u"Skip files:", None))
        self.pushButton_9.setText(QCoreApplication.translate("profile_settings", u"Add", None))
        self.pushButton_10.setText(QCoreApplication.translate("profile_settings", u"Remove", None))
        self.label_9.setText(QCoreApplication.translate("profile_settings", u"Skip directories:", None))
        self.pushButton_11.setText(QCoreApplication.translate("profile_settings", u"Remove", None))
        self.pushButton_12.setText(QCoreApplication.translate("profile_settings", u"Add", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.exemptions_tab_2), QCoreApplication.translate("profile_settings", u"Monitored Files", None))
        self.checkBox_4.setText(QCoreApplication.translate("profile_settings", u"Enable Logging", None))
        self.label_10.setText(QCoreApplication.translate("profile_settings", u"Log location:", None))
        self.pushButton_4.setText(QCoreApplication.translate("profile_settings", u"Browse", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.logging_tab_2), QCoreApplication.translate("profile_settings", u"Logging", None))
        self.label_11.setText(QCoreApplication.translate("profile_settings", u"Rate Limit [B/s]", None))
        self.label_12.setText(QCoreApplication.translate("profile_settings", u"(Mbit/s)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("profile_settings", u"Rate Limit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("profile_settings", u"Page", None))
        self.pushButton_13.setText(QCoreApplication.translate("profile_settings", u"Save", None))
    # retranslateUi

