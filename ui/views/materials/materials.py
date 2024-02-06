from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QTableView, QPushButton, \
    QToolBar

import qtawesome as qta
from ui.widgets import Search


class MaterialsView(QWidget):
    def __init__(self):
        super(MaterialsView, self).__init__()

        search_widget = Search()

        self.setObjectName("search-field")

        layout = QVBoxLayout(self)

        self.search = Search()
        self.categories_combo = QComboBox()
        self.categories_combo.addItems([
            "Books",
            "Novels",
            "Story Books",
            "Articles",
            "Periodicals",
            "Magazines",
            "News Papers"
        ])
        self.grades_combo = QComboBox()
        self.grades_combo.addItems([
            "-- All grades --",
            "Grade 1",
            "Grade 2",
            "Grade 3",
            "Grade 4",
            "Grade 5",
            "Grade 6",
            "Grade 7",
            "Grade 8",
            "Grade 9",
            "Grade 10",
            "Grade 11",
            "Grade 12"
        ])
        self.grades_combo.insertSeparator(4)
        self.grades_combo.insertSeparator(7)
        self.grades_combo.insertSeparator(10)

        self.add_material_btn = QPushButton("Add Material")

        header_layout = QHBoxLayout()
        header_layout.setContentsMargins(0, 15, 0, 15)
        header_layout.addWidget(search_widget)
        header_layout.addStretch()
        header_layout.addWidget(self.categories_combo)
        header_layout.addWidget(self.grades_combo)

        self.tool_bar = QToolBar()
        self.tool_bar.setObjectName("white_back")
        self.tool_bar.setIconSize(QSize(25, 25))
        self.tool_bar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.tool_bar.addAction(qta.icon("ph.eye"), "View")
        self.tool_bar.addSeparator()
        self.tool_bar.addAction(qta.icon("ph.pencil"), "Edit")
        self.tool_bar.addSeparator()
        self.tool_bar.addAction(qta.icon("ph.arrows-left-right-light"), "Loan")
        self.tool_bar.addSeparator()
        self.tool_bar.addAction(qta.icon("ph.plus"), "Create")

        layout.addLayout(header_layout)
        layout.addWidget(self.tool_bar)
        layout.addWidget(QTableView())
