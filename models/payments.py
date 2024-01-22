from PySide6.QtSql import QSqlRelationalTableModel


class Payments(QSqlRelationalTableModel):
    def __init__(self):
        super(Payments, self).__init__()

    def make_payment(self):
        pass

    def get_payments(self):
        pass

