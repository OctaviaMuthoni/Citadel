from PySide6.QtWidgets import QApplication

# from share.logger import AppLogger

# TODO: log all database errors in db.log file
# logger = AppLogger()

# establish server connection
if __name__ == "__main__":
    app = QApplication()
    from database.database import db

    if db.open():
        print("Database connection established successfully")
    else:
        print("Failed to connect: ", db.lastError())


    def migrate():
        # Read queries from schema.sql file.
        with open("schema.sql") as schema:
            queries = schema.read().split(';')
            print(queries)

    print("ok noe")
# generate_library_card('John Doe', '123456789', '2023-12-31', save_path='library_card_template.png')

