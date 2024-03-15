from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QFormLayout, QGridLayout, \
    QCheckBox, QCommandLinkButton, QGroupBox, QStackedWidget

# Local imports
from views.share import FormField, SubHeader, Toast, DateEdit, ImageWidget, OptionButtonsGroup, LineEdit, ComboBox, PushButton

from share import load_settings


# load institution configuration settings
settings = load_settings('institution')


class MemberRegistrationForm(QFrame):

    def __init__(self):
        super(MemberRegistrationForm, self).__init__()

        self.toast = Toast()
        self.image_widget = ImageWidget()

        self.member_type_options_group = OptionButtonsGroup(
            "",
            ["Student", "Employee"],
            required=True
        )

        self.member_type_options_group.setObjectName("borderless")
        self.member_type_options_group.button_group.checkedButton()

        self.name_edit = LineEdit("[a-zA-Z]{2:20}\\s[a-zA-Z]{2:20}\\s[a-zA-Z]{2:20}",
                                  "Full name eg. John Doe Smith")

        self.dob_edit = DateEdit("YYYY/MM/DD")

        self.gender_options_group = OptionButtonsGroup(
            "Gender",
            ["Male", "Female", "Other"]
        )

        self.current_residence = LineEdit(r"^[a-zA-Z0-9\s\-.,#']+$")
        self.permanent_address = LineEdit(r"^[a-zA-Z0-9\s\-.,#']+$")
        self.phone = LineEdit(r"^\+?\d{1,3}?[-. (]?\d{3}[-. )]?\d{3}[-. ]?\d{4}$")
        self.email = LineEdit(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

        self.id_number_edit = LineEdit("[0-9]{8}")
        self.employee_number_edit = LineEdit("[A-Z]{4}[0-9]{6}")
        self.nemis_number_edit = LineEdit("[A-Z]*[0-9]*")
        self.assessment_number_edit = LineEdit("[A-Z]{1}[0-9]{10}")
        self.admission_number_edit = LineEdit("[0-9]{5}")

        self.department_combo = ComboBox([
            "Administration", "Academics", "Kitchen", "Security", "House Keeping"
        ])

        self.role_combo = ComboBox([
            "Teacher", "Director", "Kitchen staff", "Head Chef"
        ])

        self.grade_combo = ComboBox([
            "Grade 1",
            "Grade 2",
            "Grade 3",
            "Grade 4",
            "Grade 5",
            "Grade 6",
            "Grade 7",
            "Grade 8",
            "Grade 9",
            "Grade 10",
            "Grade 11",
            "Grade 12"
        ])

        self.stream_combo = ComboBox([
            "East", "West", "North", "South"
        ])

        self.declaration_checkbox = QCheckBox("""
            Submitted a correctly signed declaration form.
        """)

        self.print_declaration_btn = QCommandLinkButton("Print declaration form")

        demographic_layout = QHBoxLayout()
        dob_field = FormField("Date of birth", self.dob_edit, Qt.Orientation.Vertical)
        dob_field.setFixedWidth(220)
        demographic_layout.addWidget(dob_field)
        demographic_layout.addWidget(self.gender_options_group)

        self.employee_details_group = QGroupBox()
        self.employee_details_group.setObjectName("borderless")
        self.emp_details_layout = QGridLayout(self.employee_details_group)
        self.emp_details_layout.setSpacing(15)
        self.emp_details_layout.addWidget(FormField("ID number", self.id_number_edit), 0, 0)
        self.emp_details_layout.addWidget(FormField("Employee number", self.employee_number_edit), 0, 1)
        self.emp_details_layout.addWidget(FormField("Department", self.department_combo), 1, 0)
        self.emp_details_layout.addWidget(FormField("Role", self.role_combo), 1, 1)

        self.student_details_group = QGroupBox()
        self.student_details_group.setObjectName("borderless")
        self.student_details_layout = QGridLayout(self.student_details_group)
        self.student_details_layout.setSpacing(15)
        self.student_details_layout.addWidget(FormField("Admission", self.admission_number_edit), 0, 0)
        self.student_details_layout.addWidget(FormField("NEMIS", self.nemis_number_edit), 0, 1)
        self.student_details_layout.addWidget(FormField("Assessment", self.assessment_number_edit), 0, 2)
        self.student_details_layout.addWidget(FormField("Grade", self.grade_combo), 1, 0)
        self.student_details_layout.addWidget(FormField("Stream", self.stream_combo), 1, 1)

        self.optional_fields = QStackedWidget()
        self.optional_fields.addWidget(self.student_details_group)
        self.optional_fields.addWidget(self.employee_details_group)

        contacts_layout = QHBoxLayout()
        contacts_layout.addWidget(FormField("Phone", self.phone, Qt.Orientation.Vertical))
        contacts_layout.addWidget(FormField("Email", self.email, Qt.Orientation.Vertical))

        residence_layout = QHBoxLayout()
        residence_layout.addWidget(FormField("Current residence", self.current_residence, Qt.Orientation.Vertical))
        residence_layout.addWidget(FormField("Permanent address", self.permanent_address, Qt.Orientation.Vertical))

        declaration_layout = QHBoxLayout()
        declaration_layout.addWidget(self.declaration_checkbox)
        declaration_layout.addStretch()
        declaration_layout.addWidget(self.print_declaration_btn)

        self.form_layout = QFormLayout()
        self.form_layout.setSpacing(15)
        self.form_layout.addWidget(self.member_type_options_group)
        self.form_layout.addRow("Name: ", self.name_edit)
        self.form_layout.addRow(demographic_layout)
        self.form_layout.addRow(self.optional_fields)
        self.form_layout.addRow(contacts_layout)
        self.form_layout.addRow(residence_layout)
        self.form_layout.addRow(declaration_layout)

        self.register_btn = PushButton("Register")
        btn_layout = QHBoxLayout()
        btn_layout.setContentsMargins(0, 10, 30, 0)
        btn_layout.addStretch()
        btn_layout.addWidget(self.register_btn)

        layout = QHBoxLayout()
        layout.setContentsMargins(30, 10, 30, 10)
        layout.addWidget(self.image_widget)
        layout.addLayout(self.form_layout)

        self.header = SubHeader("Register")

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.header)
        main_layout.addLayout(layout)
        main_layout.addLayout(btn_layout)
        main_layout.addStretch()
        self.event_listener()

    def event_listener(self):
        self.member_type_options_group.button_group.buttonToggled.connect(self.re_render)
        self.register_btn.clicked.connect(self.validate)

    def validate(self):
        print(self.name_edit.validate())
        icon = "ph.circle-wavy-warning-light"
        self.toast.show_message("Success", "error", icon)

    def re_render(self, btn):
        if btn.text() == "Student":
            self.optional_fields.setCurrentIndex(0)
        else:
            self.optional_fields.setCurrentIndex(1)
