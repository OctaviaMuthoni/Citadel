from PySide6.QtCore import QSortFilterProxyModel
from PySide6.QtSql import QSqlTableModel, QSqlQuery

from share import db
from share.exceptions import DatabaseExceptions

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


class MembersModel(QSqlTableModel):
    def __init__(self):
        super(MembersModel, self).__init__()

        db.open()
        print("testing db", db.isOpen())
        self.setTable("students")
        self.select()

        self.setEditStrategy(QSqlTableModel.EditStrategy.OnManualSubmit)

    def deactivate(self, member_id):
        qry = QSqlQuery()
        qry.prepare("UPDATE members SET status = 'Inactive' WHERE member_id = :member")
        qry.bindValue(":member", member_id)

        if qry.exec():
            self.submitAll()  # Update the model to reflect the changes in the database
            db.commit()
            return True
        else:
            print("Error during update:", qry.lastError().text())
            db.rollback()

        return False

    def get_member(self, member_id):
        qry = QSqlQuery()
        qry.prepare("SELECT * FROM members WHERE member_id = :member")
        qry.bindValue(":member", member_id)

        if qry.exec() and qry.next():
            member_data = {
                'member_id': qry.value('member_id'),
                'name': qry.value('name'),
                'gender': qry.value('gender'),
                'dob': qry.value('dob'),
                'phone': qry.value('phone'),
                'email': qry.value('email'),
                'residence': qry.value('residence'),
                'status': qry.value('status'),
                'profile_image': qry.value('profile_image'),
                'adm_number': qry.value('id_number')
            }
            return Member(**member_data)
        else:
            print("Error retrieving member:", qry.lastError().text())

        return None

    def add_member(self, member_data):
        qry = QSqlQuery()

        # Assuming 'members' table columns are 'member_id', 'name', 'status', etc.
        qry.prepare("INSERT INTO members (name, status) VALUES (:name, :status)")
        qry.bindValue(":name", member_data.get('name', ''))
        qry.bindValue(":status", member_data.get('status', 'Active'))  # Default to 'Active' if not provided

        if qry.exec():
            self.layoutChanged.emit()
            db.commit()
            return True
        else:
            db.rollback()
            raise DatabaseExceptions(db.lastError().text())


