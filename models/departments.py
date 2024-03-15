from PySide6.QtSql import QSqlQuery, QSqlTableModel

from classes import Department

from database.database import db


class DepartmentsModel(QSqlTableModel):
    def __init__(self):
        super(DepartmentsModel, self).__init__()

        db.open()

        self.select()

        self.setEditStrategy(QSqlTableModel.EditStrategy.OnManualSubmit)

    def departments(self) -> list[Department]:
        qry = QSqlQuery("SELECT * FROM departments")

        departments = list()
        if qry.exec():
            while qry.next():
                record = qry.record()
                dept = list()
                for i in range(record.count()):
                    dept.append(record.value('department'))
                departments.append(Department(*dept))

        return departments

    def add_department(self, department: Department) -> bool:
        qry = QSqlQuery()
        qry.prepare("""
            INSERT INTO departments
            (department_id, department)
            VALUES (:id, :name)
        """)

        qry.bindValue(":id", department.department_id)
        qry.bindValue(":name", department.department)

        if qry.exec():
            db.commit()
            return True
        else:
            print(db.lastError())
            return False

    def drop_department(self, department_id):
        qry = QSqlQuery()
        qry.prepare("""
                    DELETE FROM departments WHERE department_id = :id
                """)

        qry.bindValue(":id", department_id)

        if qry.exec():
            db.commit()
            return True
        else:
            print(db.lastError())
            return False

