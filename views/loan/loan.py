"""
    This is a view module for the loan package.
    It shows all borrowed materials and provide an interface to borrow and return materials from the library.
"""
from PySide6.QtCore import Qt, QSize, QDateTime
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QLabel, QFormLayout, QTableWidgetItem, \
    QHeaderView

from models import MembersModel
from models.loan import LoanModel
from views.share import FormField, LineEdit, PushButton, ImageWidget


class LoanView(QWidget):
    def __init__(self):
        super(LoanView, self).__init__()

        self.material_edit = LineEdit("")
        self.borrow_btn = PushButton("Borrow")
        self.return_btn = PushButton("Return")

        borrow_return_layout = QHBoxLayout()
        borrow_return_layout.addWidget(self.material_edit)
        borrow_return_layout.addStretch()
        borrow_return_layout.addWidget(self.borrow_btn)
        borrow_return_layout.addWidget(self.return_btn)
        
        self.materials_table = QTableWidget()
        
        materials_widget = QWidget()
        materials_layout = QVBoxLayout(materials_widget)
        materials_layout.addLayout(borrow_return_layout)
        materials_layout.addWidget(self.materials_table)

        self.member_id_edit = LineEdit("")
        self.member_id_edit.textChanged.connect(lambda x: self.member_id_edit.setText(x.upper()))
        self.member_id_edit.returnPressed.connect(self.get_member)
        self.image_preview = ImageWidget(ImageWidget.ImageWidgetMode.PREVIEW)

        self.name_lbl = QLabel()
        self.adm_lbl = QLabel()
        self.nemis_lbl = QLabel()
        self.assessment_lbl = QLabel()

        self.borrowed_lbl = QLabel()
        self.borrowed_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.borrowed_lbl.setFixedSize(QSize(150, 150))
        self.borrowed_lbl.setObjectName('borrow-count')

        form = QFormLayout()
        form.addRow("NAME:", self.name_lbl)
        form.addRow("ASSESSMENT:", self.assessment_lbl)
        form.addRow("ADMISSION:", self.adm_lbl)
        form.addRow("NEMIS:", self.nemis_lbl)

        member_preview_widget = QWidget()
        preview_layout = QVBoxLayout(member_preview_widget)
        preview_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        preview_layout.addWidget(FormField("MEMBER ID:", self.member_id_edit))
        preview_layout.addWidget(self.image_preview)
        preview_layout.addLayout(form)
        preview_layout.addStretch()
        preview_layout.addWidget(self.borrowed_lbl)
        preview_layout.addStretch()
        member_preview_widget.setFixedWidth(300)

        layout = QHBoxLayout(self)
        layout.addWidget(member_preview_widget)
        layout.addWidget(materials_widget)

    def get_member(self):
        member_id = self.member_id_edit.text()
        members_model = MembersModel()
        member = members_model.get_member(member_id)

        loan_model = LoanModel()
        if member:
            self.render_table(loan_model.get_member_loan(member_id))

            self.name_lbl.setText(member['name'])
            self.assessment_lbl.setText(member['assessment'])
            self.nemis_lbl.setText(member['nemis'])
            self.adm_lbl.setText(member['admission'])
            self.image_preview.imageChangedSignal.emit(f"res/images/profile_images/{member['profile_image']}")

    def render_table(self, data):
        if data:

            self.borrowed_lbl.setText(f'{len(data)}/5')
            
            header_labels = data[0].keys()
            self.materials_table.setColumnCount(len(header_labels))
            self.materials_table.verticalHeader().hide()
            self.materials_table.setRowCount(len(data))
            self.materials_table.setHorizontalHeaderLabels(header_labels)
            self.materials_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

            for r, rd in enumerate(data):
                for c, v in enumerate(rd.values()):
                    if type(v) == QDateTime:
                        v = v.toString()
                    item = QTableWidgetItem(v)
                    self.materials_table.setItem(r, c, item)



