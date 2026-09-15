# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_new_profile.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_create_new_profile(object):
    def setupUi(self, create_new_profile):
        if not create_new_profile.objectName():
            create_new_profile.setObjectName(u"create_new_profile")
        create_new_profile.resize(578, 129)
        self.gridLayout = QGridLayout(create_new_profile)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(create_new_profile)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)

        self.label_new_profile_name = QLabel(create_new_profile)
        self.label_new_profile_name.setObjectName(u"label_new_profile_name")

        self.gridLayout.addWidget(self.label_new_profile_name, 0, 0, 1, 1)

        self.pushButton_create = QPushButton(create_new_profile)
        self.pushButton_create.setObjectName(u"pushButton_create")

        self.gridLayout.addWidget(self.pushButton_create, 2, 0, 1, 3)

        self.lineEdit_new_profile_name = QLineEdit(create_new_profile)
        self.lineEdit_new_profile_name.setObjectName(u"lineEdit_new_profile_name")

        self.gridLayout.addWidget(self.lineEdit_new_profile_name, 0, 1, 1, 1)

        self.label_sync_dir = QLabel(create_new_profile)
        self.label_sync_dir.setObjectName(u"label_sync_dir")

        self.gridLayout.addWidget(self.label_sync_dir, 1, 0, 1, 1)

        self.lineEdit_sync_dir = QLineEdit(create_new_profile)
        self.lineEdit_sync_dir.setObjectName(u"lineEdit_sync_dir")

        self.gridLayout.addWidget(self.lineEdit_sync_dir, 1, 1, 1, 1)

        self.label_3 = QLabel(create_new_profile)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)


        self.retranslateUi(create_new_profile)

        QMetaObject.connectSlotsByName(create_new_profile)
    # setupUi

    def retranslateUi(self, create_new_profile):
        create_new_profile.setWindowTitle(QCoreApplication.translate("create_new_profile", u"Create new profile", None))
        self.label.setText(QCoreApplication.translate("create_new_profile", u"E.g. john@live.com", None))
        self.label_new_profile_name.setText(QCoreApplication.translate("create_new_profile", u"New profile name", None))
        self.pushButton_create.setText(QCoreApplication.translate("create_new_profile", u"Create new profile", None))
        self.label_sync_dir.setText(QCoreApplication.translate("create_new_profile", u"Sync directory", None))
        self.label_3.setText(QCoreApplication.translate("create_new_profile", u"E.g. ~/OneDrive_john@live.com/", None))
    # retranslateUi

