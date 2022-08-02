"""библеотеки для телеграмма"""
import telebot

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


@bot.message_handler(commands=['clear'])
def clear_command(message):
    bot.delete_message(message.chat.id, message.message_id - 1)


'''Виртуальные кнопки'''


@bot.message_handler(commands=['play'])
def play_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton('SDD', callback_data='sdd'),
        telebot.types.InlineKeyboardButton('Memory', callback_data='memory'),
        telebot.types.InlineKeyboardButton('mother', callback_data='mother')
    )
    bot.send_message(message.chat.id, 'Что хотите найти?', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def inline(c):
    keyboard = telebot.types.InlineKeyboardMarkup()
    if c.data == 'sdd':
        keyboard.add(
            telebot.types.InlineKeyboardButton('A-data', callback_data='A-data'),
            telebot.types.InlineKeyboardButton('Samsung', callback_data='Samsung'),
            telebot.types.InlineKeyboardButton('Apacer', callback_data='Apacer')
        )
        bot.send_message(c.message.chat.id, 'Какое sdd вас интересует?', reply_markup=keyboard)

    elif c.data == 'memory':
        keyboard.add(
            telebot.types.InlineKeyboardButton('kingston', callback_data='kingston'),
            telebot.types.InlineKeyboardButton('Crucial', callback_data='Crucial'),
            telebot.types.InlineKeyboardButton('Patriot', callback_data='Patriot')
        )
        bot.send_message(c.message.chat.id, 'Какая оперативная память вас интересует?', reply_markup=keyboard)
        
    elif c.data == 'mother':
        keyboard.add(
            telebot.types.InlineKeyboardButton('Asus', callback_data='asus'),
            telebot.types.InlineKeyboardButton('MSI', callback_data='msi'),
            telebot.types.InlineKeyboardButton('Gygabyte', callback_data='gygabyte')
        )
        bot.send_message(c.message.chat.id, 'Какая материнская плата вас интересует?', reply_markup=keyboard)


    bot.answer_callback_query(callback_query_id=c.id, text='Ваш результат!')
    if c.data == 'A-data':
        bot.send_message(c.message.chat.id, text='120 ГБ 2.5" SATA накопитель A-Data SU650')
    elif c.data == 'Samsung':
        bot.send_message(c.message.chat.id, text='500 ГБ 2.5" SATA накопитель Samsung 870 EVO')
    elif c.data == 'Apacer':
        bot.send_message(c.message.chat.id, text='120 ГБ 2.5" SATA накопитель Apacer AS340 PANTHER')
    elif c.data == 'kingston':
        bot.send_message(c.message.chat.id, text='Kingston FURY Beast Black [KF432C16BBK2/16] 16 ГБ')
    elif c.data == 'Crucial':
        bot.send_message(c.message.chat.id, text='Crucial [CT4G4DFS8266] 4 ГБ')
    elif c.data == 'Patriot':
        bot.send_message(c.message.chat.id, text=' Patriot Viper Steel [PVS416G320C6K] 16 ГБ')
    elif c.data == 'asus':
        bot.send_message(c.message.chat.id, text='ASUS PRIME H510M-K')
    elif c.data == 'msi':
        bot.send_message(c.message.chat.id, text='MSI MAG B550 TOMAHAWK')
    elif c.data == 'gygabyte':
        bot.send_message(c.message.chat.id, text='GIGABYTE B560M DS3H V2')


"""Запускаем бота После ее добавления у бота будет постоянно проверяться наличие новых сообщений"""

bot.infinity_polling()
