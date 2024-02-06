import sys
from PySide6.QtWidgets import QApplication

from core.settings import Settings
from ui import LoginWindow
# from citadexx import MainWindow

# instantiate classes
settings = Settings()


# read styles - based on current theme



def main():

    # styles = load_styles()

    try:
        # create an application instance
        app = QApplication(sys.argv)

        # create a login window instance
        window = LoginWindow()
        # window.setStyleSheet(styles)

        window.show()
        print("shown login")
        sys.exit(app.exec())

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
