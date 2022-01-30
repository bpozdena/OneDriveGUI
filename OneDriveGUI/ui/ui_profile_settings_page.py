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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QSpinBox, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_profile_settings(object):
    def setupUi(self, profile_settings):
        if not profile_settings.objectName():
            profile_settings.setObjectName(u"profile_settings")
        profile_settings.resize(664, 723)
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

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(profile_settings)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(650, 600))
        self.exemptions_tab_2 = QWidget()
        self.exemptions_tab_2.setObjectName(u"exemptions_tab_2")
        self.verticalLayout_5 = QVBoxLayout(self.exemptions_tab_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox_8 = QGroupBox(self.exemptions_tab_2)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.gridLayout_9 = QGridLayout(self.groupBox_8)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pushButton_3 = QPushButton(self.groupBox_8)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_5.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.label_sync_dir = QLabel(self.groupBox_8)
        self.label_sync_dir.setObjectName(u"label_sync_dir")

        self.gridLayout_5.addWidget(self.label_sync_dir, 0, 0, 1, 1)

        self.lineEdit_sync_dir = QLineEdit(self.groupBox_8)
        self.lineEdit_sync_dir.setObjectName(u"lineEdit_sync_dir")

        self.gridLayout_5.addWidget(self.lineEdit_sync_dir, 0, 1, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_5, 1, 0, 1, 1)

        self.checkBox_sync_root_files = QCheckBox(self.groupBox_8)
        self.checkBox_sync_root_files.setObjectName(u"checkBox_sync_root_files")

        self.gridLayout_9.addWidget(self.checkBox_sync_root_files, 2, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.groupBox_8)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.tabWidget.addTab(self.exemptions_tab_2, "")
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
        self.spinBox_rate_limit.setMinimum(125000)
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
        self.formLayout = QFormLayout(self.groupBox_4)
        self.formLayout.setObjectName(u"formLayout")
        self.label_monitor_interval = QLabel(self.groupBox_4)
        self.label_monitor_interval.setObjectName(u"label_monitor_interval")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_monitor_interval)

        self.spinBox_monitor_interval = QSpinBox(self.groupBox_4)
        self.spinBox_monitor_interval.setObjectName(u"spinBox_monitor_interval")
        self.spinBox_monitor_interval.setMaximum(1000000)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.spinBox_monitor_interval)

        self.label_monitor_fullscan_frequency = QLabel(self.groupBox_4)
        self.label_monitor_fullscan_frequency.setObjectName(u"label_monitor_fullscan_frequency")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_monitor_fullscan_frequency)

        self.spinBox_monitor_fullscan_frequency = QSpinBox(self.groupBox_4)
        self.spinBox_monitor_fullscan_frequency.setObjectName(u"spinBox_monitor_fullscan_frequency")
        self.spinBox_monitor_fullscan_frequency.setMaximum(1000000)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.spinBox_monitor_fullscan_frequency)

        self.label_classify_as_big_delete = QLabel(self.groupBox_4)
        self.label_classify_as_big_delete.setObjectName(u"label_classify_as_big_delete")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_classify_as_big_delete)

        self.spinBox_classify_as_big_delete = QSpinBox(self.groupBox_4)
        self.spinBox_classify_as_big_delete.setObjectName(u"spinBox_classify_as_big_delete")
        self.spinBox_classify_as_big_delete.setMaximum(1000000)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.spinBox_classify_as_big_delete)

        self.label_user_agent = QLabel(self.groupBox_4)
        self.label_user_agent.setObjectName(u"label_user_agent")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_user_agent)

        self.lineEdit_user_agent = QLineEdit(self.groupBox_4)
        self.lineEdit_user_agent.setObjectName(u"lineEdit_user_agent")
        self.lineEdit_user_agent.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_user_agent.setMaxLength(32767)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit_user_agent)

        self.label_azure_ad_endpoint = QLabel(self.groupBox_4)
        self.label_azure_ad_endpoint.setObjectName(u"label_azure_ad_endpoint")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_azure_ad_endpoint)

        self.lineEdit_azure_ad_endpoint = QLineEdit(self.groupBox_4)
        self.lineEdit_azure_ad_endpoint.setObjectName(u"lineEdit_azure_ad_endpoint")
        self.lineEdit_azure_ad_endpoint.setMaximumSize(QSize(200, 16777215))

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEdit_azure_ad_endpoint)

        self.label_azure_tenant_id = QLabel(self.groupBox_4)
        self.label_azure_tenant_id.setObjectName(u"label_azure_tenant_id")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_azure_tenant_id)

        self.lineEdit_azure_tenant_id = QLineEdit(self.groupBox_4)
        self.lineEdit_azure_tenant_id.setObjectName(u"lineEdit_azure_tenant_id")
        self.lineEdit_azure_tenant_id.setMaximumSize(QSize(200, 16777215))

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lineEdit_azure_tenant_id)

        self.label_sync_dir_permissions = QLabel(self.groupBox_4)
        self.label_sync_dir_permissions.setObjectName(u"label_sync_dir_permissions")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_sync_dir_permissions)

        self.spinBox_sync_dir_permissions = QSpinBox(self.groupBox_4)
        self.spinBox_sync_dir_permissions.setObjectName(u"spinBox_sync_dir_permissions")
        self.spinBox_sync_dir_permissions.setMaximum(777)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.spinBox_sync_dir_permissions)

        self.label_sync_file_permissions = QLabel(self.groupBox_4)
        self.label_sync_file_permissions.setObjectName(u"label_sync_file_permissions")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_sync_file_permissions)

        self.spinBox_sync_file_permissions = QSpinBox(self.groupBox_4)
        self.spinBox_sync_file_permissions.setObjectName(u"spinBox_sync_file_permissions")
        self.spinBox_sync_file_permissions.setMaximum(777)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.spinBox_sync_file_permissions)

        self.label_operation_timeout = QLabel(self.groupBox_4)
        self.label_operation_timeout.setObjectName(u"label_operation_timeout")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_operation_timeout)

        self.spinBox_operation_timeout = QSpinBox(self.groupBox_4)
        self.spinBox_operation_timeout.setObjectName(u"spinBox_operation_timeout")
        self.spinBox_operation_timeout.setMaximum(1000000)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.spinBox_operation_timeout)


        self.verticalLayout_8.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.tab_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_4 = QGridLayout(self.groupBox_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.checkBox_force_http_2 = QCheckBox(self.groupBox_5)
        self.checkBox_force_http_2.setObjectName(u"checkBox_force_http_2")

        self.gridLayout_4.addWidget(self.checkBox_force_http_2, 2, 1, 1, 1)

        self.checkBox_check_nomount = QCheckBox(self.groupBox_5)
        self.checkBox_check_nomount.setObjectName(u"checkBox_check_nomount")

        self.gridLayout_4.addWidget(self.checkBox_check_nomount, 4, 1, 1, 1)

        self.checkBox_resync = QCheckBox(self.groupBox_5)
        self.checkBox_resync.setObjectName(u"checkBox_resync")

        self.gridLayout_4.addWidget(self.checkBox_resync, 4, 2, 1, 1)

        self.checkBox_download_only = QCheckBox(self.groupBox_5)
        self.checkBox_download_only.setObjectName(u"checkBox_download_only")

        self.gridLayout_4.addWidget(self.checkBox_download_only, 0, 1, 1, 1)

        self.checkBox_local_first = QCheckBox(self.groupBox_5)
        self.checkBox_local_first.setObjectName(u"checkBox_local_first")

        self.gridLayout_4.addWidget(self.checkBox_local_first, 5, 1, 1, 1)

        self.checkBox_dry_run = QCheckBox(self.groupBox_5)
        self.checkBox_dry_run.setObjectName(u"checkBox_dry_run")

        self.gridLayout_4.addWidget(self.checkBox_dry_run, 2, 2, 1, 1)

        self.checkBox_disable_upload_validation = QCheckBox(self.groupBox_5)
        self.checkBox_disable_upload_validation.setObjectName(u"checkBox_disable_upload_validation")

        self.gridLayout_4.addWidget(self.checkBox_disable_upload_validation, 3, 1, 1, 1)

        self.checkBox_bypass_data_preservation = QCheckBox(self.groupBox_5)
        self.checkBox_bypass_data_preservation.setObjectName(u"checkBox_bypass_data_preservation")

        self.gridLayout_4.addWidget(self.checkBox_bypass_data_preservation, 5, 2, 1, 1)

        self.checkBox_no_remote_delete = QCheckBox(self.groupBox_5)
        self.checkBox_no_remote_delete.setObjectName(u"checkBox_no_remote_delete")

        self.gridLayout_4.addWidget(self.checkBox_no_remote_delete, 0, 2, 1, 1)

        self.checkBox_remove_source_files = QCheckBox(self.groupBox_5)
        self.checkBox_remove_source_files.setObjectName(u"checkBox_remove_source_files")

        self.gridLayout_4.addWidget(self.checkBox_remove_source_files, 3, 2, 1, 1)

        self.checkBox_upload_only = QCheckBox(self.groupBox_5)
        self.checkBox_upload_only.setObjectName(u"checkBox_upload_only")

        self.gridLayout_4.addWidget(self.checkBox_upload_only, 1, 1, 1, 1)

        self.checkBox_sync_business_shared_folders = QCheckBox(self.groupBox_5)
        self.checkBox_sync_business_shared_folders.setObjectName(u"checkBox_sync_business_shared_folders")

        self.gridLayout_4.addWidget(self.checkBox_sync_business_shared_folders, 1, 2, 1, 1)


        self.verticalLayout_8.addWidget(self.groupBox_5)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_4)

        self.tabWidget.addTab(self.tab_2, "")
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

        self.pushButton_log_dir = QPushButton(self.groupBox_7)
        self.pushButton_log_dir.setObjectName(u"pushButton_log_dir")

        self.gridLayout_8.addWidget(self.pushButton_log_dir, 1, 2, 1, 1)

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
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.horizontalLayout_2 = QHBoxLayout(self.tab_6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_login = QPushButton(self.tab_6)
        self.pushButton_login.setObjectName(u"pushButton_login")

        self.horizontalLayout_2.addWidget(self.pushButton_login)

        self.pushButton_logout = QPushButton(self.tab_6)
        self.pushButton_logout.setObjectName(u"pushButton_logout")

        self.horizontalLayout_2.addWidget(self.pushButton_logout)

        self.tabWidget.addTab(self.tab_6, "")

        self.horizontalLayout.addWidget(self.tabWidget)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.pushButton_discart = QPushButton(profile_settings)
        self.pushButton_discart.setObjectName(u"pushButton_discart")

        self.verticalLayout_2.addWidget(self.pushButton_discart)

        self.pushButton_save = QPushButton(profile_settings)
        self.pushButton_save.setObjectName(u"pushButton_save")

        self.verticalLayout_2.addWidget(self.pushButton_save)


        self.retranslateUi(profile_settings)

        self.tabWidget.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(profile_settings)
    # setupUi

    def retranslateUi(self, profile_settings):
        profile_settings.setWindowTitle(QCoreApplication.translate("profile_settings", u"OneDriveGUI - Profile Settings", None))
        self.label_profile_name.setText(QCoreApplication.translate("profile_settings", u"Profile name", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("profile_settings", u"Monitored directory", None))
        self.pushButton_3.setText(QCoreApplication.translate("profile_settings", u"Browse", None))
        self.label_sync_dir.setText(QCoreApplication.translate("profile_settings", u"Sync Folder:", None))
        self.checkBox_sync_root_files.setText(QCoreApplication.translate("profile_settings", u"Sync root files", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.exemptions_tab_2), QCoreApplication.translate("profile_settings", u"Monitored Files", None))
        self.groupBox.setTitle(QCoreApplication.translate("profile_settings", u"Excluded files", None))
        self.pushButton_add_skip_file.setText(QCoreApplication.translate("profile_settings", u"Add", None))
        self.pushButton_rm_skip_file.setText(QCoreApplication.translate("profile_settings", u"Remove", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("profile_settings", u"Excluded directories", None))
        self.checkBox_skip_dir_strict_match.setText(QCoreApplication.translate("profile_settings", u"Strict match", None))
        self.pushButton_rm_skip_dir.setText(QCoreApplication.translate("profile_settings", u"Remove", None))
        self.pushButton_add_skip_dir.setText(QCoreApplication.translate("profile_settings", u"Add", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("profile_settings", u"Others", None))
        self.checkBox_skip_symlinks.setText(QCoreApplication.translate("profile_settings", u"Exclude symlinks", None))
        self.checkBox_check_nosync.setText(QCoreApplication.translate("profile_settings", u"Check for .nosync", None))
        self.checkBox_skip_dotfiles.setText(QCoreApplication.translate("profile_settings", u"Exclude dotfiles (hidden files)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("profile_settings", u"Excluded files", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("profile_settings", u"Account Rate Limit", None))
        self.label_rate_limit.setText(QCoreApplication.translate("profile_settings", u"Rate Limit [B/s]", None))
        self.label_rate_limit_mbps.setText(QCoreApplication.translate("profile_settings", u"(Mibit/s)", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("profile_settings", u"Advanced Properties", None))
        self.label_monitor_interval.setText(QCoreApplication.translate("profile_settings", u"Monitor interval", None))
        self.label_monitor_fullscan_frequency.setText(QCoreApplication.translate("profile_settings", u"Monitor full-scan frequency", None))
        self.label_classify_as_big_delete.setText(QCoreApplication.translate("profile_settings", u"Clasify as big delete", None))
        self.label_user_agent.setText(QCoreApplication.translate("profile_settings", u"User-agent", None))
        self.label_azure_ad_endpoint.setText(QCoreApplication.translate("profile_settings", u"Azure AD endpoint", None))
        self.label_azure_tenant_id.setText(QCoreApplication.translate("profile_settings", u"Azure tenant ID", None))
        self.label_sync_dir_permissions.setText(QCoreApplication.translate("profile_settings", u"Sync dir permissions", None))
        self.label_sync_file_permissions.setText(QCoreApplication.translate("profile_settings", u"Sync file permissions", None))
        self.label_operation_timeout.setText(QCoreApplication.translate("profile_settings", u"Operation timeout", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("profile_settings", u"Advanced options", None))
        self.checkBox_force_http_2.setText(QCoreApplication.translate("profile_settings", u"Force HTTP2", None))
        self.checkBox_check_nomount.setText(QCoreApplication.translate("profile_settings", u"Check for .nomount", None))
        self.checkBox_resync.setText(QCoreApplication.translate("profile_settings", u"Full re-sync", None))
        self.checkBox_download_only.setText(QCoreApplication.translate("profile_settings", u"Download only", None))
        self.checkBox_local_first.setText(QCoreApplication.translate("profile_settings", u"Local first", None))
        self.checkBox_dry_run.setText(QCoreApplication.translate("profile_settings", u"Dry run", None))
        self.checkBox_disable_upload_validation.setText(QCoreApplication.translate("profile_settings", u"Disable upload validation", None))
        self.checkBox_bypass_data_preservation.setText(QCoreApplication.translate("profile_settings", u"Bypass data preservation", None))
        self.checkBox_no_remote_delete.setText(QCoreApplication.translate("profile_settings", u"No remote delete", None))
        self.checkBox_remove_source_files.setText(QCoreApplication.translate("profile_settings", u"Remove source files", None))
        self.checkBox_upload_only.setText(QCoreApplication.translate("profile_settings", u"Upload only", None))
        self.checkBox_sync_business_shared_folders.setText(QCoreApplication.translate("profile_settings", u"Sync business shared folders", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("profile_settings", u"Sync Options", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("profile_settings", u"Logging", None))
        self.checkBox_enable_logging.setText(QCoreApplication.translate("profile_settings", u"Enable Logging", None))
        self.label_log_dir.setText(QCoreApplication.translate("profile_settings", u"Log location:", None))
        self.checkBox_debug_https.setText(QCoreApplication.translate("profile_settings", u"Debug HTTPS", None))
        self.pushButton_log_dir.setText(QCoreApplication.translate("profile_settings", u"Browse", None))
        self.label_monitor_log_frequency.setText(QCoreApplication.translate("profile_settings", u"Monitor log frequency", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("profile_settings", u"Notifications", None))
        self.label_min_notify_changes.setText(QCoreApplication.translate("profile_settings", u"Minimum notify changes", None))
        self.checkBox_disable_notifications.setText(QCoreApplication.translate("profile_settings", u"Disable notifications", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_logging), QCoreApplication.translate("profile_settings", u"Logging", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("profile_settings", u"Webhook settings", None))
        self.label_webhook_public_url.setText(QCoreApplication.translate("profile_settings", u"Public URL", None))
        self.label_webhook_listening_host.setText(QCoreApplication.translate("profile_settings", u"Listening host", None))
        self.label_webhook_listening_port.setText(QCoreApplication.translate("profile_settings", u"Listening port", None))
        self.label_webhook_expiration_interval.setText(QCoreApplication.translate("profile_settings", u"Expiration interval", None))
        self.label_webhook_renewal_interval.setText(QCoreApplication.translate("profile_settings", u"Renewal interval", None))
        self.checkBox_webhook_enabled.setText(QCoreApplication.translate("profile_settings", u"Enable webhook", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("profile_settings", u"Webhooks", None))
        self.pushButton_login.setText(QCoreApplication.translate("profile_settings", u"Login", None))
        self.pushButton_logout.setText(QCoreApplication.translate("profile_settings", u"Logout", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("profile_settings", u"Account", None))
        self.pushButton_discart.setText(QCoreApplication.translate("profile_settings", u"Discard changes", None))
        self.pushButton_save.setText(QCoreApplication.translate("profile_settings", u"Save", None))
    # retranslateUi

