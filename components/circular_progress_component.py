from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsTextItem


class CircularProgress(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        # Set the size of the view
        self.setFixedSize(200, 200)

        # Set the background color of the view
        self.setStyleSheet("background-color: white;")

        # Set the center coordinates
        center_x, center_y = self.width() / 2, self.height() / 2

        # Set the radius and thickness of the ring
        radius = 80

        # Create a circular background
        background = QGraphicsEllipseItem(center_x - radius, center_y - radius, 2 * radius, 2 * radius)
        background.setPen(Qt.NoPen)
        background.setBrush(Qt.lightGray)
        self.scene.addItem(background)

        # Create a progress ring
        self.progress_ring = QGraphicsEllipseItem(center_x - radius, center_y - radius, 2 * radius, 2 * radius)
        self.progress_ring.setPen(Qt.NoPen)
        self.progress_ring.setBrush(Qt.green)
        self.progress_ring.setStartAngle(0)  # Start angle at 0 degrees
        self.scene.addItem(self.progress_ring)

        # Display the current value text
        self.progress_text = QGraphicsTextItem(f"0/5")
        self.progress_text.setDefaultTextColor(Qt.black)
        self.progress_text.setFont(QFont("Arial", 12))
        self.progress_text.setPos(center_x - self.progress_text.boundingRect().width() / 2,
                                  center_y - self.progress_text.boundingRect().height() / 2)
        self.scene.addItem(self.progress_text)

    def set_value(self, value):
        # Update the progress ring based on the value
        max_value = 5
        angle = int((360 * value) / max_value)
        self.progress_ring.setSpanAngle(angle * 16)

        # Update the text
        self.progress_text.setPlainText(f"{value}/{max_value}")
