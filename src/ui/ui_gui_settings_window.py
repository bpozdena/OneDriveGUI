# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_settings_window.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QGroupBox,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_gui_settings_window(object):
    def setupUi(self, gui_settings_window):
        if not gui_settings_window.objectName():
            gui_settings_window.setObjectName(u"gui_settings_window")
        gui_settings_window.resize(640, 480)
        self.verticalLayout_2 = QVBoxLayout(gui_settings_window)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(gui_settings_window)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.checkBox_start_minimized = QCheckBox(self.groupBox)
        self.checkBox_start_minimized.setObjectName(u"checkBox_start_minimized")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.checkBox_start_minimized)

        self.checkBox_show_debug = QCheckBox(self.groupBox)
        self.checkBox_show_debug.setObjectName(u"checkBox_show_debug")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.checkBox_show_debug)

        self.checkBox_save_debug = QCheckBox(self.groupBox)
        self.checkBox_save_debug.setObjectName(u"checkBox_save_debug")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.checkBox_save_debug)


        self.verticalLayout_3.addLayout(self.formLayout)


        self.verticalLayout.addWidget(self.groupBox)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.pushButton_save = QPushButton(gui_settings_window)
        self.pushButton_save.setObjectName(u"pushButton_save")

        self.verticalLayout_2.addWidget(self.pushButton_save)


        self.retranslateUi(gui_settings_window)

        QMetaObject.connectSlotsByName(gui_settings_window)
    # setupUi

    def retranslateUi(self, gui_settings_window):
        gui_settings_window.setWindowTitle(QCoreApplication.translate("gui_settings_window", u"OneDriveGUI - Settings", None))
        self.groupBox.setTitle(QCoreApplication.translate("gui_settings_window", u"OneDriveGUI behaviour", None))
        self.checkBox_start_minimized.setText(QCoreApplication.translate("gui_settings_window", u"Start OneDriveGUI minimized", None))
        self.checkBox_show_debug.setText(QCoreApplication.translate("gui_settings_window", u"Show debug logs in console (when GUI is started from terminal)", None))
        self.checkBox_save_debug.setText(QCoreApplication.translate("gui_settings_window", u"Save debug logs to file", None))
        self.pushButton_save.setText(QCoreApplication.translate("gui_settings_window", u"Save", None))
    # retranslateUi

