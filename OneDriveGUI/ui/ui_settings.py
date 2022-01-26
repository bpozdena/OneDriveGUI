# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_settings_window(object):
    def setupUi(self, settings_window):
        if not settings_window.objectName():
            settings_window.setObjectName(u"settings_window")
        settings_window.resize(601, 817)
        self.verticalLayout_2 = QVBoxLayout(settings_window)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listWidget = QListWidget(settings_window)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMinimumSize(QSize(200, 0))

        self.verticalLayout.addWidget(self.listWidget)

        self.pushButton_3 = QPushButton(settings_window)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(settings_window)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(settings_window)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(settings_window)

        QMetaObject.connectSlotsByName(settings_window)
    # setupUi

    def retranslateUi(self, settings_window):
        settings_window.setWindowTitle(QCoreApplication.translate("settings_window", u"Form", None))
        self.pushButton_3.setText(QCoreApplication.translate("settings_window", u"Remove profile", None))
        self.pushButton_2.setText(QCoreApplication.translate("settings_window", u"Create new profile", None))
        self.pushButton.setText(QCoreApplication.translate("settings_window", u"Import existing profile", None))
    # retranslateUi

