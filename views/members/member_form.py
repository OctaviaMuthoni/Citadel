from PySide6.QtCore import QSize, Signal
from PySide6.QtWidgets import QFrame, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QRadioButton, QButtonGroup, \
    QGroupBox, QCheckBox, QFormLayout, QToolBar, QComboBox

import qtawesome as qta

from classes.member import Member, Gender
from components import LineEdit, ImageComponent


class CreateMemberView(QFrame):

    memberChangedSignal = Signal(object)

    def __init__(self, parent):
        super(CreateMemberView, self).__init__(parent=parent)

        self.member = Member()

        self.actions_tool_bar = QToolBar()
        self.actions_tool_bar.setObjectName("sbrand")
        self.actions_tool_bar.setIconSize(QSize(30, 30))
        self.actions_tool_bar.addAction(qta.icon("ph.arrow-left",
                                                 color="teal"),
                                        "Back",
                                        lambda: self.parent().setCurrentIndex(0))
        self.actions_tool_bar.addWidget(QLabel("Add Member"))

        self.profile_image_upload = ImageComponent()

        self.name_edit = LineEdit("Fullname:", "Jane Doe Smith")
        self.id_edit = LineEdit("ID/Adm No./Reg No./Emp No.:", "N11/3/0416/014")
        self.email = LineEdit("Email:", "jane@doemailbox.com")
        self.phone = LineEdit("Phone:", "+254 700 000 000")
        self.residence = LineEdit("Residence:", "Cedar Ridge Hostels Rm. 14")

        self.member_type_combo = QComboBox()
        self.member_type_combo.addItems([
            "Student",
            "Teacher",
            "Other Staff"
        ])

        self.male = QRadioButton("Male")
        self.female = QRadioButton("Female")
        self.other = QRadioButton("Other")

        self.gender_btn_group = QButtonGroup()
        self.gender_btn_group.addButton(self.male)
        self.gender_btn_group.addButton(self.female)
        self.gender_btn_group.addButton(self.other)

        self.dob_edit = LineEdit("Dob", "01/01/99")
        self.gender_group = QGroupBox("Gender")

        self.terms_agreement_checkbox = QCheckBox()
        self.rules_print_btn = QPushButton("Print declaration form")
        self.rules_print_btn.setIcon(qta.icon("ph.printer-light"))
        self.rules_print_btn.setIconSize(QSize(25, 25))

        self.create_member_btn = QPushButton("Add Member")

        gender_layout = QHBoxLayout(self.gender_group)
        gender_layout.setSpacing(50)
        gender_layout.addWidget(self.male)
        gender_layout.addWidget(self.female)
        gender_layout.addWidget(self.other)

        personal_layout = QHBoxLayout()
        personal_layout.addWidget(self.dob_edit)
        personal_layout.addWidget(self.gender_group)

        address_layout = QHBoxLayout()
        address_layout.addWidget(self.phone)
        address_layout.addWidget(self.residence)

        member_type_layout = QHBoxLayout()
        member_type_layout.addWidget(self.id_edit)
        member_type_layout.addWidget(QLabel("Member type:"))
        member_type_layout.addWidget(self.member_type_combo)

        member_form_layout = QFormLayout()
        member_form_layout.addWidget(self.name_edit)
        member_form_layout.addRow(member_type_layout)
        member_form_layout.addRow(personal_layout)
        member_form_layout.addWidget(self.email)
        member_form_layout.addRow(address_layout)

        form_layout = QHBoxLayout()
        form_layout.addWidget(self.profile_image_upload)
        form_layout.addLayout(member_form_layout)

        declaration_layout = QHBoxLayout()
        declaration_layout.setSpacing(0)
        declaration_layout.addWidget(self.terms_agreement_checkbox)
        declaration_layout.addWidget(QLabel("""
            Check this box to certify that member has read the library rules and submitted 
            a fully signed declaration letter agreeing to the terms and condition
        """))
        declaration_layout.addStretch()
        declaration_layout.addWidget(self.rules_print_btn)

        layout = QVBoxLayout(self)
        layout.addWidget(self.actions_tool_bar)
        layout.addLayout(form_layout)
        layout.addLayout(declaration_layout)
        layout.addStretch()
        layout.addWidget(self.create_member_btn)

        self.setObjectName("white_back")
        self.profile_image_upload.imageChangeSignal.connect(self.update_profile_image)

    def update_profile_image(self, img):
        self.member.profile_image = img

    def render_form(self):
        if self.member.profile_image:
            self.profile_image_upload.imageChangeSignal.emit(f"resources/images/{self.member.profile_image}")
        self.name_edit.set_text(self.member.name)
        self.dob_edit.set_text(self.member.dob)
        self.email.set_text(self.member.email)
        self.phone.set_text(self.member.phone)
        self.residence.set_text(self.member.residence)
        self.id_edit.set_text(self.member.adm_number)

        checked = self.gender_btn_group.checkedButton()
        if checked:
            checked.setChecked(False)

        if self.member.gender == Gender.MALE.value:
            self.male.setChecked(True)
        elif self.member.gender == Gender.FEMALE.value:
            self.female.setChecked(True)
        elif self.member.gender == Gender.OTHER.value:
            self.other.setChecked(True)

    def set_member(self, member):
        self.member = member
        self.render_form()
