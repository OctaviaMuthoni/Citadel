from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QComboBox, QToolBar, QSplitter, QLabel

import qtawesome as qta

from components import CustomTableView, Search
from core import ImageComponentMode
from models.members import MembersModel, CustomFilterProxyModel, Member, Status


class MembersListView(QWidget):
    def __init__(self, parent):
        super(MembersListView, self).__init__(parent=parent)

        self.members_model = MembersModel()
        self.proxy_model = CustomFilterProxyModel()
        self.proxy_model.setSourceModel(self.members_model)

        self.search_edit = Search()
        self.search_edit.search_input.textChanged.connect(self.proxy_model.setFilterName)

        self.grade_combo = QComboBox()
        self.grade_combo.currentTextChanged.connect(self.proxy_model.setFilterGrade)
        self.grade_combo.addItem("-- All --")
        for i in range(1, 13):
            self.grade_combo.addItem(str(i))

        self.status_combo = QComboBox()
        self.status_combo.currentTextChanged.connect(self.proxy_model.setFilterStatus)
        self.status_combo.addItem("-- All --")
        self.status_combo.addItems([
            Status.ACTIVE.value,
            Status.INACTIVE.value,
            Status.SUSPENDED.value,
            Status.TERMINATED.value
        ])

        search_filter_layout = QHBoxLayout()
        search_filter_layout.setContentsMargins(0, 0, 0, 20)
        search_filter_layout.addWidget(self.search_edit)
        search_filter_layout.addStretch()
        search_filter_layout.addWidget(self.grade_combo)
        search_filter_layout.addWidget(self.status_combo)

        self.view_action = QAction(qta.icon("ph.eye", color="#05ADAD"), "View")
        self.view_action.triggered.connect(self.view_member_profile)

        self.edit_action = QAction(qta.icon("ph.pencil-line-light", color="blue"), "Edit")
        self.edit_action.triggered.connect(self.update_member)

        self.activate_action = QAction(qta.icon("ph.activity-light", color="teal"), "Activate")
        self.activate_action.triggered.connect(self.deactivate_member)

        self.create_action = QAction(qta.icon("ph.user-plus-light", color="green"), "Create")
        self.create_action.triggered.connect(self.create_new_member)

        self.tool_bar = QToolBar()
        self.tool_bar.setObjectName("white_back")
        self.tool_bar.setIconSize(QSize(25, 25))
        self.tool_bar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.tool_bar.addWidget(QLabel("Showing 2 out of 2"))
        self.tool_bar.addWidget(QSplitter())
        self.tool_bar.addAction(self.view_action)
        self.tool_bar.addSeparator()
        self.tool_bar.addAction(self.edit_action)
        self.tool_bar.addSeparator()
        self.tool_bar.addAction(self.activate_action)
        self.tool_bar.addSeparator()
        self.tool_bar.addAction(self.create_action)

        self.model = MembersModel()

        self.table = CustomTableView()
        self.table.setModel(self.proxy_model)

        self.table.setObjectName("custom_table")

        layout = QVBoxLayout(self)
        layout.addLayout(search_filter_layout)
        layout.addWidget(self.tool_bar)
        layout.addWidget(self.table)

        self.update_actions_state()
        self.table.clicked.connect(self.update_actions_state)

    def create_new_member(self):
        self.parent().setCurrentIndex(1)
        member_form = self.parent().currentWidget()
        member_form.profile_image_upload.change_mode(ImageComponentMode.UPLOAD)
        member_form.set_member(Member())

    def update_member(self):
        self.parent().setCurrentIndex(1)
        member_form = self.parent().currentWidget()
        member_form.profile_image_upload.change_mode(ImageComponentMode.PREVIEW)
        selected_index = self.table.selectionModel().currentIndex()
        if selected_index.isValid():
            member_id = selected_index.siblingAtColumn(0).data(Qt.DisplayRole)
            member = self.model.get_member(member_id)
            member_form.set_member(member)
        else:
            print("invalid index")

    def update_actions_state(self):
        has_selection = self.table.selectionModel().hasSelection()

        self.view_action.setEnabled(has_selection)
        self.edit_action.setEnabled(has_selection)
        self.activate_action.setEnabled(has_selection)

    def deactivate_member(self):
        selected_index = self.table.selectionModel().currentIndex()
        if selected_index.isValid():
            member_id = selected_index.siblingAtColumn(0).data(Qt.DisplayRole)
            self.model.deactivate(member_id)

            self.model.select()
            self.proxy_model.setSourceModel(self.model)

            self.update_actions_state()

    def view_member_profile(self):
        selected_index = self.table.selectionModel().currentIndex()
        if selected_index.isValid():
            member_id = selected_index.siblingAtColumn(0).data(Qt.DisplayRole)
            member = self.model.get_member(member_id)
            self.parent().setCurrentIndex(2)
            self.parent().currentWidget().set_member(member)
