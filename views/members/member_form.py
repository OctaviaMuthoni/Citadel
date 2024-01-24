from PySide6.QtCore import QSize
from PySide6.QtWidgets import QFrame, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QRadioButton, QButtonGroup, \
    QGroupBox, QCheckBox, QFormLayout, QToolBar, QComboBox

import qtawesome as qta

from components import LineEdit, ImageComponent
from models.members import Member, Gender


class MembersForm(QFrame):

    def __init__(self, parent):
        super(MembersForm, self).__init__(parent=parent)

        self.member = Member()

        self.profile_image_upload = ImageComponent()

        self.f_name_edit = LineEdit("Firstname:", "Jane")
        self.m_name_edit = LineEdit("Middlename:", "Doe")
        self.l_name_edit = LineEdit("Lastname:", "Smith")

        self.identification_type_combo = QComboBox()
        self.identification_type_combo.addItems([
            "National ID card",
            "Student ID card",
            "Employment card"
        ])
        self.id_edit = LineEdit("ID/Adm No./Reg No./Emp No.:", "N11/3/0416/014")

        self.email_edit = LineEdit("Email:", "jane@doemailbox.com")
        self.phone_edit = LineEdit("Phone:", "+254 700 000 000")
        self.current_residence = LineEdit("Current residence:", "Cedar Ridge Hostels Rm. 14")
        self.permanent_address = LineEdit("Permanent address:", "126, Tom Mboya street")

        self.subscription_combo = QComboBox()
        self.subscription_combo.addItems([
            "Freemium Limited",
            "Freemium Unlimited",
            "Premium"
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

        self.activation_fee_edit = LineEdit("Subscription fee", "0.00")
        self.borrowing_limit_edit = LineEdit("Limit", "0")

        self.create_member_btn = QPushButton("Add Member")

        name_layout = QHBoxLayout()
        name_layout.addWidget(self.f_name_edit)
        name_layout.addWidget(self.m_name_edit)
        name_layout.addWidget(self.l_name_edit)

        identification_layout = QHBoxLayout()
        identification_layout.addWidget(self.identification_type_combo)
        identification_layout.addWidget(self.id_edit)

        gender_layout = QHBoxLayout(self.gender_group)
        gender_layout.setSpacing(50)
        gender_layout.addWidget(self.male)
        gender_layout.addWidget(self.female)
        gender_layout.addWidget(self.other)

        personal_layout = QHBoxLayout()
        personal_layout.addWidget(self.dob_edit)
        personal_layout.addWidget(self.gender_group)

        address_layout = QHBoxLayout()
        address_layout.addWidget(self.current_residence)
        address_layout.addWidget(self.permanent_address)

        contacts_layout = QHBoxLayout()
        contacts_layout.addWidget(self.phone_edit)
        contacts_layout.addWidget(self.email_edit)

        subscription_layout = QHBoxLayout()
        subscription_layout.addWidget(self.subscription_combo)
        subscription_layout.addStretch()

        member_form_layout = QFormLayout()
        member_form_layout.addRow(name_layout)
        member_form_layout.addRow(identification_layout)
        member_form_layout.addRow(personal_layout)
        member_form_layout.addRow(contacts_layout)
        member_form_layout.addRow(address_layout)
        member_form_layout.addRow(subscription_layout)

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


