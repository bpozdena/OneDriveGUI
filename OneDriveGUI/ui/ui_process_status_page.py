# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'process_status_page.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

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
        self.frame.setMinimumSize(QSize(0, 100))
        self.frame.setStyleSheet(u"background-color: rgb(0, 120, 212);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 2, 2, 1, 1)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 3)


        self.verticalLayout.addWidget(self.frame)

        self.listWidget = QListWidget(status_page)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.listWidget.setSortingEnabled(False)

        self.verticalLayout.addWidget(self.listWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(status_page)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.pushButton)

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
        status_page.setWindowTitle(QCoreApplication.translate("status_page", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("status_page", u"...", None))
        self.label_3.setText(QCoreApplication.translate("status_page", u"...", None))
        self.label_6.setText(QCoreApplication.translate("status_page", u"Onedrive is ...", None))
        self.pushButton.setText(QCoreApplication.translate("status_page", u"Open Folder", None))
        self.pushButton_2.setText(QCoreApplication.translate("status_page", u"Sync", None))
        self.pushButton_settings.setText(QCoreApplication.translate("status_page", u"Settings", None))
    # retranslateUi

