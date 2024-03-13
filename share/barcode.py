from barcode import writer, get_barcode_class
from PIL.Image import Image


# TODO: implement functions to read barcode

def generate_card_barcode(card_data: dict, show_text=False) -> Image:
    barcode_image = get_barcode_class('code39')(card_data, writer=writer.ImageWriter())
    barcode_image = barcode_image.render(text=show_text)

    return barcode_image


def generate_isbn_barcode(isbn_number: int) -> Image:
    barcode_image = get_barcode_class('code128')(isbn_number, writer=writer.ImageWriter())
    barcode_image = barcode_image.render()

    return barcode_image


def read_barcode(barcode_image) -> dict | int:
    pass
