from enum import Enum

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QFont, QColor, QPalette
from PySide6.QtWidgets import QPushButton, QGraphicsDropShadowEffect


class PushButton(QPushButton):
    Colors = ["#f7f7f7", "#09A643", "#CF0609", "#08ADCF", "#C4C216"]
    ObjectName = ["default", "success", "cancel", "info", "warning"]
    ButtonType = Enum("ButtonType",
                      [("DEFAULT", 0), ("SUCCESS", 1), ("CANCEL", 2), ("INFO", 3), ("WARNING", 4)])

    def __init__(self, callback, text, icon="", button_type: ButtonType = ButtonType.DEFAULT):
        super(PushButton, self).__init__(text)

        self.color = self.Colors[button_type.value]

        shadow_effect = QGraphicsDropShadowEffect(self)
        shadow_effect.setBlurRadius(20)
        shadow_effect.setColor(self.color)
        shadow_effect.setOffset(2, 2)
        self.setGraphicsEffect(shadow_effect)

        if icon:
            self.setIcon(icon)

        self.setIconSize(QSize(25, 25))

        self.setFixedSize(QSize(150, 40))
        self.setFont(QFont("Lucida UI", 13))

        self.setBackgroundRole(QPalette.ColorRole.Highlight)

        self.clicked.connect(callback)

