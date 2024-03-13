import sys
from PySide6.QtCore import Qt, QTimer, QRect, QPoint, QPropertyAnimation
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
import qtawesome as qta


class Toast(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.icon_label = QLabel()
        self.message_label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.icon_label, alignment=Qt.AlignCenter)
        layout.addWidget(self.message_label, alignment=Qt.AlignCenter)

        self.setLayout(layout)

        self.setStyleSheet("background-color: rgba(50, 50, 50, 200); color: white; border-radius: 5px;")
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

    def show_message(self, message, icon=None):
        self.message_label.setText(message)

        if icon:
            pixmap = qta.icon(icon).pixmap(30)
            self.icon_label.setPixmap(pixmap)
        else:
            self.icon_label.clear()

        screen = QApplication.primaryScreen().geometry()
        self.move(screen.right() - self.width() - 20, screen.bottom() + 20)
        self.show()

        self.animation = QPropertyAnimation(self, b"pos")
        self.animation.setDuration(500)
        self.animation.setStartValue(self.pos())
        self.animation.setEndValue(QPoint(screen.right() - self.width() - 20, screen.bottom() - self.height() - 20))
        self.animation.start()

        QTimer.singleShot(3000, self.hide_animation)

    def hide_animation(self):
        screen = QApplication.primaryScreen().geometry()
        self.animation.setStartValue(self.pos())
        self.animation.setEndValue(QPoint(screen.right() - self.width() - 20, screen.bottom() + 20))
        self.animation.finished.connect(self.hide)
        self.animation.start()

