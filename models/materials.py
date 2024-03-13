from PySide6.QtSql import QSqlRelationalTableModel


class MaterialsModel(QSqlRelationalTableModel):
    """
        This model manages library materials. Different materials has different attributes and features.
        # common attributes:
            material_id - In format: media type/category/material number(vesion)/cummulation number
            title
            subject

        # conditional - if published:
            - ISBN
            - publisher
            - publication date


        ## uncommon details:
        - number of pages
        - length
        - genre
        - class
        - age limit
        - etc
    """
    def __init__(self):
        super(MaterialsModel, self).__init__()

        self.setTable("materials")

    def fetch_material(self):
        """
        :return: Returns all materials from the materials table
        """
        return self.select()
