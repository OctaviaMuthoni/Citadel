from uuid import UUID

from PySide6.QtSql import QSqlTableModel

from classes import Grade
from share import db


class GradesModel(QSqlTableModel):
    def __init__(self):
        super(GradesModel, self).__init__()

        db.open()

        if db.isOpen():
            self.setTable("grades")
            self.select()

    def add_grade(self, grade: Grade):
        pass

    def add_grades(self, grades: [Grade]):
        pass

    def remove_grade(self, grade_id: UUID):
        pass



