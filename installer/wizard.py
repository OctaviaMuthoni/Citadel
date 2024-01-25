from PySide6.QtCore import Qt, QSize
from PySide6.QtSql import QSqlDatabase
from PySide6.QtWidgets import QApplication, QWizard, QWizardPage, QVBoxLayout, QLabel, QLineEdit, QComboBox, \
    QPushButton, QGroupBox, QGridLayout, QProgressBar, QCommandLinkButton, QSpinBox, QHBoxLayout, QTextEdit, QFrame

from components import LineEdit, ImageComponent, ButtonsWidget, PushButton
from core import STYLES_PATH
from src.settings import Settings


class DatabaseConfig(QWizardPage):
    def __init__(self):
        super(DatabaseConfig, self).__init__()

        self.drivers = QSqlDatabase.drivers()

        self.drivers_combo = QComboBox()
        self.drivers_combo.addItems(self.drivers)

        self.status_lbl = QLabel()

        self.db_name_edit = LineEdit("DB name:", "database name", orientation=Qt.Orientation.Horizontal)
        self.host_edit = LineEdit("Host", "127.0.0.1")
        self.port_edit = LineEdit("Port", "3306")
        self.user_edit = LineEdit("DB User", "database user")
        self.password_edit = LineEdit("Password", "password")
        self.test_btn = QPushButton("Test Connection")
        self.load_sql_btn = QPushButton("Load Sql")
        self.progress_monitor = QProgressBar()

        self.db_config_group = QGroupBox("Initial Config")
        initial_config_layout = QGridLayout(self.db_config_group)
        initial_config_layout.addWidget(self.drivers_combo, 0, 0)
        initial_config_layout.addWidget(self.status_lbl, 0, 1)
        initial_config_layout.addWidget(self.db_name_edit, 1, 0, 1, 2)
        initial_config_layout.addWidget(self.host_edit, 2, 0)
        initial_config_layout.addWidget(self.port_edit, 2, 1)
        initial_config_layout.addWidget(self.user_edit, 3, 0)
        initial_config_layout.addWidget(self.password_edit, 3, 1)
        initial_config_layout.addWidget(self.test_btn, 5, 0)
        initial_config_layout.addWidget(self.load_sql_btn, 5, 1)
        initial_config_layout.addWidget(self.progress_monitor, 4, 0, 1, 2)

        self.backup_config_group = QGroupBox("Backup Config")
        backup_config_layout = QGridLayout(self.backup_config_group)

        self.backup_method_combo = QComboBox()
        self.backup_method_combo.addItems(["Manual", "Automatic"])
        self.frequency_spin = QSpinBox()
        self.frequency_spin.setPrefix("Backup Frequency")
        self.frequency_spin.setSuffix("Days")
        self.backup_path_edit = LineEdit("Backup Path", "C://path/to/backup")
        self.file_browser_btn = QCommandLinkButton("Choose File")
        self.backup_btn = QPushButton("Backup")

        backup_config_layout.addWidget(self.backup_method_combo, 0, 0)
        backup_config_layout.addWidget(self.frequency_spin, 0, 1)
        backup_config_layout.addWidget(self.file_browser_btn, 1, 0)
        backup_config_layout.addWidget(self.backup_path_edit, 1, 1)
        backup_config_layout.addWidget(self.backup_btn, 2, 0)

        layout = QVBoxLayout(self)
        layout.addWidget(self.db_config_group)
        layout.addWidget(self.backup_config_group)


class ApplicationConfig(QWizardPage):
    def __init__(self):
        super(ApplicationConfig, self).__init__()

        self.settings = Settings()

        layout = QVBoxLayout(self)

        basic_info_layout = QGridLayout()
        self.logo_upload = ImageComponent(self.settings.get_settings('logo', ""))
        self.slogan_textedit = QTextEdit()
        self.slogan_textedit.setText(self.settings.get_settings('slogan', ""))
        self.institution_edit = LineEdit("Institution", "institution")
        self.institution_edit.set_text(self.settings.get_settings('institution', ""))

        address_layout = QHBoxLayout()
        # address_layout.addWidget()

        contacts_layout = QHBoxLayout()

        social_layout = QHBoxLayout()

        basic_info_layout.addWidget(self.logo_upload, 0, 0)
        basic_info_layout.addWidget(self.institution_edit, 0, 1)
        basic_info_layout.addWidget(self.slogan_textedit, 1, 1)

        layout.addLayout(basic_info_layout)

        self.completeChanged.connect(lambda: print("completed"))
        print(self.isComplete())

    def save_settings(self):
        s = dict()
        s['institutions'] = self.institution_edit.text()
        s['slogan'] = self.slogan_textedit.document().toPlainText()
        # self.settings['logo'] = self.logo_upload.
        for k, v in s.items():
            self.settings.edit_settings(k, v)


class InstallWizard(QWizard):
    def __init__(self):
        super(InstallWizard, self).__init__()

        self.addPage(ApplicationConfig())
        self.addPage(DatabaseConfig())
        self.setWindowTitle("Citadel Installation Wizard")

        self.setFixedSize(QSize(840, 500))


if __name__ == "__main__":
    app = QApplication([])

    wizard = InstallWizard()
    with open(f"{STYLES_PATH}/styles.qss") as s:
        styles = s.read() + """
            QWizard, QWizardPage {
                background-color: red;
            }
        """
        wizard.setStyleSheet(styles)
    wizard.show()

    app.exec()
