# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'process_status_page.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QToolButton, QVBoxLayout,
    QWidget)

class Ui_status_page(object):
    def setupUi(self, status_page):
        if not status_page.objectName():
            status_page.setObjectName(u"status_page")
        status_page.resize(441, 763)
        self.verticalLayout = QVBoxLayout(status_page)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(status_page)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 80))
        self.frame.setStyleSheet(u"background-color: rgb(0, 120, 212);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.toolButton_start = QToolButton(self.frame)
        self.toolButton_start.setObjectName(u"toolButton_start")
        self.toolButton_start.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.toolButton_start, 5, 0, 1, 1)

        self.label_onedrive_status = QLabel(self.frame)
        self.label_onedrive_status.setObjectName(u"label_onedrive_status")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_onedrive_status.setFont(font)
        self.label_onedrive_status.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_onedrive_status.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_onedrive_status, 1, 0, 1, 5)

        self.label_status = QLabel(self.frame)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setMaximumSize(QSize(20, 16777215))
        self.label_status.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_status, 5, 2, 1, 1)

        self.toolButton_stop = QToolButton(self.frame)
        self.toolButton_stop.setObjectName(u"toolButton_stop")
        self.toolButton_stop.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.toolButton_stop, 5, 1, 1, 1)

        self.label_account_type = QLabel(self.frame)
        self.label_account_type.setObjectName(u"label_account_type")
        self.label_account_type.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_account_type.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_account_type, 3, 0, 1, 5)

        self.label_free_space = QLabel(self.frame)
        self.label_free_space.setObjectName(u"label_free_space")
        self.label_free_space.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_free_space.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_free_space, 5, 4, 1, 1)

        self.label_version_check = QLabel(self.frame)
        self.label_version_check.setObjectName(u"label_version_check")
        self.label_version_check.setMaximumSize(QSize(20, 16777215))
        self.label_version_check.setStyleSheet(u"QToolTip { color: white; }")

        self.gridLayout.addWidget(self.label_version_check, 5, 3, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        self.listWidget = QListWidget(status_page)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.listWidget.setSortingEnabled(False)

        self.verticalLayout.addWidget(self.listWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_open_dir = QPushButton(status_page)
        self.pushButton_open_dir.setObjectName(u"pushButton_open_dir")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_open_dir.sizePolicy().hasHeightForWidth())
        self.pushButton_open_dir.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.pushButton_open_dir)

        self.pushButton_2 = QPushButton(status_page)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_settings = QPushButton(status_page)
        self.pushButton_settings.setObjectName(u"pushButton_settings")
        sizePolicy.setHeightForWidth(self.pushButton_settings.sizePolicy().hasHeightForWidth())
        self.pushButton_settings.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.pushButton_settings)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(status_page)

        QMetaObject.connectSlotsByName(status_page)
    # setupUi

    def retranslateUi(self, status_page):
        status_page.setWindowTitle(QCoreApplication.translate("status_page", u"OneDriveGUI - Process Status", None))
        self.toolButton_start.setText(QCoreApplication.translate("status_page", u"Start", None))
        self.label_onedrive_status.setText(QCoreApplication.translate("status_page", u"Onedrive is sync not running", None))
        self.label_status.setText("")
        self.toolButton_stop.setText(QCoreApplication.translate("status_page", u"Stop", None))
        self.label_account_type.setText("")
        self.label_free_space.setText("")
        self.label_version_check.setText("")
        self.pushButton_open_dir.setText(QCoreApplication.translate("status_page", u"Open Sync Directory", None))
        self.pushButton_2.setText(QCoreApplication.translate("status_page", u"Sync", None))
        self.pushButton_settings.setText(QCoreApplication.translate("status_page", u"Settings", None))
    # retranslateUi

