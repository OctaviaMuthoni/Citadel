from PySide6.QtCore import QSize
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QGridLayout, QTabWidget, QSpacerItem, QHBoxLayout

from models.departments import DepartmentsModel
from models.roles_model import RolesModel
from views.share import FormField, LineEdit, MultiSelectCombo, ListWidget
from views.share.image_widget import ImageWidget


class DepartmentsView(QWidget):
    def __init__(self):
        super(DepartmentsView, self).__init__()

        self.department_model = DepartmentsModel()
        self.roles_model = RolesModel()

        self.department_list = ListWidget(self.department_model)
        self.roles_list = ListWidget(self.roles_model)

        layout = QHBoxLayout(self)
        layout.addWidget(self.department_list)
        layout.addWidget(self.roles_list)


class ContactsView(QWidget):
    def __init__(self):
        super().__init__()

        # contacts fields
        self.email = LineEdit("")
        self.phone_1 = LineEdit("")
        self.phone_2 = LineEdit("")

        # address fields
        self.po_address = LineEdit("")
        self.po_code = LineEdit("")
        self.website = LineEdit("")
        self.location = LineEdit("")

        # grades
        self.grades = MultiSelectCombo(["Grade {x}" for x in range(1, 13)])
        self.streams = LineEdit("")

        # departments
        self.department_widget = DepartmentsView()

        layout = QVBoxLayout(self)
        layout.addWidget(self.department_widget)


class ManageInstitutionView(QWidget):
    def __init__(self):
        super(ManageInstitutionView, self).__init__()

        self.logo_upload = ImageWidget(size=QSize(200, 200))
        self.name_edit = QLineEdit()
        self.motto_edit = QLineEdit()

        details_layout = QGridLayout()
        details_layout.addWidget(FormField("Institution name: ", self.name_edit), 0, 1)
        details_layout.addWidget(FormField("Institution motto: ", self.motto_edit), 1, 1)
        details_layout.addItem(QSpacerItem(100, 100), 2, 1)
        details_layout.addWidget(self.logo_upload, 0, 0, 3, 1)

        self.policy_widget = QWidget()
        self.contacts_widget = ContactsView()
        self.address_widget = QWidget()

        self.details_tab_widget = QTabWidget()
        self.details_tab_widget.addTab(self.contacts_widget, "Contacts")
        self.details_tab_widget.addTab(self.address_widget, "Address")
        self.details_tab_widget.addTab(self.policy_widget, "Policy")

        layout = QVBoxLayout(self)
        layout.addLayout(details_layout)
        layout.addWidget(self.details_tab_widget)



