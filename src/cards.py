"""
    This module contains all methods to generate a member card, generate bar code and read bar code.
"""

from PIL import Image, ImageDraw, ImageFont


def generate_library_card(user_name, card_number, expiration_date, save_path='library_card_template.png'):
    # Create a blank white image for the views card
    card_width = 400
    card_height = 250
    card_color = 'white'
    card_image = Image.new('RGB', (card_width, card_height), card_color)
    draw = ImageDraw.Draw(card_image)

    # Set fonts
    title_font = ImageFont.truetype('arial.ttf', 20)
    data_font = ImageFont.truetype('arial.ttf', 16)

    # Draw card header
    # title_text = 'Library Card'
    # title_width, title_height = title_font.getsize(title_text)
    # title_position = ((card_width - title_width) // 2, 10)
    # draw.text(title_position, title_text, font=title_font, fill='black')

    # Draw user name
    user_name_text = f'Name: {user_name}'
    draw.text((20, 50), user_name_text, font=data_font, fill='black')

    # Draw card number
    card_number_text = f'Card Number: {card_number}'
    draw.text((20, 80), card_number_text, font=data_font, fill='black')

    # Draw expiration date
    expiration_date_text = f'Expires: {expiration_date}'
    draw.text((20, 110), expiration_date_text, font=data_font, fill='black')

    # Save the views card template
    card_image.save(save_path)


# Example usage:
generate_library_card('John Doe', '123456789', '2023-12-31', save_path='library_card_template.png')
