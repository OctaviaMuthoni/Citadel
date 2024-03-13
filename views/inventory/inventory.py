"""
    This module shows a list of all library inventory items.
    These include:-
                - Chairs
                - Tables
                - Computers
                - Bookshelves
    An item belongs to either of these categories:- Furniture, Electronics, Cleaning Items, Utensils etc.
"""
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QWidget, QVBoxLayout, QToolBar, QHBoxLayout, QSplitter, QTableView

import qtawesome as qta

from models.inventory import InventoryModel
from models.sort_filter_proxy import SortFilterProxyModel
from views.share import FormField
from views.share import ComboBox
from views.share import SearchEdit


class InventoryView(QWidget):
    def __init__(self):
        super(InventoryView, self).__init__()

        self.condition_combo = ComboBox([
            "-- All --"
            "Ok",
            "Broken reparable",
            "Broken beyond repair"
        ])

        self.inventory_type_combo = ComboBox([
            "-- All --",
            "Furniture",
            "Electronics",
            "Other"
        ])

        self.search_edit = SearchEdit()

        self.actions_toolbar = QToolBar()
        self.actions_toolbar.setIconSize(QSize(25, 25))
        self.actions_toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.actions_toolbar.addWidget(QSplitter())
        self.actions_toolbar.addAction(qta.icon("fa5s.file-invoice-dollar", color='gray'), "Purchase")
        self.actions_toolbar.addAction(qta.icon("ph.arrows-left-right-light", color='gray'), "Transfer")
        # self.actions_toolbar.addAction(qta.icon("ph.printer", color='gray'), "Print")
        # self.actions_toolbar.addAction(qta.icon("ph.download", color='gray'), "Download")
        # self.actions_toolbar.addAction(qta.icon("mdi.book-remove-outline", color='gray'), "Remove")
        self.actions_toolbar.addAction(qta.icon("ph.pencil", color='gray'), "Edit")
        self.actions_toolbar.addAction(qta.icon("ph.plus", color='gray'), "New")

        self.actions_toolbar.setObjectName("in-page-menu")

        filters_layout = QHBoxLayout()
        filters_layout.addWidget(self.search_edit)
        filters_layout.addStretch()
        filters_layout.addWidget(FormField("Item type", self.inventory_type_combo))
        filters_layout.addWidget(FormField("Condition", self.condition_combo))

        self.model = InventoryModel()
        self.proxy_model = SortFilterProxyModel(self.model, text_columns=['name'])

        self.inventory_table = QTableView()
        self.inventory_table.setModel(self.proxy_model)

        layout = QVBoxLayout(self)
        layout.setSpacing(20)
        layout.addLayout(filters_layout)
        layout.addWidget(self.actions_toolbar)
        layout.addWidget(self.inventory_table)



