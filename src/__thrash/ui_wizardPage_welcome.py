# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wizardPage_welcome.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget,
    QWizardPage)

class Ui_WizardPage(object):
    def setupUi(self, WizardPage):
        if not WizardPage.objectName():
            WizardPage.setObjectName(u"WizardPage")
        WizardPage.resize(628, 420)
        self.label = QLabel(WizardPage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(230, 160, 271, 18))
        self.label_2 = QLabel(WizardPage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 280, 441, 20))

        self.retranslateUi(WizardPage)

        QMetaObject.connectSlotsByName(WizardPage)
    # setupUi

    def retranslateUi(self, WizardPage):
        WizardPage.setWindowTitle(QCoreApplication.translate("WizardPage", u"WizardPage", None))
        self.label.setText(QCoreApplication.translate("WizardPage", u"Welcome to OneDriveGUI", None))
        self.label_2.setText(QCoreApplication.translate("WizardPage", u"This wizard will help you with initial OneDrive profile creation/import.", None))
    # retranslateUi

