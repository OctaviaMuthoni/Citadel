import sys

from PySide6.QtCore import QPropertyAnimation, QRect, QEasingCurve, QParallelAnimationGroup, QPoint
from PySide6.QtWidgets import QLabel, QApplication, QFrame, QVBoxLayout, QPushButton, QWidget, QHBoxLayout, QSizePolicy


class Citadel(QWidget):
    def __init__(self):
        super().__init__()

        self.menu_toggle = QPushButton("show menu")
        self.menu_toggle.clicked.connect(self.toggle_menu)

        self.sidebar = QLabel("side bar")
        self.sidebar.setFixedWidth(200)
        self.sidebar.setObjectName("sidebar")

        self.main_content = QFrame()
        self.main_content.setObjectName("main-content")

        layout = QVBoxLayout(self.main_content)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(self.menu_toggle)

        mlayout = QHBoxLayout(self)
        mlayout.setContentsMargins(0, 0, 0, 0)
        mlayout.setSpacing(0)
        mlayout.addWidget(self.sidebar)
        mlayout.addWidget(self.main_content)

        self.setStyleSheet("""
            #sidebar {
                background: red;
                border: 1px solid red;
            }
            #main-content {
                background-color: green;
            }
        """)

        self.animation_group = QParallelAnimationGroup()
        self.animation_group.setDirection(QPropertyAnimation.Direction.Backward)
        self.sidebar_pos = self.mapToGlobal(self.sidebar.pos())

    def toggle_menu(self):
        sidebar_anim = QPropertyAnimation(self.sidebar, b'pos')
        sidebar_anim.setStartValue(self.sidebar_pos)
        sidebar_anim.setEndValue(QPoint(
            self.sidebar_pos.x() - self.sidebar.width(),
            self.sidebar_pos.y())
        )
        sidebar_anim.setDuration(500)

        main_content_animation = QPropertyAnimation(self.main_content, b'geometry')
        start = QRect(
            self.sidebar_pos.x() + self.sidebar.width(),
            self.sidebar_pos.y(),
            self.width() - self.sidebar.width(),
            self.height()
        )
        end = QRect(
            self.sidebar_pos.x(),
            self.sidebar_pos.y(),
            self.width(),
            self.height()
        )

        main_content_animation.setStartValue(start)
        main_content_animation.setEndValue(end)
        main_content_animation.setDuration(500)

        self.animation_group.addAnimation(sidebar_anim)
        self.animation_group.addAnimation(main_content_animation)

        if self.animation_group.direction() == QPropertyAnimation.Direction.Forward:
            self.animation_group.setDirection(QPropertyAnimation.Direction.Backward)
        else:
            self.animation_group.setDirection(QPropertyAnimation.Direction.Forward)

        self.animation_group.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Citadel()
    window.show()
    sys.exit(app.exec())
