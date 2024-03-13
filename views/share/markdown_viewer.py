from PySide6.QtWidgets import QTextEdit


class MarkdownViewer(QTextEdit):
    def __init__(self):
        super().__init__()