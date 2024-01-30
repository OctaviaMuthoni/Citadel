import os
import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from core import STYLES_PATH
from musoni import MainWindow
from src.logger import AppLogger
from src.settings import Settings
from views.auth.login import LoginWindow

if __name__ == '__main__':

    logger = AppLogger()

    styles_path = os.path.join(STYLES_PATH, 'styles.qss')

    # noinspection PyBroadException
    try:
        with open(styles_path) as stylesheet:
            styles = stylesheet.read()

        app = QApplication([])
        app.setWindowIcon(QIcon("falcon.ico"))
        settings = Settings()

        window = LoginWindow(settings)
        window.setWindowTitle(settings.get_settings("institution", "The Musoni Academy"))

        main_window = None  # Create an instance but don't show it initially

        def handle_login_signal(user):
            global main_window
            main_window = MainWindow()
            main_window.setWindowTitle("The Musoni Academy")
            window.close()
            main_window.showMaximized()

        app.setStyleSheet(styles)
        window.loginSignal.connect(handle_login_signal)
        window.show()
        sys.exit(app.exec())

    except Exception as e:
        logger.log_error(e.code(), e.message(), e.__traceback__)
