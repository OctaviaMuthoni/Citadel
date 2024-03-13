import sys

from PySide6.QtWidgets import QApplication

from lms import LMS
from views import LoginWindow


def main():
    try:
        # create an application instance
        app = QApplication(sys.argv)

        main_window = LMS()

        # create a login window instance
        window = LoginWindow()

        def show_main_window():
            window.close()
            main_window.showMaximized()

        window.loginSignal.connect(show_main_window)

        window.show()
        sys.exit(app.exec())

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
