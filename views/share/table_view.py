from PySide6.QtWidgets import QTableView, QHeaderView


class TableView(QTableView):
    def __init__(self):
        super().__init__()

        vertical_header = self.verticalHeader()
        vertical_header.setHidden(True)

        horizontal_header = self.horizontalHeader()
        horizontal_header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # on click select a single row
        self.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.setSelectionMode(QTableView.SelectionMode.SingleSelection)

        # Ensure table is readonly
        self.setEditTriggers(QTableView.EditTrigger.NoEditTriggers)

        self.setAlternatingRowColors(True)
