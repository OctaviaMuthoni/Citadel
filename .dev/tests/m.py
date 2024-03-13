import sys
from math import pi, sin, cos

from PySide6.QtCore import Qt, QPointF, QPoint
from PySide6.QtGui import QBrush, QColor, QPainterPath, QPixmap, QRegion, QPolygon
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QGraphicsScene, QGraphicsView, QWidget


class HexagonButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setFixedSize(120, 130)
        self.setStyleSheet("""
            QPushButton {
                background-color: #fafaaf; color: white; border: none; font: 11pt Arial;
            }
            QPushButton:hover, QPushButton:focus {
                background: #f1f11f;
            }
        """)
        self.setMask(self.create_hexagon_mask(self.size()))

    def create_hexagon_mask(self, size):
        polygon = QPolygon()
        # polygon.push_back()
        # path = QPainterPath()
        polygon.push_back(QPoint(size.width() / 2, 0))
        polygon.push_back(QPoint(size.width(), size.height() / 4))
        polygon.push_back(QPoint(size.width(), size.height() * 3 / 4))
        polygon.push_back(QPoint(size.width() / 2, size.height()))
        polygon.push_back(QPoint(0, size.height() * 3 / 4))
        polygon.push_back(QPoint(0, size.height() / 4))
        polygon.push_back(QPoint(0, size.height() / 4))
        polygon.push_back(QPoint(0, size.height() / 4))
        # polygon.closeSubpath()
        return QRegion(polygon)


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
        button1 = HexagonButton("Metarials")
        button2 = HexagonButton("Members")
        button3 = HexagonButton("Reports")
        button4 = HexagonButton("Loan")
        button5 = HexagonButton("Cards")
        button6 = HexagonButton("Schedule")
        button7 = HexagonButton("Notifications")
        button8 = HexagonButton("test")
        button9 = HexagonButton("Cards")
        button10 = HexagonButton("Schedule")
        button11 = HexagonButton("Notifications")
        button12 = HexagonButton("test")

        self.hexagon_buttons.append([
           button6, button5, button4, button2, button3, button1
        ])

        for i in self.hexagon_buttons[0]:
            self.scene.addWidget(i)

    def arrange_hexagon_buttons(self):
        radius = 130
        center = QPointF(self.width() / 2, self.height() / 2)

        for i, button in enumerate(self.hexagon_buttons[0]):
            angle = i * (360 // len(self.hexagon_buttons[0]))
            print(angle)
            x = center.x() + radius * cos(angle * pi / 180)
            y = center.y() + radius * sin(angle * pi / 180)
            button.move(x - button.width() / 2, y - button.height() / 2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    landing_page = LandingPage()
    landing_page.show()
    sys.exit(app.exec())
