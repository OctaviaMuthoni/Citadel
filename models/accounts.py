"""
    This module manages accounts and their subscriptions.
    A member will have an account with a subscription fees.
    All accounts with deficit will not have access to library services.
"""
from PySide6.QtSql import QSqlRelationalTableModel


class MemberAccounts(QSqlRelationalTableModel):
    def __init__(self):
        super(MemberAccounts, self).__init__()

    def create_account(self, member_id, card_number, ):
        # creates a new account
        pass

    def suspend_account(self):
        # suspend account: account can be suspended if it has a record of malicious damage.
        # misconduct
        # breaking library rules
        pass

    def terminate_account(self):
        # libray card expires, the account is terminated.
        pass

    def restore_account(self):
        # account can be restored automatically if suspension period is over of manually if period is indefinite.
        pass

    def update_payments(self):
        # Adds a bill to the account every end of month or every end of term based on the account subscription type
        pass


