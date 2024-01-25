from PySide6.QtWidgets import QApplication, QWizard, QWizardPage, QVBoxLayout, QLabel, QLineEdit

class ConfigPage(QWizardPage):
    def __init__(self):
        super(ConfigPage, self).__init__()

        layout = QVBoxLayout()

        self.database_label = QLabel("Database Name:")
        self.database_edit = QLineEdit()

        layout.addWidget(self.database_label)
        layout.addWidget(self.database_edit)

        self.setLayout(layout)

class InstallWizard(QWizard):
    def __init__(self):
        super(InstallWizard, self).__init__()

        self.addPage(ConfigPage())
        self.setWindowTitle("Installation Wizard")

if __name__ == "__main__":
    app = QApplication([])

    wizard = InstallWizard()
    wizard.show()

    app.exec()
