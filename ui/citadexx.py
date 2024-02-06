from PySide6.QtCore import Qt, QSize, Signal
from PySide6.QtGui import QPixmap, QAction, QIcon
from PySide6.QtWidgets import QMainWindow, QToolBar, QStackedWidget, QLabel, QFrame, QVBoxLayout

import qtawesome as qta
from ui.widgets import Header
from ui.views import MembersView, MaterialsView, LoanView, PaymentsView, ScheduleView, ReportsView, CardsView, \
    ManagementView

from core.settings import Settings
settings = Settings()

class MenuButton(QAction):
    def __init__(self, parent: QToolBar, icon: str, text: str):
        self._icon = qta.icon(icon, color="cyan", color_active="#05add3")

        super().__init__(self._icon, text)

        parent.addAction(self)
        self.setToolTip("")
        self.setSeparator(True)
        self.setObjectName("menu-button")


class Menu(QToolBar):
    navigateSignal = Signal(int, QAction)

    def __init__(self):
        super().__init__()

        # configure menu
        self.setFloatable(False)
        self.setMovable(False)
        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.setIconSize(QSize(30, 30))
        self.setToolTipDuration(0)

        brand_pixmap = QPixmap("favicon.ico")
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
            MenuButton(self, "ph.users-light", "members"),
            MenuButton(self, "ph.books-light", "materials"),
            MenuButton(self, "ph.book", "catalogue"),
            MenuButton(self, "ph.handshake-light", "loan"),
            MenuButton(self, "ph.newspaper-clipping-light", "cards"),
            MenuButton(self, "ph.currency-circle-dollar-light", "payments"),
            MenuButton(self, "ph.calendar-light", "schedule"),
            MenuButton(self, "ei.cogs", "management"),
            MenuButton(self, "ph.chart-line-light", "report"),
        ]

        self.actionTriggered.connect(self.trigger)
        self.setFixedWidth(220)
        self.setObjectName("menu")

    def trigger(self, action: MenuButton):
        self.navigateSignal.emit(self.menu_buttons.index(action), action)


class CentralWidget(QFrame):
    def __init__(self):
        super(CentralWidget, self).__init__()

        self.header = Header()
        self.content_widget = QStackedWidget()
        self.content_widget.setObjectName("content")

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
        layout.setContentsMargins(20, 10, 20, 20)
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

        # the header
        self.header_widget = Header()

        # the central widget
        self.central_widget = CentralWidget()
        self.setCentralWidget(self.central_widget)

        # Menu setup
        self.menu = Menu()
        self.addToolBar(Qt.ToolBarArea.LeftToolBarArea, self.menu)

        self.event_handler()
        self.load_styles()

    def event_handler(self):
        self.menu.navigateSignal.connect(self.central_widget.navigate)

    def load_styles(self):
        # application defaults to dark theme if no theme is set in settings.
        theme = settings.get_settings("application/theme", "light")
        stylesheet_path = f"resources/stylesheets/{theme}.qss"
        # read stylesheet and return
        with open(stylesheet_path) as stylesheet:
            self.setStyleSheet(stylesheet.read())