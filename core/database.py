from PySide6.QtSql import QSqlDatabase

from core.settings import Settings

settings = Settings()

db_settings = settings.get_group_settings("database")

driver = db_settings.get('driver',  'QSQLITE')
host = db_settings.get('host', 'localhost')
port = db_settings.get('port', '3360')
name = db_settings.get('name', 'citadexx')
user = db_settings.get('user', 'root')
passwd = db_settings.get('password', '')

db = QSqlDatabase.addDatabase(driver)

if db.isDriverAvailable(driver):
    if driver == "QSQLITE":
        db.setDatabaseName(f"{name}.db")

    else:
        db.setDatabaseName(name)
        db.setHostName(host)
        db.setPort(port)
        db.setUserName(user)
        db.setPassword(passwd)
#
# db.open()
# print(db.isOpen(), db.lastError())
# print(db.drivers())
