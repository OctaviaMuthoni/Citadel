import qtawesome as qta
from PySide6.QtCore import QSize, Qt, Signal, QModelIndex
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QToolBar, QSplitter, QPushButton

# import model
from models.members import MembersModel
from models.sort_filter_proxy import SortFilterProxyModel
from views.share import FormField, ComboBox
from views.share import TableView
from views.share import SearchEdit
from share import Status


class MembersListView(QWidget):

    viewMemberSignal = Signal(str)
    editMemberSignal = Signal(str)
    createMemberSignal = Signal()

    def __init__(self):
        super(MembersListView, self).__init__()

        self.members_model = MembersModel()
        self.proxy_model = SortFilterProxyModel(self.members_model, text_columns=[0, 1])
        self.proxy_model.add_filter(5, "department")
        self.proxy_model.add_filter(6, "grade")
        self.proxy_model.add_filter(7, "status")

        self.member_type_combo = ComboBox([
            "Student",
            "Employee"
        ])

        self.member_type_field = FormField("Member type", self.member_type_combo)

        # members view table
        self.table = TableView()
        self.table.setModel(self.proxy_model)

        # search widget
        self.search_edit = SearchEdit()

        # departments filter combobox
        self.departments_combo = ComboBox([
            "-- All --",
            "Administration",
            "Academics",
            "Kitchen",
            "House keeping",
            "Security"
        ])
        self.department_field = FormField("Department", self.departments_combo)
        self.department_field.setHidden(True)

        # grade filter combobox
        self.grade_combo = ComboBox(["-- All --"])
        for i in range(1, 13):
            self.grade_combo.addItem(str(i))

        self.grade_field = FormField("Grade", self.grade_combo)

        # status filter combobox
        self.status_combo = ComboBox(["-- All --"])
        self.status_combo.addItems([
            Status.ACTIVE,
            Status.INACTIVE,
            Status.SUSPENDED,
            Status.TERMINATED
        ])

        self.status_field = FormField("Status", self.status_combo)

        # clear filters button
        self.clear_filters_btn = QPushButton()
        self.clear_filters_btn.setDisabled(self.no_filters())
        self.clear_filters_btn.setIconSize(QSize(25, 25))
        self.clear_filters_btn.setIcon(
            qta.icon('mdi.filter-outline', options=[{
                'color': '#05ADD3',
                'color_active': '#05ADD3',
                'color_disabled': '#e9e9e9',
                'active': 'mdi6.filter-remove'
            }])
        )

        # filters layout
        search_filter_layout = QHBoxLayout()
        search_filter_layout.setSpacing(15)
        search_filter_layout.setContentsMargins(0, 0, 0, 0)
        search_filter_layout.addWidget(self.search_edit)
        search_filter_layout.addStretch()
        search_filter_layout.addWidget(self.member_type_field)
        search_filter_layout.addWidget(self.department_field)
        search_filter_layout.addWidget(self.grade_field)
        search_filter_layout.addWidget(self.status_field)
        search_filter_layout.addWidget(self.clear_filters_btn)

        #
        # self.proxy_model = None

        # actions
        self.view_action = QAction(qta.icon("ph.eye", color="#05ADAD"), "View")
        self.view_action.setEnabled(self.table.selectionModel().hasSelection())

        self.edit_action = QAction(qta.icon("ph.pencil-line-light", color="blue"), "Edit")
        self.edit_action.setEnabled(self.table.selectionModel().hasSelection())

        self.create_action = QAction(qta.icon("ph.user-plus-light", color="green"), "Create")

        # actions menu
        self.tool_bar = QToolBar()
        self.tool_bar.setObjectName("in-page-menu")
        self.tool_bar.setIconSize(QSize(25, 25))
        self.tool_bar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.tool_bar.addWidget(QSplitter())
        self.tool_bar.addAction(self.view_action)
        self.tool_bar.addSeparator()
        self.tool_bar.addAction(self.edit_action)
        self.tool_bar.addSeparator()
        self.tool_bar.addAction(self.create_action)

        # main layout
        layout = QVBoxLayout(self)
        layout.setSpacing(20)
        layout.addLayout(search_filter_layout)
        layout.addWidget(self.tool_bar)
        layout.addWidget(self.table)

        self.event_listener()

    def event_listener(self):
        self.table.clicked.connect(self.update_options)
        self.member_type_combo.currentTextChanged.connect(self.load_model)
        self.create_action.triggered.connect(self.createMemberSignal.emit)
        self.edit_action.triggered.connect(self.editMemberSignal.emit)
        self.view_action.triggered.connect(self.show_profile)
        self.clear_filters_btn.clicked.connect(self.clear_filters)
        self.departments_combo.currentTextChanged.connect(lambda department: self.update_filters("department", department))
        self.grade_combo.currentTextChanged.connect(lambda grade: self.update_filters("grade", grade))
        self.search_edit.search_input.textChanged.connect(self.search)
        self.status_combo.currentTextChanged.connect(lambda status: self.update_filters("status", status))

    def show_profile(self):
        cur_idx = self.table.selectionModel().currentIndex().siblingAtColumn(0)
        self.viewMemberSignal.emit(cur_idx.data())

    def load_model(self, member_type):
        self.members_model.setTable(member_type.lower() + 's')
        self.members_model.select()
        self.proxy_model.setSourceModel(self.members_model)

        self.clear_filters()

        if member_type == "Student":
            self.department_field.setHidden(True)
            self.grade_field.setHidden(False)
        else:
            self.department_field.setHidden(False)
            self.grade_field.setHidden(True)

    def search(self, text):
        self.proxy_model.setFilterText(text)
        self.clear_filters_btn.setDisabled(self.no_filters())
        self.update_options()

    def no_filters(self):
        _filters = (not self.search_edit.search_input.text()
                    and self.status_combo.currentIndex() == 0
                    and self.grade_combo.currentIndex() == 0
                    and self.departments_combo.currentIndex() == 0)
        return _filters

    def update_filters(self, key, value):
        print(key, value)
        self.proxy_model.setProperty(key, value)
        self.update_options()
        self.clear_filters_btn.setDisabled(self.no_filters())

    def update_options(self):
        has_selection = self.table.selectionModel().hasSelection()
        self.view_action.setEnabled(has_selection)
        self.edit_action.setEnabled(has_selection)

    def clear_filters(self):
        self.grade_combo.setCurrentIndex(0)
        self.status_combo.setCurrentIndex(0)
        self.search_edit.search_input.setText("")
        self.departments_combo.setCurrentIndex(0)
