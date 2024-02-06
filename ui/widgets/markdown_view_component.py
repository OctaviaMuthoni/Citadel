import markdown
from PySide6.QtWidgets import QTextBrowser


class MarkdownViewer(QTextBrowser):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setReadOnly(True)

    def load_markdown_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            markdown_content = file.read()
            html_content = markdown.markdown(markdown_content)
            self.setHtml(html_content)
