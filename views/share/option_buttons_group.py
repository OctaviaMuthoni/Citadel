from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGroupBox, QButtonGroup, QVBoxLayout, QHBoxLayout, QRadioButton, QCheckBox, QSizePolicy


class OptionButtonsGroup(QGroupBox):
    def __init__(self,
                 group_name,
                 options: list,
                 orientation: Qt.Orientation = Qt.Orientation.Horizontal,
                 required: bool = False,
                 exclusive: bool = True):
        super(OptionButtonsGroup, self).__init__(group_name)

        self.button_group = QButtonGroup()
        self.button_group.setExclusive(exclusive)

        Button = QRadioButton if exclusive else QCheckBox

        self.orientation = orientation
        QVBoxLayout(self) if orientation == Qt.Orientation.Vertical else QHBoxLayout(self)

        for option in options:
            self.add_button(Button(option))

        if required:
            first_option = self.button_group.buttons()[0]
            first_option.setChecked(True)

        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

    def add_button(self, button: QRadioButton | QCheckBox):
        self.layout().addWidget(button)
        self.button_group.addButton(button)
