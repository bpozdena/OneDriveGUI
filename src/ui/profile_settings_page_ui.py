# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profile_settings_page.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QSpinBox, QTabWidget,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_profile_settings(object):
    def setupUi(self, profile_settings):
        if not profile_settings.objectName():
            profile_settings.setObjectName(u"profile_settings")
        profile_settings.resize(820, 692)
        self.verticalLayout_2 = QVBoxLayout(profile_settings)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.label_profile_name = QLabel(profile_settings)
        self.label_profile_name.setObjectName(u"label_profile_name")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_profile_name.setFont(font)
        self.label_profile_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_profile_name)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.tabWidget = QTabWidget(profile_settings)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(800, 600))
        self.monitored_tab_2 = QWidget()
        self.monitored_tab_2.setObjectName(u"monitored_tab_2")
        self.verticalLayout_5 = QVBoxLayout(self.monitored_tab_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox_8 = QGroupBox(self.monitored_tab_2)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.gridLayout_9 = QGridLayout(self.groupBox_8)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pushButton_sync_dir_browse = QPushButton(self.groupBox_8)
        self.pushButton_sync_dir_browse.setObjectName(u"pushButton_sync_dir_browse")

        self.gridLayout_5.addWidget(self.pushButton_sync_dir_browse, 0, 2, 1, 1)

        self.label_sync_dir = QLabel(self.groupBox_8)
        self.label_sync_dir.setObjectName(u"label_sync_dir")

        self.gridLayout_5.addWidget(self.label_sync_dir, 0, 0, 1, 1)

        self.lineEdit_sync_dir = QLineEdit(self.groupBox_8)
        self.lineEdit_sync_dir.setObjectName(u"lineEdit_sync_dir")

        self.gridLayout_5.addWidget(self.lineEdit_sync_dir, 0, 1, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_5, 1, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.groupBox_8)

        self.groupBox_12 = QGroupBox(self.monitored_tab_2)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.gridLayout_3 = QGridLayout(self.groupBox_12)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.checkBox_auto_sync = QCheckBox(self.groupBox_12)
        self.checkBox_auto_sync.setObjectName(u"checkBox_auto_sync")
        font1 = QFont()
        font1.setBold(True)
        self.checkBox_auto_sync.setFont(font1)

        self.gridLayout_3.addWidget(self.checkBox_auto_sync, 0, 0, 1, 1)

        self.pushButton_logout = QPushButton(self.groupBox_12)
        self.pushButton_logout.setObjectName(u"pushButton_logout")

        self.gridLayout_3.addWidget(self.pushButton_logout, 2, 0, 1, 1)

        self.pushButton_login = QPushButton(self.groupBox_12)
        self.pushButton_login.setObjectName(u"pushButton_login")

        self.gridLayout_3.addWidget(self.pushButton_login, 1, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.groupBox_12)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.tabWidget.addTab(self.monitored_tab_2, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_8 = QVBoxLayout(self.tab_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.groupBox_10 = QGroupBox(self.tab_2)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.gridLayout_11 = QGridLayout(self.groupBox_10)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.spinBox_rate_limit = QSpinBox(self.groupBox_10)
        self.spinBox_rate_limit.setObjectName(u"spinBox_rate_limit")
        self.spinBox_rate_limit.setMinimum(131072)
        self.spinBox_rate_limit.setMaximum(125000000)
        self.spinBox_rate_limit.setSingleStep(12500)

        self.gridLayout_11.addWidget(self.spinBox_rate_limit, 0, 1, 1, 1)

        self.label_rate_limit = QLabel(self.groupBox_10)
        self.label_rate_limit.setObjectName(u"label_rate_limit")

        self.gridLayout_11.addWidget(self.label_rate_limit, 0, 0, 1, 1)

        self.horizontalSlider_rate_limit = QSlider(self.groupBox_10)
        self.horizontalSlider_rate_limit.setObjectName(u"horizontalSlider_rate_limit")
        self.horizontalSlider_rate_limit.setMinimum(125000)
        self.horizontalSlider_rate_limit.setMaximum(125000000)
        self.horizontalSlider_rate_limit.setSingleStep(12500)
        self.horizontalSlider_rate_limit.setPageStep(12500)
        self.horizontalSlider_rate_limit.setOrientation(Qt.Horizontal)

        self.gridLayout_11.addWidget(self.horizontalSlider_rate_limit, 1, 0, 1, 4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer, 0, 3, 1, 1)

        self.label_rate_limit_mbps = QLabel(self.groupBox_10)
        self.label_rate_limit_mbps.setObjectName(u"label_rate_limit_mbps")

        self.gridLayout_11.addWidget(self.label_rate_limit_mbps, 0, 2, 1, 1)


        self.verticalLayout_8.addWidget(self.groupBox_10)

        self.groupBox_4 = QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.horizontalLayout = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_monitor_interval = QLabel(self.groupBox_4)
        self.label_monitor_interval.setObjectName(u"label_monitor_interval")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_monitor_interval)

        self.spinBox_monitor_interval = QSpinBox(self.groupBox_4)
        self.spinBox_monitor_interval.setObjectName(u"spinBox_monitor_interval")
        self.spinBox_monitor_interval.setMaximum(1000000)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.spinBox_monitor_interval)

        self.label_monitor_fullscan_frequency = QLabel(self.groupBox_4)
        self.label_monitor_fullscan_frequency.setObjectName(u"label_monitor_fullscan_frequency")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_monitor_fullscan_frequency)

        self.spinBox_monitor_fullscan_frequency = QSpinBox(self.groupBox_4)
        self.spinBox_monitor_fullscan_frequency.setObjectName(u"spinBox_monitor_fullscan_frequency")
        self.spinBox_monitor_fullscan_frequency.setMaximum(1000000)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.spinBox_monitor_fullscan_frequency)

        self.label_classify_as_big_delete = QLabel(self.groupBox_4)
        self.label_classify_as_big_delete.setObjectName(u"label_classify_as_big_delete")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_classify_as_big_delete)

        self.spinBox_classify_as_big_delete = QSpinBox(self.groupBox_4)
        self.spinBox_classify_as_big_delete.setObjectName(u"spinBox_classify_as_big_delete")
        self.spinBox_classify_as_big_delete.setMaximum(1000000)

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.spinBox_classify_as_big_delete)

        self.label_operation_timeout = QLabel(self.groupBox_4)
        self.label_operation_timeout.setObjectName(u"label_operation_timeout")

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.label_operation_timeout)

        self.spinBox_operation_timeout = QSpinBox(self.groupBox_4)
        self.spinBox_operation_timeout.setObjectName(u"spinBox_operation_timeout")
        self.spinBox_operation_timeout.setMaximum(1000000)

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.spinBox_operation_timeout)

        self.label_drive_id = QLabel(self.groupBox_4)
        self.label_drive_id.setObjectName(u"label_drive_id")

        self.formLayout_4.setWidget(4, QFormLayout.LabelRole, self.label_drive_id)

        self.lineEdit_drive_id = QLineEdit(self.groupBox_4)
        self.lineEdit_drive_id.setObjectName(u"lineEdit_drive_id")

        self.formLayout_4.setWidget(4, QFormLayout.FieldRole, self.lineEdit_drive_id)


        self.horizontalLayout.addLayout(self.formLayout_4)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_10)

        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_sync_file_permissions = QLabel(self.groupBox_4)
        self.label_sync_file_permissions.setObjectName(u"label_sync_file_permissions")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_sync_file_permissions)

        self.spinBox_sync_file_permissions = QSpinBox(self.groupBox_4)
        self.spinBox_sync_file_permissions.setObjectName(u"spinBox_sync_file_permissions")
        self.spinBox_sync_file_permissions.setMaximum(777)

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.spinBox_sync_file_permissions)

        self.label_sync_dir_permissions = QLabel(self.groupBox_4)
        self.label_sync_dir_permissions.setObjectName(u"label_sync_dir_permissions")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_sync_dir_permissions)

        self.spinBox_sync_dir_permissions = QSpinBox(self.groupBox_4)
        self.spinBox_sync_dir_permissions.setObjectName(u"spinBox_sync_dir_permissions")
        self.spinBox_sync_dir_permissions.setMaximum(777)

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.spinBox_sync_dir_permissions)

        self.label_user_agent = QLabel(self.groupBox_4)
        self.label_user_agent.setObjectName(u"label_user_agent")

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.label_user_agent)

        self.lineEdit_user_agent = QLineEdit(self.groupBox_4)
        self.lineEdit_user_agent.setObjectName(u"lineEdit_user_agent")
        self.lineEdit_user_agent.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_user_agent.setMaxLength(32767)

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.lineEdit_user_agent)

        self.label_azure_ad_endpoint = QLabel(self.groupBox_4)
        self.label_azure_ad_endpoint.setObjectName(u"label_azure_ad_endpoint")

        self.formLayout_5.setWidget(3, QFormLayout.LabelRole, self.label_azure_ad_endpoint)

        self.lineEdit_azure_ad_endpoint = QLineEdit(self.groupBox_4)
        self.lineEdit_azure_ad_endpoint.setObjectName(u"lineEdit_azure_ad_endpoint")
        self.lineEdit_azure_ad_endpoint.setMaximumSize(QSize(16777215, 16777215))

        self.formLayout_5.setWidget(3, QFormLayout.FieldRole, self.lineEdit_azure_ad_endpoint)

        self.label_azure_tenant_id = QLabel(self.groupBox_4)
        self.label_azure_tenant_id.setObjectName(u"label_azure_tenant_id")

        self.formLayout_5.setWidget(4, QFormLayout.LabelRole, self.label_azure_tenant_id)

        self.lineEdit_azure_tenant_id = QLineEdit(self.groupBox_4)
        self.lineEdit_azure_tenant_id.setObjectName(u"lineEdit_azure_tenant_id")
        self.lineEdit_azure_tenant_id.setMaximumSize(QSize(16777215, 16777215))

        self.formLayout_5.setWidget(4, QFormLayout.FieldRole, self.lineEdit_azure_tenant_id)


        self.horizontalLayout.addLayout(self.formLayout_5)


        self.verticalLayout_8.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.tab_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_4 = QGridLayout(self.groupBox_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.checkBox_force_http_11 = QCheckBox(self.groupBox_5)
        self.checkBox_force_http_11.setObjectName(u"checkBox_force_http_11")

        self.gridLayout_4.addWidget(self.checkBox_force_http_11, 4, 1, 1, 1)

        self.checkBox_upload_only = QCheckBox(self.groupBox_5)
        self.checkBox_upload_only.setObjectName(u"checkBox_upload_only")

        self.gridLayout_4.addWidget(self.checkBox_upload_only, 2, 1, 1, 1)

        self.checkBox_no_remote_delete = QCheckBox(self.groupBox_5)
        self.checkBox_no_remote_delete.setObjectName(u"checkBox_no_remote_delete")

        self.gridLayout_4.addWidget(self.checkBox_no_remote_delete, 3, 1, 1, 1)

        self.checkBox_check_nomount = QCheckBox(self.groupBox_5)
        self.checkBox_check_nomount.setObjectName(u"checkBox_check_nomount")

        self.gridLayout_4.addWidget(self.checkBox_check_nomount, 5, 1, 1, 1)

        self.checkBox_download_only = QCheckBox(self.groupBox_5)
        self.checkBox_download_only.setObjectName(u"checkBox_download_only")

        self.gridLayout_4.addWidget(self.checkBox_download_only, 1, 1, 1, 1)

        self.checkBox_local_first = QCheckBox(self.groupBox_5)
        self.checkBox_local_first.setObjectName(u"checkBox_local_first")

        self.gridLayout_4.addWidget(self.checkBox_local_first, 0, 1, 1, 1)

        self.checkBox_dry_run = QCheckBox(self.groupBox_5)
        self.checkBox_dry_run.setObjectName(u"checkBox_dry_run")

        self.gridLayout_4.addWidget(self.checkBox_dry_run, 0, 2, 1, 1)

        self.checkBox_resync = QCheckBox(self.groupBox_5)
        self.checkBox_resync.setObjectName(u"checkBox_resync")

        self.gridLayout_4.addWidget(self.checkBox_resync, 1, 2, 1, 1)

        self.checkBox_bypass_data_preservation = QCheckBox(self.groupBox_5)
        self.checkBox_bypass_data_preservation.setObjectName(u"checkBox_bypass_data_preservation")

        self.gridLayout_4.addWidget(self.checkBox_bypass_data_preservation, 2, 2, 1, 1)

        self.checkBox_remove_source_files = QCheckBox(self.groupBox_5)
        self.checkBox_remove_source_files.setObjectName(u"checkBox_remove_source_files")

        self.gridLayout_4.addWidget(self.checkBox_remove_source_files, 3, 2, 1, 1)

        self.checkBox_disable_upload_validation = QCheckBox(self.groupBox_5)
        self.checkBox_disable_upload_validation.setObjectName(u"checkBox_disable_upload_validation")

        self.gridLayout_4.addWidget(self.checkBox_disable_upload_validation, 4, 2, 1, 1)


        self.verticalLayout_8.addWidget(self.groupBox_5)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_4)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_7 = QVBoxLayout(self.tab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.lineEdit_skip_file = QLineEdit(self.groupBox)
        self.lineEdit_skip_file.setObjectName(u"lineEdit_skip_file")

        self.gridLayout_6.addWidget(self.lineEdit_skip_file, 1, 0, 1, 1)

        self.pushButton_add_skip_file = QPushButton(self.groupBox)
        self.pushButton_add_skip_file.setObjectName(u"pushButton_add_skip_file")

        self.gridLayout_6.addWidget(self.pushButton_add_skip_file, 1, 1, 1, 1)

        self.pushButton_rm_skip_file = QPushButton(self.groupBox)
        self.pushButton_rm_skip_file.setObjectName(u"pushButton_rm_skip_file")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_rm_skip_file.sizePolicy().hasHeightForWidth())
        self.pushButton_rm_skip_file.setSizePolicy(sizePolicy)

        self.gridLayout_6.addWidget(self.pushButton_rm_skip_file, 0, 1, 1, 1)

        self.listWidget_skip_file = QListWidget(self.groupBox)
        self.listWidget_skip_file.setObjectName(u"listWidget_skip_file")

        self.gridLayout_6.addWidget(self.listWidget_skip_file, 0, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_6)


        self.verticalLayout_7.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.checkBox_skip_dir_strict_match = QCheckBox(self.groupBox_2)
        self.checkBox_skip_dir_strict_match.setObjectName(u"checkBox_skip_dir_strict_match")

        self.verticalLayout_4.addWidget(self.checkBox_skip_dir_strict_match)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.pushButton_rm_skip_dir = QPushButton(self.groupBox_2)
        self.pushButton_rm_skip_dir.setObjectName(u"pushButton_rm_skip_dir")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_rm_skip_dir.sizePolicy().hasHeightForWidth())
        self.pushButton_rm_skip_dir.setSizePolicy(sizePolicy1)

        self.gridLayout_7.addWidget(self.pushButton_rm_skip_dir, 0, 1, 1, 1)

        self.listWidget_skip_dir = QListWidget(self.groupBox_2)
        self.listWidget_skip_dir.setObjectName(u"listWidget_skip_dir")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.listWidget_skip_dir.sizePolicy().hasHeightForWidth())
        self.listWidget_skip_dir.setSizePolicy(sizePolicy2)

        self.gridLayout_7.addWidget(self.listWidget_skip_dir, 0, 0, 1, 1)

        self.lineEdit_skip_dir = QLineEdit(self.groupBox_2)
        self.lineEdit_skip_dir.setObjectName(u"lineEdit_skip_dir")

        self.gridLayout_7.addWidget(self.lineEdit_skip_dir, 1, 0, 1, 1)

        self.pushButton_add_skip_dir = QPushButton(self.groupBox_2)
        self.pushButton_add_skip_dir.setObjectName(u"pushButton_add_skip_dir")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_add_skip_dir.sizePolicy().hasHeightForWidth())
        self.pushButton_add_skip_dir.setSizePolicy(sizePolicy3)

        self.gridLayout_7.addWidget(self.pushButton_add_skip_dir, 1, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_7)


        self.verticalLayout_7.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox_skip_symlinks = QCheckBox(self.groupBox_3)
        self.checkBox_skip_symlinks.setObjectName(u"checkBox_skip_symlinks")

        self.gridLayout_2.addWidget(self.checkBox_skip_symlinks, 0, 1, 1, 1)

        self.checkBox_check_nosync = QCheckBox(self.groupBox_3)
        self.checkBox_check_nosync.setObjectName(u"checkBox_check_nosync")

        self.gridLayout_2.addWidget(self.checkBox_check_nosync, 0, 0, 1, 1)

        self.checkBox_skip_dotfiles = QCheckBox(self.groupBox_3)
        self.checkBox_skip_dotfiles.setObjectName(u"checkBox_skip_dotfiles")

        self.gridLayout_2.addWidget(self.checkBox_skip_dotfiles, 1, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.groupBox_3)

        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_10 = QVBoxLayout(self.tab_3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.groupBox_11 = QGroupBox(self.tab_3)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_11)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_sync_list = QLabel(self.groupBox_11)
        self.label_sync_list.setObjectName(u"label_sync_list")

        self.verticalLayout_11.addWidget(self.label_sync_list)

        self.checkBox_sync_root_files = QCheckBox(self.groupBox_11)
        self.checkBox_sync_root_files.setObjectName(u"checkBox_sync_root_files")

        self.verticalLayout_11.addWidget(self.checkBox_sync_root_files)

        self.textEdit_sync_list = QTextEdit(self.groupBox_11)
        self.textEdit_sync_list.setObjectName(u"textEdit_sync_list")

        self.verticalLayout_11.addWidget(self.textEdit_sync_list)


        self.verticalLayout_10.addWidget(self.groupBox_11)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout = QVBoxLayout(self.tab_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_sync_business_shared_folders = QGroupBox(self.tab_4)
        self.groupBox_sync_business_shared_folders.setObjectName(u"groupBox_sync_business_shared_folders")
        self.groupBox_sync_business_shared_folders.setCheckable(True)
        self.groupBox_sync_business_shared_folders.setChecked(True)
        self.gridLayout_12 = QGridLayout(self.groupBox_sync_business_shared_folders)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_business_available = QLabel(self.groupBox_sync_business_shared_folders)
        self.label_business_available.setObjectName(u"label_business_available")

        self.gridLayout_12.addWidget(self.label_business_available, 3, 0, 1, 1)

        self.checkBox_sync_business_shared_folders = QCheckBox(self.groupBox_sync_business_shared_folders)
        self.checkBox_sync_business_shared_folders.setObjectName(u"checkBox_sync_business_shared_folders")

        self.gridLayout_12.addWidget(self.checkBox_sync_business_shared_folders, 0, 0, 1, 1)

        self.listWidget_available_business_folders = QListWidget(self.groupBox_sync_business_shared_folders)
        self.listWidget_available_business_folders.setObjectName(u"listWidget_available_business_folders")

        self.gridLayout_12.addWidget(self.listWidget_available_business_folders, 6, 0, 1, 1)

        self.label_business_selected = QLabel(self.groupBox_sync_business_shared_folders)
        self.label_business_selected.setObjectName(u"label_business_selected")

        self.gridLayout_12.addWidget(self.label_business_selected, 3, 2, 1, 1)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_5)

        self.pushButton_add_business_folder = QPushButton(self.groupBox_sync_business_shared_folders)
        self.pushButton_add_business_folder.setObjectName(u"pushButton_add_business_folder")
        self.pushButton_add_business_folder.setMaximumSize(QSize(50, 16777215))

        self.verticalLayout_14.addWidget(self.pushButton_add_business_folder)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_6)


        self.gridLayout_12.addLayout(self.verticalLayout_14, 6, 1, 1, 1)

        self.listWidget_selected_business_folders = QListWidget(self.groupBox_sync_business_shared_folders)
        self.listWidget_selected_business_folders.setObjectName(u"listWidget_selected_business_folders")

        self.gridLayout_12.addWidget(self.listWidget_selected_business_folders, 6, 2, 1, 1)

        self.pushButton_get_business_folders = QPushButton(self.groupBox_sync_business_shared_folders)
        self.pushButton_get_business_folders.setObjectName(u"pushButton_get_business_folders")

        self.gridLayout_12.addWidget(self.pushButton_get_business_folders, 4, 0, 1, 1)

        self.pushButton_remove_business_folders = QPushButton(self.groupBox_sync_business_shared_folders)
        self.pushButton_remove_business_folders.setObjectName(u"pushButton_remove_business_folders")

        self.gridLayout_12.addWidget(self.pushButton_remove_business_folders, 4, 2, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_sync_business_shared_folders)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout = QGridLayout(self.tab_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_9 = QGroupBox(self.tab_5)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.formLayout_2 = QFormLayout(self.groupBox_9)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_webhook_public_url = QLabel(self.groupBox_9)
        self.label_webhook_public_url.setObjectName(u"label_webhook_public_url")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_webhook_public_url)

        self.lineEdit_webhook_public_url = QLineEdit(self.groupBox_9)
        self.lineEdit_webhook_public_url.setObjectName(u"lineEdit_webhook_public_url")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lineEdit_webhook_public_url)

        self.label_webhook_listening_host = QLabel(self.groupBox_9)
        self.label_webhook_listening_host.setObjectName(u"label_webhook_listening_host")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_webhook_listening_host)

        self.lineEdit_webhook_listening_host = QLineEdit(self.groupBox_9)
        self.lineEdit_webhook_listening_host.setObjectName(u"lineEdit_webhook_listening_host")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.lineEdit_webhook_listening_host)

        self.label_webhook_listening_port = QLabel(self.groupBox_9)
        self.label_webhook_listening_port.setObjectName(u"label_webhook_listening_port")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_webhook_listening_port)

        self.spinBox_webhook_listening_port = QSpinBox(self.groupBox_9)
        self.spinBox_webhook_listening_port.setObjectName(u"spinBox_webhook_listening_port")
        self.spinBox_webhook_listening_port.setMinimum(1)
        self.spinBox_webhook_listening_port.setMaximum(65353)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.spinBox_webhook_listening_port)

        self.label_webhook_expiration_interval = QLabel(self.groupBox_9)
        self.label_webhook_expiration_interval.setObjectName(u"label_webhook_expiration_interval")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_webhook_expiration_interval)

        self.spinBox_webhook_expiration_interval = QSpinBox(self.groupBox_9)
        self.spinBox_webhook_expiration_interval.setObjectName(u"spinBox_webhook_expiration_interval")
        self.spinBox_webhook_expiration_interval.setMaximum(1000000)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.spinBox_webhook_expiration_interval)

        self.label_webhook_renewal_interval = QLabel(self.groupBox_9)
        self.label_webhook_renewal_interval.setObjectName(u"label_webhook_renewal_interval")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_webhook_renewal_interval)

        self.spinBox_webhook_renewal_interval = QSpinBox(self.groupBox_9)
        self.spinBox_webhook_renewal_interval.setObjectName(u"spinBox_webhook_renewal_interval")
        self.spinBox_webhook_renewal_interval.setMaximum(1000000)

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.spinBox_webhook_renewal_interval)

        self.checkBox_webhook_enabled = QCheckBox(self.groupBox_9)
        self.checkBox_webhook_enabled.setObjectName(u"checkBox_webhook_enabled")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.checkBox_webhook_enabled)


        self.gridLayout.addWidget(self.groupBox_9, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_logging = QWidget()
        self.tab_logging.setObjectName(u"tab_logging")
        self.verticalLayout_6 = QVBoxLayout(self.tab_logging)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.groupBox_7 = QGroupBox(self.tab_logging)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.checkBox_enable_logging = QCheckBox(self.groupBox_7)
        self.checkBox_enable_logging.setObjectName(u"checkBox_enable_logging")

        self.gridLayout_8.addWidget(self.checkBox_enable_logging, 0, 0, 1, 1)

        self.label_log_dir = QLabel(self.groupBox_7)
        self.label_log_dir.setObjectName(u"label_log_dir")

        self.gridLayout_8.addWidget(self.label_log_dir, 1, 0, 1, 1)

        self.checkBox_debug_https = QCheckBox(self.groupBox_7)
        self.checkBox_debug_https.setObjectName(u"checkBox_debug_https")

        self.gridLayout_8.addWidget(self.checkBox_debug_https, 4, 0, 1, 1)

        self.lineEdit_log_dir = QLineEdit(self.groupBox_7)
        self.lineEdit_log_dir.setObjectName(u"lineEdit_log_dir")

        self.gridLayout_8.addWidget(self.lineEdit_log_dir, 1, 1, 1, 1)

        self.pushButton_log_dir_browse = QPushButton(self.groupBox_7)
        self.pushButton_log_dir_browse.setObjectName(u"pushButton_log_dir_browse")

        self.gridLayout_8.addWidget(self.pushButton_log_dir_browse, 1, 2, 1, 1)

        self.label_monitor_log_frequency = QLabel(self.groupBox_7)
        self.label_monitor_log_frequency.setObjectName(u"label_monitor_log_frequency")

        self.gridLayout_8.addWidget(self.label_monitor_log_frequency, 3, 0, 1, 1)

        self.spinBox_monitor_log_frequency = QSpinBox(self.groupBox_7)
        self.spinBox_monitor_log_frequency.setObjectName(u"spinBox_monitor_log_frequency")

        self.gridLayout_8.addWidget(self.spinBox_monitor_log_frequency, 3, 1, 1, 1)


        self.verticalLayout_9.addLayout(self.gridLayout_8)


        self.verticalLayout_6.addWidget(self.groupBox_7)

        self.groupBox_6 = QGroupBox(self.tab_logging)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.formLayout_3 = QFormLayout(self.groupBox_6)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_min_notify_changes = QLabel(self.groupBox_6)
        self.label_min_notify_changes.setObjectName(u"label_min_notify_changes")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_min_notify_changes)

        self.spinBox_min_notify_changes = QSpinBox(self.groupBox_6)
        self.spinBox_min_notify_changes.setObjectName(u"spinBox_min_notify_changes")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.spinBox_min_notify_changes)

        self.checkBox_disable_notifications = QCheckBox(self.groupBox_6)
        self.checkBox_disable_notifications.setObjectName(u"checkBox_disable_notifications")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.checkBox_disable_notifications)


        self.verticalLayout_6.addWidget(self.groupBox_6)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.tabWidget.addTab(self.tab_logging, "")

        self.verticalLayout_13.addWidget(self.tabWidget)


        self.verticalLayout_2.addLayout(self.verticalLayout_13)

        self.pushButton_discard = QPushButton(profile_settings)
        self.pushButton_discard.setObjectName(u"pushButton_discard")

        self.verticalLayout_2.addWidget(self.pushButton_discard)

        self.pushButton_save = QPushButton(profile_settings)
        self.pushButton_save.setObjectName(u"pushButton_save")

        self.verticalLayout_2.addWidget(self.pushButton_save)


        self.retranslateUi(profile_settings)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(profile_settings)
    # setupUi

    def retranslateUi(self, profile_settings):
        profile_settings.setWindowTitle(QCoreApplication.translate("profile_settings", u"OneDriveGUI - Profile Settings", None))
        self.label_profile_name.setText(QCoreApplication.translate("profile_settings", u"Profile name", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.groupBox_8.setTitle(QCoreApplication.translate("profile_settings", u"Monitored directory", None))
        self.pushButton_sync_dir_browse.setText(QCoreApplication.translate("profile_settings", u"Browse", None))
#if QT_CONFIG(tooltip)
        self.label_sync_dir.setToolTip(QCoreApplication.translate("profile_settings", u"Specify local sync directory location for this profile.", None))
#endif // QT_CONFIG(tooltip)
        self.label_sync_dir.setText(QCoreApplication.translate("profile_settings", u"Sync Directory:", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("profile_settings", u"Account actions", None))
#if QT_CONFIG(tooltip)
        self.checkBox_auto_sync.setToolTip(QCoreApplication.translate("profile_settings", u"Automatically start sync for this profile when OneDriveGUI starts.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_auto_sync.setText(QCoreApplication.translate("profile_settings", u"Auto-sync on GUI startup", None))
#if QT_CONFIG(tooltip)
        self.pushButton_logout.setToolTip(QCoreApplication.translate("profile_settings", u"Logout user from this profile and force login during next sync attempt. ", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_logout.setText(QCoreApplication.translate("profile_settings", u"Logout", None))
        self.pushButton_login.setText(QCoreApplication.translate("profile_settings", u"Login", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.monitored_tab_2), QCoreApplication.translate("profile_settings", u"Monitored Files", None))
#if QT_CONFIG(tooltip)
        self.groupBox_10.setToolTip(QCoreApplication.translate("profile_settings", u"<html><head/><body><p>To minimise the Internet bandwidth for upload and download operations, you can configure the bandwidth limit option. </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_10.setTitle(QCoreApplication.translate("profile_settings", u"Account Bandwidth Limit", None))
        self.label_rate_limit.setText(QCoreApplication.translate("profile_settings", u"Rate Limit [B/s]", None))
        self.label_rate_limit_mbps.setText(QCoreApplication.translate("profile_settings", u"(Mb/s)", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("profile_settings", u"Advanced Properties", None))
#if QT_CONFIG(tooltip)
        self.label_monitor_interval.setToolTip(QCoreApplication.translate("profile_settings", u"<html><head/><body><p>The monitor interval is defined as the wait time 'between' sync's when running in monitor mode. </p><p>When this interval expires, the client will check OneDrive for changes online, performing data </p><p>integrity checks and scanning the local <span style=\" font-weight:700;\">Sync Directory</span> for new content.</p><p><br/></p><p>By default without configuration, monitor interval is set to <span style=\" font-weight:700;\">300</span> seconds. Setting this value </p><p>to <span style=\" font-weight:700;\">600</span> will run the sync process every <span style=\" font-weight:700;\">10 minutes</span>.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_monitor_interval.setText(QCoreApplication.translate("profile_settings", u"Monitor interval", None))
#if QT_CONFIG(tooltip)
        self.label_monitor_fullscan_frequency.setToolTip(QCoreApplication.translate("profile_settings", u"This configuration option controls the number of 'monitor_interval' iterations between when a \n"
"full scan of your data is performed to ensure data integrity and consistency.\n"
"\n"
"By default without configuration, 'monitor_fullscan_frequency' is set to 12. In this default state,\n"
"this means that a full scan is performed every 'monitor_interval' x 'monitor_fullscan_frequency' = 3600 seconds. \n"
"This is only applicable when running in --monitor mode.\n"
"\n"
"Setting this value to 24 means that the full scan of OneDrive and checking the integrity of the data stored \n"
"locally will occur every 2 hours (assuming 'monitor_interval' is set to 300 seconds).", None))
#endif // QT_CONFIG(tooltip)
        self.label_monitor_fullscan_frequency.setText(QCoreApplication.translate("profile_settings", u"Monitor full-scan frequency", None))
#if QT_CONFIG(tooltip)
        self.label_classify_as_big_delete.setToolTip(QCoreApplication.translate("profile_settings", u"Number of children in a path that is locally removed which will be classified as a 'big data delete'", None))
#endif // QT_CONFIG(tooltip)
        self.label_classify_as_big_delete.setText(QCoreApplication.translate("profile_settings", u"Clasify as big delete", None))
#if QT_CONFIG(tooltip)
        self.label_operation_timeout.setToolTip(QCoreApplication.translate("profile_settings", u"Operation Timeout is the maximum amount of time (seconds) a file operation is allowed to take. This includes DNS resolution, connecting, data transfer, etc.", None))
#endif // QT_CONFIG(tooltip)
        self.label_operation_timeout.setText(QCoreApplication.translate("profile_settings", u"Operation timeout", None))
        self.label_drive_id.setText(QCoreApplication.translate("profile_settings", u"SharePoint Library Drive ID", None))
#if QT_CONFIG(tooltip)
        self.label_sync_file_permissions.setToolTip(QCoreApplication.translate("profile_settings", u"<html><head/><body><p>Utilise the <a href=\"https://chmod-calculator.com/\"><span style=\" text-decoration: underline; color:#5e81ac;\">Unix Permissions Calculator</span></a> to assist in determining the required permissions.</p><p><br/></p><p>Important: Special permission bits (setuid, setgid, sticky bit) are not supported. </p><p>Valid permission values are from <span style=\" font-weight:700;\">000</span> to <span style=\" font-weight:700;\">777</span> only.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_sync_file_permissions.setText(QCoreApplication.translate("profile_settings", u"Sync file permissions", None))
#if QT_CONFIG(tooltip)
        self.label_sync_dir_permissions.setToolTip(QCoreApplication.translate("profile_settings", u"<html><head/><body><p>Utilise the <a href=\"https://chmod-calculator.com/\"><span style=\" text-decoration: underline; color:#5e81ac;\">Unix Permissions Calculator</span></a> to assist in determining the required permissions.</p><p><br/></p><p>Important: Special permission bits (setuid, setgid, sticky bit) are not supported. </p><p>Valid permission values are from <span style=\" font-weight:700;\">000</span> to <span style=\" font-weight:700;\">777</span> only.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_sync_dir_permissions.setText(QCoreApplication.translate("profile_settings", u"Sync dir permissions", None))
#if QT_CONFIG(tooltip)
        self.label_user_agent.setToolTip(QCoreApplication.translate("profile_settings", u"Specify a User Agent string to the http client", None))
#endif // QT_CONFIG(tooltip)
        self.label_user_agent.setText(QCoreApplication.translate("profile_settings", u"User-agent", None))
#if QT_CONFIG(tooltip)
        self.label_azure_ad_endpoint.setToolTip(QCoreApplication.translate("profile_settings", u"<html><head/><body><p>Refer to the documentation for <a href=\"https://github.com/abraunegg/onedrive/blob/master/docs/USAGE.md#configuring-the-client-for-single-tenant-application-use\"><span style=\" text-decoration: underline; color:#5e81ac;\">single tenant application use</span></a>.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_azure_ad_endpoint.setText(QCoreApplication.translate("profile_settings", u"Azure AD endpoint", None))
#if QT_CONFIG(tooltip)
        self.label_azure_tenant_id.setToolTip(QCoreApplication.translate("profile_settings", u"<html><head/><body><p>Refer to the documentation for <a href=\"https://github.com/abraunegg/onedrive/blob/master/docs/USAGE.md#configuring-the-client-for-single-tenant-application-use\"><span style=\" text-decoration: underline; color:#5e81ac;\">single tenant application use</span></a>.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_azure_tenant_id.setText(QCoreApplication.translate("profile_settings", u"Azure tenant ID", None))
#if QT_CONFIG(tooltip)
        self.groupBox_5.setToolTip(QCoreApplication.translate("profile_settings", u"<html><head/><body><p>Perform a 'one-way' upload sync.<br/></p><p><span style=\" font-weight:700;\">Note</span>: If a file or folder is present on OneDrive, that does not exist locally, it will be removed. </p><p>If the data on OneDrive should be kept, please enable '<span style=\" font-weight:700;\">No remote delete</span>' option.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_5.setTitle(QCoreApplication.translate("profile_settings", u"Advanced options", None))
#if QT_CONFIG(tooltip)
        self.checkBox_force_http_11.setToolTip(QCoreApplication.translate("profile_settings", u"Forces the use of HTTP/1.1 instead of the default HTTP/2 .", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_force_http_11.setText(QCoreApplication.translate("profile_settings", u"Force HTTP 1.1", None))
#if QT_CONFIG(tooltip)
        self.checkBox_upload_only.setToolTip(QCoreApplication.translate("profile_settings", u"Replicate the locally configured sync_dir state to OneDrive, by only uploading local changes to OneDrive. \n"
"\n"
"Do not download changes from OneDrive.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_upload_only.setText(QCoreApplication.translate("profile_settings", u"Upload only", None))
#if QT_CONFIG(tooltip)
        self.checkBox_no_remote_delete.setToolTip(QCoreApplication.translate("profile_settings", u"Do not delete local file 'deletes' from OneDrive when using --upload-only", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_no_remote_delete.setText(QCoreApplication.translate("profile_settings", u"No remote delete", None))
#if QT_CONFIG(tooltip)
        self.checkBox_check_nomount.setToolTip(QCoreApplication.translate("profile_settings", u"<html><head/><body><pre style=\" margin-top:0px; margin-bottom:16px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:145%;\"><span style=\" font-family:'ui-monospace','SFMono-Regular','SF Mono','Menlo','Consolas','Liberation Mono','monospace'; color:#c9d1d9; background-color:transparent;\">Check for the presence of </span><span style=\" font-family:'ui-monospace','SFMono-Regular','SF Mono','Menlo','Consolas','Liberation Mono','monospace'; font-weight:700; color:#c9d1d9; background-color:transparent;\">.nosync</span><span style=\" font-family:'ui-monospace','SFMono-Regular','SF Mono','Menlo','Consolas','Liberation Mono','monospace'; color:#c9d1d9; background-color:transparent;\"> in the syncdir root. If found, do not perform sync.</span></pre></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_check_nomount.setText(QCoreApplication.translate("profile_settings", u"Check for .nomount", None))
#if QT_CONFIG(tooltip)
        self.checkBox_download_only.setToolTip(QCoreApplication.translate("profile_settings", u"Replicate the OneDrive online state locally, by only downloading changes from OneDrive. \n"
"\n"
"Do not upload local changes to OneDrive.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_download_only.setText(QCoreApplication.translate("profile_settings", u"Download only", None))
#if QT_CONFIG(tooltip)
        self.checkBox_local_first.setToolTip(QCoreApplication.translate("profile_settings", u"Synchronize from the local directory source first, before downloading changes from OneDrive.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_local_first.setText(QCoreApplication.translate("profile_settings", u"Local first", None))
#if QT_CONFIG(tooltip)
        self.checkBox_dry_run.setToolTip(QCoreApplication.translate("profile_settings", u"Perform a trial sync with no changes made.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_dry_run.setText(QCoreApplication.translate("profile_settings", u"Dry run", None))
#if QT_CONFIG(tooltip)
        self.checkBox_resync.setToolTip(QCoreApplication.translate("profile_settings", u"Forget the last saved state, perform a full sync.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_resync.setText(QCoreApplication.translate("profile_settings", u"Full re-sync", None))
        self.checkBox_bypass_data_preservation.setText(QCoreApplication.translate("profile_settings", u"Bypass data preservation", None))
#if QT_CONFIG(tooltip)
        self.checkBox_remove_source_files.setToolTip(QCoreApplication.translate("profile_settings", u"Remove source file after successful transfer to OneDrive when using --upload-only .", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_remove_source_files.setText(QCoreApplication.translate("profile_settings", u"Remove source files", None))
#if QT_CONFIG(tooltip)
        self.checkBox_disable_upload_validation.setToolTip(QCoreApplication.translate("profile_settings", u"Disable download validation when downloading from OneDrive.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_disable_upload_validation.setText(QCoreApplication.translate("profile_settings", u"Disable upload validation", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("profile_settings", u"Sync Options", None))
#if QT_CONFIG(tooltip)
        self.groupBox.setToolTip(QCoreApplication.translate("profile_settings", u"<html><head/><body><p>This option is used to 'skip' certain files and supports pattern matching.</p><p>Patterns are case insensitive. <span style=\" font-weight:700;\">*</span> and <span style=\" font-weight:700;\">? </span><a href=\"https://technet.microsoft.com/en-us/library/bb490639.aspx\"><span style=\" text-decoration: underline; color:#5e81ac;\">wildcards characters</span></a> are supported. </p><p>Use <span style=\" font-weight:700;\">|</span> to separate multiple patterns.<br/></p><p><span style=\" text-decoration: underline;\">Files can be skipped in the following fashion:</span></p><p>-Specify a wildcard, eg: '<span style=\" font-weight:700;\">*.txt</span>' (skip all txt files)</p><p>-Explicitly specify the filename and it's full path relative to your sync_dir, eg: '<span style=\" font-weight:700;\">path/to/file/filename.ext</span>'</p><p>-Explicitly specify the filename only and skip every instance of this filename, eg: '<span style=\" font-weight:700;\">filename.ext</span>'</p><p><br/></p><p><span "
                        "style=\" text-decoration: underline;\">By default, the following files will be skipped:</span></p><p>-Files that start with <span style=\" font-weight:700;\">~</span></p><p>-Files that start with <span style=\" font-weight:700;\">.~</span> (like .~lock.* files generated by LibreOffice)</p><p>-Files that end in <span style=\" font-weight:700;\">.tmp</span></p><p><br/></p><p><span style=\" font-weight:700;\">Important:</span> Do not use a skip file entry of <span style=\" font-weight:700;\">.*</span> as this will prevent correct searching of local changes to process.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox.setTitle(QCoreApplication.translate("profile_settings", u"Skip files", None))
        self.pushButton_add_skip_file.setText(QCoreApplication.translate("profile_settings", u"Add", None))
        self.pushButton_rm_skip_file.setText(QCoreApplication.translate("profile_settings", u"Remove", None))
#if QT_CONFIG(tooltip)
        self.groupBox_2.setToolTip(QCoreApplication.translate("profile_settings", u"<html><head/><body><p>This option is used to 'skip' certain directories and supports pattern matching.</p><p><br/></p><p>Patterns are case insensitive. <span style=\" font-weight:700;\">*</span> and <span style=\" font-weight:700;\">? </span><a href=\"https://technet.microsoft.com/en-us/library/bb490639.aspx\"><span style=\" text-decoration: underline; color:#5e81ac;\">wildcards characters</span></a> are supported. </p><p>Use <span style=\" font-weight:700;\">|</span> to separate multiple patterns.</p><p><br/></p><p><span style=\" font-weight:700;\">Important</span>: Entries under Skip directories are relative to your <span style=\" font-weight:700;\">Sync directory</span> path.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_2.setTitle(QCoreApplication.translate("profile_settings", u"Skip directories", None))
        self.checkBox_skip_dir_strict_match.setText(QCoreApplication.translate("profile_settings", u"Strict match", None))
        self.pushButton_rm_skip_dir.setText(QCoreApplication.translate("profile_settings", u"Remove", None))
        self.pushButton_add_skip_dir.setText(QCoreApplication.translate("profile_settings", u"Add", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("profile_settings", u"Others", None))
#if QT_CONFIG(tooltip)
        self.checkBox_skip_symlinks.setToolTip(QCoreApplication.translate("profile_settings", u"Skip syncing of symlinks.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_skip_symlinks.setText(QCoreApplication.translate("profile_settings", u"Skip symlinks", None))
#if QT_CONFIG(tooltip)
        self.checkBox_check_nosync.setToolTip(QCoreApplication.translate("profile_settings", u"Check for the presence of .nosync in each directory. If found, skip directory from sync.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_check_nosync.setText(QCoreApplication.translate("profile_settings", u"Check for .nosync", None))
#if QT_CONFIG(tooltip)
        self.checkBox_skip_dotfiles.setToolTip(QCoreApplication.translate("profile_settings", u"Skip dot files and folders from syncing", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_skip_dotfiles.setText(QCoreApplication.translate("profile_settings", u"Skip dotfiles (hidden files)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("profile_settings", u"Excluded files", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("profile_settings", u"Sync List", None))
        self.label_sync_list.setText(QCoreApplication.translate("profile_settings", u"Selective sync allows you to sync only specific files and directories. <br> See <a href=\"https://github.com/abraunegg/onedrive/blob/master/docs/USAGE.md#performing-a-selective-sync-via-sync_list-file\">official documentation </a> for more details.", None))
#if QT_CONFIG(tooltip)
        self.checkBox_sync_root_files.setToolTip(QCoreApplication.translate("profile_settings", u"Sync all files in Sync Directory root when using Sync List.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_sync_root_files.setText(QCoreApplication.translate("profile_settings", u"Sync root files", None))
#if QT_CONFIG(tooltip)
        self.textEdit_sync_list.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("profile_settings", u"Selective Sync", None))
        self.groupBox_sync_business_shared_folders.setTitle(QCoreApplication.translate("profile_settings", u"Sync business shared folders", None))
        self.label_business_available.setText(QCoreApplication.translate("profile_settings", u"Available Business Shared Folders:", None))
#if QT_CONFIG(tooltip)
        self.checkBox_sync_business_shared_folders.setToolTip(QCoreApplication.translate("profile_settings", u"<html><head/><body><p>Refer to <a href=\"https://github.com/abraunegg/onedrive/blob/master/docs/BusinessSharedFolders.md\"><span style=\" text-decoration: underline; color:#5e81ac;\">Business Shared Folders</span></a> for configuration assistance.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_sync_business_shared_folders.setText(QCoreApplication.translate("profile_settings", u"Sync business shared folders", None))
        self.label_business_selected.setText(QCoreApplication.translate("profile_settings", u"Selected Business Shared Folders:", None))
        self.pushButton_add_business_folder.setText(QCoreApplication.translate("profile_settings", u">>", None))
        self.pushButton_get_business_folders.setText(QCoreApplication.translate("profile_settings", u"Get Shared Folders", None))
        self.pushButton_remove_business_folders.setText(QCoreApplication.translate("profile_settings", u"Remove", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("profile_settings", u"Shared Folders", None))
#if QT_CONFIG(tooltip)
        self.groupBox_9.setToolTip(QCoreApplication.translate("profile_settings", u"<html><head/><body><p>Refer to <a href=\"https://github.com/abraunegg/onedrive/blob/master/docs/USAGE.md#use-webhook-to-subscribe-to-remote-updates-in-monitor-mode\"><span style=\" text-decoration: underline; color:#5e81ac;\">webhook documentation</span></a> for more details. </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_9.setTitle(QCoreApplication.translate("profile_settings", u"Webhook settings", None))
        self.label_webhook_public_url.setText(QCoreApplication.translate("profile_settings", u"Public URL", None))
        self.label_webhook_listening_host.setText(QCoreApplication.translate("profile_settings", u"Listening host", None))
        self.label_webhook_listening_port.setText(QCoreApplication.translate("profile_settings", u"Listening port", None))
        self.label_webhook_expiration_interval.setText(QCoreApplication.translate("profile_settings", u"Expiration interval", None))
        self.label_webhook_renewal_interval.setText(QCoreApplication.translate("profile_settings", u"Renewal interval", None))
        self.checkBox_webhook_enabled.setText(QCoreApplication.translate("profile_settings", u"Enable webhook", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("profile_settings", u"Webhooks", None))
#if QT_CONFIG(tooltip)
        self.groupBox_7.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.groupBox_7.setTitle(QCoreApplication.translate("profile_settings", u"Logging", None))
#if QT_CONFIG(tooltip)
        self.checkBox_enable_logging.setToolTip(QCoreApplication.translate("profile_settings", u"Enable OneDrive client activity logging to a separate log file.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_enable_logging.setText(QCoreApplication.translate("profile_settings", u"Enable Logging", None))
#if QT_CONFIG(tooltip)
        self.label_log_dir.setToolTip(QCoreApplication.translate("profile_settings", u"Directory where logging output is saved to, needs to end with a slash.", None))
#endif // QT_CONFIG(tooltip)
        self.label_log_dir.setText(QCoreApplication.translate("profile_settings", u"Log location:", None))
#if QT_CONFIG(tooltip)
        self.checkBox_debug_https.setToolTip(QCoreApplication.translate("profile_settings", u"Debug OneDrive HTTPS communication.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_debug_https.setText(QCoreApplication.translate("profile_settings", u"Debug HTTPS", None))
        self.pushButton_log_dir_browse.setText(QCoreApplication.translate("profile_settings", u"Browse", None))
#if QT_CONFIG(tooltip)
        self.label_monitor_log_frequency.setToolTip(QCoreApplication.translate("profile_settings", u"Frequency of logging in monitor mode.", None))
#endif // QT_CONFIG(tooltip)
        self.label_monitor_log_frequency.setText(QCoreApplication.translate("profile_settings", u"Monitor log frequency", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("profile_settings", u"Notifications", None))
#if QT_CONFIG(tooltip)
        self.label_min_notify_changes.setToolTip(QCoreApplication.translate("profile_settings", u"Minimum number of pending incoming changes necessary to trigger a desktop notification.", None))
#endif // QT_CONFIG(tooltip)
        self.label_min_notify_changes.setText(QCoreApplication.translate("profile_settings", u"Minimum notify changes", None))
#if QT_CONFIG(tooltip)
        self.checkBox_disable_notifications.setToolTip(QCoreApplication.translate("profile_settings", u"Do not use desktop notifications in monitor mode.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_disable_notifications.setText(QCoreApplication.translate("profile_settings", u"Disable notifications", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_logging), QCoreApplication.translate("profile_settings", u"Logging", None))
        self.pushButton_discard.setText(QCoreApplication.translate("profile_settings", u"Discard changes", None))
        self.pushButton_save.setText(QCoreApplication.translate("profile_settings", u"Save", None))
    # retranslateUi

