from PySide6.QtCharts import QChart, QChartView, QLineSeries
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QFormLayout, QGroupBox, QLabel

from views.share import SubHeader
from views.share.image_widget import ImageWidget


class MemberProfileView(QWidget):

    backSignal = Signal()

    def __init__(self):
        super(MemberProfileView, self).__init__()

        self.image_preview = ImageWidget()

        self.member_status_lbl = QLabel("Active")
        self.setObjectName("status-active")

        self.member_balance_lbl = QLabel("0.00")
        self.member_balance_lbl.setObjectName("balance")

        self.header = SubHeader("Profile")

        self.activity_chart = QChartView()
        self.activity_chart.setMaximumHeight(200)
        chart = QChart()
        series = QLineSeries()
        series.append(1.2, 4)
        series.append(1.4, 6)
        series.append(1.8, 8)
        series.append(2.0, 12)
        series.append(1.2, 4)
        chart.addSeries(series)
        self.activity_chart.setChart(chart)

        layout = QVBoxLayout(self)

        personal_details_layout = QHBoxLayout()
        details_form_layout = QFormLayout()

        personal_details_layout.addWidget(self.image_preview)
        personal_details_layout.addLayout(details_form_layout)
        personal_details_layout.addStretch()
        personal_details_layout.addWidget(self.activity_chart)

        self.profile_group = QGroupBox()

        layout.addWidget(self.header)
        layout.addLayout(personal_details_layout)
        layout.addWidget(self.profile_group)

    def set_member(self, member):
        self.member_status_lbl.setText(member.status)
        self.image_preview.imageChangeSignal.emit(f"resources/images/{member.profile_image}")
