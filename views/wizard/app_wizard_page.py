from PySide6.QtWidgets import QWizardPage, QVBoxLayout, QGridLayout, QTextEdit, QHBoxLayout
from components import ImageComponent, LineEdit

from core.settings import Settings


class ApplicationConfigWizardPage(QWizardPage):
    def __init__(self):
        super(ApplicationConfigWizardPage, self).__init__()

        self.settings = Settings()

        layout = QVBoxLayout(self)

        basic_info_layout = QGridLayout()
        self.logo_upload = ImageComponent(self.settings.get_settings('logo', ""))
        self.slogan_textedit = QTextEdit()
        self.slogan_textedit.setText(self.settings.get_settings('slogan', ""))
        self.institution_edit = LineEdit("Institution", "institution")
        self.institution_edit.set_text(self.settings.get_settings('institution', ""))

        address_layout = QHBoxLayout()
        # address_layout.addWidget()

        contacts_layout = QHBoxLayout()

        social_layout = QHBoxLayout()

        basic_info_layout.addWidget(self.logo_upload, 0, 0)
        basic_info_layout.addWidget(self.institution_edit, 0, 1)
        basic_info_layout.addWidget(self.slogan_textedit, 1, 1)

        layout.addLayout(basic_info_layout)

        self.completeChanged.connect(lambda: print("completed"))
        print(self.isComplete())

    def save_settings(self):
        s = dict()
        s['institutions'] = self.institution_edit.text()
        s['slogan'] = self.slogan_textedit.document().toPlainText()
        # self.settings['logo'] = self.logo_upload.
        for k, v in s.items():
            self.settings.edit_settings(k, v)