from PySide6.QtCore import QSortFilterProxyModel
from PySide6.QtSql import QSqlTableModel, QSqlQuery

from core.database import db
from core.exceptions import DatabaseExceptions

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


class Gender(Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


class Status(Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"
    TERMINATED = "Terminated"
    SUSPENDED = "Suspended"


@dataclass
class Member:
    # from member sign up form
    member_id: str = field(default="")
    name: str = field(default="")
    profile_image: str = field(default="")
    adm_number: int = field(default="")
    dob: datetime.date = field(default="")
    residence: str = field(default="")
    gender: Gender = field(default="")
    phone: str = field(default="")
    email: str = field(default="")

    # Other member attributes
    status: Status = field(default="Inactive")
    join_date: datetime.date = field(default=datetime.today())


class MembersModel(QSqlTableModel):
    def __init__(self):
        super(MembersModel, self).__init__()

        db.open()
        self.setTable("members")
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


class CustomFilterProxyModel(QSortFilterProxyModel):
    def __init__(self):
        super(CustomFilterProxyModel, self).__init__()

        model = MembersModel()
        self.setSourceModel(model)

        self.filter_name = ""
        self.filter_grade = ""
        self.filter_status = ""

    def setFilterName(self, name):
        self.filter_name = name
        self.invalidateFilter()

    def setFilterGrade(self, grade):
        self.filter_grade = grade
        self.invalidateFilter()

    def setFilterStatus(self, status):
        self.filter_status = status
        self.invalidateFilter()

    def filterAcceptsRow(self, source_row, source_parent):
        source_model = self.sourceModel()

        # Assuming the columns in the table are 'member_id', 'name', 'grade', 'status', etc.
        member_id = source_model.data(source_model.index(source_row, 0))
        member_name = source_model.data(source_model.index(source_row, 2))
        member_grade = source_model.data(source_model.index(source_row, 5))
        member_status = source_model.data(source_model.index(source_row, 10))

        # Check if the name, grade, and status match the filter criteria
        name_match = self.filter_name.lower() in member_name.lower() or self.filter_name.lower() in member_id.lower()
        grade_match = not self.filter_grade or self.filter_grade == "-- All --" or self.filter_grade == member_grade
        status_match = not self.filter_status or self.filter_status == "-- All --" or self.filter_status == member_status

        return name_match and grade_match and status_match
