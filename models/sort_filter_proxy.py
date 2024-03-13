from typing import Any

from PySide6.QtCore import QSortFilterProxyModel, Qt
from PySide6.QtSql import QSqlTableModel


class SortFilterProxyModel(QSortFilterProxyModel):
    def __init__(self, source_model: QSqlTableModel, text_columns: list):
        super(SortFilterProxyModel, self).__init__()

        self.setSourceModel(source_model)

        self.text_columns = text_columns

        self.filters = []

        self.filter_text = ""

    def add_filter(self, column: int, name: str):
        self.setProperty(name, "")
        self.filters.append((column, name))

    def setProperty(self, name: str, value: Any) -> bool:
        result = super().setProperty(name, value)
        self.invalidateFilter()
        return result

    def setFilterText(self, txt):
        self.filter_text = txt
        self.invalidateFilter()

    def filterAcceptsRow(self, source_row, source_parent):
        source_model = self.sourceModel()
        self.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        text_search = []
        for col in self.text_columns:
            text_search.append(self.filter_text.lower() in source_model.data(source_model.index(source_row, col)).lower())

        other_filters = []
        for f in self.filters:
            val = self.property(f[1])
            data_val = source_model.data(source_model.index(source_row, f[0]))
            other_filters.append(not val or val == "-- All --" or val.lower() == data_val.lower())

        return any(text_search) and all(other_filters)
