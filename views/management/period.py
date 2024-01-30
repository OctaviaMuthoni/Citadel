from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLabel, QPushButton, QGridLayout

from components import LineEdit, CustomTableView
from components.message import Notifier
# from models.period import PeriodModel


class PeriodManagementView(QWidget):
    def __init__(self):
        super(PeriodManagementView, self).__init__()

        # self.period_model = PeriodModel()

        layout = QVBoxLayout(self)

        self.start_date_lbl = QLabel()
        self.end_date_lbl = QLabel()
        self.period_lbl = QLabel()

        self.period_name_edit = LineEdit("Period:", placeholder="eg. Term 2, 2023")
        self.start_date_edit = LineEdit("Start date:", placeholder="April 29, 2023")
        self.end_date_edit = LineEdit("End date:", placeholder="August 4, 2023")

        self.periods_table = CustomTableView()
        self.periods_table.setObjectName("custom_table")
        # self.periods_table.setModel(self.period_model)

        self.open_header_widget = self.create_open_header()
        self.closed_header_widget = self.create_closed_header()

        layout.addWidget(self.open_header_widget)
        layout.addWidget(self.closed_header_widget)
        layout.addWidget(self.periods_table)

        self.render_header()
        # self.period_model.layoutChanged.connect(self.render_header)
        
    def create_open_header(self):
        open_period_widget = QWidget()
        open_period_layout = QFormLayout(open_period_widget)

        close_period_btn = QPushButton("Close Period")
        close_period_btn.clicked.connect(self.close_period)

        c_lbl = QLabel("Current Period")
        c_lbl.setObjectName("sbrand")
        open_period_layout.addWidget(c_lbl)
        open_period_layout.addWidget(self.period_lbl)
        open_period_layout.addWidget(self.start_date_lbl)
        open_period_layout.addWidget(self.end_date_lbl)
        open_period_layout.addWidget(close_period_btn)
        
        return open_period_widget
    
    def create_closed_header(self):
        open_period_btn = QPushButton("Start Period")
        open_period_btn.clicked.connect(self.open_period)

        no_open_period_widget = QWidget()
        no_open_period_layout = QGridLayout(no_open_period_widget)
        no_open_period_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        no_open_period_layout.addWidget(Notifier(), 0, 0, 1, 3)
        no_open_period_layout.addWidget(self.period_name_edit, 1, 0)
        no_open_period_layout.addWidget(self.start_date_edit, 1, 1)
        no_open_period_layout.addWidget(self.end_date_edit, 1, 2)

        no_open_period_layout.addWidget(open_period_btn, 2, 1)

        return no_open_period_widget
        
    def render_header(self):
        # current_period = self.period_model.get_open_period()
        # print(current_period)
        # if current_period:
        #     self.open_header_widget.setHidden(True)
        #     self.closed_header_widget.setHidden(False)
        #     self.start_date_lbl = QLabel(f"Start date: {current_period.start_date}")
        #     self.end_date_lbl = QLabel(f"End date: {current_period.end_date}")
        #     self.period_lbl = QLabel(f"Period: {current_period.period}")
        # else:
        #     self.closed_header_widget.setHidden(False)
        #     self.open_header_widget.setHidden(True)
        pass

    def open_period(self):
        # p = Period(
        #     period=self.period_name_edit.text(),
        #     start_date=self.start_date_edit.text(),
        #     end_date=self.end_date_edit.text()
        # )
        pass

        # self.period_model.start_period(p)

    def close_period(self):
        # self.period_model.close_period()
        pass
