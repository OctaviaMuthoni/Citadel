import qtawesome as qta
from PySide6.QtCore import QSize, Qt, Signal
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QFormLayout, QLineEdit, QVBoxLayout, \
    QFrame

# from citadexx import MainWindow
# import local modules
# import resources_rc
from core import Colors
from ui.citadexx import MainWindow

# importing custom widgets
from ui.widgets import ButtonsWidget, PushButton
from ui.widgets.message import Notifier

# importing required models
from models.users import UsersModel

# importing core functionality files
from core.settings import Settings


class LoginWindow(QFrame):
    # signals
    loginSignal = Signal(str)

    def __init__(self):
        super(LoginWindow, self).__init__()

        # self.setWindowIcon(QIcon("favicon.ico"))
        # self.setWindowTitle("Citadexx")

        self.settings = Settings()
        self.user_model = UsersModel()
        self.main_window = MainWindow()

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
        side_lbl.setFixedWidth(300)
        side_lbl.setObjectName("side-lbl")
        side_img = QPixmap(self.settings.get_settings("logo", "favicon.ico"))
        logo_lbl.setPixmap(side_img)

        email_link_lbl = QLabel("muthonioctavia@gmail.com")
        phone_lbl = QLabel("+254 718 758 807")
        web_link_lbl = QLabel("www.theacademiccitadel.com")

        web_icon_lbl = QLabel()
        web_icon_lbl.setPixmap(qta.icon("ph.globe", color=Colors.ALTERNATE_ICON_COLOR).pixmap(30))
        email_icon_lbl = QLabel()
        email_icon_lbl.setPixmap(qta.icon("ph.envelope", color=Colors.ALTERNATE_ICON_COLOR).pixmap(30))
        phone_icon_lbl = QLabel()
        phone_icon_lbl.setPixmap(qta.icon("ph.phone", color=Colors.ALTERNATE_ICON_COLOR).pixmap(30))

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
                                    qta.icon("ph.lock-key-open", color=Colors.ACCENT),
                                    PushButton.ButtonType.INFO)

        self.username_edit = QLineEdit()
        self.username_edit.setPlaceholderText("LIB/9/99999")
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)

        btns_widget = ButtonsWidget()
        btns_widget.add_button(self.login_btn)

        title_lbl = QLabel(self.settings.get_settings("institution/name", "The Citadexx Academy"))
        title_lbl.setObjectName("brand-name")
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

        self.event_listener()

        self.setStyleSheet("""
            * {
                font-family: "arial";
                font-size: 10pt;
                color: #0598A8;
            }
            
            /* Login window styles */
            #login-background {
                background: url("resources/images/login_bg.jpg");
            }
            
            #side-lbl {
                background: #0598A8;
            }
            
            #side-lbl QLabel {
                color: #f1f1f1;
            }
            
            #brand-name {
                font-size: 22pt;
                font-family: "Casandra Light";
                font-weight: 200;
                color: #0598A8;
            }
            /* End of login window styles */
        """)

    def event_listener(self):
        self.username_edit.textChanged.connect(self.username_to_upper)

    # TODO: implement user sessions and a limited number pf password retries
    def authenticate(self):
        # username = self.username_edit.text()
        # password = self.password_edit.text()
        #
        # user = self.user_model.get_user(username)
        #
        # if user:
        #     if user.attempts > 0:
        #         pass
        #     if user.password == encryption.hash_password(password):
        #         # create a new user session
        #         self.user_model.create_session(user)
        #         self.user_model.reset_attempts()
        #
        # else:
        #     self.notifier.configure_notifier("Invalid password. If you are having trouble signing in, contact your admin")
        #     self.user_model.add_attempt()
        # self.loginSignal.emit("tada")
        self.main_window.showMaximized()
        self.close()

    def username_to_upper(self, username):
        self.username_edit.setText(username.upper())
