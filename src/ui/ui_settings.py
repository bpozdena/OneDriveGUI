# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_settings_window(object):
    def setupUi(self, settings_window):
        if not settings_window.objectName():
            settings_window.setObjectName(u"settings_window")
        settings_window.resize(272, 765)
        self.verticalLayout_2 = QVBoxLayout(settings_window)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 6, -1, -1)
        self.label_profiles = QLabel(settings_window)
        self.label_profiles.setObjectName(u"label_profiles")

        self.verticalLayout.addWidget(self.label_profiles)

        self.listWidget_profiles = QListWidget(settings_window)
        self.listWidget_profiles.setObjectName(u"listWidget_profiles")
        self.listWidget_profiles.setMinimumSize(QSize(200, 0))
        self.listWidget_profiles.setMaximumSize(QSize(250, 16777215))

        self.verticalLayout.addWidget(self.listWidget_profiles)

        self.pushButton_remove = QPushButton(settings_window)
        self.pushButton_remove.setObjectName(u"pushButton_remove")

        self.verticalLayout.addWidget(self.pushButton_remove)

        self.pushButton_create_import = QPushButton(settings_window)
        self.pushButton_create_import.setObjectName(u"pushButton_create_import")

        self.verticalLayout.addWidget(self.pushButton_create_import)

        self.pushButton_open_create = QPushButton(settings_window)
        self.pushButton_open_create.setObjectName(u"pushButton_open_create")

        self.verticalLayout.addWidget(self.pushButton_open_create)

        self.pushButton_open_import = QPushButton(settings_window)
        self.pushButton_open_import.setObjectName(u"pushButton_open_import")

        self.verticalLayout.addWidget(self.pushButton_open_import)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(settings_window)

        QMetaObject.connectSlotsByName(settings_window)
    # setupUi

    def retranslateUi(self, settings_window):
        settings_window.setWindowTitle(QCoreApplication.translate("settings_window", u"OneDriveGUI - Settings", None))
        self.label_profiles.setText(QCoreApplication.translate("settings_window", u"Profiles:", None))
        self.pushButton_remove.setText(QCoreApplication.translate("settings_window", u"Remove profile", None))
        self.pushButton_create_import.setText(QCoreApplication.translate("settings_window", u"Create/Import profile", None))
        self.pushButton_open_create.setText(QCoreApplication.translate("settings_window", u"Create new profile", None))
        self.pushButton_open_import.setText(QCoreApplication.translate("settings_window", u"Import existing profile", None))
    # retranslateUi

