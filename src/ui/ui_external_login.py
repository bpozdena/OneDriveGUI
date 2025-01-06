# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'external_login.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_ExternalLoginWindow(object):
    def setupUi(self, ExternalLoginWindow):
        if not ExternalLoginWindow.objectName():
            ExternalLoginWindow.setObjectName(u"ExternalLoginWindow")
        ExternalLoginWindow.resize(783, 321)
        self.verticalLayout = QVBoxLayout(ExternalLoginWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.layout_external_login = QVBoxLayout()
        self.layout_external_login.setObjectName(u"layout_external_login")
        self.label_1 = QLabel(ExternalLoginWindow)
        self.label_1.setObjectName(u"label_1")

        self.layout_external_login.addWidget(self.label_1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.layout_external_login.addItem(self.verticalSpacer_2)

        self.label_2 = QLabel(ExternalLoginWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"")

        self.layout_external_login.addWidget(self.label_2)

        self.lineEdit_response_url = QLineEdit(ExternalLoginWindow)
        self.lineEdit_response_url.setObjectName(u"lineEdit_response_url")

        self.layout_external_login.addWidget(self.lineEdit_response_url)

        self.pushButton_login = QPushButton(ExternalLoginWindow)
        self.pushButton_login.setObjectName(u"pushButton_login")

        self.layout_external_login.addWidget(self.pushButton_login)


        self.verticalLayout.addLayout(self.layout_external_login)


        self.retranslateUi(ExternalLoginWindow)

        QMetaObject.connectSlotsByName(ExternalLoginWindow)
    # setupUi

    def retranslateUi(self, ExternalLoginWindow):
        ExternalLoginWindow.setWindowTitle(QCoreApplication.translate("ExternalLoginWindow", u"Form", None))
        self.label_1.setText(QCoreApplication.translate("ExternalLoginWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700; text-decoration: underline;\">OneDrive login has been requested</span></p><p>You will be asked to open a specific URL by using your web browser where you will have to login into your Microsoft Account and give <br/>OneDrive client the permission to access your files. </p><p>After giving permission to OneDrive client, you will be redirected to a blank page. Copy the URI of the blank page into the below field.</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("ExternalLoginWindow", u"<html><head/><body><p>1) Login to OneDrive in your browser by <a href=\"https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=d50ca740-c83f-4d1b-b616-12c519384f0c&amp;scope=Files.ReadWrite%20Files.ReadWrite.all%20Sites.Read.All%20Sites.ReadWrite.All%20offline_access&amp;response_type=code&amp;prompt=login&amp;redirect_uri=https://login.microsoftonline.com/common/oauth2/nativeclient\"><span style=\" text-decoration: underline; color:#5e81ac;\">clicking this link.</span></a></p><p>2) Copy the response URI from your browser's address bar into the below field. </p><p>3) Press Save.</p></body></html>", None))
        self.pushButton_login.setText(QCoreApplication.translate("ExternalLoginWindow", u"Save", None))
    # retranslateUi

