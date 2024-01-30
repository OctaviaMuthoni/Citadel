from PySide6.QtWidgets import QApplication, QMainWindow, QToolButton, QMenu, QVBoxLayout, QPushButton, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Create a central widget and a layout
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # Create a tool button
        tool_button = QToolButton()
        tool_button.setText("Menu Button")

        # Create a menu and add actions
        menu = QMenu(self)
        menu.addAction("Action 1")
        menu.addAction("Action 2")

        # Set the menu for the tool button
        tool_button.setMenu(menu)

        # Create other buttons
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")

        # Add widgets to the layout
        layout.addWidget(tool_button)
        layout.addWidget(button1)
        layout.addWidget(button2)

        # Set the central widget
        self.setCentralWidget(central_widget)

        self.setWindowTitle("Menu Example")
        self.setGeometry(100, 100, 400, 200)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
