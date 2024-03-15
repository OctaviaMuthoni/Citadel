from PySide6.QtSql import QSqlDatabase

from share import load_settings

db = QSqlDatabase.addDatabase('QMYSQL')


# get other database configurations
settings = load_settings('database')


db.setDatabaseName(settings.get('db_name'))
db.setPort(int(settings.get('port')))
db.setHostName(settings.get('host'))
db.setUserName(settings.get('user'))
db.setPassword(settings.get('password'))
