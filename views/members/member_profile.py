from PySide6.QtCharts import QChart, QChartView, QLineSeries
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QFormLayout, QGroupBox, QToolBar, QLabel, QSplitter

import qtawesome as qta
from components import ImageComponent, ProgressBar


class MemberProfileView(QWidget):
    def __init__(self, parent):
        super(MemberProfileView, self).__init__(parent=parent)

        self.image_preview = ImageComponent()
        self.member_status_lbl = QLabel("Active")
        self.setObjectName("active_status_lbl")
        self.member_balance_lbl = QLabel("0.00")
        self.member_balance_lbl.setObjectName("balance")

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

        cp = ProgressBar()
        cp.set_value(3)

        personal_details_layout.addWidget(self.image_preview)
        personal_details_layout.addLayout(details_form_layout)
        personal_details_layout.addWidget(cp)
        personal_details_layout.addStretch()
        personal_details_layout.addWidget(self.activity_chart)

        self.actions_tool_bar = QToolBar()
        self.actions_tool_bar.setObjectName("sbrand")
        self.actions_tool_bar.setIconSize(QSize(30, 30))
        self.actions_tool_bar.addAction(qta.icon("ph.arrow-left",
                                                 color="teal"),
                                        "Back",
                                        lambda: self.parent().setCurrentIndex(0))
        self.actions_tool_bar.addWidget(QLabel("Member Profile"))
        self.actions_tool_bar.addWidget(QSplitter())
        self.actions_tool_bar.addWidget(self.member_status_lbl)
        self.actions_tool_bar.addWidget(self.member_balance_lbl)

        self.profile_group = QGroupBox()

        layout.addWidget(self.actions_tool_bar)
        layout.addLayout(personal_details_layout)
        layout.addWidget(self.profile_group)

    def set_member(self, member):
        self.member_status_lbl.setText(member.status)
        self.image_preview.imageChangeSignal.emit(f"resources/images/{member.profile_image}")
