from PySide6.QtWidgets import QHBoxLayout, QFrame

from ui.widgets import PushButton


class ButtonsWidget(QFrame):
    def __init__(self):
        super(ButtonsWidget, self).__init__()

        layout = QHBoxLayout(self)

        layout.addStretch()

    def add_button(self, button: PushButton):
        self.layout().addWidget(button)
