import sys

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QToolBar, QApplication, QStackedWidget, QLabel, QFrame, QVBoxLayout, QWidget

import qtawesome as qta

from components import Header
from views import MembersView, MaterialsView, LoanView, PaymentsView, ScheduleView, ReportsView, CardsView, \
    ManagementView


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.header_widget = Header()

        # Menu setup
        self.tool_bar = QToolBar("Citadel")
        self.tool_bar.setIconSize(QSize(30, 30))
        self.tool_bar.setFixedWidth(250)
        self.tool_bar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.tool_bar.setFloatable(False)
        self.tool_bar.setMovable(False)

        brand_widget = QFrame()
        brand_layout = QVBoxLayout(brand_widget)
        brand_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        brand_pixmap = QPixmap("falcon.ico")
        self.brand_lbl = QLabel()
        self.brand_lbl.setFixedSize(QSize(140, 120))
        self.brand_lbl.setScaledContents(True)
        self.brand_lbl.setPixmap(brand_pixmap)

        brand_layout.addWidget(self.brand_lbl)

        self.tool_bar.addWidget(brand_widget)
        self.tool_bar.addSeparator()
        self.addToolBar(Qt.ToolBarArea.LeftToolBarArea, self.tool_bar)
        self.tool_bar.setObjectName("main_tool_bar")
        self.create_menu()

        self.prev_action = self.tool_bar.actions()[2]

        self.header_widget.set_title(self.prev_action.text())
        self.header_widget.set_icon(self.prev_action.icon())
        self.prev_action.setCheckable(True)
        self.prev_action.setChecked(True)

        self.content_widget = QStackedWidget()

        self.create_central_widget()

        self.event_handler()

    def event_handler(self):
        self.tool_bar.actionTriggered.connect(self.navigate)

    def navigate(self, action):
        idx = self.tool_bar.actions().index(action)
        
        self.content_widget.setCurrentIndex(idx - 2)
        self.prev_action.setChecked(False)
        action.setCheckable(True)
        action.setChecked(True)
        self.prev_action = action
        self.header_widget.set_title(action.text())
        self.header_widget.set_icon(action.icon())

    def create_menu(self):
        self.tool_bar.addAction(qta.icon("ph.user-light", color="cyan"), "Members")
        self.tool_bar.addAction(qta.icon("ph.books-light", color="cyan"), "Materials")
        self.tool_bar.addAction(qta.icon("ph.handshake-light", color="cyan"), "Loan")
        self.tool_bar.addAction(qta.icon("ph.newspaper-clipping-light", color="cyan"), "Cards")
        self.tool_bar.addAction(qta.icon("ph.currency-circle-dollar-light", color="cyan"), "Payments")
        self.tool_bar.addAction(qta.icon("ph.calendar-light", color="cyan"), "Schedule")
        self.tool_bar.addAction(qta.icon("ei.cogs", color="cyan"), "Management")
        self.tool_bar.addAction(qta.icon("ph.chart-line-light", color="cyan"), "Report")

    # Central widget setup
    def create_central_widget(self):
        central_widget = QWidget()

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

        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.header_widget)
        layout.addWidget(self.content_widget)

        self.setCentralWidget(central_widget)

