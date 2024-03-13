from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTableView, QPushButton, QToolBar

import qtawesome as qta

from models.categories_model import CategoriesModel
from models.materials import MaterialsModel
from views.share import ComboBox
from views.share import SearchEdit


class MaterialsView(QWidget):
    def __init__(self):
        super(MaterialsView, self).__init__()

        # get materials model
        self.materials_model = MaterialsModel()
        self.categories_model = CategoriesModel()

        layout = QVBoxLayout(self)

        self.search = SearchEdit()

        self.categories_combo = ComboBox([
            "Books",
            "Novels",
            "Story Books",
            "Articles",
            "Periodicals",
            "Magazines",
            "News Papers"
        ])

        self.sub_category_combo = ComboBox([
            "-- All topics --",
            "History",
            "Geography",
            "Biology",
            "Computing",
            "Agriculture",
            "Business",
            "Physics",
            "Chemistry",
            "Religion",
            "Health",
            "Mathematics",
            "Languages"
        ])

        self.add_material_btn = QPushButton("Add Material")

        header_layout = QHBoxLayout()
        header_layout.setContentsMargins(0, 15, 0, 15)
        header_layout.addWidget(self.search)
        header_layout.addStretch()
        header_layout.addWidget(self.categories_combo)
        # header_layout.addWidget(self.topics_combo)

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
