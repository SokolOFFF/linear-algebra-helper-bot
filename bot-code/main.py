import telebot
import config
# import linal

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

theory_and_calculating_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
theory_button = types.KeyboardButton("Theory")
calc_button = types.KeyboardButton("Calculating")
theory_and_calculating_markup.add(theory_button, calc_button)

value_of_calc = ""
old_value_of_calc = ""
calc_keyboard = ""


@bot.message_handler(content_types=['text'], commands=['start', 'help'])
def handle_start_help(message):
    if message.text == "/start":
        bot.send_sticker(message.chat.id, sticker=config.start_sticker)
        bot.send_message(message.chat.id,
                         text="Hello, {0.first_name}!\nI am <b>{1.first_name}</b>, and I am <b>LinAl bot</b>. \nI hope I can help you somehow. ❤️".format(
                             message.from_user, bot.get_me()), parse_mode='HTML',
                         reply_markup=theory_and_calculating_markup)
    if message.text == "/help":
        bot.send_sticker(message.chat.id, sticker=config.help_sticker)
        bot.send_message(message.chat.id, text="Use buttons to navigate!", reply_markup=theory_and_calculating_markup)


@bot.message_handler(content_types=['text'], commands=['vector_calculator', 'matrix_calculator'])
def calculating_commands_checker(message):
    if message.text == "/vector_calculator":
        vector_keyboard(message)
    if message.text == "/matrix_calculator":
        matrix_keyboard(message)


@bot.message_handler(content_types=['text'])
def message_checker(message):
    if message.chat.type == 'private':
        if message.text == 'Theory':
            theory(message)
        elif message.text == "Calculating":
            whole_calculating(message)
        else:
            error(message)


# TODO: implement function
def vector_calculate(message, value):
    bot.send_message(message.chat.id, text="not implemented yet :<")


# TODO: implement function
def matrix_keyboard(message):
    bot.send_message(message.chat.id, text="not implemented yet :<")


def vector_keyboard(message):
    global calc_keyboard
    calc_keyboard = config.vector_calc_keyboard
    bot.send_message(message.chat.id, text='Type Here', reply_markup=calc_keyboard)

    bot.edit_message_text(chat_id=message.chat.id,
                          message_id=message.message_id,
                          text="What do you want to work with?",
                          reply_markup=None)


def error(message):
    bot.send_message(message.chat.id, text="Sorry, unknown command, please, check your input.")


def theory(message):
    themes_markup = types.InlineKeyboardMarkup(row_width=1)
    themes = config.themes
    for i in range(len(themes)):
        item = types.InlineKeyboardButton(themes[i], callback_data=str(i))
        themes_markup.add(item)

    bot.send_message(message.chat.id, text="Here are some themes. Select anything:", reply_markup=themes_markup)


def whole_calculating(message):
    adding_values_markup = types.InlineKeyboardMarkup(row_width=1)
    adding_vector_button = types.InlineKeyboardButton("Calculate vectors", callback_data="calculatingvectors")
    adding_matrix_button = types.InlineKeyboardButton("Calculate matriсes", callback_data="calculatingmatrices")
    adding_values_markup.add(adding_vector_button, adding_matrix_button)
    bot.send_message(message.chat.id, text="What do you want to work with?", reply_markup=adding_values_markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global value_of_calc, old_value_of_calc, calc_keyboard
    try:
        if call.message:
            match call.data:
                case "no":
                    value_of_calc = value_of_calc + " "

                case "C":
                    value_of_calc = ""

                case "n0":
                    value_of_calc = value_of_calc + "0"

                case "n1":
                    value_of_calc = value_of_calc + "1"

                case "n2":
                    value_of_calc = value_of_calc + "2"

                case "n3":
                    value_of_calc = value_of_calc + "3"

                case "n4":
                    value_of_calc = value_of_calc + "4"

                case "n5":
                    value_of_calc = value_of_calc + "5"

                case "n6":
                    value_of_calc = value_of_calc + "6"

                case "n7":
                    value_of_calc = value_of_calc + "7"

                case "n8":
                    value_of_calc = value_of_calc + "8"

                case "n9":
                    value_of_calc = value_of_calc + "9"

                case "[":
                    value_of_calc = value_of_calc + " [ "

                case "]":
                    value_of_calc = value_of_calc + " ] "

                case "*":
                    value_of_calc = value_of_calc + " * "

                case "x":
                    value_of_calc = value_of_calc + " x "

                case "+":
                    value_of_calc = value_of_calc + " + "

                case "-":
                    value_of_calc = value_of_calc + " - "

                case ",":
                    value_of_calc = value_of_calc + ", "

            if value_of_calc != old_value_of_calc:
                if value_of_calc == "":
                    bot.edit_message_text(chat_id=call.message.chat.id,
                                          message_id=call.message.message_id,
                                          text="0",
                                          reply_markup=calc_keyboard)
                    return 0
                else:
                    bot.edit_message_text(chat_id=call.message.chat.id,
                                          message_id=call.message.message_id,
                                          text=value_of_calc,
                                          reply_markup=calc_keyboard)
                    old_value_of_calc = value_of_calc
                    return 0
            elif call.data == 'C':
                return 0
            if call.data == "=V":
                vector_calculate(call.message, value_of_calc)
                value_of_calc = ""
                old_value_of_calc = ""
                bot.edit_message_text(chat_id=call.message.chat.id,
                                      message_id=call.message.message_id,
                                      text="0",
                                      reply_markup=calc_keyboard)
                return 0

            if call.data == 'calculatingvectors':
                vector_keyboard(call.message)
                return 0

            if call.data == 'calculatingmatrices':
                matrix_keyboard(call.message)
                return 0

            for i in range(len(config.themes)):
                if call.data == str(i):
                    bot.send_message(call.message.chat.id, config.links_to_themes[i])
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text="Here it is:",
                                  reply_markup=None)
    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)
