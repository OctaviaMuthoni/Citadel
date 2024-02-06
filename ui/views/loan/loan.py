"""
    This is a view module for the loan package.
    It shows all borrowed materials and provide an interface to borrow and return materials from the library.
"""

from PySide6.QtWidgets import QWidget


class LoanView(QWidget):
    def __init__(self):
        super(LoanView, self).__init__()

