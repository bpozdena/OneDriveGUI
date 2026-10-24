# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'external_login.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layout_external_login.addItem(self.verticalSpacer_2)

        self.pushButton_browser_login = QPushButton(ExternalLoginWindow)
        self.pushButton_browser_login.setObjectName(u"pushButton_browser_login")

        self.layout_external_login.addWidget(self.pushButton_browser_login)

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
        self.label_1.setText(QCoreApplication.translate("ExternalLoginWindow", u"<html><head/><body><p\n"
"                                    align=\"center\"><span style=\"\n"
"                                    font-weight:700; text-decoration: underline;\">OneDrive\n"
"                                    login has been requested</span></p><p>You will\n"
"                                    be asked to open a specific URL by using your web browser where\n"
"                                    you will have to login into your Microsoft Account and give\n"
"                                    <br/>OneDrive client the permission to access your files.\n"
"                                    </p><p>After giving permission to OneDrive client,\n"
"                                    you will be redirected to a blank page. Copy the URI of the\n"
"                                    blank page into the below\n"
"                                    field.</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.pushButton_browser_login.setToolTip(QCoreApplication.translate("ExternalLoginWindow", u"The OneDrive client opens your default web browser and completes the login automatically - no need to copy anything.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_browser_login.setText(QCoreApplication.translate("ExternalLoginWindow", u"Sign in with web browser", None))
        self.label_2.setText(QCoreApplication.translate("ExternalLoginWindow", u"<html><head/><body><p>1)Login to\n"
"                                    OneDrive in your browser by <a\n"
"                                    href=\"https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=d50ca740-c83f-4d1b-b616-12c519384f0c&amp;scope=Files.ReadWrite%20Files.ReadWrite.all%20Sites.Read.All%20Sites.ReadWrite.All%20offline_access&amp;response_type=code&amp;prompt=login&amp;redirect_uri=https://login.microsoftonline.com/common/oauth2/nativeclient\"><span\n"
"                                    style=\" text-decoration: underline;\n"
"                                    color:#5e81ac;\">clicking this\n"
"                                    link.</span></a></p><p>2)Copy the\n"
"                                    response URI from your browser's address bar to the below field.\n"
"                                    </p><p>3)Press\n"
"                                    Save.</p></body></html>", None))
        self.pushButton_login.setText(QCoreApplication.translate("ExternalLoginWindow", u"Login", None))
    # retranslateUi

