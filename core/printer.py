from PySide6.QtCore import Qt
from PySide6.QtGui import QTextDocument, QTextCursor
from PySide6.QtPrintSupport import QPrinter
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget

class PrintWithoutDialog(QMainWindow):
    def __init__(self):
        super(PrintWithoutDialog, self).__init__()

        # Initialize UI components
        self.init_ui()

    def init_ui(self):
        # Create a QTextEdit widget for document editing
        self.text_edit = QTextEdit(self)
        self.text_edit.setPlainText("Hello, this is a sample text for printing.")

        # Create a button to trigger printing
        print_button = QPushButton("Print", self)
        print_button.clicked.connect(self.print_document)

        # Create a layout
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(print_button)

        # Create a central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)

        # Set the central widget
        self.setCentralWidget(central_widget)

        # Set up the main window
        self.setWindowTitle('Print without Dialog')
        self.setGeometry(100, 100, 600, 400)

    def print_document(self):
        # Create a QTextDocument
        document = QTextDocument()
        document.setPlainText(self.text_edit.toPlainText())

        # Create a printer with pre-configured settings
        printer = QPrinter()
        printer.setPrinterName("Your Printer Name")  # Replace with your printer's name
        # printer.setPageLayout(QPrinter)
        # printer.setOrientation(QPrinter.OutputFormat.NativeFormat)

        # Print the document
        document.print_(printer)


if __name__ == "__main__":
    app = QApplication([])
    window = PrintWithoutDialog()
    window.show()
    app.exec()
