from PySide6.QtCore import Qt, QSequentialAnimationGroup, QEasingCurve, QRect, QPropertyAnimation
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel

import qtawesome as qta

from core import MessageSeverity, Colors


class Notifier(QFrame):
    def __init__(self, parent=None):
        super(Notifier, self).__init__(parent=parent)

        self.options = {
            "info": {"icon": "ph.info", "color": Colors.INFO},
            "warning": {"icon": "ph.warning", "color": Colors.WARNING},
            "error": {"icon": "ph.warning-octagon", "color": Colors.ERROR},
            "success": {"icon": "ph.check-circle", "color": Colors.SUCCESS}
        }

        self.icon_lbl = QLabel()
        self.message_lbl = QLabel("text")

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.icon_lbl)
        layout.addWidget(self.message_lbl)

    def configure_notifier(self, message, severity: MessageSeverity = MessageSeverity.SUCCESS):
        self.message_lbl.setText(message)
        option = self.options[severity]

        icon = qta.icon(option['icon'], color=option['color'])
        self.icon_lbl.setPixmap(icon.pixmap(30))

        self.setObjectName(severity)

        bulge_animation = QPropertyAnimation(self, b'geometry', self)
        bulge_animation.setStartValue(self.geometry())
        bulge_animation.setEndValue(QRect(0, 100, self.width(), self.height()))
        bulge_animation.setDuration(1000)  # Adjust duration as needed
        bulge_animation.setEasingCurve(QEasingCurve.OutBack)

        # Animation for bulging in
        shrink_animation = QPropertyAnimation(self, b'geometry', self)
        shrink_animation.setStartValue(bulge_animation.endValue())
        shrink_animation.setEndValue(QRect(0, -self.height(), self.width(), self.height()))
        shrink_animation.setDuration(1000)  # Adjust duration as needed
        shrink_animation.setEasingCurve(QEasingCurve.InBack)

        # Set up a sequential animation group
        animation_group = QSequentialAnimationGroup(self)
        animation_group.addAnimation(bulge_animation)
        animation_group.addPause(2000)
        animation_group.addAnimation(shrink_animation)

        # Start the animation
        animation_group.start()
