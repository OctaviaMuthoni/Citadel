"""
    This module shows a list of all library inventory items.
    These include:-
                - Chairs
                - Tables
                - Computers
                - Bookshelves
    An item belongs to either of these categories:- Furniture, Electronics, Cleaning Items, Utensils etc.
"""
from PySide6.QtWidgets import QWidget


class InventoryView(QWidget):
    def __init__(self):
        super(InventoryView, self).__init__()