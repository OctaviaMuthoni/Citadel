"""
    This component is a window that defines a default structure for a nested window.
    The nested window can not be displayed through a menu button trigger from a main menu.
    Each of these windows has the following properties:
        - A back button - This is used to call back the calling window usually the parent window.
        - A window title - While the parent window has a title each of the sub-windows has a distinct title.

    This class enables each sub-window to have a standardized look and feel
"""
from PySide6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel, QWidget

import qtawesome as qta

from core import Colors, ICON_SIZE


class SubWindow(QFrame):
    def __init__(self, content_widget: QWidget, title: str = "Sub Window"):
        super(SubWindow, self).__init__()

        layout = QVBoxLayout(self)

        # ----------------------------- Start sub window header creation -----------------------------------
        header = QFrame()
        header_layout = QHBoxLayout(header)

        icon = qta.icon("ph.arrow-left-bold", color=Colors.PRIMARY)

        icon_lbl = QLabel()
        icon_lbl.setPixmap(icon.pixmap(ICON_SIZE))

        title_lbl = QLabel(title)
        title_lbl.setObjectName("sub_title")

        header_layout.addWidget(icon_lbl)
        header_layout.addWidget(title_lbl)
        header_layout.addStretch()
        # ---------------------------- End header creation -------------------------------------------------

        layout.addWidget(header)
        layout.addWidget(content_widget)

        self.setObjectName("sub_window")
