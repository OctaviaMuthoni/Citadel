from PySide6.QtCore import QDate, QSize, Qt, QObject, QEvent
from PySide6.QtWidgets import QFrame, QDateEdit, QHBoxLayout, QPushButton, QCalendarWidget

import qtawesome as qta


class DateEdit(QFrame):

    def __init__(self, date: QDate = None):
        super(DateEdit, self).__init__()

        layout = QHBoxLayout(self)

        self.date_edit = QDateEdit()
        self.calendar_view = QCalendarWidget()
        self.calendar_view.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.calendar_btn = QPushButton(qta.icon("ph.calendar-light", color="teal"), "Calendar")
        self.calendar_btn.setFlat(True)
        self.calendar_btn.setIconSize(QSize(30, 30))
        self.calendar_btn.clicked.connect(self.show_calendar)
        if date:
            self.date_edit.setDate(date)

        layout.addWidget(self.date_edit)
        layout.addWidget(self.calendar_btn)

        self.setObjectName("date-edit")
        # self.installEventFilter(self)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.HoverEnter:
            print(obj)
            return True
        return super().eventFilter(obj, event)

    def show_calendar(self):
        x = self.calendar_btn.x()
        y = self.calendar_btn.y()
        self.calendar_view.setGeometry(x, y, 300, 300)
        self.calendar_view.show()