from PySide6.QtWidgets import QComboBox


class MultiSelectCombo(QComboBox):
    def __init__(self, items: list):
        super().__init__()

        self.addItems(items)
