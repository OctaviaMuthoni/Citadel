from PySide6.QtSql import QSqlTableModel


class CategoriesModel(QSqlTableModel):
    """
        This model represents the materials broad category
        These include:
            - Print media
                books
                    course books
                    supplementary books
                novels
                    genres: action
                            fiction
                            love
                            history
                            mystery
                story books
                    genres: action
                            fiction
                            love
                            history
                            mystery
                periodicals
                maps, articles, newspapers, journals, magazines
                etc.

            - audio files
                All above in audio files like radio lessons
            - video files
                All above in video clips like the acted version of the birth of Jesus, wildlife or physical features.

        Materials are classified into these categories regardless of their print media.
    """
    def __init__(self):
        super().__init__()
