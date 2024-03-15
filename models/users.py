import random
from uuid import uuid4

from PySide6.QtCore import QDateTime
from PySide6.QtSql import QSqlTableModel, QSqlQuery

from classes import User
from database.database import db


class UsersModel(QSqlTableModel):
    def __init__(self):
        super(UsersModel, self).__init__()

        db.open()
        self.setTable('users')

        self.setEditStrategy(QSqlTableModel.EditStrategy.OnManualSubmit)

    def create_user(self, user: User):
        qry = QSqlQuery()
        qry.prepare("""
            INSERT INTO users 
            (user_uuid, profile_image, username, email, role, password, attempts)
            VALUES (:user_uuid, :profile_image, :username, :email, :role, :password, :attempts);
        """)

        qry.bindValue(":user_uuid", user.user_uuid)
        qry.bindValue(":profile_image", user.profile_image)
        qry.bindValue(":username", user.username)
        qry.bindValue(":email", user.email)
        qry.bindValue(":role", user.role)
        qry.bindValue(":password", user.password)
        qry.bindValue(":attempts", user.attempts)

        if qry.exec():
            db.commit()
            return True
        else:
            db.rollback()
            return False

    def get_user(self, username):
        qry = QSqlQuery()
        qry.prepare("SELECT * FROM users WHERE username = :username")
        qry.bindValue(":username", username)

        if qry.exec():
            while qry.next():
                record = qry.record()
                user = dict()
                for i in range(record.count()):
                    user[record.fieldName(i)] = record.value(i)

                return User(**user)
        else:
            print("Error:", db.lastError())

    def create_otp(self, user_uuid):
        unused_qry = QSqlQuery()
        unused_qry.prepare("""
                SELECT otp
                FROM otps 
                WHERE user_uuid = :user_uuid 
                AND status = 'UNUSED'
                LIMIT 1
            """)
        unused_qry.bindValue(":user_uuid", user_uuid)

        if unused_qry.exec() and unused_qry.next():
            return unused_qry.value(0)

        db.transaction()

        qry = QSqlQuery()
        qry.prepare("""
            INSERT INTO otps 
            (otp_uuid, user_uuid, otp, created_on, expires_on) 
            VALUES (:otp_uuid, :user_uuid, :otp, :created_on, :expires_on)
        """)

        created_on = QDateTime().currentDateTime()
        expires_on = created_on.addSecs(3600)

        otp = random.randint(100000, 999999)
        otp_uuid = str(uuid4())

        qry.bindValue(":otp_uuid", otp_uuid)
        qry.bindValue(":user_uuid", user_uuid)
        qry.bindValue(":otp", otp)
        qry.bindValue(":created_on", created_on)
        qry.bindValue(":expires_on", expires_on)

        event_name = otp_uuid.replace('-', '_')
        schedule_time = expires_on.toPython()

        if qry.exec():
            event_qry = QSqlQuery(f"""
                CREATE EVENT {event_name}
                ON SCHEDULE AT '{schedule_time}'
                DO UPDATE otps SET status = 'EXPIRED' WHERE otp_uuid = '{otp_uuid}'
            """)

            if event_qry.exec():
                db.commit()
                return otp
            else:
                db.rollback()
                return False
        else:
            db.rollback()
            return False

    def update_profile_image(self, user_uuid, profile_image):
        qry = QSqlQuery()
        qry.prepare("""
                    UPDATE users
                    SET profile_image = :profile_image
                    WHERE user_uuid = :user_uuid;
                """)

        qry.bindValue(":user_uuid", user_uuid)
        qry.bindValue(":profile_image", profile_image)

        if qry.exec():
            db.commit()
            return True
        else:
            db.rollback()
            return False

    def update_role(self, user_uuid, role):
        qry = QSqlQuery()
        qry.prepare("""
                    UPDATE users
                    SET role = :role
                    WHERE user_uuid = :user_uuid;
                """)

        qry.bindValue(":user_uuid", user_uuid)
        qry.bindValue(":role", role)

        if qry.exec():
            db.commit()
            return True
        else:
            db.rollback()
            return False

    def reduce_attempts(self, user_uuid):
        qry = QSqlQuery()
        qry.prepare("""
                    UPDATE users
                    SET attempts = attempts - 1
                    WHERE user_uuid = :user_uuid;
                """)

        qry.bindValue(":user_uuid", user_uuid)

        if qry.exec():
            db.commit()
            return True
        else:
            db.rollback()
            return False

    def reset_attempts(self, user_uuid):
        qry = QSqlQuery()
        qry.prepare("""
                    UPDATE users
                    SET attempts = 3
                    WHERE user_uuid = :user_uuid;
                """)

        qry.bindValue(":user_uuid", user_uuid)

        if qry.exec():
            db.commit()
            return True
        else:
            db.rollback()
            return False
