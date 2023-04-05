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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_status_page(object):
    def setupUi(self, status_page):
        if not status_page.objectName():
            status_page.setObjectName(u"status_page")
        status_page.resize(441, 763)
        status_page.setStyleSheet(u"border: 0px;")
        self.verticalLayout = QVBoxLayout(status_page)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(status_page)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 100))
        self.frame.setStyleSheet(u"background-color: rgb(0, 120, 212);\n"
"border: 0px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(6, 6, 6, -1)
        self.pushButton_quit = QPushButton(self.frame)
        self.pushButton_quit.setObjectName(u"pushButton_quit")
        self.pushButton_quit.setMaximumSize(QSize(40, 16777215))
        self.pushButton_quit.setStyleSheet(u"QToolTip { color: white; }\n"
"QPushButton:pressed {background-color: rgba(0, 0, 0, 0.1)}")
        self.pushButton_quit.setIconSize(QSize(20, 20))
        self.pushButton_quit.setFlat(True)

        self.horizontalLayout_3.addWidget(self.pushButton_quit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pushButton_close = QPushButton(self.frame)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setMaximumSize(QSize(40, 16777215))
        self.pushButton_close.setStyleSheet(u"QToolTip { color: white; }\n"
"QPushButton:pressed {background-color: rgba(0, 0, 0, 0.1)}")
        self.pushButton_close.setIconSize(QSize(24, 24))
        self.pushButton_close.setFlat(True)

        self.horizontalLayout_3.addWidget(self.pushButton_close)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.label_onedrive_status = QLabel(self.frame)
        self.label_onedrive_status.setObjectName(u"label_onedrive_status")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_onedrive_status.setFont(font)
        self.label_onedrive_status.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_onedrive_status.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_onedrive_status)

        self.label_account_type = QLabel(self.frame)
        self.label_account_type.setObjectName(u"label_account_type")
        self.label_account_type.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_account_type.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_account_type)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, -1, 0, 6)
        self.pushButton_start_stop = QPushButton(self.frame)
        self.pushButton_start_stop.setObjectName(u"pushButton_start_stop")
        self.pushButton_start_stop.setMaximumSize(QSize(30, 16777215))
        self.pushButton_start_stop.setStyleSheet(u"QToolTip { color: white; }\n"
"QPushButton:pressed {background-color: rgba(0, 0, 0, 0.1)}")
        self.pushButton_start_stop.setIconSize(QSize(22, 22))
        self.pushButton_start_stop.setFlat(True)

        self.horizontalLayout_2.addWidget(self.pushButton_start_stop)

        self.pushButton_start = QPushButton(self.frame)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setMaximumSize(QSize(30, 16777215))
        self.pushButton_start.setStyleSheet(u"QToolTip { color: white; }\n"
"QPushButton:pressed {background-color: rgba(0, 0, 0, 0.1)}")
        self.pushButton_start.setIconSize(QSize(20, 20))
        self.pushButton_start.setFlat(True)

        self.horizontalLayout_2.addWidget(self.pushButton_start)

        self.pushButton_stop = QPushButton(self.frame)
        self.pushButton_stop.setObjectName(u"pushButton_stop")
        self.pushButton_stop.setMaximumSize(QSize(30, 16777215))
        self.pushButton_stop.setStyleSheet(u"QToolTip { color: white; }\n"
"QPushButton:pressed {background-color: rgba(0, 0, 0, 0.1)}")
        self.pushButton_stop.setIconSize(QSize(20, 20))
        self.pushButton_stop.setFlat(True)

        self.horizontalLayout_2.addWidget(self.pushButton_stop)

        self.label_version_check = QLabel(self.frame)
        self.label_version_check.setObjectName(u"label_version_check")
        self.label_version_check.setMaximumSize(QSize(20, 16777215))
        self.label_version_check.setStyleSheet(u"QToolTip { color: white; }")

        self.horizontalLayout_2.addWidget(self.label_version_check)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_free_space = QLabel(self.frame)
        self.label_free_space.setObjectName(u"label_free_space")
        font1 = QFont()
        font1.setBold(True)
        self.label_free_space.setFont(font1)
        self.label_free_space.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_free_space.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_free_space)

        self.label_free_space_icon = QLabel(self.frame)
        self.label_free_space_icon.setObjectName(u"label_free_space_icon")
        self.label_free_space_icon.setMaximumSize(QSize(26, 16777215))
        self.label_free_space_icon.setStyleSheet(u"QToolTip { color: white; }")

        self.horizontalLayout_2.addWidget(self.label_free_space_icon)

        self.label_status = QLabel(self.frame)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setMinimumSize(QSize(30, 0))
        self.label_status.setMaximumSize(QSize(30, 16777215))
        self.label_status.setStyleSheet(u"QToolTip { color: white; }")

        self.horizontalLayout_2.addWidget(self.label_status)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.frame)

        self.listWidget = QListWidget(status_page)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setStyleSheet(u"QScrollBar:vertical {\n"
"    background: white;\n"
"	width: 12px;\n"
"	padding: 2px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: darkgrey;\n"
"	border-radius: 4px;\n"
"	width: 8px;\n"
"	margin: 0px 2px;\n"
"	min-height: 20px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"	width: 10px;\n"
"	border-radius: 5px;\n"
"	margin: 0px 1px;\n"
"}\n"
"\n"
"QScrollBar::down-button, QScrollBar::add-line, QScrollBar::sub-line {\n"
"	border: none;\n"
"	width: 0px;\n"
"	height: 0px;\n"
"}")
        self.listWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.listWidget.setSortingEnabled(False)

        self.verticalLayout.addWidget(self.listWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 6, -1, 6)
        self.pushButton_open_dir = QPushButton(status_page)
        self.pushButton_open_dir.setObjectName(u"pushButton_open_dir")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_open_dir.sizePolicy().hasHeightForWidth())
        self.pushButton_open_dir.setSizePolicy(sizePolicy)
        self.pushButton_open_dir.setStyleSheet(u"QPushButton:pressed { background-color: rgba(0, 0, 0, 10)}")
        self.pushButton_open_dir.setIconSize(QSize(26, 26))
        self.pushButton_open_dir.setFlat(True)

        self.horizontalLayout.addWidget(self.pushButton_open_dir)

        self.pushButton_profiles = QPushButton(status_page)
        self.pushButton_profiles.setObjectName(u"pushButton_profiles")
        sizePolicy.setHeightForWidth(self.pushButton_profiles.sizePolicy().hasHeightForWidth())
        self.pushButton_profiles.setSizePolicy(sizePolicy)
        self.pushButton_profiles.setStyleSheet(u"QPushButton:pressed { background-color: rgba(0, 0, 0, 10)}")
        self.pushButton_profiles.setIconSize(QSize(26, 26))
        self.pushButton_profiles.setFlat(True)

        self.horizontalLayout.addWidget(self.pushButton_profiles)

        self.pushButton_gui_settings = QPushButton(status_page)
        self.pushButton_gui_settings.setObjectName(u"pushButton_gui_settings")
        sizePolicy.setHeightForWidth(self.pushButton_gui_settings.sizePolicy().hasHeightForWidth())
        self.pushButton_gui_settings.setSizePolicy(sizePolicy)
        self.pushButton_gui_settings.setStyleSheet(u"QPushButton:pressed { background-color: rgba(0, 0, 0, 10)}")
        self.pushButton_gui_settings.setIconSize(QSize(26, 26))
        self.pushButton_gui_settings.setFlat(True)

        self.horizontalLayout.addWidget(self.pushButton_gui_settings)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(status_page)

        QMetaObject.connectSlotsByName(status_page)
    # setupUi

    def retranslateUi(self, status_page):
        status_page.setWindowTitle(QCoreApplication.translate("status_page", u"OneDriveGUI - Process Status", None))
#if QT_CONFIG(tooltip)
        self.pushButton_quit.setToolTip(QCoreApplication.translate("status_page", u"Quit", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_quit.setText(QCoreApplication.translate("status_page", u"Quit", None))
#if QT_CONFIG(tooltip)
        self.pushButton_close.setToolTip(QCoreApplication.translate("status_page", u"Close to tray/dock", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_close.setText(QCoreApplication.translate("status_page", u"Close", None))
        self.label_onedrive_status.setText(QCoreApplication.translate("status_page", u"OneDrive sync is not running", None))
        self.label_account_type.setText("")
        self.pushButton_start_stop.setText(QCoreApplication.translate("status_page", u"start/stop", None))
#if QT_CONFIG(tooltip)
        self.pushButton_start.setToolTip(QCoreApplication.translate("status_page", u"Start Sync", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_start.setText(QCoreApplication.translate("status_page", u"Start", None))
#if QT_CONFIG(tooltip)
        self.pushButton_stop.setToolTip(QCoreApplication.translate("status_page", u"Stop Sync", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_stop.setText(QCoreApplication.translate("status_page", u"Stop", None))
        self.label_version_check.setText("")
#if QT_CONFIG(tooltip)
        self.label_free_space.setToolTip(QCoreApplication.translate("status_page", u"Free Space", None))
#endif // QT_CONFIG(tooltip)
        self.label_free_space.setText("")
#if QT_CONFIG(tooltip)
        self.label_free_space_icon.setToolTip(QCoreApplication.translate("status_page", u"Free Space", None))
#endif // QT_CONFIG(tooltip)
        self.label_free_space_icon.setText(QCoreApplication.translate("status_page", u"TextLabel", None))
#if QT_CONFIG(tooltip)
        self.label_status.setToolTip(QCoreApplication.translate("status_page", u"Sync is stopped", None))
#endif // QT_CONFIG(tooltip)
        self.label_status.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_open_dir.setToolTip(QCoreApplication.translate("status_page", u"Open Sync Directory", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_open_dir.setText(QCoreApplication.translate("status_page", u"Open Sync Directory", None))
#if QT_CONFIG(tooltip)
        self.pushButton_profiles.setToolTip(QCoreApplication.translate("status_page", u"Profiles", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_profiles.setText(QCoreApplication.translate("status_page", u"Profiles", None))
#if QT_CONFIG(tooltip)
        self.pushButton_gui_settings.setToolTip(QCoreApplication.translate("status_page", u"OneDriveGUI Settings", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_gui_settings.setText(QCoreApplication.translate("status_page", u"GUI Settings", None))
    # retranslateUi

