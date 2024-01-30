from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QIntValidator, QRegularExpressionValidator, QDoubleValidator


class PortValidator(QIntValidator):
    def __init__(self):
        super(PortValidator, self).__init__()
        self.setRange(80, 9999)


class StringValidator(QRegularExpressionValidator):
    def __init__(self):
        super(StringValidator, self).__init__()

        self.reg_exp = QRegularExpression("[a-zA-Z]")
        self.setRegularExpression(self.reg_exp)


class EmailValidator(QRegularExpressionValidator):
    def __init__(self):
        super(EmailValidator, self).__init__()

        self.reg_exp = QRegularExpression("[a-zA-Z]")
        self.setRegularExpression(self.reg_exp)


class PhoneValidator(QRegularExpressionValidator):
    def __init__(self):
        super(PhoneValidator, self).__init__()

        self.reg_exp = QRegularExpression("[a-zA-Z]")
        self.setRegularExpression(self.reg_exp)


class DateValidator(QRegularExpressionValidator):
    def __init__(self):
        super(DateValidator, self).__init__()

        self.reg_exp = QRegularExpression("[a-zA-Z]")
        self.setRegularExpression(self.reg_exp)


class MemberNumberValidator(QRegularExpressionValidator):
    def __init__(self):
        super(MemberNumberValidator, self).__init__()

        self.reg_exp = QRegularExpression("[a-zA-Z]")
        self.setRegularExpression(self.reg_exp)


class CurrenctValidator(QDoubleValidator):
    def __init__(self):
        super(CurrenctValidator, self).__init__()

        self.setRange(0.00, 999999999.00)
        self.setDecimals(2)
