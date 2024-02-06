from datetime import datetime, timedelta

from PySide6.QtCore import QDate, Qt
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QVBoxLayout, QTableWidget, QLabel, QHeaderView, QHBoxLayout, \
    QSplitter, QComboBox, QFrame, QLineEdit
import qtawesome as qta
from ui.widgets import Search, PushButton, LineEdit

# TODO: Load actual data about the current period from the database
period = {
    "start_date": QDate(2024, 1, 8),
    "end_date": QDate(2024, 4, 16),
    "period_name": "Term One 2024",
    "status": "current"
}


class ScheduleView(QWidget):
    def __init__(self):
        super(ScheduleView, self).__init__()

    #     self.v_headers = []
    #     self.h_headers = [
    #         "8:00am \n - \n 9:00am",
    #         "9:00am \n - \n 10:00am",
    #         "10:00am \n - \n 11:00am",
    #         "11:00am \n - \n 12:00 noon",
    #         "12:00 noon \n - \n 1:00pm",
    #         "1:00pm \n - \n 2:00pm",
    #         "2:00pm \n - \n 3:00pm",
    #         "3:00pm \n - \n 5:00pm",
    #     ]
    #
    #     layout = QVBoxLayout(self)
    #
    #     self.search_widget = Search()
    #
    #     self.month_combo = QComboBox()
    #     self.week_combo = QComboBox()
    #
    #     self.schedule_table = QTableWidget(6, 8)
    #     self.schedule_table.setHorizontalHeaderLabels(self.h_headers)
    #     self.schedule_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    #     self.schedule_table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    #     self.schedule_table.setAlternatingRowColors(True)
    #     self.schedule_table.setObjectName("scheduler")
    #
    #     self.preview_widget = QWidget()
    #     self.preview_widget.setFixedWidth(300)
    #
    #     self.splitter_widget = QSplitter()
    #     self.splitter_widget.addWidget(self.schedule_table)
    #     self.splitter_widget.addWidget(self.preview_widget)
    #
    #     self.first_btn = PushButton(self.go_first, "", qta.icon("ph.caret-double-left-light"))
    #     self.prev_btn = PushButton(self.go_prev, "", qta.icon("ph.caret-left-light"))
    #     self.week_edit = QLineEdit()
    #     self.next_btn = PushButton(self.go_next, "", qta.icon("ph.caret-right-light"))
    #     self.last_btn = PushButton(self.go_last, "", qta.icon("ph.caret-double-right-light"))
    #
    #     self.pagination_widget = QFrame()
    #     self.pagination_widget.setFixedHeight(40)
    #     pagination_layout = QHBoxLayout(self.pagination_widget)
    #     pagination_layout.addStretch()
    #     pagination_layout.addWidget(self.first_btn)
    #     pagination_layout.addWidget(self.prev_btn)
    #     pagination_layout.addWidget(self.week_edit)
    #     pagination_layout.addWidget(self.next_btn)
    #     pagination_layout.addWidget(self.last_btn)
    #     pagination_layout.addStretch()
    #
    #     filter_layout = QHBoxLayout()
    #     filter_layout.addWidget(QLabel("Current Period"))
    #     filter_layout.addWidget(self.month_combo)
    #     filter_layout.addWidget(self.week_combo)
    #     filter_layout.addStretch()
    #
    #     layout.addWidget(self.search_widget)
    #     layout.addLayout(filter_layout)
    #     layout.addWidget(self.splitter_widget)
    #     layout.addWidget(self.pagination_widget)
    #
    #     self.configure_schedule()
    #
    # def go_first(self):
    #     pass
    #
    # def go_prev(self):
    #     pass
    #
    # def go_next(self):
    #     pass
    #
    # def go_last(self):
    #     pass
    #
    # def configure_schedule(self):
    #     # get current date
    #     today = QDate().currentDate()
    #     weeks_no = self.get_weeks_number()
    #     self.week_combo.addItems([f"week {i}" for i in range(1, weeks_no + 1)])
    #
    #     # today
    #     day = today.day() - today.dayOfWeek()
    #     year = today.year()
    #     month = today.month()
    #
    #     for i in range(7):
    #         d = QDate(year, month, day)
    #         self.v_headers.append(d.toString())
    #         day += 1
    #
    #     self.schedule_table.setVerticalHeaderLabels(self.v_headers)
    #
    #     # get current week
    #     current_week = today.weekNumber()[0] - period["start_date"].weekNumber()[0] + 1
    #     self.week_combo.setCurrentText(f"week {current_week}")
    #     # date = QDate().
    #
    # def get_weeks_number(self) -> int:
    #     """
    #     This method computes the number of weeks between start of current period and the end date.
    #     :return: int - representing number of weeks.
    #     """
    #     return period["end_date"].weekNumber()[0] - period["start_date"].weekNumber()[0] + 1
