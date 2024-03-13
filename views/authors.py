from PySide6.QtWidgets import QWidget, QGridLayout, QHBoxLayout, QFormLayout, QTextEdit

from views.share import ImageWidget, LineEdit, DateEdit, OptionButtonsGroup, FormField


class AuthorsView(QWidget):
    def __init__(self):
        super(AuthorsView, self).__init__()

        author_form = self.create_author_form()

        layout = QGridLayout(self)
        layout.addWidget(author_form)

    def create_author_form(self) -> QWidget:
        widget = QWidget()

        image_widget = ImageWidget()

        name_edit = LineEdit("")
        yob_edit = DateEdit("YYYY/MM/DD")
        yod_edit = DateEdit("YYYY/MM/DD")
        gender_group = OptionButtonsGroup("Gender", ["Male", "Female", "Other"])
        nationality_edit = LineEdit("")

        years_layout = QHBoxLayout()
        years_layout.addWidget(FormField("Year of birth", yob_edit))
        years_layout.addWidget(FormField("Year of death", yod_edit))

        demo_layout = QHBoxLayout()
        demo_layout.addWidget(FormField("Nationality", nationality_edit))
        demo_layout.addWidget(gender_group)

        career_textedit = QTextEdit()

        form = QFormLayout()
        form.addWidget(name_edit)
        form.addRow(demo_layout)
        form.addRow(years_layout)
        form.addWidget(career_textedit)

        layout = QHBoxLayout(widget)
        layout.addWidget(image_widget)
        layout.addLayout(form)

        return widget
