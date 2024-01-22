from PySide6.QtCore import QSortFilterProxyModel
from PySide6.QtSql import QSqlRelationalTableModel


class MaterialsProxyModel(QSortFilterProxyModel):
    def __init__(self):
        super(MaterialsProxyModel, self).__init__()

        source_model = MaterialsModel()
        self.setSourceModel(source_model)


class MaterialsModel(QSqlRelationalTableModel):
    def __init__(self):
        super(MaterialsModel, self).__init__()

        self.setTable("materials")

    def fetch_material(self):
        """
        :return: Returns all materials from the materials table
        """
        return self.select()
