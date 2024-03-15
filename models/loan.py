from PySide6.QtCore import QDate, QDateTime
from PySide6.QtSql import QSqlTableModel, QSqlQuery

from database.database import db


class LoanModel(QSqlTableModel):
    def __init__(self):
        super(LoanModel, self).__init__()

        db.open()
        self.setTable('loan')
        self.select()
        self.setEditStrategy(QSqlTableModel.EditStrategy.OnManualSubmit)

    def get_member_loan(self, member):
        qry = QSqlQuery()

        qry.prepare("""
            SELECT 
                l.loan_id,
                l.material_id,
                m.title,
                l.issue_date,
                l.due_date,
                CASE WHEN l.due_date > :current_date THEN 'OVERDUE' ELSE 'PREDUE' END AS status
            FROM loan l
            INNER JOIN materials m ON m.material_id = l.material_id
            WHERE member_id = :member
        """)

        qry.bindValue(':member', member)
        qry.bindValue(':current_date', QDateTime.currentDateTime())

        materials = []
        if qry.exec():
            while qry.next():
                record = qry.record()
                materials.append({record.fieldName(i): record.value(i) for i in range(record.count())})
        else:
            print(self.lastError())

        return materials
