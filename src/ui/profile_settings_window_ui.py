# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profile_settings_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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

class Ui_profile_settings_window(object):
    def setupUi(self, profile_settings_window):
        if not profile_settings_window.objectName():
            profile_settings_window.setObjectName(u"profile_settings_window")
        profile_settings_window.resize(322, 800)
        self.verticalLayout_2 = QVBoxLayout(profile_settings_window)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 6, -1, -1)
        self.label_profiles = QLabel(profile_settings_window)
        self.label_profiles.setObjectName(u"label_profiles")

        self.verticalLayout.addWidget(self.label_profiles)

        self.listWidget_profiles = QListWidget(profile_settings_window)
        self.listWidget_profiles.setObjectName(u"listWidget_profiles")
        self.listWidget_profiles.setMinimumSize(QSize(300, 0))
        self.listWidget_profiles.setMaximumSize(QSize(250, 16777215))

        self.verticalLayout.addWidget(self.listWidget_profiles)

        self.pushButton_remove = QPushButton(profile_settings_window)
        self.pushButton_remove.setObjectName(u"pushButton_remove")

        self.verticalLayout.addWidget(self.pushButton_remove)

        self.pushButton_create_import = QPushButton(profile_settings_window)
        self.pushButton_create_import.setObjectName(u"pushButton_create_import")

        self.verticalLayout.addWidget(self.pushButton_create_import)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(profile_settings_window)

        QMetaObject.connectSlotsByName(profile_settings_window)
    # setupUi

    def retranslateUi(self, profile_settings_window):
        profile_settings_window.setWindowTitle(QCoreApplication.translate("profile_settings_window", u"OneDriveGUI - Profiles", None))
        self.label_profiles.setText(QCoreApplication.translate("profile_settings_window", u"Profiles:", None))
#if QT_CONFIG(tooltip)
        self.pushButton_remove.setToolTip(QCoreApplication.translate("profile_settings_window", u"<html><head/><body><p>Removes selected profile from OneDriveGUI only.</p><p>The OneDrive client config files and synced files will remain untouched and can be re-imported again.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_remove.setText(QCoreApplication.translate("profile_settings_window", u"Remove profile", None))
#if QT_CONFIG(tooltip)
        self.pushButton_create_import.setToolTip(QCoreApplication.translate("profile_settings_window", u"Opens wizard which allows creation of new profiles or import of existing ones.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_create_import.setText(QCoreApplication.translate("profile_settings_window", u"Add profile", None))
    # retranslateUi

