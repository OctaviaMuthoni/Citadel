import qtawesome as qta
from PySide6.QtCore import QSize, Qt, Signal
from PySide6.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QFrame


class SearchEdit(QFrame):

    textChanged = Signal(str)

    def __init__(self):
        super(SearchEdit, self).__init__()

        self.search_icon = QLabel()
        self.search_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.search_icon.setFixedSize(QSize(30, 30))
        self.search_icon.setPixmap(qta.icon("ph.magnifying-glass-light", color="#0598a8").pixmap(25))

        self.search_input = QLineEdit()
        self.search_input.setClearButtonEnabled(True)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        layout.addWidget(self.search_icon)
        layout.addWidget(self.search_input)

        self.setFixedHeight(30)
        self.setObjectName("search-widget")

        self.search_input.textChanged.connect(self.textChanged.emit)

    def text(self) -> str:
        return self.search_input.text()



