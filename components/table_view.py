from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QTableView, QHeaderView, QSizePolicy


class CustomTableView(QTableView):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Set the selection behavior to select the entire row
        self.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)

        # Limit to selection of only one row
        self.setSelectionMode(QTableView.SelectionMode.SingleSelection)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Remove row headers
        self.verticalHeader().setVisible(False)

        header = self.horizontalHeader()
        header.setStretchLastSection(True)
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Highlight, QColor("#230598a8"))
        palette.setColor(QPalette.ColorRole.HighlightedText, QColor("#656565"))
        self.setPalette(palette)

        self.setAlternatingRowColors(True)
