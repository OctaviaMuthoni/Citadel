from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QActionGroup, Qt, QPixmap
from PySide6.QtWidgets import QWidget, QToolBar, QStackedWidget, QVBoxLayout, QLabel, QDateEdit, \
    QHBoxLayout, QTableView, QSplitter, QComboBox, QSpinBox, QPushButton


import qtawesome as qta
import barcode
from barcode.writer import ImageWriter

from views.share import ComboBox
from views.share import SearchEdit


class CardsList(QWidget):
    def __init__(self):
        super().__init__()

        self.search = SearchEdit()
        self.status_combo = ComboBox([
            "in use",
            "lost",
            "expired",
            "replaced",
            "returned"
        ])

        self.issue_date_edit = QDateEdit()

        filter_layout = QHBoxLayout()
        filter_layout.addWidget(self.search)
        filter_layout.addStretch()
        filter_layout.addWidget(self.issue_date_edit)
        filter_layout.addWidget(self.status_combo)

        self.cards_table_view = QTableView()

        layout = QVBoxLayout(self)
        layout.addLayout(filter_layout)
        layout.addWidget(self.cards_table_view)


CARD_HEIGHT = 500
CARD_WIDTH = 800
BG_COLOR = "#fafafa"


class CardsTemplate(QSplitter):
    def __init__(self):
        super().__init__()

        self.title_font_combo = QComboBox()
        self.title_font_combo.addItems([
            "arial", "times"
        ])

        self.title_font_size_spinbox = QSpinBox()
        self.title_font_size_spinbox.setValue(30)

        self.details_font_combo = QComboBox()
        self.details_font_combo.addItems([
            "arial", "times"
        ])

        self.details_font_size_spinbox = QSpinBox()
        self.details_font_size_spinbox.setValue(30)

        self.save_btn = QPushButton("save")
        self.save_btn.clicked.connect(self.preview_template)

        self.config_widget = QWidget()
        config_layout = QVBoxLayout(self.config_widget)
        config_layout.addWidget(self.title_font_combo)
        config_layout.addWidget(self.title_font_size_spinbox)
        config_layout.addWidget(self.details_font_combo)
        config_layout.addWidget(self.details_font_size_spinbox)
        config_layout.addWidget(self.save_btn)

        self.template_preview_widget = QWidget()
        template_layout = QVBoxLayout(self.template_preview_widget)

        self.template_lbl = QLabel()

        template_layout.addWidget(self.template_lbl)

        self.addWidget(self.config_widget)
        self.addWidget(self.template_preview_widget)

        self.preview_template()

    def preview_template(self):
        self.generate_card_template()
        template = QPixmap("res/card_template.jpg")
        self.template_lbl.setPixmap(template)

    def generate_card_template(self):

        title_size = self.title_font_size_spinbox.value()
        title_font = self.title_font_combo.currentText()

        details_size = self.details_font_size_spinbox.value()
        details_font = self.details_font_combo.currentText()

        title_font = ImageFont.truetype(f'{title_font}.ttf', title_size)
        disclaimer_font = ImageFont.truetype('arial.ttf', 28)
        details_font = ImageFont.truetype(f'{details_font}.ttf', details_size)

        # Create a new image instance for the card
        card = Image.new('RGB', (CARD_WIDTH, CARD_HEIGHT), BG_COLOR)
        draw = ImageDraw.Draw(card)

        # Load and paste the face image
        face_image = Image.open("res/images/wambui.jpg")
        face_image = face_image.resize((250, 250))
        face_image = face_image.convert("RGBA")

        # Draw the solid color background shapes
        draw.rectangle(((0, 0), (CARD_WIDTH, 100)), "#05ADD3")
        draw.line(((0, 120), (CARD_WIDTH, 120)), "#05ADD3", width=1)
        card.paste(face_image, (30, 145))
        draw.polygon(((0, 0), (220, 0), (0, 220)), "#05ADD3")
        draw.polygon(((0, 0), (150, 0), (0, 150)), "#EAEDFE")
        draw.line(((0, CARD_HEIGHT - 80), (CARD_WIDTH, CARD_HEIGHT - 80)), "#05ADD3", width=1)
        draw.polygon(((CARD_WIDTH, CARD_HEIGHT), (CARD_WIDTH - 150, CARD_HEIGHT), (CARD_WIDTH, CARD_HEIGHT - 150)),
                     "#EAEDFE")
        draw.polygon(((CARD_WIDTH, CARD_HEIGHT), (CARD_WIDTH - 80, CARD_HEIGHT), (CARD_WIDTH, CARD_HEIGHT - 80)),
                     "#05ADD3")

        # Load and resize the logo image
        logo_image = Image.open("favicon.ico")
        logo_image = logo_image.resize((120, 120))

        draw.text((310, 150), "Name: xxxxxx Muthoni Nderitu", font=details_font, fill='#333333',
                  bg='rgba(255, 255, 255, 100)')
        draw.text((310, 185), "Member No.: N11/3/00416/014", font=details_font, fill='#333333',
                  bg='rgba(255, 255, 255, 100)')
        draw.text((310, 220), "Issue date: 08/2023", font=details_font, fill='#333333', bg='rgba(255, 255, 255, 100)')
        draw.text((310, 255), "Expiry date: 04/2024", font=details_font, fill='#333333', bg='rgba(255, 255, 255, 100)')

        barcode_image = barcode.get_barcode_class('code39')("N11/3/0416/014", writer=ImageWriter())
        barcode_image = barcode_image.render(text="")
        resized_barcode_image = barcode_image.resize((460, 70))
        card.paste(resized_barcode_image, (280, 330))

        # Draw text
        draw.text((150, 15), "THE LILY ACADEMY", font=title_font, fill='#fafafa', bg='rgba(0, 0, 0, 0)')
        draw.text((150, 50), "LIBRARY CARD", font=title_font, fill='#fafafa', bg='rgba(0, 0, 0, 0)')
        draw.text((30, CARD_HEIGHT - 60), "For Library Use Only - Not Proof of Current Status", font=disclaimer_font,
                  fill='#05ADD3', bg='rgba(0, 0, 0, 0)')

        # Paste the logo image onto the card
        card.paste(logo_image, (30, 10), logo_image)

        # Save the card template
        card.save("res/templates/card_template.jpg")


class LostCards(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Lost"))


class CardsReplacement(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("replacement"))


class CardsView(QWidget):

    def __init__(self):
        super(CardsView, self).__init__()

        # create a dictionary of views
        self.views = {
            "list": CardsList(),
            "template": CardsTemplate(),
            "lost": LostCards(),
            "replace": CardsReplacement()
        }

        # create a toolbar for the cards
        self.cards_toolbar = QToolBar()

        # configure toolbar
        self.cards_toolbar.setIconSize(QSize(30, 30))
        self.cards_toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        # actions that redirect to a view
        list_action = QAction(qta.icon("fa.id-card", color="#05ADD3"), "list")
        template_action = QAction(qta.icon("fa.vcard-o", color="#05ADD3"), "template")
        lost_action = QAction(qta.icon("mdi.credit-card-remove-outline", color="#05ADD3"), "lost")
        replace_action = QAction(qta.icon("mdi.credit-card-sync-outline", color="#05ADD3"), "replace")

        # Create action group for actions redirecting to a view
        action_group = QActionGroup(self.cards_toolbar)
        action_group.addAction(list_action)
        action_group.addAction(template_action)
        action_group.addAction(lost_action)
        action_group.addAction(replace_action)

        # set callback for action view
        action_group.triggered.connect(self.navigate)

        # add actions to toolbar
        self.cards_toolbar.addAction(list_action)
        self.cards_toolbar.addAction(template_action)
        self.cards_toolbar.addAction(lost_action)
        self.cards_toolbar.addAction(replace_action)
        self.cards_toolbar.addAction(qta.icon("mdi.credit-card-plus", color="#05ADD3"), "issue", self.issue)
        self.cards_toolbar.addAction(qta.icon("mdi.credit-card-refund-outline", color="#05ADD3"), "export", self.export)

        # Add views to central widget
        self.cards_central_widget = QStackedWidget()
        for view in self.views.values():
            self.cards_central_widget.addWidget(view)

        # Add widgets to main layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.cards_toolbar)
        layout.addWidget(self.cards_central_widget)

    def navigate(self, action):
        self.cards_central_widget.setCurrentWidget(self.views[action.text().lower()])

    def issue(self):
        print("card issued")

    def export(self):
        print("cards_exported")
