from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGroupBox, QVBoxLayout, QHBoxLayout, QRadioButton, QButtonGroup


class RadioButtonGroup(QGroupBox):
    def __init__(self, title, buttons: list, orientation: Qt.Orientation = Qt.Orientation.Horizontal):
        super(RadioButtonGroup, self).__init__(title)

        self.btn_group = QButtonGroup()

        radio_layout = QVBoxLayout if orientation == Qt.Orientation.Vertical else QHBoxLayout
        layout = radio_layout(self)

        for btn in buttons:
            btn = QRadioButton(btn)
            layout.addWidget(btn)
            self.btn_group.addButton(btn)

    def value(self):
        return self.btn_group.checkedButton().text()

