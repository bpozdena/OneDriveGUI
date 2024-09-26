# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_settings_windowfuZzTA.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_gui_settings_window(object):
    def setupUi(self, gui_settings_window):
        if not gui_settings_window.objectName():
            gui_settings_window.setObjectName(u"gui_settings_window")
        gui_settings_window.resize(640, 750)
        self.verticalLayout_2 = QVBoxLayout(gui_settings_window)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea = QScrollArea(gui_settings_window)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 620, 691))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.checkBox_start_minimized = QCheckBox(self.groupBox)
        self.checkBox_start_minimized.setObjectName(u"checkBox_start_minimized")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.checkBox_start_minimized)


        self.verticalLayout_3.addLayout(self.formLayout)


        self.verticalLayout_5.addWidget(self.groupBox)

        self.groupBox_4 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_client_bin_path = QLabel(self.groupBox_4)
        self.label_client_bin_path.setObjectName(u"label_client_bin_path")

        self.horizontalLayout_6.addWidget(self.label_client_bin_path)

        self.lineEdit_client_bin_path = QLineEdit(self.groupBox_4)
        self.lineEdit_client_bin_path.setObjectName(u"lineEdit_client_bin_path")

        self.horizontalLayout_6.addWidget(self.lineEdit_client_bin_path)

        self.pushButton_client_bin_path = QPushButton(self.groupBox_4)
        self.pushButton_client_bin_path.setObjectName(u"pushButton_client_bin_path")

        self.horizontalLayout_6.addWidget(self.pushButton_client_bin_path)


        self.verticalLayout_5.addWidget(self.groupBox_4)

        self.groupBox_3 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout = QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.checkBox_frameless_window = QCheckBox(self.groupBox_3)
        self.checkBox_frameless_window.setObjectName(u"checkBox_frameless_window")

        self.gridLayout.addWidget(self.checkBox_frameless_window, 0, 0, 1, 1)

        self.checkBox_combined_start_stop_button = QCheckBox(self.groupBox_3)
        self.checkBox_combined_start_stop_button.setObjectName(u"checkBox_combined_start_stop_button")

        self.gridLayout.addWidget(self.checkBox_combined_start_stop_button, 1, 0, 1, 1)

        self.checkBox_QWebEngine_login = QCheckBox(self.groupBox_3)
        self.checkBox_QWebEngine_login.setObjectName(u"checkBox_QWebEngine_login")

        self.gridLayout.addWidget(self.checkBox_QWebEngine_login, 2, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.groupBox_3)

        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_debug_level = QLabel(self.groupBox_2)
        self.label_debug_level.setObjectName(u"label_debug_level")

        self.horizontalLayout_3.addWidget(self.label_debug_level)

        self.comboBox_debug_level = QComboBox(self.groupBox_2)
        self.comboBox_debug_level.addItem("")
        self.comboBox_debug_level.addItem("")
        self.comboBox_debug_level.addItem("")
        self.comboBox_debug_level.addItem("")
        self.comboBox_debug_level.addItem("")
        self.comboBox_debug_level.setObjectName(u"comboBox_debug_level")

        self.horizontalLayout_3.addWidget(self.comboBox_debug_level)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.checkBox_show_debug = QCheckBox(self.groupBox_2)
        self.checkBox_show_debug.setObjectName(u"checkBox_show_debug")

        self.verticalLayout_4.addWidget(self.checkBox_show_debug)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.checkBox_save_debug = QCheckBox(self.groupBox_2)
        self.checkBox_save_debug.setObjectName(u"checkBox_save_debug")

        self.horizontalLayout_4.addWidget(self.checkBox_save_debug)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_log_file = QLabel(self.groupBox_2)
        self.label_log_file.setObjectName(u"label_log_file")

        self.horizontalLayout_5.addWidget(self.label_log_file)

        self.lineEdit_log_file = QLineEdit(self.groupBox_2)
        self.lineEdit_log_file.setObjectName(u"lineEdit_log_file")

        self.horizontalLayout_5.addWidget(self.lineEdit_log_file)

        self.pushButton_log_file = QPushButton(self.groupBox_2)
        self.pushButton_log_file.setObjectName(u"pushButton_log_file")

        self.horizontalLayout_5.addWidget(self.pushButton_log_file)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_log_rotation_interval = QLabel(self.groupBox_2)
        self.label_log_rotation_interval.setObjectName(u"label_log_rotation_interval")

        self.horizontalLayout.addWidget(self.label_log_rotation_interval)

        self.spinBox_log_rotation_interval = QSpinBox(self.groupBox_2)
        self.spinBox_log_rotation_interval.setObjectName(u"spinBox_log_rotation_interval")

        self.horizontalLayout.addWidget(self.spinBox_log_rotation_interval)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_log_backup_count = QLabel(self.groupBox_2)
        self.label_log_backup_count.setObjectName(u"label_log_backup_count")

        self.horizontalLayout_2.addWidget(self.label_log_backup_count)

        self.spinBox_log_backup_count = QSpinBox(self.groupBox_2)
        self.spinBox_log_backup_count.setObjectName(u"spinBox_log_backup_count")

        self.horizontalLayout_2.addWidget(self.spinBox_log_backup_count)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.verticalLayout_5.addWidget(self.groupBox_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

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
        self.groupBox_4.setTitle(QCoreApplication.translate("gui_settings_window", u"OneDrive client options", None))
        self.label_client_bin_path.setText(QCoreApplication.translate("gui_settings_window", u"Path to OneDrive client binary", None))
        self.pushButton_client_bin_path.setText(QCoreApplication.translate("gui_settings_window", u"Browse", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("gui_settings_window", u"Appearance (experimental)", None))
        self.checkBox_frameless_window.setText(QCoreApplication.translate("gui_settings_window", u"Frameless Window for X11", None))
        self.checkBox_combined_start_stop_button.setText(QCoreApplication.translate("gui_settings_window", u"Combined Start/Stop button", None))
        self.checkBox_QWebEngine_login.setText(QCoreApplication.translate("gui_settings_window", u"Use QWebEngine for login", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("gui_settings_window", u"Logging", None))
        self.label_debug_level.setText(QCoreApplication.translate("gui_settings_window", u"Debug level:               ", None))
        self.comboBox_debug_level.setItemText(0, QCoreApplication.translate("gui_settings_window", u"DEBUG", None))
        self.comboBox_debug_level.setItemText(1, QCoreApplication.translate("gui_settings_window", u"INFO", None))
        self.comboBox_debug_level.setItemText(2, QCoreApplication.translate("gui_settings_window", u"WARNING", None))
        self.comboBox_debug_level.setItemText(3, QCoreApplication.translate("gui_settings_window", u"ERROR", None))
        self.comboBox_debug_level.setItemText(4, QCoreApplication.translate("gui_settings_window", u"CRITICAL", None))

        self.checkBox_show_debug.setText(QCoreApplication.translate("gui_settings_window", u"Show debug logs in console (stdout)", None))
        self.checkBox_save_debug.setText(QCoreApplication.translate("gui_settings_window", u"Save debug logs to file", None))
        self.label_log_file.setText(QCoreApplication.translate("gui_settings_window", u"Log file: ", None))
        self.pushButton_log_file.setText(QCoreApplication.translate("gui_settings_window", u"Browse", None))
        self.label_log_rotation_interval.setText(QCoreApplication.translate("gui_settings_window", u"Log rotation (hours): ", None))
        self.label_log_backup_count.setText(QCoreApplication.translate("gui_settings_window", u"Log backup count:     ", None))
        self.pushButton_save.setText(QCoreApplication.translate("gui_settings_window", u"Save", None))
    # retranslateUi

