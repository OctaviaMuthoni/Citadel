from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit, QWidget, QHBoxLayout, QVBoxLayout, QLabel


class LineEdit(QWidget):
    def __init__(self,
                 label,
                 placeholder,
                 orientation: Qt.Orientation = Qt.Orientation.Horizontal):
        super(LineEdit, self).__init__()

        preferred_layout = QVBoxLayout if orientation == Qt.Orientation.Vertical else QHBoxLayout
        layout = preferred_layout(self)

        self.lineedit = QLineEdit()
        self.lineedit.setPlaceholderText(placeholder)

        self.label = QLabel(label)

        layout.addWidget(self.label)
        layout.addWidget(self.lineedit)

    def set_text(self, text):
        self.lineedit.setText(text)

    def text(self):
        return self.lineedit.text()
