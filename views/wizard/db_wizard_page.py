from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QTextDocument
from PySide6.QtSql import QSqlDatabase
from PySide6.QtWidgets import QWizardPage, QComboBox, QLabel, QPushButton, QGroupBox, QProgressBar, QGridLayout, \
    QSpinBox, QCommandLinkButton, QVBoxLayout, QTextEdit, QFrame, QHBoxLayout, QFormLayout
from components import LineEdit

import qtawesome as qta

class DatabaseConfigWizardPage(QWizardPage):
    def __init__(self):
        super(DatabaseConfigWizardPage, self).__init__()

        self.drivers = QSqlDatabase.drivers()

        self.drivers_combo = QComboBox()
        self.drivers_combo.addItems(self.drivers)

        self.status_lbl = QLabel()
        self.message_edit = QTextEdit()

        self.db_name_edit = LineEdit("DB name:", "database name", orientation=Qt.Orientation.Horizontal)

        self.host_edit = LineEdit("Host", "127.0.0.1")
        self.port_spin = QSpinBox()

        self.user_edit = LineEdit("DB User", "database user")
        self.password_edit = LineEdit("Password", "password")

        self.test_btn = QPushButton("Test Connection")
        self.seed_btn = QPushButton("Seed Database")

        self.progress_monitor = QProgressBar()

        # self.db_config_group = QGroupBox("Initial Config")
        # initial_config_layout = QGridLayout(self.db_config_group)
        # initial_config_layout.addWidget(self.drivers_combo, 0, 0)
        # initial_config_layout.addWidget(self.status_lbl, 0, 1)
        # initial_config_layout.addWidget(self.db_name_edit, 1, 0, 1, 2)
        # initial_config_layout.addWidget(self.host_edit, 2, 0)
        # initial_config_layout.addWidget(self.port_edit, 2, 1)
        # initial_config_layout.addWidget(self.user_edit, 3, 0)
        # initial_config_layout.addWidget(self.password_edit, 3, 1)
        # initial_config_layout.addWidget(self.test_btn, 5, 0)
        # initial_config_layout.addWidget(self.load_sql_btn, 5, 1)
        # initial_config_layout.addWidget(self.progress_monitor, 4, 0, 1, 2)
        #
        # self.backup_config_group = QGroupBox("Backup Config")
        # backup_config_layout = QGridLayout(self.backup_config_group)

        # self.backup_method_combo = QComboBox()
        # self.backup_method_combo.addItems(["Manual", "Automatic"])
        # self.frequency_spin = QSpinBox()
        # self.frequency_spin.setPrefix("Backup Frequency")
        # self.frequency_spin.setSuffix("Days")
        # self.backup_path_edit = LineEdit("Backup Path", "C://path/to/backup")
        # self.file_browser_btn = QCommandLinkButton("Choose File")
        # self.backup_btn = QPushButton("Backup")

        # backup_config_layout.addWidget(self.backup_method_combo, 0, 0)
        # backup_config_layout.addWidget(self.frequency_spin, 0, 1)
        # backup_config_layout.addWidget(self.file_browser_btn, 1, 0)
        # backup_config_layout.addWidget(self.backup_path_edit, 1, 1)
        # backup_config_layout.addWidget(self.backup_btn, 2, 0)

        database_icon_lbl = QLabel()
        database_icon_lbl.setScaledContents(True)
        database_icon_lbl.setFixedSize(QSize(200, 200))
        database_icon_lbl.setPixmap(qta.icon("database", color="#0598a8").pixmap(512))

        self.side_frame = QFrame()
        side_frame_layout = QVBoxLayout(self.side_frame)
        side_frame_layout.addWidget(database_icon_lbl)
        side_frame_layout.addStretch()

        config_form_layout = QFormLayout()
        config_form_layout.addWidget()

        layout = QHBoxLayout(self)
        layout.addWidget(self.side_frame)
        layout.addLayout(config_form_layout)
        layout.addWidget(self.db_config_group)
        layout.addWidget(self.backup_config_group)