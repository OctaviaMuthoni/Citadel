from PySide6.QtCore import QSize, Qt, Signal, QRect
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QFormLayout, QLineEdit, QVBoxLayout, \
    QFrame

import qtawesome as qta

from components import ButtonsWidget, PushButton
from components.message import Notifier

from models.users import UsersModel
from src import auth


class LoginWindow(QFrame):
    loginSignal = Signal(str)

    def __init__(self, settings):
        super(LoginWindow, self).__init__()

        self.settings = settings
        self.user_model = UsersModel()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        background_lbl = QLabel()
        background_lbl.setScaledContents(True)
        background_lbl.setObjectName("login-background")
        layout.addWidget(background_lbl)

        main_layout = QHBoxLayout(background_lbl)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # side image label
        side_lbl = QLabel()
        side_lbl_layout = QVBoxLayout(side_lbl)

        logo_lbl = QLabel()
        logo_lbl.setFixedSize(QSize(220, 220))
        logo_lbl.setScaledContents(True)
        side_lbl.setFixedWidth(350)
        side_lbl.setObjectName("side_lbl")
        side_img = QPixmap(self.settings.get_settings("logo", "falcon.ico"))
        logo_lbl.setPixmap(side_img)

        email_link_lbl = QLabel("muthonioctavia@gmail.com")
        phone_lbl = QLabel("+254 718 758 807")
        web_link_lbl = QLabel("www.theacademiccitadel.com")

        web_icon_lbl = QLabel()
        web_icon_lbl.setPixmap(qta.icon("ph.globe", color="#0598a8").pixmap(30))
        email_icon_lbl = QLabel()
        email_icon_lbl.setPixmap(qta.icon("ph.envelope", color="maroon").pixmap(30))
        phone_icon_lbl = QLabel()
        phone_icon_lbl.setPixmap(qta.icon("ph.phone", color="green").pixmap(30))

        contacts_form = QFormLayout()
        contacts_form.setVerticalSpacing(0)
        contacts_form.addRow(web_icon_lbl, web_link_lbl)
        contacts_form.addRow(email_icon_lbl, email_link_lbl)
        contacts_form.addRow(phone_icon_lbl, phone_lbl)

        side_lbl_layout.addWidget(logo_lbl)
        side_lbl_layout.addStretch()
        side_lbl_layout.addLayout(contacts_form)
        side_lbl_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.login_btn = PushButton(self.authenticate,
                                    "Login",
                                    qta.icon("ph.lock-key-open", color="#08ADCF"),
                                    PushButton.ButtonType.INFO)

        self.username_edit = QLineEdit()
        self.username_edit.setPlaceholderText("LIB/9/99999")
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)

        btns_widget = ButtonsWidget()
        btns_widget.add_button(self.login_btn)

        title_lbl = QLabel(settings.get_settings("institution", "The Academic Musoni"))
        title_lbl.setObjectName("title-lbl")
        title_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # login form
        login_widget = QWidget()
        login_widget.setObjectName("login-widget")
        login_layout = QVBoxLayout(login_widget)
        login_layout.setSpacing(0)
        form = QFormLayout()
        form.setContentsMargins(100, 0, 100, 100)
        form.setVerticalSpacing(28)
        form.setHorizontalSpacing(15)
        form.addWidget(title_lbl)
        form.addRow("Username:", self.username_edit)
        form.addRow("Password:", self.password_edit)
        form.addWidget(btns_widget)

        self.notifier = Notifier(self)

        login_layout.addWidget(title_lbl)
        login_layout.addWidget(self.notifier)
        login_layout.addLayout(form)

        main_layout.addWidget(side_lbl)
        main_layout.addWidget(login_widget)

        self.setFixedSize(QSize(900, 470))
        self.setObjectName("login")
        self.event_listener()

    def event_listener(self):
        self.username_edit.textChanged.connect(self.username_to_upper)

    def authenticate(self):
        # username = self.username_edit.text()
        # password = self.password_edit.text()
        #
        # user = self.user_model.get_user(username)
        #
        # if user and user.password == auth.hash_password(password):
        #     self.loginSignal.emit(user)
        # else:
        #     self.notifier.configure_notifier("error message")
        self.loginSignal.emit("user")

    def username_to_upper(self, username):
        self.username_edit.setText(username.upper())
