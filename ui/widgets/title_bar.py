from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QPushButton

import qtawesome as qta


class TitleBar(QFrame):
    def __init__(self, title="", icon: QPixmap = QPixmap()):
        super(TitleBar, self).__init__()

        self.setObjectName("title-bar")
        self.setFixedHeight(30)

        self.title_lbl = QLabel(title)

        self.icon_lbl = QLabel()
        self.icon_lbl.setScaledContents(True)
        self.icon_lbl.setPixmap(icon)

        self.minimize_btn = QPushButton(qta.icon("fa5.window-minimize", color="silver"), "")
        # self.minimize_btn.setI
        self.maximize_btn = QPushButton(qta.icon("fa5s.window-restore", color="silver"), "")
        self.close_btn = QPushButton(qta.icon("fa.close", color="red"), "")

        layout = QHBoxLayout(self)
        layout.addWidget(self.icon_lbl)
        layout.addWidget(self.title_lbl)
        layout.addStretch()
        layout.addWidget(self.minimize_btn)
        layout.addWidget(self.maximize_btn)
        layout.addWidget(self.close_btn)

    def set_title(self, title):
        self.title_lbl.setText(title)

    def set_icon(self, icon):
        self.icon_lbl.setPixmap(icon)
