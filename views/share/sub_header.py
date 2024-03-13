from PySide6.QtCore import Signal, QSize
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QFrame, QLabel, QHBoxLayout, QPushButton

import qtawesome as qta


class SubHeader(QFrame):
    backSignal = Signal()

    def __init__(self, title):
        super(SubHeader, self).__init__()

        self.title_lbl = QLabel(title)
        self.title_lbl.setObjectName("sub-title")

        self.back_btn = QPushButton()
        self.back_btn.setFlat(True)
        self.back_btn.setIconSize(QSize(30, 30))
        self.back_btn.setFixedWidth(40)
        self.back_btn.setIcon(qta.icon("ph.arrow-left", options=[{
            "color": "#05ADD3",
            "color_active": "#f9f9f9"
        }]).pixmap(35))
        self.back_btn.clicked.connect(self.backSignal.emit)

        self.setObjectName("sub-header")
        self.setFixedHeight(35)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.back_btn)
        layout.addWidget(self.title_lbl)
