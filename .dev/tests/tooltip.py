from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QStyledItemDelegate
from PySide6.QtCore import Qt

class RotatedTextDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        text = index.data(Qt.DisplayRole)
        if text:
            painter.save()
            painter.translate(option.rect.center())
            painter.rotate(-90)
            painter.drawText(0, 0, text)
            painter.restore()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Rotated Text in QTableWidgetItem")
        self.setGeometry(100, 100, 400, 300)

        self.table = QTableWidget(4, 3)
        self.table.setHorizontalHeaderLabels(["Column 1", "Column 2", "Column 3"])

        # Fill cells with rotated text
        for i in range(4):
            for j in range(3):
                item = QTableWidgetItem(f"Cell {i},{j}")
                item.setData(Qt.DisplayRole, f"Cell {i},{j}")  # Set data for DisplayRole
                self.table.setItem(i, j, item)

        # Set delegate for all cells
        self.table.setItemDelegate(RotatedTextDelegate())

        self.setCentralWidget(self.table)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
