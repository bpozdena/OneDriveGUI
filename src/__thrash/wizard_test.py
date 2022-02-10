from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import Property, Qt
from PySide6.QtWidgets import (
    QWizard,
    QGridLayout,
    QLineEdit,
    QWizardPage,
    QLabel,
    QVBoxLayout,
    QComboBox,
    QApplication,
)


class QIComboBox(QComboBox):
    def __init__(self, parent=None):
        super(QIComboBox, self).__init__(parent)


class MagicWizard(QWizard):
    def __init__(self, parent=None):
        super(MagicWizard, self).__init__(parent)
        self.addPage(WizardPage_welcome(self))
        self.addPage(wizardPage_version_check(self))
        self.setWindowTitle("OneDriveGUI Setup Wizard")
        self.resize(640, 480)
        self.setWindowIcon(QIcon("resources/images/icons8-clouds-48.png"))


class WizardPage_welcome(QWizardPage):
    def __init__(self, parent=None):
        super(WizardPage_welcome, self).__init__(parent)
        self.setTitle("Welcome to OneDriveGUI")
        # self.setSubTitle("SubTitle")

        # self.label1 = QLabel()
        # self.label1.setText("Welcome to OneDriveGUI")

        self.label_2 = QLabel()
        self.label_2.setText("This wizard will help you with initial OneDrive profile creation/import.")

        layout = QVBoxLayout()
        # layout.addWidget(self.label1)
        layout.addWidget(self.label_2)
        self.setLayout(layout)


class wizardPage_version_check(QWizardPage):
    def __init__(self, parent=None):
        super(wizardPage_version_check, self).__init__(parent)
        self.setTitle("OneDrive version check")

        # self.label_3 = QLabel()
        # self.label_3.setText("Installed OneDrive version:")

        self.label_4 = QLabel()
        self.label_4.setText("Installed/Not Installed/ version")

        self.label_5 = QLabel()
        self.label_5.setWordWrap(True)
        self.label_5.setText(
            "OneDrive Client for Linux does not seem to be installed. Please install it by following " \
            "<a href='https://github.com/abraunegg/onedrive/blob/master/docs/INSTALL.md'>instructions</a> for your distro. "
        )

        layout = QVBoxLayout()
        # layout.addWidget(self.label_3)
        layout.addWidget(self.label_4)
        layout.addWidget(self.label_5)
        self.setLayout(layout)




if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    wizard = MagicWizard()
    wizard.show()
    sys.exit(app.exec_())
