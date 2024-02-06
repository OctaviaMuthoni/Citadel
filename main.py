import sys
from PySide6.QtWidgets import QApplication

from core.settings import Settings
from ui.views import LoginWindow
from citadexx import MainWindow

# instantiate classes
settings = Settings()


# read styles - based on current theme
def load_styles():
    print("loading styles")
    # application defaults to dark theme if no theme is set in settings.
    theme = settings.get_settings("application/theme", "light")
    stylesheet_path = f"resources/stylesheets/{theme}.qss"
    # read stylesheet and return
    with open(stylesheet_path) as stylesheet:
        return stylesheet.read()


def main():

    styles = load_styles()

    try:
        print("got here")
        # create an application instance
        app = QApplication(sys.argv)

        # create a login window instance
        main_window = MainWindow()
        print("main window created")
        main_window.setStyleSheet(styles)
        window = LoginWindow(main_window)
        window.setStyleSheet(styles)
        print("styles set")

        # create a function to handle login signal
        # def handle_login_signal():
        #     global main_window
        #     main_window = MainWindow()
        #     main_window.showMaximized()
        #     window.close()

        # window.loginSignal.connect(handle_login_signal)
        window.show()
        print("shown login")
        sys.exit(app.exec())

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
