"""библеотеки для телеграмма"""
import telebot

'''import random'''
'''import json'''

"""Токен самого бота"""
bot = telebot.TeleBot('5544754274:AAE1f6T3fJOlpPkDFM69Cz6zbKh5ML3NDLo')

"""Ответы на сообщения """


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id,
                     'Приветствую на нашем канале Shop-place.\n' +
                     'Если есть проблемы с ботом, Напиши /help.\n' +
                     'Для очищения чата, используйте /clear.\n' +
                     'Чтобы начать работу, Напиши /play')


@bot.message_handler(commands=['help'])
def help_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            'Написать разработчику', url='https://www.youtube.com/watch?v=DkEf9eus0Zc'
        )
    )
    bot.send_message(message.chat.id, 'Грустно если не работает', reply_markup=keyboard)


'''Виртуальные кнопки'''


@bot.message_handler(commands=['play'])
def play_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'SDD', callback_data='sdd'
        ),
        telebot.types.InlineKeyboardButton(
            'Memory', callback_data='memory'
        ),
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'mother', callback_data='mother'
        )
    )
    bot.send_message(message.chat.id, 'Что хотите найти?', reply_markup=keyboard)


@bot.message_handler(commands=['clear'])
def clear_command(message):
    bot.delete_message(message.chat.id, message.message_id - 1)



@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Спасибо за честный ответ!')
    answer = ''
    if call.data == 'sdd':
        answer = 'увы, у вас нет денег!'
    elif call.data == 'memory':
        answer = 'аа оперативки нет!'
    elif call.data == 'mother':
        answer = 'мать сгорела )))))))))'

    # bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    bot.send_message(call.message.chat.id, answer)


"""Запускаем бота После ее добавления у бота будет постоянно проверяться наличие новых сообщений"""
bot.polling(none_stop=True, interval=0)
