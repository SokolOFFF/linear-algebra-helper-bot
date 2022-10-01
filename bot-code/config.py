import telebot

from SECRETS import BOT_TOKEN

TOKEN = BOT_TOKEN
help_sticker = "https://t.me/stikertforlinal/2"
start_sticker = "https://t.me/stikertforlinal/3"
themes = ["Dot Product", "Cross Product", "Matrix"]
links_to_themes = ["https://en.wikipedia.org/wiki/Dot_product",
                   "https://en.wikipedia.org/wiki/Cross_product",
                   "https://en.wikipedia.org/wiki/Matrix_(mathematics)"]

vector_calc_keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)

vector_calc_keyboard.row(telebot.types.InlineKeyboardButton("[", callback_data="["),
                         telebot.types.InlineKeyboardButton("]", callback_data="]"),
                         telebot.types.InlineKeyboardButton("X", callback_data="x"),
                         telebot.types.InlineKeyboardButton("*", callback_data="*"))

vector_calc_keyboard.row(telebot.types.InlineKeyboardButton("7", callback_data="n7"),
                         telebot.types.InlineKeyboardButton("8", callback_data="n8"),
                         telebot.types.InlineKeyboardButton("9", callback_data="n9"),
                         telebot.types.InlineKeyboardButton("+", callback_data="+"))

vector_calc_keyboard.row(telebot.types.InlineKeyboardButton("4", callback_data="n4"),
                         telebot.types.InlineKeyboardButton("5", callback_data="n5"),
                         telebot.types.InlineKeyboardButton("6", callback_data="n6"),
                         telebot.types.InlineKeyboardButton("-", callback_data="-"))

vector_calc_keyboard.row(telebot.types.InlineKeyboardButton("1", callback_data="n1"),
                         telebot.types.InlineKeyboardButton("2", callback_data="n2"),
                         telebot.types.InlineKeyboardButton("3", callback_data="n3"),
                         telebot.types.InlineKeyboardButton("C", callback_data="C"))

vector_calc_keyboard.row(telebot.types.InlineKeyboardButton(" ", callback_data="no"),
                         telebot.types.InlineKeyboardButton("0", callback_data="n0"),
                         telebot.types.InlineKeyboardButton(",", callback_data=","),
                         telebot.types.InlineKeyboardButton("=", callback_data="=V"))
