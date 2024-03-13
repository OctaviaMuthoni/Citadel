from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QColor, QFont
from PySide6.QtWidgets import QPushButton, QGraphicsDropShadowEffect

import qtawesome as qta


class PushButton(QPushButton):
    def __init__(self, text, icon=None, color=QColor(), color_active=QColor()):
        super(PushButton, self).__init__(text)

        shadow_effect = QGraphicsDropShadowEffect(self)
        shadow_effect.setBlurRadius(20)
        shadow_effect.setColor("#65000000")
        shadow_effect.setOffset(4, 4)
        self.setGraphicsEffect(shadow_effect)

        self.setMinimumSize(QSize(100, 33))
        self.setIconSize(QSize(30, 30))

        if icon:
            self.setIcon(icon) if type(icon) == QIcon else self.setIcon(
                qta.icon(icon, color=color, color_active=color_active)
            )

        self.setObjectName("push_button")