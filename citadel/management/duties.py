from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem, QTextCursor
from PySide6.QtWidgets import QWidget, QGridLayout, QFormLayout, QButtonGroup, QCheckBox, QGroupBox, QHBoxLayout, \
    QPushButton, QListView, QTextEdit, QLabel, QSizePolicy

from components import LineEdit


class DutiesView(QWidget):
    def __init__(self):
        super(DutiesView, self).__init__()

        self.save_btn = QPushButton("Save")
        self.save_btn.clicked.connect(self.save_duty)

        self.duties_form = self.create_duties_form()
        self.duties_list = self.create_duties_list()
        self.allocation_list = self.create_allocation_list()

        layout = QGridLayout(self)
        layout.addLayout(self.duties_form, 0, 0)
        layout.addWidget(self.duties_list, 1, 0)
        layout.addWidget(self.allocation_list, 0, 1, 2, 1)

    def create_duties_form(self):
        duties_form = QFormLayout()
        duty_lineedit = LineEdit("Duty:", "eg. dusting shelves")
        days_btn_grp = QButtonGroup()

        mon_checkbox = QCheckBox("Mon")
        tue_checkbox = QCheckBox("Tue")
        wed_checkbox = QCheckBox("Wed")
        thurs_checkbox = QCheckBox("Thurs")
        fri_checkbox = QCheckBox("Fri")
        sat_checkbox = QCheckBox("Sat")
        sun_checkbox = QCheckBox("Sun")

        days_btn_grp.addButton(mon_checkbox)
        days_btn_grp.addButton(tue_checkbox)
        days_btn_grp.addButton(wed_checkbox)
        days_btn_grp.addButton(thurs_checkbox)
        days_btn_grp.addButton(fri_checkbox)
        days_btn_grp.addButton(sat_checkbox)
        days_btn_grp.addButton(sun_checkbox)

        days_grp_box = QGroupBox("Duty Action Days")
        days_grp_box_layout = QHBoxLayout(days_grp_box)

        for btn in days_btn_grp.buttons():
            days_grp_box_layout.addWidget(btn)

        duty_description = QTextEdit("Describe what assigned persons are expected to do.")

        duties_form.addWidget(duty_lineedit)
        duties_form.addWidget(days_grp_box)
        duties_form.addWidget(duty_description)
        duties_form.addWidget(self.save_btn)

        return duties_form

    def create_duties_list(self):
        duties_list = QListView()
        model = QStandardItemModel()
        for k, duty in enumerate([
            {"duty": "House keeping", "description": "Here you go"},
            {"duty": "front desk", "description": "You should do this and that"}
        ]):
            model.setItem(k, 0, QStandardItem(duty["duty"]))
            model.setItem(k, 1, QStandardItem(duty["description"]))

        duties_list.setModel(model)

        return duties_list

    def create_allocation_list(self):
        days = {
            "mon": "Monday",
            "tue": "Tuesday",
            "wed": "Wednesday",
            "thurs": "Thursday",
            "fri": "Friday",
            "sat": "Saturday"
        }

        w = QWidget()
        # w.setObjectName("white_back")
        w_layout = QGridLayout(w)

        row = 0
        col = 0

        for day, full_name in days.items():
            label = QLabel(full_name)
            text_edit = QTextEdit()
            text_edit.setObjectName("white_back")
            # Set up the QTextEdit properties
            text_edit.setPlainText("1. ")
            text_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            text_edit.setTabChangesFocus(True)
            text_edit.installEventFilter(self)

            # Add the QLabel and QTextEdit to the layout
            w_layout.addWidget(label, row, col, alignment=Qt.AlignCenter)
            w_layout.addWidget(text_edit, row + 1, col, alignment=Qt.AlignTop)

            # Move to the next column or row
            col += 1
            if col > 1:
                col = 0
                row += 2

        w_layout.setSpacing(10)
        # w.setObjectName("white_back")
        return w

    def eventFilter(self, obj, event):
        if event.type() == event.Type.KeyPress and event.key() == Qt.Key_Return:
            # Handle Enter key press to insert a new numbered list
            if isinstance(obj, QTextEdit):
                cursor = obj.textCursor()
                cursor.movePosition(QTextCursor.EndOfBlock)
                cursor.insertText('\n')
                cursor.insertText(str(cursor.blockNumber() + 1) + ". ")
                return True
        return super().eventFilter(obj, event)

    def save_duty(self):
        pass
