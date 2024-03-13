from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QGridLayout, QWidget

from views.share import FormField, ImageWidget


class Form(QFrame):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

        self.fields = dict()
        self.setObjectName("form")

    def addField(self, form_field: FormField | ImageWidget, row=0, column=0, row_span=1, col_span=1):
        self.layout().addWidget(form_field, row, column, row_span, col_span)
        self.fields[form_field.name] = form_field

    def addWidget(self, widget: QWidget, row=0, column=0, row_span=1, col_span=1):
        self.layout().addWidget(widget, row, column, row_span, col_span)

    def isValid(self):
        # a form is only valid if all fields in the form are valid
        for field in self.fields:
            if not field.isValid():
                field.setObjectName("invalid-form-field")
                return False

        return True

    def data(self) -> dict:
        """
            The function gets all data from the fields.
        :return: form_data: A dictionary of all fields data
        """
        form_data = dict()
        for field in self.fields:
            form_data[field.name] = field.value

        return form_data

    # def hide_columns(self, row, columns: list):
    #     for column in columns:
    #         item = self.layout().itemAtPosition(row, column)
    #         if item:
    #             widget = item.widget()
    #             if widget:
    #                 widget.hide()
    #
    # def hide_row(self, row):
    #     for i in range(self.layout().columnCount()):
    #         item = self.layout().itemAtPosition(row, i)
    #         if item:
    #             widget = item.widget()
    #             if widget:
    #                 widget.hide()
    #     self.layout().setRowStretch(row, 0)
    #
    # def show_row(self, row):
    #     for i in range(self.layout().columnCount()):
    #         item = self.layout().itemAtPosition(row, i)
    #         if item:
    #             widget = item.widget()
    #             if widget:
    #                 widget.show()
    #
    # def reset(self):
    #     for field in self.fields:
    #         # field.reset()
    #         pass
