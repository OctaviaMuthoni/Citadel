from PySide6.QtWidgets import QWidget, QVBoxLayout

from views.share import SearchEdit, SubHeader


class DepartmentsView(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        self.header = SubHeader("Departments")
        self.search_edit = SearchEdit()

        layout.addWidget(self.header)
        layout.addWidget(self.search_edit)
