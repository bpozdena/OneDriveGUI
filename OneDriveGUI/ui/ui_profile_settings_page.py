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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_profile_settings(object):
    def setupUi(self, profile_settings):
        if not profile_settings.objectName():
            profile_settings.setObjectName(u"profile_settings")
        profile_settings.resize(614, 785)
        self.verticalLayout_2 = QVBoxLayout(profile_settings)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(profile_settings)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(600, 600))
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

        self.lineEdit_sync_dir = QLineEdit(self.exemptions_tab_2)
        self.lineEdit_sync_dir.setObjectName(u"lineEdit_sync_dir")

        self.gridLayout_5.addWidget(self.lineEdit_sync_dir, 0, 1, 1, 1)

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
        self.pushButton_rm_skip_dir = QPushButton(self.exemptions_tab_2)
        self.pushButton_rm_skip_dir.setObjectName(u"pushButton_rm_skip_dir")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_rm_skip_dir.sizePolicy().hasHeightForWidth())
        self.pushButton_rm_skip_dir.setSizePolicy(sizePolicy1)

        self.gridLayout_7.addWidget(self.pushButton_rm_skip_dir, 0, 1, 1, 1)

        self.listWidget_skip_dir = QListWidget(self.exemptions_tab_2)
        self.listWidget_skip_dir.setObjectName(u"listWidget_skip_dir")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.listWidget_skip_dir.sizePolicy().hasHeightForWidth())
        self.listWidget_skip_dir.setSizePolicy(sizePolicy2)

        self.gridLayout_7.addWidget(self.listWidget_skip_dir, 0, 0, 1, 1)

        self.lineEdit_skip_dir = QLineEdit(self.exemptions_tab_2)
        self.lineEdit_skip_dir.setObjectName(u"lineEdit_skip_dir")

        self.gridLayout_7.addWidget(self.lineEdit_skip_dir, 1, 0, 1, 1)

        self.pushButton_add_skip_dir = QPushButton(self.exemptions_tab_2)
        self.pushButton_add_skip_dir.setObjectName(u"pushButton_add_skip_dir")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_add_skip_dir.sizePolicy().hasHeightForWidth())
        self.pushButton_add_skip_dir.setSizePolicy(sizePolicy3)

        self.gridLayout_7.addWidget(self.pushButton_add_skip_dir, 1, 1, 1, 1)


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
        self.gridLayout = QGridLayout(self.tab_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_rate_limit = QLabel(self.tab_5)
        self.label_rate_limit.setObjectName(u"label_rate_limit")

        self.gridLayout.addWidget(self.label_rate_limit, 0, 0, 1, 1)

        self.lineEdit_rate_limit = QLineEdit(self.tab_5)
        self.lineEdit_rate_limit.setObjectName(u"lineEdit_rate_limit")
        self.lineEdit_rate_limit.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout.addWidget(self.lineEdit_rate_limit, 0, 1, 1, 1)

        self.label_rate_limit_mbps = QLabel(self.tab_5)
        self.label_rate_limit_mbps.setObjectName(u"label_rate_limit_mbps")

        self.gridLayout.addWidget(self.label_rate_limit_mbps, 0, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.tabWidget.addTab(self.tab_6, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_discart = QPushButton(profile_settings)
        self.pushButton_discart.setObjectName(u"pushButton_discart")

        self.horizontalLayout.addWidget(self.pushButton_discart)

        self.pushButton_save = QPushButton(profile_settings)
        self.pushButton_save.setObjectName(u"pushButton_save")

        self.horizontalLayout.addWidget(self.pushButton_save)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(profile_settings)

        self.tabWidget.setCurrentIndex(0)


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
        self.pushButton_rm_skip_dir.setText(QCoreApplication.translate("profile_settings", u"Remove", None))
        self.pushButton_add_skip_dir.setText(QCoreApplication.translate("profile_settings", u"Add", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.exemptions_tab_2), QCoreApplication.translate("profile_settings", u"Monitored Files", None))
        self.checkBox_4.setText(QCoreApplication.translate("profile_settings", u"Enable Logging", None))
        self.label_10.setText(QCoreApplication.translate("profile_settings", u"Log location:", None))
        self.pushButton_4.setText(QCoreApplication.translate("profile_settings", u"Browse", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.logging_tab_2), QCoreApplication.translate("profile_settings", u"Logging", None))
        self.label_rate_limit.setText(QCoreApplication.translate("profile_settings", u"Rate Limit [B/s]", None))
        self.label_rate_limit_mbps.setText(QCoreApplication.translate("profile_settings", u"(Mbit/s)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("profile_settings", u"Rate Limit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("profile_settings", u"Page", None))
        self.pushButton_discart.setText(QCoreApplication.translate("profile_settings", u"Discard changes", None))
        self.pushButton_save.setText(QCoreApplication.translate("profile_settings", u"Save", None))
    # retranslateUi

