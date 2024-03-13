from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QVBoxLayout, QFrame, QListWidget, QLabel, QWidget, QSizePolicy, QHBoxLayout, QLineEdit, \
    QPushButton, QListView, QTreeView


class ListWidget(QFrame):
    def __init__(self, model):
        super(ListWidget, self).__init__()

        self.model = model

        self.title_lbl = QLabel("List Widget")

        self.list_widget = QTreeView()
        self.list_widget.setModel(self.model)

        self.item_edit = QLineEdit()
        self.save_btn = QPushButton("Save")

        self.item_frame = QFrame()
        item_layout = QHBoxLayout(self.item_frame)
        item_layout.addWidget(self.item_edit)
        item_layout.addWidget(self.save_btn)

        layout = QVBoxLayout(self)
        layout.addWidget(self.title_lbl)
        layout.addWidget(self.item_frame)
        layout.addWidget(self.list_widget)

        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setObjectName("list-widget")

        self.event_listener()

    def event_listener(self):
        self.save_btn.clicked.connect(self.add_item)

    def set_title(self, title: str):
        self.title_lbl.setText(title)

    def add_item(self):
         item = QStandardItem()
         item.setText(self.item_edit.text())

         it = QStandardItem()
         it.setText("text")

         row = self.model.rowCount()
         self.model.setItem(row, 0, item)
         self.model.setItem(row, 1, it)
