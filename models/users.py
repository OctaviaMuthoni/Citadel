from dataclasses import dataclass
from PySide6.QtSql import QSqlTableModel, QSqlQuery

from src.auth import hash_password
from src.database import db
from src.exceptions import DatabaseExceptions


@dataclass
class User:
    member_id: str
    password: str
    role_id: int
    user_id: int = -1

    def hashed_password(self):
        return hash_password(self.password)


class UsersModel(QSqlTableModel):
    def __init__(self):
        super(UsersModel, self).__init__()

        db.open()
        self.setTable("users")
        self.select()

    def get_user(self, member_id):
        qry = QSqlQuery()
        qry.prepare("SELECT * FROM users WHERE member_id = :member")
        qry.bindValue(":member", member_id)

        if qry.exec() and qry.next():
            user_data = {
                'member_id': qry.value('member_id'),
                'user_id': qry.value('user_id'),
                'role_id': qry.value('role_id'),
                'password': qry.value('password')
            }
            return User(**user_data)
        else:
            print("Error retrieving member:", qry.lastError().text())

        return None

    def add_user(self, user: User):
        qry = QSqlQuery()
        qry_string = "INSERT INTO users VALUES (:member_id, :password, :role)"
        qry.prepare(qry_string)

        qry.bindValue(":member_id", user.member_id)
        qry.bindValue(":password", user.hashed_password())
        qry.bindValue(":role", user.role_id)

        if qry.exec():
            self.layoutChanged.emit()
            db.commit()
            return True
        else:
            db.rollback()
            raise DatabaseExceptions(db.lastError().text())

    def remove_user(self, user_id):
        qry = QSqlQuery()
        qry_string = "DELETE FROM users WHERE user_id = :user_id"
        qry.prepare(qry_string)

        qry.bindValue(":user_id", user_id)

        if qry.exec():
            self.layoutChanged.emit()
            db.commit()
            return True
        else:
            db.rollback()
            raise DatabaseExceptions(db.lastError().text())

    def update_user(self, user_id, new_password):
        qry = QSqlQuery()
        qry_string = "UPDATE users SET password = :password WHERE user_id = :user_id"
        qry.prepare(qry_string)

        qry.bindValue(":user_id", user_id)
        qry.bindValue(":password", new_password)

        if qry.exec():
            self.layoutChanged.emit()
            db.commit()
            return True
        else:
            db.rollback()
            raise DatabaseExceptions(db.lastError().text())

    def update_role(self, user_id, role):
        qry = QSqlQuery()
        qry_string = "UPDATE users SET role = :role WHERE user_id = :user_id"
        qry.prepare(qry_string)

        qry.bindValue(":user_id", user_id)
        qry.bindValue(":role", role)

        if qry.exec():
            self.layoutChanged.emit()
            db.commit()
            return True
        else:
            db.rollback()
            raise DatabaseExceptions(db.lastError().text())

    def get_user_rights(self, user_id):
        pass

    def set_user_rights(self, user, rights):
        pass

    def add_role(self, role, rights):
        pass

    def remove_role(self, role_id):
        pass
