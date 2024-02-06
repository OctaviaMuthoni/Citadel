from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QWidget, QVBoxLayout, QToolBar, QLabel, QStackedWidget

import qtawesome as qta

from ui.views.management.duties import DutiesView
from ui.views.management.institution import ManageInstitutionView
from ui.views.management.period import PeriodManagementView
from ui.views.management.rules import ManageRulesView


class ManagementView(QWidget):
    def __init__(self):
        super(ManagementView, self).__init__()

        layout = QVBoxLayout(self)

        # management actions
        self.manage_periods_action = QAction(qta.icon("ph.calendar", color="#05add3"), "periods", checkable=True)
        self.current_action = self.manage_periods_action
        self.current_action.setChecked(True)
        self.manage_users_action = QAction(qta.icon("ph.user", color="#05add3"), "users", checkable=True)
        self.manage_time_action = QAction(qta.icon("ph.clock", color="#05add3"), "time", checkable=True)
        self.manage_duties_action = QAction(qta.icon("ei.broom", color="#05add3"), "duties", checkable=True)
        self.manage_rules_action = QAction(qta.icon("ph.clipboard-text", color="#05add3"), "rules", checkable=True)
        self.manage_member_action = QAction(qta.icon("ph.buildings", color="#05add3"), "institution", checkable=True)

        self.tool_bar = QToolBar()
        self.tool_bar.setObjectName("white_back")
        self.tool_bar.setIconSize(QSize(25, 25))
        self.tool_bar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.tool_bar.addAction(self.manage_periods_action)
        self.tool_bar.addSeparator()
        self.tool_bar.addAction(self.manage_users_action)
        self.tool_bar.addSeparator()
        self.tool_bar.addAction(self.manage_time_action)
        self.tool_bar.addSeparator()
        self.tool_bar.addAction(self.manage_duties_action)
        self.tool_bar.addSeparator()
        self.tool_bar.addAction(self.manage_rules_action)
        self.tool_bar.addSeparator()
        self.tool_bar.addAction(self.manage_member_action)

        self.manage_users_widget = QLabel("Users")
        self.manage_periods_widget = PeriodManagementView()
        self.manage_rules_widget = ManageRulesView()
        self.manage_time_widget = QLabel("Time")
        self.manage_duties_widget = DutiesView()
        self.manage_institution_widget = ManageInstitutionView()

        self.central_widget = QStackedWidget()
        self.central_widget.addWidget(self.manage_periods_widget)
        self.central_widget.addWidget(self.manage_users_widget)
        self.central_widget.addWidget(self.manage_rules_widget)
        self.central_widget.addWidget(self.manage_time_widget)
        self.central_widget.addWidget(self.manage_duties_widget)
        self.central_widget.addWidget(self.manage_institution_widget)

        layout.addWidget(self.tool_bar)
        layout.addWidget(self.central_widget)

        self.tool_bar.actionTriggered.connect(self.update_view)

    def update_view(self, action):
        self.current_action.setChecked(False)
        self.current_action = action
        self.current_action.setChecked(True)
        text = action.text()
        w = self.__getattribute__(f"manage_{text}_widget")
        self.central_widget.setCurrentWidget(w)

