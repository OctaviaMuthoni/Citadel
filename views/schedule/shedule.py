from PySide6.QtCore import QDate, Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QLabel, QHeaderView, QHBoxLayout, \
    QComboBox, QFrame, QLineEdit, QStyledItemDelegate, QTableWidgetItem
import qtawesome as qta

from views.share import PushButton
# from share import PushButton
from views.share.search_edit import SearchEdit

# from share import Search

# TODO: Load actual data about the current period from the database
period = {
    "start_date": QDate(2024, 1, 8),
    "end_date": QDate(2024, 4, 16),
    "period_name": "Term One 2024",
    "status": "current"
}


class RotatedTextDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        text = index.data(Qt.DisplayRole)
        if text:
            painter.save()
            painter.translate(option.rect.center())
            painter.rotate(-90)
            painter.drawText(0, 0, text)
            painter.restore()


class ScheduleView(QWidget):
    def __init__(self):
        super(ScheduleView, self).__init__()

        self.v_headers = []
        self.h_headers = [
            "8:00am\n-\n8:40am",
            "8:40am\n-\n9:20am",
            "9:20am\n-\n9:30am",
            "9:30am\n-\n10:10am",
            "10:10am\n-\n10:50am",
            "10:50am\n-\n11:20am",
            "11:20am\n-\n12:00pm",
            "12:00pm\n-\n12:40pm",
            "12:40pm\n-\n2:00pm",
            "2:00pm\n-\n2:40pm",
            "2:40pm\n-\n3:20pm",
            "3:20am\n-\n4:00am",
            "4:00am\n-\n5:00am"
        ]

        layout = QVBoxLayout(self)
        layout.setSpacing(20)
        self.search_widget = SearchEdit()

        self.month_combo = QComboBox()
        self.week_combo = QComboBox()

        self.schedule_table = QTableWidget(7, 13)
        self.schedule_table.setHorizontalHeaderLabels(self.h_headers)
        self.schedule_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.schedule_table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.schedule_table.setAlternatingRowColors(True)
        self.schedule_table.setObjectName("scheduler")
        self.schedule_table.setSpan(0, 2, self.schedule_table.rowCount(), 1)
        self.schedule_table.setSpan(0, 5, self.schedule_table.rowCount(), 1)
        self.schedule_table.setSpan(0, 8, self.schedule_table.rowCount(), 1)
        self.schedule_table.setSpan(0, 12, self.schedule_table.rowCount(), 1)

        self.schedule_table.setItem(0, 2, QTableWidgetItem("Short Break"))
        self.schedule_table.setItem(0, 5, QTableWidgetItem("Long Break"))
        self.schedule_table.setItem(0, 8, QTableWidgetItem("Lunch Break"))
        self.schedule_table.setItem(0, 12, QTableWidgetItem("Borrowing and Returning"))

        self.schedule_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        # for row in range(self.schedule_table.rowCount()):
        #     self.schedule_table.setRowHeight(row, 60)
        self.schedule_table.setMaximumHeight(400)
        self.schedule_table.setItemDelegate(RotatedTextDelegate())
        # self.schedule_table.setItemDelegateForColumn(4, RotatedTextDelegate())
        # self.schedule_table.setItemDelegateForColumn(8, RotatedTextDelegate())
        # self.schedule_table.setItemDelegateForColumn(12, RotatedTextDelegate())

        self.preview_widget = QWidget()
        self.preview_widget.setFixedWidth(300)

        # self.splitter_widget = QSplitter()
        # self.splitter_widget.addWidget(self.schedule_table)

        self.first_btn = PushButton("", qta.icon("ph.caret-double-left-light"))
        self.prev_btn = PushButton("", qta.icon("ph.caret-left-light"))
        self.week_edit = QLineEdit()
        self.next_btn = PushButton("", qta.icon("ph.caret-right-light"))
        self.last_btn = PushButton("", qta.icon("ph.caret-double-right-light"))

        self.pagination_widget = QFrame()
        self.pagination_widget.setFixedHeight(40)
        pagination_layout = QHBoxLayout(self.pagination_widget)
        pagination_layout.addStretch()
        pagination_layout.addWidget(self.first_btn)
        pagination_layout.addWidget(self.prev_btn)
        pagination_layout.addWidget(self.week_edit)
        pagination_layout.addWidget(self.next_btn)
        pagination_layout.addWidget(self.last_btn)
        pagination_layout.addStretch()

        filter_layout = QHBoxLayout()
        filter_layout.addWidget(self.search_widget)
        filter_layout.addStretch()
        filter_layout.addWidget(QLabel("Current Period"))
        filter_layout.addWidget(self.month_combo)
        filter_layout.addWidget(self.week_combo)

        # layout.addWidget(self.search_widget)
        layout.addLayout(filter_layout)
        # layout.addSpacerItem(QSpacerItem(100, 100))
        layout.addWidget(self.schedule_table)

        self.configure_schedule()

    def go_first(self):
        pass

    def go_prev(self):
        pass

    def go_next(self):
        pass

    def go_last(self):
        pass

    def configure_schedule(self):
        # get current date
        today = QDate().currentDate()
        weeks_no = self.get_weeks_number()
        self.week_combo.addItems([f"week {i}" for i in range(1, weeks_no + 1)])

        # today
        day = today.day() - today.dayOfWeek()
        year = today.year()
        month = today.month()

        for i in range(7):
            d = QDate(year, month, day)
            # print(d.toString())
            self.v_headers.append(d.toString())
            day += 1

        # print(self.v_headers)
        self.schedule_table.setVerticalHeaderLabels(self.v_headers)

        # get current week
        current_week = today.weekNumber()[0] - period["start_date"].weekNumber()[0] + 1
        self.week_combo.setCurrentText(f"week {current_week}")
        # date = QDate().

    def get_weeks_number(self) -> int:
        """
        This method computes the number of weeks between start of current period and the end date.
        :return: int - representing number of weeks.
        """
        return period["end_date"].weekNumber()[0] - period["start_date"].weekNumber()[0] + 1
