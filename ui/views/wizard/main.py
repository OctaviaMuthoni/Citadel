import sys

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QWizard, QApplication

from .app_wizard_page import ApplicationConfigWizardPage
from .db_wizard_page import DatabaseConfigWizardPage


class ConfigWizard(QWizard):
    def __init__(self):
        super(ConfigWizard, self).__init__()

        self.addPage(ApplicationConfigWizardPage())
        self.addPage(DatabaseConfigWizardPage())
        self.setWindowTitle("Musoni Installation Wizard")

        self.setFixedSize(QSize(840, 500))


# This module can be launched as an independent application when one needs to configure the application after installation.
# Otherwise, it will be lauched if an attempt to lauch application is made before basic configurations are made.
if __name__ == "__main__":
    app = QApplication(sys.argv)
    wizard = ConfigWizard()
    wizard.show()
    sys.exit(app.exec())
