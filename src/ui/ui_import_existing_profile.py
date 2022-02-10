# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'import_existing_profile.ui'
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

class Ui_import_profile(object):
    def setupUi(self, import_profile):
        if not import_profile.objectName():
            import_profile.setObjectName(u"import_profile")
        import_profile.resize(620, 148)
        self.gridLayout = QGridLayout(import_profile)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_profile_name = QLineEdit(import_profile)
        self.lineEdit_profile_name.setObjectName(u"lineEdit_profile_name")

        self.gridLayout.addWidget(self.lineEdit_profile_name, 0, 1, 1, 1)

        self.label_config_path = QLabel(import_profile)
        self.label_config_path.setObjectName(u"label_config_path")
#if QT_CONFIG(tooltip)
        self.label_config_path.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.label_config_path.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_config_path, 1, 0, 1, 1)

        self.label_5 = QLabel(import_profile)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 2, 1, 1)

        self.label_profile_name = QLabel(import_profile)
        self.label_profile_name.setObjectName(u"label_profile_name")
#if QT_CONFIG(tooltip)
        self.label_profile_name.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.label_profile_name.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_profile_name, 0, 0, 1, 1)

        self.lineEdit_config_path = QLineEdit(import_profile)
        self.lineEdit_config_path.setObjectName(u"lineEdit_config_path")

        self.gridLayout.addWidget(self.lineEdit_config_path, 1, 1, 1, 1)

        self.pushButton_import = QPushButton(import_profile)
        self.pushButton_import.setObjectName(u"pushButton_import")

        self.gridLayout.addWidget(self.pushButton_import, 2, 0, 1, 3)

        self.label_4 = QLabel(import_profile)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)


        self.retranslateUi(import_profile)

        QMetaObject.connectSlotsByName(import_profile)
    # setupUi

    def retranslateUi(self, import_profile):
        import_profile.setWindowTitle(QCoreApplication.translate("import_profile", u"Import existing profile", None))
        self.label_config_path.setText(QCoreApplication.translate("import_profile", u"Path to config file", None))
        self.label_5.setText(QCoreApplication.translate("import_profile", u"E.g. ~/.config/onedrive/config", None))
        self.label_profile_name.setText(QCoreApplication.translate("import_profile", u"Profile Name", None))
        self.pushButton_import.setText(QCoreApplication.translate("import_profile", u"Import profile", None))
        self.label_4.setText(QCoreApplication.translate("import_profile", u"E.g. john@live.com", None))
    # retranslateUi

