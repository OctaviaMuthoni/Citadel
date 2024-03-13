import qtawesome as qta
from PySide6.QtCore import Qt, QTimer, QPoint, QPropertyAnimation, QSize
from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QApplication, QLabel, QHBoxLayout, QFrame, QWidget


class Toast(QWidget):
    COLORS = {
        "success": ["#CCFFD1", "#30DE64"],
        "info": ["#F4FFFE", "#21D5FF"],
        "warning": ["#F8FFCA", "#FFD516"],
        "error": ["#FFD7DA", "#FF0000"],
    }

    def __init__(self, parent=None):
        super().__init__(parent)

        self.icon_label = QLabel()
        self.message_label = QLabel()

        layout = QHBoxLayout()
        layout.setContentsMargins(15, 0, 0, 0)
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.icon_label, alignment=Qt.AlignCenter)
        layout.addWidget(self.message_label, alignment=Qt.AlignCenter)

        self.setLayout(layout)

        self.setMinimumSize(QSize(500, 40))
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        self.set_palette("error")

    def set_palette(self, message_type):
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(self.COLORS[message_type][0]))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(self.COLORS[message_type][1]))
        self.setPalette(palette)

    def show_message(self, message, message_type, icon=None):
        self.message_label.setText(message)

        if icon:
            pixmap = qta.icon(icon, color=self.COLORS[message_type][1]).pixmap(30)
            self.icon_label.setPixmap(pixmap)
        else:
            self.icon_label.clear()

        screen = QApplication.primaryScreen().geometry()

        self.show()

        self.animation = QPropertyAnimation(self, b"pos")

        self.animation.setDuration(200)
        self.animation.setStartValue(QPoint(screen.width() // 2 - self.width() // 2 + 100, -50))
        self.animation.setEndValue(QPoint(screen.width() // 2 - self.width() // 2 + 100, 50))
        self.animation.start()

        QTimer.singleShot(2000, self.hide_animation)

    def hide_animation(self):
        screen = QApplication.primaryScreen().geometry()
        self.animation.setStartValue(self.pos())
        self.animation.setEndValue(QPoint(screen.width() // 2 - self.width() // 2 + 100, -50))
        self.animation.finished.connect(self.close)
        self.animation.start()
