from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QSpinBox, QDoubleSpinBox, \
    QTextEdit, QComboBox


class FormInput(QFrame):
    def __init__(self, label: str, input_field, orientation: Qt.Orientation = Qt.Orientation.Horizontal):
        super(FormInput, self).__init__()

        layout = QHBoxLayout() if orientation == Qt.Orientation.Horizontal else QVBoxLayout()

        self.label = label if type(label) == QLabel else QLabel(label)

        self.input_field = input_field

        layout.addWidget(self.label)
        layout.addWidget(self.input_field)

        self.setLayout(layout)
        self.setObjectName("form_input")

    def value(self):
        value = ""
        input_type = type(self.input_field)
        if input_type in [QSpinBox, QDoubleSpinBox]:
            value = self.input_field.value()
        elif input_type == QLineEdit:
            value = self.input_field.text()
        elif input_type == QTextEdit:
            value = self.input_field.toPlainText()
        elif input_type == QComboBox:
            value = self.input_field.currentText()

        return value

    def set_value(self, value):
        input_type = type(self.input_field)
        if input_type in [QSpinBox, QDoubleSpinBox]:
            self.input_field.setValue(value)
        elif input_type == QLineEdit:
            self.input_field.setText(value)
        elif input_type == QTextEdit:
            self.input_field.setText()
        elif input_type == QComboBox:
            self.input_field.setCurrentText(value)

    def set_validator(self, validator):
        if type(self.input_field) == QLineEdit:
            self.input_field.setValidator(validator)
