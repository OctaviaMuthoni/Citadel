import qtawesome as qta
from PySide6.QtCore import QSize, Signal, Qt
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtSql import QSqlDatabase
from PySide6.QtWidgets import QHBoxLayout, QLabel, QFormLayout, QPushButton, QTabWidget, QGridLayout, QWidget, \
    QTextEdit, QGroupBox, QComboBox, QProgressBar, QSpinBox, QCommandLinkButton

from ui.widgets import ImageComponent, LineEdit
from core.settings import Settings


class ApplicationSettingsView(QWidget):
    settingsChanged = Signal(str, str)

    def __init__(self):
        super(ApplicationSettingsView, self).__init__()

        self.settings = Settings()

        layout = QGridLayout(self)

        self.logo_upload = ImageComponent(self.settings.get_settings('logo', ""))
        self.slogan_textedit = QTextEdit()
        self.slogan_textedit.setText(self.settings.get_settings('slogan', ""))
        self.institution_edit = LineEdit("Institution", "institution")
        self.institution_edit.set_text(self.settings.get_settings('institution', ""))

        self.save_btn = QPushButton("Save")
        self.save_btn.clicked.connect(self.save_settings)

        layout.addWidget(self.logo_upload, 0, 0)
        layout.addWidget(self.institution_edit, 0, 1)
        layout.addWidget(self.slogan_textedit, 1, 1)
        layout.addWidget(self.save_btn)

    def save_settings(self):
        s = dict()
        s['institutions'] = self.institution_edit.text()
        s['slogan'] = self.slogan_textedit.document().toPlainText()
        # self.settings['logo'] = self.logo_upload.
        for k, v in s.items():
            self.settings.edit_settings(k, v)

    # def load_settings(self):
    #     self.settings["institution"] = self.current_settings.get_settings("institution")
    #     self.settings["slogan"] = self.current_settings.get_settings("slogan", "slogan")
    #     self.settings["logo"] = self.current_settings.get_settings("logo", "slogan")


class UserManagementSettings(QWidget):
    def __init__(self):
        super(UserManagementSettings, self).__init__()


class DatabaseSettingsView(QWidget):
    def __init__(self):
        super(DatabaseSettingsView, self).__init__()

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

        layout = QHBoxLayout(self)
        layout.addWidget(self.db_config_group)
        layout.addWidget(self.backup_config_group)


class SettingsView(QWidget):
    def __init__(self):
        super(SettingsView, self).__init__()

        layout = QGridLayout(self)
        logo_lbl = QLabel()
        logo_lbl.setFixedSize(120, 120)
        logo_lbl.setScaledContents(True)
        logo_lbl.setPixmap(QPixmap("resources/images/falcon.png"))

        application_settings_view = ApplicationSettingsView()
        database_config_view = DatabaseSettingsView()

        settings_tabs = QTabWidget()
        # settings_tabs.setTabPosition(QTabWidget.TabPosition.West)
        settings_tabs.setIconSize(QSize(25, 25))
        settings_tabs.setFont(QFont("Arial", 12))
        settings_tabs.addTab(application_settings_view, qta.icon("ph.windows-logo-fill"), "Application")
        settings_tabs.addTab(QLabel("User"), qta.icon("ph.user-gear-light"), "User")
        settings_tabs.addTab(database_config_view, qta.icon("ph.database"), "Database")
        settings_tabs.addTab(QLabel("printer"), qta.icon("ph.printer-light"), "Printer")

        self.download_btn = QPushButton()
        self.download_btn.setIcon(qta.icon("ph.download-light", color="blue"))
        self.download_btn.setIconSize(QSize(25, 25))

        self.print_btn = QPushButton()
        self.print_btn.setIcon(qta.icon("ph.printer-light", color="maroon"))
        self.print_btn.setIconSize(QSize(25, 25))

        self.save_btn = QPushButton("Save")
        self.save_btn.setIcon(qta.icon("ri.save-line"))

        options_layout = QHBoxLayout()
        options_layout.addStretch()
        options_layout.addWidget(self.save_btn)

        brand_name = QLabel("Admin Settings Panel")
        brand_name.setObjectName("sbrand")
        details = QFormLayout()
        details.addRow(brand_name)
        details.addWidget(QLabel("Last Review: 12/12/2023"))
        details.addWidget(QLabel("Overseen By: George. B. Oguta"))

        layout.addWidget(logo_lbl, 0, 0)
        layout.addLayout(details, 0, 1)
        layout.addWidget(settings_tabs, 1, 0, 1, 2)
        layout.addLayout(options_layout, 2, 0, 1, 2)
