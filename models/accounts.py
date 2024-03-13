"""
    This model queries the members account view data.
"""
from enum import Enum

from PySide6.QtSql import QSqlTableModel


class BillPurpose(Enum):
    pass


class Accounts(QSqlTableModel):
    def __init__(self):
        super().__init__()

        # accounts is a view that gets data from bills table
        self.setTable("accounts")
