import sys
from math import cos, pi, sin

from PySide6.QtCore import QPointF, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QGraphicsScene, QGraphicsView
# from numpy import sin


class HexagonButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setFixedSize(100, 100)
        self.setStyleSheet("background-color: #FF5733; color: white; border: none;")


class LandingPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hexagonal Navigation")
        self.setGeometry(100, 100, 800, 600)

        self.centralWidget = QGraphicsView()
        self.setCentralWidget(self.centralWidget)

        self.scene = QGraphicsScene()
        self.centralWidget.setScene(self.scene)

        self.hexagon_buttons = []

        self.create_hexagon_buttons()
        self.arrange_hexagon_buttons()

    def create_hexagon_buttons(self):
        for i in range(6):
            button = HexagonButton(f"Button {i + 1}")
            self.hexagon_buttons.append(button)
            self.scene.addWidget(button)

    def arrange_hexagon_buttons(self):
        radius = 200
        center = QPointF(self.width() / 2, self.height() / 2)

        for i, button in enumerate(self.hexagon_buttons):
            angle = i * 60
            x = center.x() + radius * cos(angle * pi / 180)
            y = center.y() + radius * sin(angle * pi / 180)
            button.move(x - button.width() / 2, y - button.height() / 2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    landing_page = LandingPage()
    landing_page.show()
    sys.exit(app.exec())
