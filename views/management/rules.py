from PySide6.QtCore import QSize
from PySide6.QtGui import QPixmap, QTextDocument
from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton, QHBoxLayout, QFormLayout

import qtawesome as qta

from components import MarkdownViewer


class ManageRulesView(QWidget):
    def __init__(self):
        super(ManageRulesView, self).__init__()

        layout = QGridLayout(self)
        logo_lbl = QLabel()
        logo_lbl.setFixedSize(200, 200)
        logo_lbl.setScaledContents(True)
        logo_lbl.setPixmap(QPixmap("resources/images/falcon.png"))

        rules_textedit = MarkdownViewer()
        rules_textedit.load_markdown_file('static/rules.md')
        rules_textedit.toMarkdown(QTextDocument.MarkdownFeature.MarkdownDialectCommonMark)

        self.download_btn = QPushButton()
        self.download_btn.setIcon(qta.icon("ph.download-light", color="blue"))
        self.download_btn.setIconSize(QSize(25, 25))

        self.print_btn = QPushButton()
        self.print_btn.setIcon(qta.icon("ph.printer-light", color="maroon"))
        self.print_btn.setIconSize(QSize(25, 25))

        options_layout = QHBoxLayout()
        options_layout.addStretch()
        options_layout.addWidget(self.download_btn)
        options_layout.addWidget(self.print_btn)
        options_layout.setContentsMargins(0, 60, 0, 0)

        brand_name = QLabel("The Academic Citadel")
        brand_name.setObjectName("sbrand")
        details = QFormLayout()
        details.addRow(brand_name)
        details.addWidget(QLabel("Last Review: 12/12/2023"))
        details.addWidget(QLabel("Overseen By: George. B. Oguta"))
        details.addRow(options_layout)

        layout.addWidget(logo_lbl, 0, 0)
        layout.addLayout(details, 0, 1)
        layout.addWidget(rules_textedit, 1, 0, 1, 2)
