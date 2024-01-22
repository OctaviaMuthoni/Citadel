from dataclasses import dataclass

from PySide6.QtSql import QSqlTableModel


class InstitutionLevel:
    PRIMARY: str = "Primary School"
    JSS: str = "Junior School"
    TERTIARY: str = "Tertiary Institution"


@dataclass
class Institution:
    name: str
    logo: str
    motto: str
    level: str
    phone_number: str
    email: str
    website: str
    location: str


class InstitutionModel(QSqlTableModel):
    def __init__(self):
        super(InstitutionModel, self).__init__()

        self.setTable("institution")


