import logging
import os
import sys

from PySide6.QtCore import QPropertyAnimation, QRect
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from core import LOGS_PATH, STYLES_PATH
from library import Library
from src.settings import Settings
from views.login import LoginWindow

if __name__ == '__main__':

    log_path = os.path.join(LOGS_PATH, 'application.log')
    styles_path = os.path.join(STYLES_PATH, 'styles.qss')

    logging.basicConfig(filename=log_path, level=logging.DEBUG)

    # noinspection PyBroadException
    try:
        with open(styles_path) as stylesheet:
            styles = stylesheet.read()

        app = QApplication([])
        app.setWindowIcon(QIcon("falcon.ico"))
        settings = Settings()

        window = LoginWindow(settings)
        window.setWindowTitle(settings.get_settings("institution", "The Citadel Academy"))

        main_window = None  # Create an instance but don't show it initially

        def handle_login_signal(user):
            global main_window
            main_window = Library(user, settings)
            main_window.setWindowTitle("The Citadel Academy")
            window.close()
            main_window.showMaximized()

        app.setStyleSheet(styles)
        window.loginSignal.connect(handle_login_signal)
        window.show()
        sys.exit(app.exec())

    except Exception as e:
        logging.exception("An error occurred:")
