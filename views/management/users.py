from PySide6.QtWidgets import QWidget, QTableView, QHBoxLayout, QFormLayout, QLineEdit, QLabel, QVBoxLayout, \
    QApplication

from models.users import UsersModel
from views.share import FormField


class UsersView(QWidget):
    def __init__(self):
        super(UsersView, self).__init__()

        self.users_model = UsersModel()

        self.users_tableview = QTableView()
        self.users_tableview.setModel(self.users_model)

        self.profile_img_lbl = QLabel()
        self.username_lbl = QLabel()

        self.current_pass_edit = QLineEdit()
        self.new_password_edit = QLineEdit()
        self.confirm_password_edit = QLineEdit()

        new_pass_layout = QHBoxLayout()
        new_pass_layout.addWidget(FormField("New password", self.new_password_edit))
        new_pass_layout.addWidget(FormField("Confirm password", self.confirm_password_edit))

        self.no_data_lbl = QLabel("The Table is currently empty")

        table_layout = QVBoxLayout()
        table_layout.addWidget(self.users_tableview)
        table_layout.addWidget(self.no_data_lbl)

        user_form = QFormLayout()
        user_form.addWidget(self.profile_img_lbl)
        user_form.addWidget(self.username_lbl)
        user_form.addRow(FormField("Current password", self.current_pass_edit))
        user_form.addRow(new_pass_layout)
        layout = QHBoxLayout(self)
        layout.addLayout(user_form)
        layout.addLayout(table_layout)

        self.render_form()

    def render_form(self):
        idx = self.users_model.index(0, 0)


if __name__ == "__main__":
    app = QApplication([])
    # window