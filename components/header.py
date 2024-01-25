from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QHBoxLayout, QFrame, QGraphicsDropShadowEffect, QLabel


class Header(QFrame):
    def __init__(self):
        super(Header, self).__init__()

        layout = QHBoxLayout(self)

        self.setObjectName("header")

        shadow_effect = QGraphicsDropShadowEffect(self)
        shadow_effect.setBlurRadius(30)
        shadow_effect.setColor("#787878")
        shadow_effect.setOffset(4, 4)
        self.setGraphicsEffect(shadow_effect)

        self.setFixedHeight(45)

        self.header_title_lbl = QLabel("Default header text")
        self.header_title_lbl.setObjectName("title")

        self.active_user_lbl = QLabel()
        self.header_icon_lbl = QLabel()

        layout.addWidget(self.header_icon_lbl)
        layout.addWidget(self.header_title_lbl)
        layout.addStretch()
        layout.addWidget(self.active_user_lbl)

    def set_title(self, title):
        self.header_title_lbl.setText(title)

    def set_icon(self, icon):
        pixmap = icon.pixmap(512)
        mask = pixmap.createMaskFromColor(QColor('cyan'), Qt.MaskOutColor)
        pixmap.fill(QColor("teal"))
        pixmap.setMask(mask)
        pixmap = pixmap.scaled(35, 35, aspectMode=Qt.KeepAspectRatio,
                               mode=Qt.SmoothTransformation)
        self.header_icon_lbl.setPixmap(pixmap)