from PySide6.QtWidgets import QWidget


class UsersView(QWidget):
    def __init__(self):
        super(UsersView, self).__init__()

        # self.users_model = UsersModel()
        #
        # self.image_widget = ImageWidget(mode=ImageWidget.ImageWidgetMode.PREVIEW)
        #
        # self.users_table = TableView()
        # self.users_table.setModel(self.users_model)
        #
        # # buttons
        # self.add_user_btn = PushButton("Add user", qta.icon("ph.user"), "green")
        # self.get_otp_btn = PushButton("Get OTP", qta.icon("ph.key"), "#05ADD3")
        # self.save_btn = PushButton("Save", qta.icon("ph.tree-structure-thin"), "#e8e8e8")
        #
        # buttons_layout = QVBoxLayout()
        # buttons_layout.addWidget(self.add_user_btn)
        # buttons_layout.addWidget(self.save_btn)
        # buttons_layout.addWidget(self.get_otp_btn)
        #
        # self.username_field = FormField("Username", LineEdit(""))
        # self.email_field = FormField("Email", LineEdit(""))
        # self.roles_field = FormField("Roles", ComboBox([
        #     "Admin",
        #     "Librarian",
        #     "Monitor"
        # ]))
        #
        # self.otp_label = QLabel("dfjgsdjkfsd")
        # palette = self.otp_label.palette()
        # palette.setColor(QPalette.ColorRole.Base, QColor("green"))
        # palette.setColor(QPalette.ColorRole.Text, QColor("white"))
        # self.otp_label.setFixedSize(QSize(180, 40))
        # self.otp_label.setPalette(palette)
        #
        # self.otp_label.setWindowOpacity(0.2)
        #
        # details_layout = QVBoxLayout()
        # details_layout.addWidget(self.username_field)
        # details_layout.addWidget(self.email_field)
        # details_layout.addWidget(self.roles_field)
        #
        # top_layout = QHBoxLayout()
        # top_layout.addWidget(self.image_widget)
        # top_layout.addLayout(details_layout)
        # top_layout.addStretch()
        # top_layout.addWidget(self.otp_label)
        # top_layout.addStretch()
        # top_layout.addLayout(buttons_layout)
        #
        #
        # layout = QVBoxLayout(self)
        # layout.setSpacing(20)
        # layout.setContentsMargins(40, 0, 40, 0)
        # layout.addWidget(SubHeader("User Management", False))
        # layout.addLayout(top_layout)
        # layout.addWidget(self.users_table)
