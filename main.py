import os
import sys

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QLabel

import resources_rc

from citadexx import MainWindow
from core import STYLES_PATH
from views import LoginWindow

if __name__ == '__main__':

    try:
        styles = ""
        with open("resources/stylesheets/light.qss") as stylesheet:
            styles += stylesheet.read()

        app = QApplication(sys.argv)

        window = LoginWindow()
        main_window = None

        def handle_login_signal():
            global main_window
            main_window = MainWindow()
            main_window.setStyleSheet(styles)
            main_window.showMaximized()
            window.close()

        # app.setStyleSheet(styles)
        window.loginSignal.connect(handle_login_signal)
        window.show()
        sys.exit(app.exec())

    except Exception as e:
        print(e)
