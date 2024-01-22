from PySide6.QtCore import QSize
from PySide6.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QPushButton, QFrame

import qtawesome as qta


class Search(QFrame):
    def __init__(self):
        super(Search, self).__init__()

        self.search_icon = QLabel()
        self.search_icon.setFixedSize(QSize(30, 30))
        self.search_icon.setPixmap(qta.icon("ph.magnifying-glass-light", color="#0598a8").pixmap(25))

        self.search_input = QLineEdit()
        self.search_input.setClearButtonEnabled(True)

        self.clear_btn = QPushButton()
        self.clear_btn.setIcon(qta.icon("ph.x-fill", color="red"))
        self.clear_btn.setFlat(True)
        self.clear_btn.hide()

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        layout.addWidget(self.search_icon)
        layout.addWidget(self.search_input)
        layout.addWidget(self.clear_btn)

        self.setObjectName("search")

    def clear(self):
        self.search_input.setText("")

    def show_clear_btn(self, txt):
        print(txt)
        if txt == "":
            self.clear_btn.hide()
        else:
            self.clear_btn.show()



