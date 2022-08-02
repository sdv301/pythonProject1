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


    if c.data == 'A-data':
        bot.send_message(c.message.chat.id, text='120 ГБ 2.5" SATA накопитель A-Data SU650  \nЦена 1 399' + '\nhttps://www.dns-shop.ru/product/775bd788e3e51b80/120-gb-25-sata-nakopitel-a-data-su650-asu650ss-120gt-r/')
    elif c.data == 'Samsung':
        bot.send_message(c.message.chat.id, text='500 ГБ 2.5" SATA накопитель Samsung 870 EVO  \nЦена 8 799' + '\nhttps://www.dns-shop.ru/product/17ee99c15ab83332/500-gb-25-sata-nakopitel-samsung-870-evo-mz-77e500bw/')
    elif c.data == 'Apacer':
        bot.send_message(c.message.chat.id, text='120 ГБ 2.5" SATA накопитель Apacer AS340 PANTHER  \nЦена 1 250' + '\nhttps://www.dns-shop.ru/product/66781d99f8b53330/120-gb-25-sata-nakopitel-apacer-as340-panther-ap120gas340g-1/')
    elif c.data == 'kingston':
        bot.send_message(c.message.chat.id, text='Kingston FURY Beast Black [KF432C16BBK2/16] 16 ГБ  \nЦена 6 099' + '\nhttps://www.dns-shop.ru/product/e8acb46cdae8d763/operativnaa-pamat-kingston-fury-beast-black-kf432c16bbk216-16-gb/'),
        bot.send_message(c.message.chat.id, text='Kingston FURY Beast Black [KF432C16BBK2/8] 8 ГБ \nЦена 4 299' + '\nhttps://www.dns-shop.ru/product/7930d6bfdae8d763/operativnaa-pamat-kingston-fury-beast-black-kf432c16bbk28-8-gb/')
        bot.send_message(c.message.chat.id, text='Kingston FURY Beast Black [KF432C16BB/8] 8 ГБ \nЦена 2 899' + '\nhttps://www.dns-shop.ru/product/cacbeacfdae8d763/operativnaa-pamat-kingston-fury-beast-black-kf432c16bb8-8-gb/')
    elif c.data == 'Crucial':
        bot.send_message(c.message.chat.id, text='Crucial [CT4G4DFS8266] 4 ГБ \nЦена 1 599' + '\nhttps://www.dns-shop.ru/product/b849abfa155f3332/operativnaa-pamat-crucial-ct4g4dfs8266-4-gb/')
    elif c.data == 'Patriot':
        bot.send_message(c.message.chat.id, text=' Patriot Viper Steel [PVS416G320C6K] 16 ГБ \nЦена 4 999' + '\nhttps://www.dns-shop.ru/product/5762c1c346fc1b80/operativnaa-pamat-patriot-viper-steel-pvs416g320c6k-16-gb/')
    elif c.data == 'asus':
        bot.send_message(c.message.chat.id, text='ASUS PRIME H510M-K \nЦена 5 499' + '\nhttps://www.dns-shop.ru/product/2012e739a9902ff1/materinskaa-plata-asus-prime-h510m-k/ ')
    elif c.data == 'msi':
        bot.send_message(c.message.chat.id, text='MSI MAG B550 TOMAHAWK \nЦена 23 999' + '\nhttps://www.dns-shop.ru/product/b9a4575dafa61b80/materinskaa-plata-msi-mag-b550-tomahawk/')
    elif c.data == 'gygabyte':
        bot.send_message(c.message.chat.id, text='GIGABYTE B560M DS3H V2 \nЦена 6 299' + '\nhttps://www.dns-shop.ru/product/d69943561a91ed20/materinskaa-plata-gigabyte-b560m-ds3h-v2/')

    bot.answer_callback_query(callback_query_id=c.id, show_alert=False, text='Спасибо за ваш выбор!')

"""Запускаем бота После ее добавления у бота будет постоянно проверяться наличие новых сообщений"""

bot.infinity_polling()

