from PySide6.QtSql import QSqlDatabase

from core.settings import Settings

settings = Settings()

# Get database configuration settings
db_settings = settings.get_group_settings("database")

driver = db_settings.get('driver')
host = db_settings.get('host')
port = db_settings.get('port')
name = db_settings.get('name')
user = db_settings.get('user')
passwd = db_settings.get('password')

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

