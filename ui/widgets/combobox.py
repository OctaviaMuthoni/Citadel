from PySide6.QtWidgets import QComboBox


class ComboBox(QComboBox):
    def __init__(self, items):
        super(ComboBox, self).__init__()

        self.addItems(items)
        self.setObjectName("combobox")

