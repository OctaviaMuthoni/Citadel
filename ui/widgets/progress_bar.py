from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QProgressBar, QLabel


class ProgressBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Set the size of the widget
        self.setFixedSize(200, 200)

        # Create a vertical layout
        layout = QVBoxLayout(self)

        # Create a progress bar
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, 5)
        layout.addWidget(self.progress_bar)

        # Display the current value text
        self.progress_text = QLabel(self.progress_bar.text())
        layout.addWidget(self.progress_text)

        # Set the center alignment for the layout
        layout.setAlignment(Qt.AlignCenter)

    def set_value(self, value):
        # Update the progress bar and text
        self.progress_bar.setValue(value)
        self.progress_text.setText(f"{value}/5")
