from PySide6.QtCharts import QChart, QChartView, QLineSeries
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QFormLayout, QGroupBox, QLabel

from views.share import SubHeader, FormField
from views.share.image_widget import ImageWidget


class MemberProfileView(QWidget):
    backSignal = Signal()

    def __init__(self):
        super(MemberProfileView, self).__init__()

        self.image_preview = ImageWidget(ImageWidget.ImageWidgetMode.PREVIEW)

        self.member_balance_lbl = QLabel("0.00")

        self.header = SubHeader("Profile")

        self.activity_chart = QChartView()
        # self.activity_chart.setMaximumHeight(200)
        chart = QChart()
        series = QLineSeries()
        series.append(1.2, 4)
        series.append(1.4, 6)
        series.append(1.8, 8)
        series.append(2.0, 12)
        series.append(1.2, 4)
        chart.addSeries(series)
        self.activity_chart.setChart(chart)
        
        self.name_lbl = QLabel()
        self.member_id_lbl = QLabel()
        
        self.admission_lbl = QLabel()
        self.assessment_lbl = QLabel()
        self.nemis_lbl = QLabel()
        
        self.phone_lbl = QLabel()
        self.email_lbl = QLabel()
        
        self.permanent_residence_lbl = QLabel()
        self.current_residence_lbl = QLabel()

        layout = QVBoxLayout(self)
        #
        # id_layout = QHBoxLayout()
        # id_layout.setContentsMargins(0, 0, 0, 0)
        # id_layout.addWidget(FormField("Admission:", self.admission_lbl))
        # id_layout.addWidget(FormField("Assessment:", self.assessment_lbl))
        # id_layout.addWidget(FormField("NEMIS:", self.nemis_lbl))
        #
        # contacts_layout = QHBoxLayout()
        # contacts_layout.setContentsMargins(0, 0, 0, 0)
        # contacts_layout.addWidget(FormField("Phone:", self.phone_lbl))
        # contacts_layout.addWidget(FormField("Email:", self.email_lbl))
        #
        # address_layout = QHBoxLayout()
        # address_layout.setContentsMargins(0, 0, 0, 0)
        # address_layout.addWidget(FormField("Permanent address:", self.permanent_residence_lbl))
        # address_layout.addWidget(FormField("Current residence:", self.current_residence_lbl))

        self.details_form_layout = QFormLayout()
        self.setContentsMargins(0, 0, 0, 0)
        self.details_form_layout.addRow("Name:", self.name_lbl)
        self.details_form_layout.addRow("Member ID:", self.member_id_lbl)
        self.details_form_layout.addRow("Admission:", self.admission_lbl)
        self.details_form_layout.addRow("Assessment:", self.assessment_lbl)
        self.details_form_layout.addRow("NEMIS:", self.nemis_lbl)
        self.details_form_layout.addRow("Phone:", self.phone_lbl)
        self.details_form_layout.addRow("Email:", self.email_lbl)
        self.details_form_layout.addRow("Current residence:", self.current_residence_lbl)
        self.details_form_layout.addRow("Permanent residence:", self.permanent_residence_lbl)

        personal_details_layout = QHBoxLayout()
        personal_details_layout.addWidget(self.image_preview)
        personal_details_layout.addLayout(self.details_form_layout)
        personal_details_layout.addStretch()
        personal_details_layout.addWidget(self.member_balance_lbl)

        activity_header = SubHeader("Activity Chart")
        activity_header.back_btn.hide()

        layout.addWidget(self.header)
        layout.addLayout(personal_details_layout)
        layout.addWidget(activity_header)
        layout.addWidget(self.activity_chart)

    def set_member(self, member):
        self.image_preview.imageChangedSignal.emit(f"res/images/profile_images/{member['profile_image']}")

        self.header.title_lbl.setText(member["name"])
        self.member_id_lbl.setText(member["member_id"])

        self.admission_lbl.setText(member["admission"])
        self.assessment_lbl.setText(member["assessment"])
        self.nemis_lbl.setText(member["nemis"])

        self.phone_lbl.setText(member["phone"])
        self.email_lbl.setText(member["email"])

        self.permanent_residence_lbl.setText(member["permanent_residence"])
        self.current_residence_lbl.setText(member["current_residence"])
