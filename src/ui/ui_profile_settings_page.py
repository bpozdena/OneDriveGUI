# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profile_settings_page.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QFormLayout,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QSizePolicy,
    QSlider,
    QSpacerItem,
    QSpinBox,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)


class Ui_profile_settings(object):
    def setupUi(self, profile_settings):
        if not profile_settings.objectName():
            profile_settings.setObjectName("profile_settings")
        profile_settings.resize(664, 723)
        self.verticalLayout_2 = QVBoxLayout(profile_settings)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.label_profile_name = QLabel(profile_settings)
        self.label_profile_name.setObjectName("label_profile_name")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_profile_name.setFont(font)
        self.label_profile_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_profile_name)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QTabWidget(profile_settings)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setMinimumSize(QSize(650, 600))
        self.exemptions_tab_2 = QWidget()
        self.exemptions_tab_2.setObjectName("exemptions_tab_2")
        self.verticalLayout_5 = QVBoxLayout(self.exemptions_tab_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_8 = QGroupBox(self.exemptions_tab_2)
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_9 = QGridLayout(self.groupBox_8)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButton_sync_dir_browse = QPushButton(self.groupBox_8)
        self.pushButton_sync_dir_browse.setObjectName("pushButton_sync_dir_browse")

        self.gridLayout_5.addWidget(self.pushButton_sync_dir_browse, 0, 2, 1, 1)

        self.label_sync_dir = QLabel(self.groupBox_8)
        self.label_sync_dir.setObjectName("label_sync_dir")

        self.gridLayout_5.addWidget(self.label_sync_dir, 0, 0, 1, 1)

        self.lineEdit_sync_dir = QLineEdit(self.groupBox_8)
        self.lineEdit_sync_dir.setObjectName("lineEdit_sync_dir")

        self.gridLayout_5.addWidget(self.lineEdit_sync_dir, 0, 1, 1, 1)

        self.gridLayout_9.addLayout(self.gridLayout_5, 1, 0, 1, 1)

        self.checkBox_sync_root_files = QCheckBox(self.groupBox_8)
        self.checkBox_sync_root_files.setObjectName("checkBox_sync_root_files")

        self.gridLayout_9.addWidget(self.checkBox_sync_root_files, 2, 0, 1, 1)

        self.verticalLayout_5.addWidget(self.groupBox_8)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.tabWidget.addTab(self.exemptions_tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_7 = QVBoxLayout(self.tab)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.lineEdit_skip_file = QLineEdit(self.groupBox)
        self.lineEdit_skip_file.setObjectName("lineEdit_skip_file")

        self.gridLayout_6.addWidget(self.lineEdit_skip_file, 1, 0, 1, 1)

        self.pushButton_add_skip_file = QPushButton(self.groupBox)
        self.pushButton_add_skip_file.setObjectName("pushButton_add_skip_file")

        self.gridLayout_6.addWidget(self.pushButton_add_skip_file, 1, 1, 1, 1)

        self.pushButton_rm_skip_file = QPushButton(self.groupBox)
        self.pushButton_rm_skip_file.setObjectName("pushButton_rm_skip_file")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_rm_skip_file.sizePolicy().hasHeightForWidth())
        self.pushButton_rm_skip_file.setSizePolicy(sizePolicy)

        self.gridLayout_6.addWidget(self.pushButton_rm_skip_file, 0, 1, 1, 1)

        self.listWidget_skip_file = QListWidget(self.groupBox)
        self.listWidget_skip_file.setObjectName("listWidget_skip_file")

        self.gridLayout_6.addWidget(self.listWidget_skip_file, 0, 0, 1, 1)

        self.verticalLayout_3.addLayout(self.gridLayout_6)

        self.verticalLayout_7.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkBox_skip_dir_strict_match = QCheckBox(self.groupBox_2)
        self.checkBox_skip_dir_strict_match.setObjectName("checkBox_skip_dir_strict_match")

        self.verticalLayout_4.addWidget(self.checkBox_skip_dir_strict_match)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.pushButton_rm_skip_dir = QPushButton(self.groupBox_2)
        self.pushButton_rm_skip_dir.setObjectName("pushButton_rm_skip_dir")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_rm_skip_dir.sizePolicy().hasHeightForWidth())
        self.pushButton_rm_skip_dir.setSizePolicy(sizePolicy1)

        self.gridLayout_7.addWidget(self.pushButton_rm_skip_dir, 0, 1, 1, 1)

        self.listWidget_skip_dir = QListWidget(self.groupBox_2)
        self.listWidget_skip_dir.setObjectName("listWidget_skip_dir")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.listWidget_skip_dir.sizePolicy().hasHeightForWidth())
        self.listWidget_skip_dir.setSizePolicy(sizePolicy2)

        self.gridLayout_7.addWidget(self.listWidget_skip_dir, 0, 0, 1, 1)

        self.lineEdit_skip_dir = QLineEdit(self.groupBox_2)
        self.lineEdit_skip_dir.setObjectName("lineEdit_skip_dir")

        self.gridLayout_7.addWidget(self.lineEdit_skip_dir, 1, 0, 1, 1)

        self.pushButton_add_skip_dir = QPushButton(self.groupBox_2)
        self.pushButton_add_skip_dir.setObjectName("pushButton_add_skip_dir")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_add_skip_dir.sizePolicy().hasHeightForWidth())
        self.pushButton_add_skip_dir.setSizePolicy(sizePolicy3)

        self.gridLayout_7.addWidget(self.pushButton_add_skip_dir, 1, 1, 1, 1)

        self.verticalLayout_4.addLayout(self.gridLayout_7)

        self.verticalLayout_7.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBox_skip_symlinks = QCheckBox(self.groupBox_3)
        self.checkBox_skip_symlinks.setObjectName("checkBox_skip_symlinks")

        self.gridLayout_2.addWidget(self.checkBox_skip_symlinks, 0, 1, 1, 1)

        self.checkBox_check_nosync = QCheckBox(self.groupBox_3)
        self.checkBox_check_nosync.setObjectName("checkBox_check_nosync")

        self.gridLayout_2.addWidget(self.checkBox_check_nosync, 0, 0, 1, 1)

        self.checkBox_skip_dotfiles = QCheckBox(self.groupBox_3)
        self.checkBox_skip_dotfiles.setObjectName("checkBox_skip_dotfiles")

        self.gridLayout_2.addWidget(self.checkBox_skip_dotfiles, 1, 0, 1, 1)

        self.verticalLayout_7.addWidget(self.groupBox_3)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_8 = QVBoxLayout(self.tab_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.groupBox_10 = QGroupBox(self.tab_2)
        self.groupBox_10.setObjectName("groupBox_10")
        self.gridLayout_11 = QGridLayout(self.groupBox_10)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.spinBox_rate_limit = QSpinBox(self.groupBox_10)
        self.spinBox_rate_limit.setObjectName("spinBox_rate_limit")
        self.spinBox_rate_limit.setMinimum(125000)
        self.spinBox_rate_limit.setMaximum(125000000)
        self.spinBox_rate_limit.setSingleStep(12500)

        self.gridLayout_11.addWidget(self.spinBox_rate_limit, 0, 1, 1, 1)

        self.label_rate_limit = QLabel(self.groupBox_10)
        self.label_rate_limit.setObjectName("label_rate_limit")

        self.gridLayout_11.addWidget(self.label_rate_limit, 0, 0, 1, 1)

        self.horizontalSlider_rate_limit = QSlider(self.groupBox_10)
        self.horizontalSlider_rate_limit.setObjectName("horizontalSlider_rate_limit")
        self.horizontalSlider_rate_limit.setMinimum(125000)
        self.horizontalSlider_rate_limit.setMaximum(125000000)
        self.horizontalSlider_rate_limit.setSingleStep(12500)
        self.horizontalSlider_rate_limit.setPageStep(12500)
        self.horizontalSlider_rate_limit.setOrientation(Qt.Horizontal)

        self.gridLayout_11.addWidget(self.horizontalSlider_rate_limit, 1, 0, 1, 4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer, 0, 3, 1, 1)

        self.label_rate_limit_mbps = QLabel(self.groupBox_10)
        self.label_rate_limit_mbps.setObjectName("label_rate_limit_mbps")

        self.gridLayout_11.addWidget(self.label_rate_limit_mbps, 0, 2, 1, 1)

        self.verticalLayout_8.addWidget(self.groupBox_10)

        self.groupBox_4 = QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName("groupBox_4")
        self.formLayout = QFormLayout(self.groupBox_4)
        self.formLayout.setObjectName("formLayout")
        self.label_monitor_interval = QLabel(self.groupBox_4)
        self.label_monitor_interval.setObjectName("label_monitor_interval")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_monitor_interval)

        self.spinBox_monitor_interval = QSpinBox(self.groupBox_4)
        self.spinBox_monitor_interval.setObjectName("spinBox_monitor_interval")
        self.spinBox_monitor_interval.setMaximum(1000000)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.spinBox_monitor_interval)

        self.label_monitor_fullscan_frequency = QLabel(self.groupBox_4)
        self.label_monitor_fullscan_frequency.setObjectName("label_monitor_fullscan_frequency")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_monitor_fullscan_frequency)

        self.spinBox_monitor_fullscan_frequency = QSpinBox(self.groupBox_4)
        self.spinBox_monitor_fullscan_frequency.setObjectName("spinBox_monitor_fullscan_frequency")
        self.spinBox_monitor_fullscan_frequency.setMaximum(1000000)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.spinBox_monitor_fullscan_frequency)

        self.label_classify_as_big_delete = QLabel(self.groupBox_4)
        self.label_classify_as_big_delete.setObjectName("label_classify_as_big_delete")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_classify_as_big_delete)

        self.spinBox_classify_as_big_delete = QSpinBox(self.groupBox_4)
        self.spinBox_classify_as_big_delete.setObjectName("spinBox_classify_as_big_delete")
        self.spinBox_classify_as_big_delete.setMaximum(1000000)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.spinBox_classify_as_big_delete)

        self.label_user_agent = QLabel(self.groupBox_4)
        self.label_user_agent.setObjectName("label_user_agent")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_user_agent)

        self.lineEdit_user_agent = QLineEdit(self.groupBox_4)
        self.lineEdit_user_agent.setObjectName("lineEdit_user_agent")
        self.lineEdit_user_agent.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_user_agent.setMaxLength(32767)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit_user_agent)

        self.label_azure_ad_endpoint = QLabel(self.groupBox_4)
        self.label_azure_ad_endpoint.setObjectName("label_azure_ad_endpoint")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_azure_ad_endpoint)

        self.lineEdit_azure_ad_endpoint = QLineEdit(self.groupBox_4)
        self.lineEdit_azure_ad_endpoint.setObjectName("lineEdit_azure_ad_endpoint")
        self.lineEdit_azure_ad_endpoint.setMaximumSize(QSize(200, 16777215))

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEdit_azure_ad_endpoint)

        self.label_azure_tenant_id = QLabel(self.groupBox_4)
        self.label_azure_tenant_id.setObjectName("label_azure_tenant_id")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_azure_tenant_id)

        self.lineEdit_azure_tenant_id = QLineEdit(self.groupBox_4)
        self.lineEdit_azure_tenant_id.setObjectName("lineEdit_azure_tenant_id")
        self.lineEdit_azure_tenant_id.setMaximumSize(QSize(200, 16777215))

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lineEdit_azure_tenant_id)

        self.label_sync_dir_permissions = QLabel(self.groupBox_4)
        self.label_sync_dir_permissions.setObjectName("label_sync_dir_permissions")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_sync_dir_permissions)

        self.spinBox_sync_dir_permissions = QSpinBox(self.groupBox_4)
        self.spinBox_sync_dir_permissions.setObjectName("spinBox_sync_dir_permissions")
        self.spinBox_sync_dir_permissions.setMaximum(777)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.spinBox_sync_dir_permissions)

        self.label_sync_file_permissions = QLabel(self.groupBox_4)
        self.label_sync_file_permissions.setObjectName("label_sync_file_permissions")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_sync_file_permissions)

        self.spinBox_sync_file_permissions = QSpinBox(self.groupBox_4)
        self.spinBox_sync_file_permissions.setObjectName("spinBox_sync_file_permissions")
        self.spinBox_sync_file_permissions.setMaximum(777)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.spinBox_sync_file_permissions)

        self.label_operation_timeout = QLabel(self.groupBox_4)
        self.label_operation_timeout.setObjectName("label_operation_timeout")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_operation_timeout)

        self.spinBox_operation_timeout = QSpinBox(self.groupBox_4)
        self.spinBox_operation_timeout.setObjectName("spinBox_operation_timeout")
        self.spinBox_operation_timeout.setMaximum(1000000)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.spinBox_operation_timeout)

        self.verticalLayout_8.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.tab_2)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_4 = QGridLayout(self.groupBox_5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.checkBox_force_http_11 = QCheckBox(self.groupBox_5)
        self.checkBox_force_http_11.setObjectName("checkBox_force_http_11")

        self.gridLayout_4.addWidget(self.checkBox_force_http_11, 2, 1, 1, 1)

        self.checkBox_check_nomount = QCheckBox(self.groupBox_5)
        self.checkBox_check_nomount.setObjectName("checkBox_check_nomount")

        self.gridLayout_4.addWidget(self.checkBox_check_nomount, 4, 1, 1, 1)

        self.checkBox_resync = QCheckBox(self.groupBox_5)
        self.checkBox_resync.setObjectName("checkBox_resync")

        self.gridLayout_4.addWidget(self.checkBox_resync, 4, 2, 1, 1)

        self.checkBox_download_only = QCheckBox(self.groupBox_5)
        self.checkBox_download_only.setObjectName("checkBox_download_only")

        self.gridLayout_4.addWidget(self.checkBox_download_only, 0, 1, 1, 1)

        self.checkBox_local_first = QCheckBox(self.groupBox_5)
        self.checkBox_local_first.setObjectName("checkBox_local_first")

        self.gridLayout_4.addWidget(self.checkBox_local_first, 5, 1, 1, 1)

        self.checkBox_dry_run = QCheckBox(self.groupBox_5)
        self.checkBox_dry_run.setObjectName("checkBox_dry_run")

        self.gridLayout_4.addWidget(self.checkBox_dry_run, 2, 2, 1, 1)

        self.checkBox_disable_upload_validation = QCheckBox(self.groupBox_5)
        self.checkBox_disable_upload_validation.setObjectName("checkBox_disable_upload_validation")

        self.gridLayout_4.addWidget(self.checkBox_disable_upload_validation, 3, 1, 1, 1)

        self.checkBox_bypass_data_preservation = QCheckBox(self.groupBox_5)
        self.checkBox_bypass_data_preservation.setObjectName("checkBox_bypass_data_preservation")

        self.gridLayout_4.addWidget(self.checkBox_bypass_data_preservation, 5, 2, 1, 1)

        self.checkBox_no_remote_delete = QCheckBox(self.groupBox_5)
        self.checkBox_no_remote_delete.setObjectName("checkBox_no_remote_delete")

        self.gridLayout_4.addWidget(self.checkBox_no_remote_delete, 0, 2, 1, 1)

        self.checkBox_remove_source_files = QCheckBox(self.groupBox_5)
        self.checkBox_remove_source_files.setObjectName("checkBox_remove_source_files")

        self.gridLayout_4.addWidget(self.checkBox_remove_source_files, 3, 2, 1, 1)

        self.checkBox_upload_only = QCheckBox(self.groupBox_5)
        self.checkBox_upload_only.setObjectName("checkBox_upload_only")

        self.gridLayout_4.addWidget(self.checkBox_upload_only, 1, 1, 1, 1)

        self.checkBox_sync_business_shared_folders = QCheckBox(self.groupBox_5)
        self.checkBox_sync_business_shared_folders.setObjectName("checkBox_sync_business_shared_folders")

        self.gridLayout_4.addWidget(self.checkBox_sync_business_shared_folders, 1, 2, 1, 1)

        self.verticalLayout_8.addWidget(self.groupBox_5)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_4)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_logging = QWidget()
        self.tab_logging.setObjectName("tab_logging")
        self.verticalLayout_6 = QVBoxLayout(self.tab_logging)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox_7 = QGroupBox(self.tab_logging)
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.checkBox_enable_logging = QCheckBox(self.groupBox_7)
        self.checkBox_enable_logging.setObjectName("checkBox_enable_logging")

        self.gridLayout_8.addWidget(self.checkBox_enable_logging, 0, 0, 1, 1)

        self.label_log_dir = QLabel(self.groupBox_7)
        self.label_log_dir.setObjectName("label_log_dir")

        self.gridLayout_8.addWidget(self.label_log_dir, 1, 0, 1, 1)

        self.checkBox_debug_https = QCheckBox(self.groupBox_7)
        self.checkBox_debug_https.setObjectName("checkBox_debug_https")

        self.gridLayout_8.addWidget(self.checkBox_debug_https, 4, 0, 1, 1)

        self.lineEdit_log_dir = QLineEdit(self.groupBox_7)
        self.lineEdit_log_dir.setObjectName("lineEdit_log_dir")

        self.gridLayout_8.addWidget(self.lineEdit_log_dir, 1, 1, 1, 1)

        self.pushButton_log_dir_browse = QPushButton(self.groupBox_7)
        self.pushButton_log_dir_browse.setObjectName("pushButton_log_dir_browse")

        self.gridLayout_8.addWidget(self.pushButton_log_dir_browse, 1, 2, 1, 1)

        self.label_monitor_log_frequency = QLabel(self.groupBox_7)
        self.label_monitor_log_frequency.setObjectName("label_monitor_log_frequency")

        self.gridLayout_8.addWidget(self.label_monitor_log_frequency, 3, 0, 1, 1)

        self.spinBox_monitor_log_frequency = QSpinBox(self.groupBox_7)
        self.spinBox_monitor_log_frequency.setObjectName("spinBox_monitor_log_frequency")

        self.gridLayout_8.addWidget(self.spinBox_monitor_log_frequency, 3, 1, 1, 1)

        self.verticalLayout_9.addLayout(self.gridLayout_8)

        self.verticalLayout_6.addWidget(self.groupBox_7)

        self.groupBox_6 = QGroupBox(self.tab_logging)
        self.groupBox_6.setObjectName("groupBox_6")
        self.formLayout_3 = QFormLayout(self.groupBox_6)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_min_notify_changes = QLabel(self.groupBox_6)
        self.label_min_notify_changes.setObjectName("label_min_notify_changes")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_min_notify_changes)

        self.spinBox_min_notify_changes = QSpinBox(self.groupBox_6)
        self.spinBox_min_notify_changes.setObjectName("spinBox_min_notify_changes")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.spinBox_min_notify_changes)

        self.checkBox_disable_notifications = QCheckBox(self.groupBox_6)
        self.checkBox_disable_notifications.setObjectName("checkBox_disable_notifications")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.checkBox_disable_notifications)

        self.verticalLayout_6.addWidget(self.groupBox_6)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.tabWidget.addTab(self.tab_logging, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout = QGridLayout(self.tab_5)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_9 = QGroupBox(self.tab_5)
        self.groupBox_9.setObjectName("groupBox_9")
        self.formLayout_2 = QFormLayout(self.groupBox_9)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_webhook_public_url = QLabel(self.groupBox_9)
        self.label_webhook_public_url.setObjectName("label_webhook_public_url")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_webhook_public_url)

        self.lineEdit_webhook_public_url = QLineEdit(self.groupBox_9)
        self.lineEdit_webhook_public_url.setObjectName("lineEdit_webhook_public_url")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lineEdit_webhook_public_url)

        self.label_webhook_listening_host = QLabel(self.groupBox_9)
        self.label_webhook_listening_host.setObjectName("label_webhook_listening_host")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_webhook_listening_host)

        self.lineEdit_webhook_listening_host = QLineEdit(self.groupBox_9)
        self.lineEdit_webhook_listening_host.setObjectName("lineEdit_webhook_listening_host")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.lineEdit_webhook_listening_host)

        self.label_webhook_listening_port = QLabel(self.groupBox_9)
        self.label_webhook_listening_port.setObjectName("label_webhook_listening_port")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_webhook_listening_port)

        self.spinBox_webhook_listening_port = QSpinBox(self.groupBox_9)
        self.spinBox_webhook_listening_port.setObjectName("spinBox_webhook_listening_port")
        self.spinBox_webhook_listening_port.setMinimum(1)
        self.spinBox_webhook_listening_port.setMaximum(65353)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.spinBox_webhook_listening_port)

        self.label_webhook_expiration_interval = QLabel(self.groupBox_9)
        self.label_webhook_expiration_interval.setObjectName("label_webhook_expiration_interval")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_webhook_expiration_interval)

        self.spinBox_webhook_expiration_interval = QSpinBox(self.groupBox_9)
        self.spinBox_webhook_expiration_interval.setObjectName("spinBox_webhook_expiration_interval")
        self.spinBox_webhook_expiration_interval.setMaximum(1000000)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.spinBox_webhook_expiration_interval)

        self.label_webhook_renewal_interval = QLabel(self.groupBox_9)
        self.label_webhook_renewal_interval.setObjectName("label_webhook_renewal_interval")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_webhook_renewal_interval)

        self.spinBox_webhook_renewal_interval = QSpinBox(self.groupBox_9)
        self.spinBox_webhook_renewal_interval.setObjectName("spinBox_webhook_renewal_interval")
        self.spinBox_webhook_renewal_interval.setMaximum(1000000)

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.spinBox_webhook_renewal_interval)

        self.checkBox_webhook_enabled = QCheckBox(self.groupBox_9)
        self.checkBox_webhook_enabled.setObjectName("checkBox_webhook_enabled")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.checkBox_webhook_enabled)

        self.gridLayout.addWidget(self.groupBox_9, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName("tab_6")
        self.verticalLayout = QVBoxLayout(self.tab_6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_auto_sync = QCheckBox(self.tab_6)
        self.checkBox_auto_sync.setObjectName("checkBox_auto_sync")

        self.verticalLayout.addWidget(self.checkBox_auto_sync)

        self.pushButton_logout = QPushButton(self.tab_6)
        self.pushButton_logout.setObjectName("pushButton_logout")

        self.verticalLayout.addWidget(self.pushButton_logout)

        self.pushButton_login = QPushButton(self.tab_6)
        self.pushButton_login.setObjectName("pushButton_login")

        self.verticalLayout.addWidget(self.pushButton_login)

        self.tabWidget.addTab(self.tab_6, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.pushButton_discart = QPushButton(profile_settings)
        self.pushButton_discart.setObjectName("pushButton_discart")

        self.verticalLayout_2.addWidget(self.pushButton_discart)

        self.pushButton_save = QPushButton(profile_settings)
        self.pushButton_save.setObjectName("pushButton_save")

        self.verticalLayout_2.addWidget(self.pushButton_save)

        self.retranslateUi(profile_settings)

        self.tabWidget.setCurrentIndex(5)

        QMetaObject.connectSlotsByName(profile_settings)

    # setupUi

    def retranslateUi(self, profile_settings):
        profile_settings.setWindowTitle(
            QCoreApplication.translate("profile_settings", "OneDriveGUI - Profile Settings", None)
        )
        self.label_profile_name.setText(QCoreApplication.translate("profile_settings", "Profile name", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("profile_settings", "Monitored directory", None))
        self.pushButton_sync_dir_browse.setText(QCoreApplication.translate("profile_settings", "Browse", None))
        self.label_sync_dir.setText(QCoreApplication.translate("profile_settings", "Sync Folder:", None))
        self.checkBox_sync_root_files.setText(QCoreApplication.translate("profile_settings", "Sync root files", None))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.exemptions_tab_2),
            QCoreApplication.translate("profile_settings", "Monitored Files", None),
        )
        self.groupBox.setTitle(QCoreApplication.translate("profile_settings", "Excluded files", None))
        self.pushButton_add_skip_file.setText(QCoreApplication.translate("profile_settings", "Add", None))
        self.pushButton_rm_skip_file.setText(QCoreApplication.translate("profile_settings", "Remove", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("profile_settings", "Excluded directories", None))
        self.checkBox_skip_dir_strict_match.setText(
            QCoreApplication.translate("profile_settings", "Strict match", None)
        )
        self.pushButton_rm_skip_dir.setText(QCoreApplication.translate("profile_settings", "Remove", None))
        self.pushButton_add_skip_dir.setText(QCoreApplication.translate("profile_settings", "Add", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("profile_settings", "Others", None))
        self.checkBox_skip_symlinks.setText(QCoreApplication.translate("profile_settings", "Exclude symlinks", None))
        self.checkBox_check_nosync.setText(QCoreApplication.translate("profile_settings", "Check for .nosync", None))
        self.checkBox_skip_dotfiles.setText(
            QCoreApplication.translate("profile_settings", "Exclude dotfiles (hidden files)", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab), QCoreApplication.translate("profile_settings", "Excluded files", None)
        )
        self.groupBox_10.setTitle(QCoreApplication.translate("profile_settings", "Account Rate Limit", None))
        self.label_rate_limit.setText(QCoreApplication.translate("profile_settings", "Rate Limit [B/s]", None))
        self.label_rate_limit_mbps.setText(QCoreApplication.translate("profile_settings", "(Mibit/s)", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("profile_settings", "Advanced Properties", None))
        self.label_monitor_interval.setText(QCoreApplication.translate("profile_settings", "Monitor interval", None))
        self.label_monitor_fullscan_frequency.setText(
            QCoreApplication.translate("profile_settings", "Monitor full-scan frequency", None)
        )
        self.label_classify_as_big_delete.setText(
            QCoreApplication.translate("profile_settings", "Clasify as big delete", None)
        )
        self.label_user_agent.setText(QCoreApplication.translate("profile_settings", "User-agent", None))
        self.label_azure_ad_endpoint.setText(QCoreApplication.translate("profile_settings", "Azure AD endpoint", None))
        self.label_azure_tenant_id.setText(QCoreApplication.translate("profile_settings", "Azure tenant ID", None))
        self.label_sync_dir_permissions.setText(
            QCoreApplication.translate("profile_settings", "Sync dir permissions", None)
        )
        self.label_sync_file_permissions.setText(
            QCoreApplication.translate("profile_settings", "Sync file permissions", None)
        )
        self.label_operation_timeout.setText(QCoreApplication.translate("profile_settings", "Operation timeout", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("profile_settings", "Advanced options", None))
        self.checkBox_force_http_11.setText(QCoreApplication.translate("profile_settings", "Force HTTP 1.1", None))
        self.checkBox_check_nomount.setText(QCoreApplication.translate("profile_settings", "Check for .nomount", None))
        self.checkBox_resync.setText(QCoreApplication.translate("profile_settings", "Full re-sync", None))
        self.checkBox_download_only.setText(QCoreApplication.translate("profile_settings", "Download only", None))
        self.checkBox_local_first.setText(QCoreApplication.translate("profile_settings", "Local first", None))
        self.checkBox_dry_run.setText(QCoreApplication.translate("profile_settings", "Dry run", None))
        self.checkBox_disable_upload_validation.setText(
            QCoreApplication.translate("profile_settings", "Disable upload validation", None)
        )
        self.checkBox_bypass_data_preservation.setText(
            QCoreApplication.translate("profile_settings", "Bypass data preservation", None)
        )
        self.checkBox_no_remote_delete.setText(
            QCoreApplication.translate("profile_settings", "No remote delete", None)
        )
        self.checkBox_remove_source_files.setText(
            QCoreApplication.translate("profile_settings", "Remove source files", None)
        )
        self.checkBox_upload_only.setText(QCoreApplication.translate("profile_settings", "Upload only", None))
        self.checkBox_sync_business_shared_folders.setText(
            QCoreApplication.translate("profile_settings", "Sync business shared folders", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("profile_settings", "Sync Options", None)
        )
        self.groupBox_7.setTitle(QCoreApplication.translate("profile_settings", "Logging", None))
        self.checkBox_enable_logging.setText(QCoreApplication.translate("profile_settings", "Enable Logging", None))
        self.label_log_dir.setText(QCoreApplication.translate("profile_settings", "Log location:", None))
        self.checkBox_debug_https.setText(QCoreApplication.translate("profile_settings", "Debug HTTPS", None))
        self.pushButton_log_dir_browse.setText(QCoreApplication.translate("profile_settings", "Browse", None))
        self.label_monitor_log_frequency.setText(
            QCoreApplication.translate("profile_settings", "Monitor log frequency", None)
        )
        self.groupBox_6.setTitle(QCoreApplication.translate("profile_settings", "Notifications", None))
        self.label_min_notify_changes.setText(
            QCoreApplication.translate("profile_settings", "Minimum notify changes", None)
        )
        self.checkBox_disable_notifications.setText(
            QCoreApplication.translate("profile_settings", "Disable notifications", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_logging), QCoreApplication.translate("profile_settings", "Logging", None)
        )
        self.groupBox_9.setTitle(QCoreApplication.translate("profile_settings", "Webhook settings", None))
        self.label_webhook_public_url.setText(QCoreApplication.translate("profile_settings", "Public URL", None))
        self.label_webhook_listening_host.setText(
            QCoreApplication.translate("profile_settings", "Listening host", None)
        )
        self.label_webhook_listening_port.setText(
            QCoreApplication.translate("profile_settings", "Listening port", None)
        )
        self.label_webhook_expiration_interval.setText(
            QCoreApplication.translate("profile_settings", "Expiration interval", None)
        )
        self.label_webhook_renewal_interval.setText(
            QCoreApplication.translate("profile_settings", "Renewal interval", None)
        )
        self.checkBox_webhook_enabled.setText(QCoreApplication.translate("profile_settings", "Enable webhook", None))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("profile_settings", "Webhooks", None)
        )
        self.checkBox_auto_sync.setText(QCoreApplication.translate("profile_settings", "Auto-sync on startup", None))
        self.pushButton_logout.setText(QCoreApplication.translate("profile_settings", "Logout", None))
        self.pushButton_login.setText(QCoreApplication.translate("profile_settings", "Login", None))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("profile_settings", "Account", None)
        )
        self.pushButton_discart.setText(QCoreApplication.translate("profile_settings", "Discard changes", None))
        self.pushButton_save.setText(QCoreApplication.translate("profile_settings", "Save", None))

    # retranslateUi
