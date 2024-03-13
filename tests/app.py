from PySide6.QtCore import QSize, Qt, Signal, QPropertyAnimation, QRect
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QFrame, QLabel, QFormLayout, \
    QCommandLinkButton, QSpacerItem, QStackedWidget

from lms import CentralWidget
from views.share import PushButton, LineEdit
from share import load_settings


class LoginPage(QFrame):
    loginSignal = Signal()

    def __init__(self):
        super(LoginPage, self).__init__()

        # brand
        self.brand_logo_lbl = QLabel()
        self.brand_logo_lbl.setScaledContents(True)
        self.brand_logo_lbl.setFixedSize(QSize(180, 180))

        self.app_name_lbl = QLabel("LIBRARY SYSTEM")
        self.app_name_lbl.setObjectName("mini-brand")
        self.app_name_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.institution_name_lbl = QLabel()
        self.institution_name_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.institution_name_lbl.setObjectName("brand")

        self.institution_motto_lbl = QLabel()
        self.institution_motto_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.error_label = QLabel("Error")
        self.error_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.error_label.setObjectName('error')
        self.error_label.setVisible(False)

        brand_widget = QFrame()
        brand_widget_layout = QVBoxLayout(brand_widget)
        brand_widget_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        brand_widget_layout.addWidget(self.error_label)
        brand_widget_layout.addWidget(self.institution_name_lbl)
        brand_widget_layout.addWidget(self.institution_motto_lbl)
        brand_widget_layout.addWidget(self.app_name_lbl)

        # brand social contacts
        self.website_lbl = QLabel()
        self.email_lbl = QLabel()
        self.phone_lbl = QLabel()

        # login action buttons
        self.forgot_pass_btn = QCommandLinkButton("Forgot Password?")
        self.login_btn = PushButton("Login")
        self.login_btn.setFixedSize(QSize(130, 35))
        self.login_btn.clicked.connect(self.loginSignal)

        # login form fields
        self.username_field = LineEdit("[a-zA-Z]{10}", "your username")
        self.password_field = LineEdit("[a-zA-Z]{10}", "your password")
        self.password_field.setEchoMode(LineEdit.EchoMode.Password)

        # login form sidebar
        sidebar = QFrame()
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.addWidget(self.brand_logo_lbl)
        sidebar_layout.addStretch()
        sidebar_layout.addWidget(self.website_lbl)
        sidebar_layout.addWidget(self.email_lbl)
        sidebar_layout.addWidget(self.phone_lbl)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.forgot_pass_btn)
        buttons_layout.addStretch()
        buttons_layout.addWidget(self.login_btn)

        # form
        self.form = QFormLayout()
        self.form.setSpacing(20)
        self.form.setContentsMargins(60, 0, 60, 0)
        self.form.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.form.addWidget(brand_widget)
        self.form.addItem(QSpacerItem(100, 10))
        self.form.addRow("Username:", self.username_field)
        self.form.addRow("Password:", self.password_field)
        self.form.addRow(buttons_layout)

        # login
        login_central_widget = QFrame()
        login_central_widget.setObjectName("login-widget")

        login_form_layout = QHBoxLayout(login_central_widget)
        login_form_layout.addWidget(sidebar)
        login_form_layout.addLayout(self.form)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(login_central_widget)

        self.setFixedSize(QSize(900, 506))

        self.setObjectName("login-page")

        self.configure()

        self.setStyleSheet("""
                    * {
                        color: #0492B3;
                        font-size: 11pt;
                    }
                    
                    #brand {
                        font-family: gabriola;
                        font-size: 32pt;
                    }
                    
                    #mini-brand {
                        font-size: 16pt;
                    }

                    #login-widget {
                        background-color: #120598A9;
                    }

                    #login-page {
                        background-image: url('res/images/ee.jpg');
                        background-position: center;
                        background-repeat: no-repeat;
                        background-color: #fefefe;
                    }
                    
                    QLineEdit {
                        border: 1px solid #4505ADD3;
                        background: #96ffffff;
                        padding: 5px;
                        border-radius: 4px;
                    }
                    
                    #error {
                        background-color: red;
                    }
                    
                """)

        self.loginSignal.connect(self.login)
        self.anim = QPropertyAnimation(self.error_label, b'geometry')

        self.p = self.error_label.pos()
    def login(self):
        pos = self.mapToParent(self.p)
        w = self.error_label.width()
        h = self.error_label.height()
        self.anim.setStartValue(QRect(pos.x() + w // 2, pos.y() + h // 2, 0, 0))
        self.anim.setEndValue(QRect(pos.x(), pos.y(), w, 40))
        self.anim.setDuration(500)

        self.anim.start()
        self.error_label.setVisible(True)
        self.anim.finished.connect(lambda: print(self.error_label.geometry()))

    def configure(self):
        settings = load_settings('institution')
        self.brand_logo_lbl.setPixmap(QPixmap(f"res/images/{settings.get('logo')}"))
        self.institution_name_lbl.setText(settings.get('name'))
        self.institution_motto_lbl.setText(settings.get('slogan'))

        self.website_lbl.setText(settings.get('website'))
        self.email_lbl.setText(settings.get('email'))
        self.phone_lbl.setText(settings.get('phone'))


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # self.login_page = LoginPage()
        self.content = CentralWidget(self)

        self.content_widget = QStackedWidget()
        # self.content_widget.addWidget(self.login_page)
        self.content_widget.addWidget(self.content)

        self.setCentralWidget(self.content_widget)

        self.styles = ""

        # self.login_page.login_btn.clicked.connect(self.login)


    # def login(self):
    #     print("got here")
    #     self.content_widget.setCurrentIndex(1)
    #     self.showMaximized()






