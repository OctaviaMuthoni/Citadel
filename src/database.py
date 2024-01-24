from PySide6.QtSql import QSqlDatabase


config_options = {
    "driver": "QSQLITE",
    "host": "127.0.0.1",
    "port": "3306",
    "user": "admin",
    "passwd": "Admin",
    "name": "citadel_db"
}


name = "citadel"
host = "127.0.0.1"
port = 3306
passwd = "Admin@Citadel12345"
user = "admin"
driver = "QMYSQL"

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

db.open()
print(db.isOpen(), db.lastError())
print(db.drivers())



