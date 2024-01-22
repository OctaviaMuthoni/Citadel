from PySide6.QtSql import QSqlTableModel


class FinesModel(QSqlTableModel):
    def __init__(self):
        super(FinesModel, self).__init__()

    def add_fine(self, fine):
        pass

    def remove_fine(self):
        pass

    def edit_fine(self, fine):
        pass

