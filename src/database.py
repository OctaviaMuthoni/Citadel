from PySide6.QtSql import QSqlDatabase


config_options = {
    "driver": "QSQLITE",
    "host": "127.0.0.1",
    "port": "3306",
    "user": "admin",
    "passwd": "Admin",
    "name": "citadel_db"
}


name = config_options['name']
host = config_options['host']
port = config_options['port']
passwd = config_options['passwd']
user = config_options['user']
driver = config_options['driver']

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



