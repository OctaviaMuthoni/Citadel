from PySide6.QtCore import QModelIndex
from PySide6.QtWidgets import QStackedWidget

from . import MembersListView, MemberRegistrationForm, MemberProfileView


class MembersView(QStackedWidget):
    def __init__(self):
        super(MembersView, self).__init__()

        self.member_profile_view = MemberProfileView()
        self.members_list_view = MembersListView()
        self.member_registration_form = MemberRegistrationForm()

        self.addWidget(self.members_list_view)
        self.addWidget(self.member_registration_form)
        self.addWidget(self.member_profile_view)

        self.members_list_view.viewMemberSignal.connect(self.view_member_profile)
        self.members_list_view.editMemberSignal.connect(self.edit_member)
        self.members_list_view.createMemberSignal.connect(self.register_member)

        self.member_registration_form.header.backSignal.connect(lambda: self.setCurrentIndex(0))
        self.member_profile_view.header.backSignal.connect(lambda: self.setCurrentIndex(0))

    def register_member(self):
        self.setCurrentIndex(1)
        self.member_registration_form.header.title_lbl.setText("Register")

    def edit_member(self):
        self.member_registration_form.header.title_lbl.setText("Update")
        self.setCurrentIndex(1)

        index = QModelIndex(self.members_list_view.table.selectionModel().currentIndex()).siblingAtColumn(0)

    def view_member_profile(self):
        self.setCurrentIndex(2)

