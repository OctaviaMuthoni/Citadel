import qtawesome as qta
from PySide6.QtCore import Qt, QPoint
from PySide6.QtWidgets import QLineEdit, QCalendarWidget, QPushButton, QHBoxLayout, QFrame


class DateEdit(QFrame):
    def __init__(self, placeholder):
        super(DateEdit, self).__init__()

        layout = QHBoxLayout(self)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText(placeholder)

        self.calendar_button = QPushButton()
        self.calendar_button.setFlat(True)
        self.calendar_button.setIcon(qta.icon("fa.calendar", color="#05ADD3"))
        self.calendar_button.clicked.connect(self.show_calendar)

        layout.addWidget(self.line_edit)
        layout.addWidget(self.calendar_button)

        self.calendar_widget = QCalendarWidget()
        self.calendar_widget.setWindowFlags(self.calendar_widget.windowFlags() | Qt.Popup)
        self.calendar_widget.clicked.connect(self.update_date)

        self.setObjectName("dateedit")
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.setFocusProxy(self.line_edit)

        self.setMaximumWidth(150)

    def show_calendar(self):
        point = self.mapToGlobal(QPoint(0, self.height()))
        height = self.calendar_widget.sizeHint().height()
        width = self.calendar_widget.sizeHint().width()
        self.calendar_widget.setGeometry(point.x() + self.line_edit.width(), point.y(), width, height)
        self.calendar_widget.show()

    def update_date(self):
        selected_date = self.calendar_widget.selectedDate()
        self.line_edit.setText(selected_date.toString("yyyy-MM-dd"))
        self.calendar_widget.close()
