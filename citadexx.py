from PySide6.QtCore import Qt, QSize, Signal
from PySide6.QtGui import QPixmap, QAction, QIcon, QColor
from PySide6.QtWidgets import QMainWindow, QToolBar, QStackedWidget, QLabel, QFrame, QVBoxLayout, QWidget, QButtonGroup, \
    QToolButton, QGraphicsDropShadowEffect, QSizePolicy

import qtawesome as qta

from components import Header
from views import MembersView, MaterialsView, LoanView, PaymentsView, ScheduleView, ReportsView, CardsView, \
    ManagementView


class MenuButton(QAction):
    def __init__(self, parent: QToolBar, icon: str, text: str):

        self._icon = qta.icon(icon, color="cyan", color_active="#05add3")

        super().__init__(self._icon, text)

        tool_button = self.parent()
        print(tool_button)
        parent.addAction(self)
        # # configure menu button
        # self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        # # self.setFixedSize(QSize(240, 45))
        # # self.setFixedWidth(230)
        # self.setIconSize(QSize(60, 60))
        # self.setCheckable(True)
        self.setObjectName("menu-button")
        #
        # self.setFixedWidth(240)
        #
        # parent.addWidget(self)
        #
        # self.clicked.connect(self.click_handler)

    def click_handler(self, x):
        print(x)

class Menu(QToolBar):
    navigateSignal = Signal(int, QToolButton)

    def __init__(self):
        super().__init__()

        # configure menu
        # self.setFixedWidth(250)
        self.setFloatable(False)
        self.setMovable(False)
        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.setIconSize(QSize(30, 30))
        self.setToolTipDuration(0)

        palette = self.palette()
        palette.setColor(self.backgroundRole(), QColor("#fafafa"))
        self.setPalette(palette)

        # shadow_effect = QGraphicsDropShadowEffect(self)
        # shadow_effect.setBlurRadius(20)
        # shadow_effect.setColor("#aa05add3")
        # shadow_effect.setOffset(2, 2)
        # self.setGraphicsEffect(shadow_effect)

        brand_pixmap = QPixmap(":/favicon.ico")
        self.brand_lbl = QLabel()
        self.brand_lbl.setFixedSize(QSize(140, 120))
        self.brand_lbl.setScaledContents(True)
        self.brand_lbl.setPixmap(brand_pixmap)

        brand_widget = QFrame()
        brand_layout = QVBoxLayout(brand_widget)
        brand_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        brand_layout.addWidget(self.brand_lbl)

        self.addWidget(brand_widget)
        self.addSeparator()

        self.menu_buttons = [
            MenuButton(self, "ph.user-light", "Members"),
            MenuButton(self, "ph.books-light", "Materials"),
            MenuButton(self, "ph.handshake-light", "Loan"),
            MenuButton(self, "ph.newspaper-clipping-light", "Cards"),
            MenuButton(self, "ph.currency-circle-dollar-light", "Payments"),
            MenuButton(self, "ph.calendar-light", "Schedule"),
            MenuButton(self, "ei.cogs", "Management"),
            MenuButton(self, "ph.chart-line-light", "Report"),
        ]

        self.setObjectName("menu")


class CentralWidget(QFrame):
    def __init__(self):
        super(CentralWidget, self).__init__()

        self.header = Header()
        self.content_widget = QStackedWidget()

        members = MembersView()
        materials = MaterialsView()
        loan = LoanView()
        payment = PaymentsView()
        schedule = ScheduleView()
        reports = ReportsView()
        cards = CardsView()
        management = ManagementView()

        self.content_widget.addWidget(members)
        self.content_widget.addWidget(materials)
        self.content_widget.addWidget(loan)
        self.content_widget.addWidget(cards)
        self.content_widget.addWidget(payment)
        self.content_widget.addWidget(schedule)
        self.content_widget.addWidget(management)
        self.content_widget.addWidget(reports)

        layout = QVBoxLayout(self)
        layout.addWidget(self.header)
        layout.addWidget(self.content_widget)

    def navigate(self, index, btn):
        text = btn.text()
        icon = btn.icon().pixmap(256)
        self.header.set_title(text)
        self.header.set_icon(icon)
        self.content_widget.setCurrentIndex(index)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # # Customize the title bar height
        # title_bar = self.titleBar()
        # title_bar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        # title_bar.setFixedHeight(40)  #

        # the header
        self.header_widget = Header()

        # the central widget
        self.central_widget = CentralWidget()
        self.setCentralWidget(self.central_widget)

        # Menu setup
        self.menu = Menu()
        self.addToolBar(Qt.ToolBarArea.LeftToolBarArea, self.menu)

        self.event_handler()

    def event_handler(self):
        self.menu.navigateSignal.connect(self.central_widget.navigate)
