from PySide6.QtWidgets import QStackedWidget

from .member_form import CreateMemberView
from .member_profile import MemberProfileView
from .members_list import MembersListView


class MembersView(QStackedWidget):
    def __init__(self):
        super(MembersView, self).__init__()

        self.member_profile_view = MemberProfileView(self)
        self.members_list_view = MembersListView(self)
        self.create_member_view = CreateMemberView(self)

        self.addWidget(self.members_list_view)
        self.addWidget(self.create_member_view)
        self.addWidget(self.member_profile_view)
