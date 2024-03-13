from PySide6.QtSql import QSqlTableModel, QSqlQuery

from share import db


class RolesModel(QSqlTableModel):
    def __init__(self):
        super(RolesModel, self).__init__()

        db.open()
        self.setTable("roles")
        self.select()

    def add_role(self, role_id, role, department_id):
        qry = QSqlQuery()
        qry.prepare("""
            INSERT INTO roles 
            (role_id, department, role)
            VALUES (:role_id, :department, :role)
        """)

        qry.bindValue(":role_id", role_id)
        qry.bindValue(":department", department_id)
        qry.bindValue(":role", role)

        if role.exec():
            db.commit()
            return True
        else:
            print(db.lastError())
            return False
