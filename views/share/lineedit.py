from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QLineEdit


class LineEdit(QLineEdit):
    def __init__(self, pattern: str, placeholder=""):
        super(LineEdit, self).__init__()

        self.setPlaceholderText(placeholder)

        self.pattern = pattern
        self.validator_ = QRegularExpressionValidator(self.pattern)

    def value(self):
        pass

    def set_value(self):
        pass

    def validate(self):
        print(self.validator_.validate(self.text(), 0))
