from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QApplication, QTableView, QStyledItemDelegate, QMainWindow, \
    QVBoxLayout, QWidget, QTableWidgetItem, QTableWidget
from PySide6.QtCore import Qt, QItemSelectionModel, QAbstractTableModel


class TableCellDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        # Custom painting logic for the cell
        if index.row() == 1 and index.column() == 2:
            painter.fillRect(option.rect, Qt.red)  # Example: Set background color to red for cell (1, 2)

        super().paint(painter, option, index)


class TableHighlighter(QMainWindow):
    def __init__(self):
        super().__init__()

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        table_view = QTableView(self)
        layout.addWidget(table_view)

        table_model = self.populate_model()
        table_view.setModel(table_model)

        # Set a custom delegate to handle cell styling
        delegate = TableCellDelegate(self)
        table_view.setItemDelegate(delegate)

        # Select a specific cell programmatically
        selection_model = table_view.selectionModel()
        index_to_select = table_model.index(1, 2)  # Row 1, Column 2
        selection_model.select(index_to_select, QItemSelectionModel.Select)

    def populate_model(self):
        rows = 5
        cols = 3

        table_model = QStandardItemModel(rows, cols)

        # Populate the model with some sample data
        for row in range(rows):
            for col in range(cols):
                item = QStandardItem(f"Row {row}, Col {col}")
                table_model.setItem(row, col, item)

        return table_model


if __name__ == "__main__":
    app = QApplication([])
    window = TableHighlighter()
    window.show()
    app.exec()
