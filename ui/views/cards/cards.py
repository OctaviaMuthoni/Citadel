from PIL import Image
from PySide6.QtWidgets import QWidget


class CardsView(QWidget):
    def __init__(self):
        super(CardsView, self).__init__()

    def issue(self):
        pass

    def lost(self):
        pass

    def generate_serial(self):
        pass

    def load_template(self) -> Image:
        pass

    def add_card(self):
        pass
