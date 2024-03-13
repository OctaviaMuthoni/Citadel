# other third party imports
import qtawesome as qta

# PySide6 library imports
from PySide6.QtCore import Qt, QSize, Signal, QRect, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QPixmap, QAction, QIcon
from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QDockWidget, QWidget, QFrame, QVBoxLayout, \
    QGraphicsDropShadowEffect, QLabel, QPushButton, QToolBar, QStackedWidget, QSizePolicy

# local imports
from views.cards import CardsView
from views.inventory import InventoryView
from views.loan import LoanView
from views.management import ManagementView
from views.materials import MaterialsView
from views.members import MembersView
from views.payment import PaymentsView
from views.reports import ReportsView
from views.schedule import ScheduleView


class MenuButton(QAction):
    def __init__(self, parent: QToolBar, icon: str, text: str):
        self._icon = qta.icon(icon, color="cyan", color_active="#05add3")

        super().__init__(self._icon, text.capitalize())

        parent.addAction(self)
        self.setToolTip("")
        self.setSeparator(True)
        self.setObjectName("menu-button")

        btn = parent.widgetForAction(self)

        btn.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        btn.setFixedHeight(35)
        btn.setMinimumWidth(180)


class Menu(QToolBar):
    navigateSignal = Signal(int, QAction)

    def __init__(self,
                 orientation: Qt.Orientation = Qt.Orientation.Horizontal,
                 button_style: Qt.ToolButtonStyle = Qt.ToolButtonStyle.ToolButtonTextBesideIcon):
        super().__init__()

        self.menu_buttons = [
            MenuButton(self, "ph.users-light", "members"),
            MenuButton(self, "ph.users-light", "cards"),
            MenuButton(self, "ph.books-light", "materials"),
            MenuButton(self, "ph.book", "catalogue"),
            MenuButton(self, "ph.handshake-light", "loan"),
            MenuButton(self, "ph.users-light", "billing"),
            MenuButton(self, "ph.newspaper-clipping-light", "inventory"),
            MenuButton(self, "ph.calendar-light", "schedule"),
            MenuButton(self, "ei.cogs", "management"),
            MenuButton(self, "ph.chart-line-light", "report"),
        ]

        self.actionTriggered.connect(self.trigger)
        self.setObjectName("menu")

        self.setIconSize(QSize(30, 30))
        self.setOrientation(orientation)
        self.setToolButtonStyle(button_style)

    def trigger(self, action: MenuButton):
        self.navigateSignal.emit(self.menu_buttons.index(action), action)


class Header(QFrame):
    def __init__(self):
        super(Header, self).__init__()

        layout = QHBoxLayout(self)
        self.setObjectName("header")

        shadow_effect = QGraphicsDropShadowEffect(self)
        shadow_effect.setBlurRadius(50)
        shadow_effect.setColor("#55000000")
        shadow_effect.setOffset(1, 5)
        self.setGraphicsEffect(shadow_effect)

        self.setFixedHeight(40)

        self.header_title_lbl = QLabel("Members")
        self.header_title_lbl.setObjectName("title")

        self.auth_user_lbl = QLabel()

        self.menu_toggle_btn = QPushButton()
        self.menu_toggle_btn.setFlat(True)
        self.menu_toggle_btn.setIconSize(QSize(30, 30))
        self.menu_toggle_btn.setObjectName("menu-toggle")
        self.menu_toggle_btn.setIcon(qta.icon("ph.list", color="#05ADD3"))

        layout.addWidget(self.menu_toggle_btn)
        layout.addWidget(self.header_title_lbl)
        layout.addStretch()
        layout.addWidget(self.auth_user_lbl)

    def set_title(self, title):
        self.header_title_lbl.setText(title)


class CentralWidget(QWidget):
    def __init__(self, parent):
        super(CentralWidget, self).__init__(parent)

        layout = QVBoxLayout(self)
        self.header = Header()
        self.content_widget = QStackedWidget()

        self.content_widget.addWidget(MembersView())
        self.content_widget.addWidget(CardsView())
        self.content_widget.addWidget(MaterialsView())
        self.content_widget.addWidget(LoanView())
        self.content_widget.addWidget(LoanView())
        self.content_widget.addWidget(PaymentsView())
        self.content_widget.addWidget(InventoryView())
        self.content_widget.addWidget(ScheduleView())
        self.content_widget.addWidget(ManagementView())
        self.content_widget.addWidget(ReportsView())

        layout.addWidget(self.header)
        layout.addWidget(self.content_widget)


class LMS(QMainWindow):
    def __init__(self):
        super(LMS, self).__init__()

        brand_pixmap = QPixmap("favicon.ico")
        self.brand_lbl = QLabel()
        self.brand_lbl.setFixedSize(QSize(140, 120))
        self.brand_lbl.setScaledContents(True)
        self.brand_lbl.setPixmap(brand_pixmap)

        brand_widget = QFrame()
        brand_layout = QVBoxLayout(brand_widget)
        brand_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        brand_layout.addWidget(self.brand_lbl)

        brand_widget.setObjectName("brand-widget")

        self.menu = Menu(Qt.Orientation.Vertical)
        self.menu.navigateSignal.connect(self.navigate)

        self.dock_menu = QDockWidget(self)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dock_menu)
        self.dock_menu.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea)
        self.dock_menu.setObjectName("dock-menu")
        self.dock_menu.setTitleBarWidget(brand_widget)
        self.dock_menu.setWidget(self.menu)

        self.slide_animation = QPropertyAnimation(self.dock_menu, b"geometry")
        self.slide_animation.setDuration(1000)
        self.slide_animation.setEasingCurve(QEasingCurve.Type.InOutCubic)
        start = self.mapToGlobal(self.menu.pos())
        print(start)
        self.slide_animation.setStartValue(self.dock_menu.geometry())
        self.slide_animation.setEndValue(QRect(self.dock_menu.geometry().topLeft().x(), self.dock_menu.geometry().topLeft().y(), 0, 0))

        self.central_widget = CentralWidget(self)
        self.central_widget.header.menu_toggle_btn.clicked.connect(self.slide_animation.start())
        self.setCentralWidget(self.central_widget)

        self.setWindowIcon(QIcon(":/favicon.ico"))
        self.setWindowTitle("Library Management System")

        with open("res/styles/light.qss") as styles:
            self.setStyleSheet(styles.read())

    def navigate(self, idx, action):
        self.central_widget.header.header_title_lbl.setText(action.text())
        self.central_widget.content_widget.setCurrentIndex(idx)
