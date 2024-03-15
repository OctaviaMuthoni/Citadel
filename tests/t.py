import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PySide6.QtGui import QPainter, QColor, QBrush, QPen
from PySide6.QtCore import Qt, QRectF

class CircleWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.value = 3/5

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Define dimensions
        side = min(self.width(), self.height())
        radius = side / 2
        center = self.rect().center()
        rect = QRectF(center.x() - radius, center.y() - radius, side, side)

        # Draw circle
        painter.setBrush(Qt.white)
        painter.drawEllipse(rect)

        # Draw shaded region
        painter.setBrush(QColor(0, 0, 255, 100))
        painter.setPen(Qt.NoPen)
        painter.drawPie(rect, 90 * 16, -self.value * 360 * 16)

        # Draw text
        painter.setPen(Qt.black)
        painter.drawText(rect, Qt.AlignCenter, f"{self.value}")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Circle Widget")
        self.setGeometry(100, 100, 400, 400)

        layout = QVBoxLayout()
        circle_widget = CircleWidget()
        layout.addWidget(circle_widget)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
