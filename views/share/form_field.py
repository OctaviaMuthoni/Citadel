import typing

from PySide6.QtCore import Qt
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel, QWidget, QSizePolicy


class FormField(QFrame):
    def __init__(self,
                 name: str,
                 input_field: QWidget,
                 orientation: Qt.Orientation = Qt.Orientation.Horizontal,
                 show_label = True):
        super(FormField, self).__init__()

        self.name = name

        # select layout based on orientation
        layout = QHBoxLayout() if orientation == Qt.Orientation.Horizontal else QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.name.replace("_", " "))
        self.input_field = input_field

        self.label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.label.setObjectName("label")
        if show_label:
            layout.addWidget(self.label)
        layout.addWidget(self.input_field)

        self.setLayout(layout)
        self.setObjectName("form-field")

    def reset(self):
        self.input_field.setText("")

    def value(self) -> typing.Any:
        return self.input_field.value()

    def setValue(self, value) -> bool:
        return self.input_field.setValue(value)

    def isValid(self) -> bool:
        return self.input_field.validator().validate()[0] == QRegularExpressionValidator.State.Acceptable
