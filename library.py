from PySide6.QtCore import Qt, QSize, Signal
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout, QGraphicsDropShadowEffect, QPushButton, \
    QStackedWidget, QTableView, QDialog, QLineEdit

import qtawesome as qta

from views import Materials
from views import SettingsView
from views import ManagementView
from views import MembersView


class MenuButton(QPushButton):
    menuButtonClicked = Signal(object)

    def __init__(self, btn_text, icon):
        super(MenuButton, self).__init__()

        self.icon_name = icon
        self._icon = qta.icon(self.icon_name, color="cyan")
        self.setIcon(self._icon)

        self.setText(btn_text)

        self.setIconSize(QSize(30, 30))
        self.setObjectName("menu-btn")

        self.clicked.connect(self.menu_button_clicked)

    def menu_button_clicked(self):
        self.menuButtonClicked.emit(self)


class SideMenu(QWidget):
    btnClickedSignal = Signal(object)

    def __init__(self):
        super(SideMenu, self).__init__()

        self.setObjectName("menu")

        self.members = MenuButton("Members", "ph.user-list-light")
        self.materials = MenuButton("Materials", "ph.books-light")
        self.transactions = MenuButton("Transactions", "ph.arrows-left-right-light")
        self.loss = MenuButton("Loss and Damages", "ph.bandaids-light")
        self.time_schedule = MenuButton("Time Schedule", "ph.calendar-light")
        self.manage_library = MenuButton("Management", "ei.cogs")
        self.reports = MenuButton("Reports", "ph.chart-line-light")

        self.settings = MenuButton("Settings", "ph.gear-six-light")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 20, 10, 10)
        layout.addWidget(self.members)
        layout.addWidget(self.materials)
        layout.addWidget(self.transactions)
        layout.addWidget(self.loss)
        layout.addWidget(self.time_schedule)
        layout.addWidget(self.manage_library)
        layout.addWidget(self.reports)
        layout.addStretch()
        layout.addWidget(self.settings)

        for child in self.children():
            if type(child) == MenuButton:
                child.menuButtonClicked.connect(self.btn_clicked)

    def btn_clicked(self, btn):
        self.btnClickedSignal.emit(btn)


class Transactions(QWidget):
    def __init__(self):
        super(Transactions, self).__init__()

        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("Transactions"))


class LossDamage(QWidget):
    def __init__(self):
        super(LossDamage, self).__init__()

        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("LossDamage"))


class ScheduleDialog(QDialog):
    def __init__(self):
        super(ScheduleDialog, self).__init__()


class TimeSchedule(QWidget):
    def __init__(self):
        super(TimeSchedule, self).__init__()

        self.add_btn = QPushButton("Add")
        self.table_schedule = QTableView()

        self.schedule_dialog = ScheduleDialog()

        self.search_edit = QLineEdit()
        self.search_edit.setClearButtonEnabled(True)
        self.search_edit.setObjectName("search")

        options_layout = QHBoxLayout()
        options_layout.addWidget(self.search_edit)
        options_layout.addStretch()
        options_layout.addWidget(self.add_btn)

        layout = QVBoxLayout(self)
        layout.addLayout(options_layout)
        layout.addWidget(self.table_schedule)

        self.add_btn.clicked.connect(self.show_dialog)

    def show_dialog(self):
        self.schedule_dialog.show()


class Reports(QWidget):
    def __init__(self):
        super(Reports, self).__init__()

        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("Reports"))


class ContentWidget(QStackedWidget):
    def __init__(self):
        super(ContentWidget, self).__init__()

        self.members = MembersView()
        self.materials = Materials()
        self.transactions = Transactions()
        self.loss_and_damages = LossDamage()
        self.time_schedule = TimeSchedule()
        self.reports = Reports()
        self.settings = SettingsView()
        self.management = ManagementView()

        self.addWidget(self.members)
        self.addWidget(self.materials)
        self.addWidget(self.transactions)
        self.addWidget(self.loss_and_damages)
        self.addWidget(self.time_schedule)
        self.addWidget(self.management)
        self.addWidget(self.reports)
        self.addWidget(self.settings)
        self.addWidget(self.members)

        self.setObjectName("content-widget")


class Library(QWidget):
    def __init__(self, user, settings):
        super(Library, self).__init__()

        # self.auth_user = user
        self.settings = settings

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        side_menu = QWidget()
        side_menu_layout = QVBoxLayout(side_menu)
        side_menu.setMinimumWidth(250)
        side_menu.setObjectName("side-menu")

        self.brand_lbl = QLabel("The Citadel")
        self.brand_lbl.setFixedHeight(60)
        self.brand_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.brand_lbl.setObjectName("brand")
        shadow_effect = QGraphicsDropShadowEffect(self)
        shadow_effect.setBlurRadius(50)
        shadow_effect.setColor("#f2f2f2")
        shadow_effect.setOffset(10, 3)
        self.brand_lbl.setGraphicsEffect(shadow_effect)

        self.menu = SideMenu()
        self.menu.btnClickedSignal.connect(self.render_window)

        side_menu_layout.setContentsMargins(0, 0, 0, 0)
        side_menu_layout.addWidget(self.brand_lbl)
        side_menu_layout.addWidget(self.menu)

        header = QWidget()
        header.setObjectName("header")
        shadow_effect = QGraphicsDropShadowEffect(self)
        shadow_effect.setBlurRadius(30)
        shadow_effect.setColor("#787878")
        shadow_effect.setOffset(4, 4)
        header.setGraphicsEffect(shadow_effect)

        header.setFixedHeight(45)
        header_layout = QHBoxLayout(header)
        self.window_title = QLabel("Transactions")
        self.window_title.setObjectName("window-title")
        active_user = QLabel("jhk")
        self.window_icon = QLabel()
        self.window_icon.setPixmap(qta.icon("ph.arrows-left-right-light", color="#05cff6").pixmap(35))
        header_layout.addWidget(self.window_icon)
        header_layout.addWidget(self.window_title)
        header_layout.addStretch()
        header_layout.addWidget(active_user)

        self.content_widget = ContentWidget()
        self.content_widget.settings.settings = self.settings
        self.content_widget.setCurrentWidget(self.content_widget.transactions)

        self.central_widget = QWidget()
        self.central_layout = QVBoxLayout(self.central_widget)
        self.central_layout.addWidget(header)
        self.central_layout.addWidget(self.content_widget)
        self.setObjectName("central-widget")

        layout.addWidget(side_menu)
        layout.addWidget(self.central_widget)

    def render_window(self, btn):
        """
        :param btn:
        :return:
        """
        self.window_title.setText(btn.text())
        self.window_icon.setPixmap(qta.icon(btn.icon_name, color="#05add3").pixmap(35))
        self.content_widget.setCurrentWidget(self.content_widget.__getattribute__(btn.text().replace(" ", "_").lower()))

    def set_user(self, user):
        pass
