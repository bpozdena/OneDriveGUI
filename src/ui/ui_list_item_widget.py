# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'list_item_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QProgressBar,
    QSizePolicy, QToolButton, QWidget)

class Ui_list_item_widget(object):
    def setupUi(self, list_item_widget):
        if not list_item_widget.objectName():
            list_item_widget.setObjectName(u"list_item_widget")
        list_item_widget.resize(426, 60)
        list_item_widget.setMinimumSize(QSize(50, 60))
        self.gridLayout = QGridLayout(list_item_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(2)
        self.gridLayout.setContentsMargins(5, 4, 2, 4)
        self.toolButton = QToolButton(list_item_widget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setEnabled(True)
        self.toolButton.setMinimumSize(QSize(0, 0))
        self.toolButton.setAutoFillBackground(False)
        icon = QIcon()
        icon.addFile(u"../resources/images/icons8-clouds-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QSize(30, 40))

        self.gridLayout.addWidget(self.toolButton, 0, 0, 5, 1)

        self.ls_label_file_name = QLabel(list_item_widget)
        self.ls_label_file_name.setObjectName(u"ls_label_file_name")
        self.ls_label_file_name.setMaximumSize(QSize(340, 16777215))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.ls_label_file_name.setFont(font)

        self.gridLayout.addWidget(self.ls_label_file_name, 0, 1, 1, 2)

        self.ls_label_2 = QLabel(list_item_widget)
        self.ls_label_2.setObjectName(u"ls_label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ls_label_2.sizePolicy().hasHeightForWidth())
        self.ls_label_2.setSizePolicy(sizePolicy)
        self.ls_label_2.setMaximumSize(QSize(170, 16777215))
        self.ls_label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.ls_label_2, 2, 2, 2, 1)

        self.ls_label_1 = QLabel(list_item_widget)
        self.ls_label_1.setObjectName(u"ls_label_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ls_label_1.sizePolicy().hasHeightForWidth())
        self.ls_label_1.setSizePolicy(sizePolicy1)
        self.ls_label_1.setMaximumSize(QSize(290, 16777215))

        self.gridLayout.addWidget(self.ls_label_1, 2, 1, 2, 1)

        self.ls_progressBar = QProgressBar(list_item_widget)
        self.ls_progressBar.setObjectName(u"ls_progressBar")
        self.ls_progressBar.setMaximumSize(QSize(16777215, 5))
        self.ls_progressBar.setValue(24)
        self.ls_progressBar.setTextVisible(False)

        self.gridLayout.addWidget(self.ls_progressBar, 1, 1, 1, 2)


        self.retranslateUi(list_item_widget)

        QMetaObject.connectSlotsByName(list_item_widget)
    # setupUi

    def retranslateUi(self, list_item_widget):
        list_item_widget.setWindowTitle(QCoreApplication.translate("list_item_widget", u"Form", None))
        self.toolButton.setText(QCoreApplication.translate("list_item_widget", u"...", None))
        self.ls_label_file_name.setText(QCoreApplication.translate("list_item_widget", u"FileName", None))
        self.ls_label_2.setText(QCoreApplication.translate("list_item_widget", u"9960KB of 9100KB", None))
        self.ls_label_1.setText(QCoreApplication.translate("list_item_widget", u"Downloading/Uploading ", None))
    # retranslateUi

