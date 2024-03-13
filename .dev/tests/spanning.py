from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Row Span Example")
        self.setGeometry(100, 100, 400, 300)

        self.table = QTableWidget()
        self.table.setRowCount(4)
        self.table.setColumnCount(3)

        # Set headers
        self.table.setHorizontalHeaderLabels(["Column 1", "Column 2", "Column 3"])

        # Fill cells with data
        self.table.setItem(0, 0, QTableWidgetItem("Item 1"))
        self.table.setItem(1, 0, QTableWidgetItem("Item 2"))
        self.table.setItem(2, 1, QTableWidgetItem("Item 3"))
        self.table.setItem(3, 1, QTableWidgetItem("Item 4"))

        # Set row spanning
        self.table.setSpan(0, 0, self.table.rowCount(), 1)
        self.table.setSpan(2, 1, self.table.rowCount() - 2, 1)

        self.setCentralWidget(self.table)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
