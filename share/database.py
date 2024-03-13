from PySide6.QtSql import QSqlDatabase

from share import load_settings


# load database configuration
settings = load_settings("database")

driver = settings.get('driver')
db_name = settings.get('db_name')
password = settings.get('password')
port = int(settings.get('port'))
host = settings.get('host')
user = settings.get('user')

db = QSqlDatabase().addDatabase(driver)

if driver == "QSQLITE":
    db_name = f"database/{db_name}.db"

db.setDatabaseName(db_name)
db.setHostName(host)
db.setPort(port)
db.setUserName(user)
db.setPassword(password)

db.open()


