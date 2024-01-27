"""
    This model represent a continuous period of time when the views is open usually a term or semester.
    Each period has a: Staring date
                       Ending date
                       Status ( whether open or closed )
                       period_id ( LP/01/2023 ) This is a views period (LP) followed by term and then year

    - All materials not returned when a period is closed are considered lost.
    - All members are rendered inactive when the period is closed.
    - When a new period is started, each member is supposed to activate before having access to views services.
    - Before activation members should clear all their account dues including:
                                                                            replacing lost materials
                                                                            paying fines
                                                                            paying views fees
"""
from datetime import datetime

from PySide6.QtSql import QSqlTableModel, QSqlQuery

# from classes.Period import Period
from models.members import MembersModel
from src.database import db


class PeriodModel(QSqlTableModel):
    def __init__(self):
        super(PeriodModel, self).__init__()

        self.setTable("periods")
        self.members = MembersModel()

    def start_period(self, period):
        qry = QSqlQuery()
        qry.prepare(f"""INSERT INTO {self.tableName()} 
                        (period, start_date, end_date, status)
                        VALUES (:period, :start, :end, :status)
                    """)

        qry.bindValue(":period", period.period)
        qry.bindValue(":start", period.start_date)
        qry.bindValue(":end", period.end_date)
        qry.bindValue(":status", period.status)

        if qry.exec():
            db.commit()
            self.select()
            return True
        else:
            print("Error opening period:", qry.lastError().text())
            db.rollback()

        return False

    def close_period(self):
        qry = QSqlQuery()
        qry.prepare("UPDATE periods SET end_date = :end_date, status = 'closed' WHERE status = 'open'")
        qry.bindValue(":end_date", datetime.today().date())
        print(qry.boundValue(':end_date'))
        if qry.exec():
            self.submitAll()
            db.commit()
            self.select()
            return True
        else:
            print("Error closing period:", qry.lastError().text())
            db.rollback()

        return False

    def get_open_period(self):
        qry = QSqlQuery()
        qry.prepare("SELECT * FROM periods WHERE status = :open")
        qry.bindValue(":open", "open")

        if qry.exec() and qry.next():
            open_period = ""

            return open_period
        else:
            print("Error getting open period:", qry.lastError())

        return None
