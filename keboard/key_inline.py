from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def get_keyboard_1_inline():
    keyboard_inline = InlineKeyboardMarkup(row_width=1)
    but_inline = InlineKeyboardButton('Читать', url='https://author.today/reader/297356')
    keyboard_inline.add(but_inline)

    return keyboard_inline


def get_keyboard_2_inline():
    keyboard_inline2 = InlineKeyboardMarkup(row_width=1)
    but_inline1 = InlineKeyboardButton('Читать', url='https://author.today/reader/346986')
    keyboard_inline2.add(but_inline1)

    return keyboard_inline2


def get_keyboard_3_inline():
    keyboard_inline3 = InlineKeyboardMarkup(row_width=1)
    but_inline2 = InlineKeyboardButton('Читать', url='https://litnet.com/ru/reader/moi-milyi-boss-b436777')
    keyboard_inline3.add(but_inline2)

    return keyboard_inline3