import telebot
from telebot import types
import datetime
import config
import exel
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


bot = telebot.TeleBot(config.BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.copy_message(message.chat.id, config.adminChat, 299)
    murkupS = types.InlineKeyboardMarkup()
    murkupS.add(types.InlineKeyboardButton('РАСПИСАНИЕ 📆', callback_data='schedule'))
    murkupS.add(types.InlineKeyboardButton('ПРОГРАММЫ ТУРОВ 🗺️', callback_data='regions'))
    murkupS.add(types.InlineKeyboardButton('ОТВЕТЫ НА ВОПРОСЫ 💬', callback_data='answers'))
    bot.copy_message(message.chat.id, config.adminChat, 283, reply_markup=murkupS)


@bot.message_handler(commands=['schedule'])
def scheduleS(message):
    murkup2 = types.InlineKeyboardMarkup()
    murkup2.add(types.InlineKeyboardButton('ПРОГРАММЫ ТУРОВ 🗺️', callback_data="regions"))
    bot.copy_message(message.chat.id, config.adminChat, config.startmes, reply_markup=murkup2)


@bot.message_handler(commands=['regions'])
def region(message):
    print(message.chat.id, message.from_user.id)
    murkupR = types.InlineKeyboardMarkup()
    l = 1
    for i in config.regions:
        murkupR.add(types.InlineKeyboardButton(i, callback_data=l))
        l += 1
    bot.send_message(message.chat.id, '*По какому туру Вы хотите получить программу?*', reply_markup=murkupR, parse_mode='MarkDown')


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    print(callback.data)
    if callback.data == 'schedule':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)

        scheduleS(callback.message)
    elif callback.data == 'regions':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)

        region(callback.message)
    elif callback.data == 'answers':
        faq(callback.message)
    try:
        if int(callback.data) > 0:
            bot.copy_message(callback.message.chat.id, config.adminChat, int(config.mes_ID_PDF[int(callback.data) - 1]))
            murkup2 = types.InlineKeyboardMarkup()
            murkup2.add(types.InlineKeyboardButton('Подписаться на ТГ-канал 📲', url=config.url_Chanel))
            bot.send_message(callback.message.chat.id, 'Для бронирования места и по любым вопросам пишите 👇\n@mary_travel_manager\n\nА также переходите в наш канал, чтобы быть в курсе всех travel-новостей!', reply_markup=murkup2)
            if str(callback.message.chat.username) == 'None':
                bot.send_message(config.adminChat, f'{callback.message.chat.first_name} {callback.message.chat.last_name}\n({callback.message.chat.id}) интересовался {config.regions[int(callback.data) - 1]} \n\n#{config.regions[int(callback.data) - 1]}', parse_mode='HTML')
            elif str(callback.message.chat.username) != 'None':
                bot.send_message(config.adminChat, f'{callback.message.chat.first_name} {callback.message.chat.last_name}\n@{callback.message.chat.username} ({callback.message.chat.id}) интересовался {config.regions[int(callback.data) - 1]} \n\n#{config.regions[int(callback.data) - 1]}', parse_mode='HTML')
            exel.append_ex([datetime.datetime.now(), callback.message.chat.id, callback.message.chat.first_name, callback.message.chat.last_name, f'@{callback.message.chat.username}', config.regions[int(callback.data) - 1]])
    except Exception as ex:
        print(ex)
        print('faq')
    if callback.data == 'faq_1':
        bot.copy_message(callback.message.chat.id, config.adminChat, 147)
    if callback.data == 'faq_2':
        bot.copy_message(callback.message.chat.id, config.adminChat, 148)
    if callback.data == 'faq_3':
        bot.copy_message(callback.message.chat.id, config.adminChat, 149)
    if callback.data == 'faq_4':
        bot.copy_message(callback.message.chat.id, config.adminChat, 150)
    if callback.data == 'faq_5':
        bot.copy_message(callback.message.chat.id, config.adminChat, 151)
    if callback.data == 'faq_6':
        bot.copy_message(callback.message.chat.id, config.adminChat, 152)


@bot.message_handler(commands=['id'])
def id_send(message):
    if config.developerMode == True:
        bot.send_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, message.chat.id)


@bot.message_handler(commands=['exel_file_unload'])
def file_unload(message):
    if str(message.chat.id) == config.adminChat:
        file = open(config.exel_file, 'rb')
        bot.send_document(message.chat.id, file)
    else:
        print('Non admin chat')



#@bot.message_handler(commands=['send_mes11'])
def id_send(message):
    a = []
    i = 0
    my_file = open("../../Проекты/Backend/MARYtravel_TG_bot/actions.txt", "r")
    while True:
        if my_file.readline(i) == '':
            break
        else:
            a.append(my_file.readline(i))
            i += 1
    my_file.close()
    print(a)


#@bot.message_handler(commands=['send_mes001'])
def id_send(message):
    a = config.all_users
    for i in a:
        bot.copy_message(i, config.adminChat, 696)
        bot.copy_message(i, config.adminChat, 671)
        murkupAT = types.InlineKeyboardMarkup()
        murkupAT.add(types.InlineKeyboardButton('Подписаться на ТГ-канал 📲', url=config.url_Chanel))
        bot.copy_message(i, config.adminChat, 676, reply_markup=murkupAT)



@bot.message_handler(commands=['faq'])
def faq(message):
    murkupF = types.InlineKeyboardMarkup()
    murkupF.add(types.InlineKeyboardButton('Как происходит бронирование?', callback_data='faq_1'))
    murkupF.add(types.InlineKeyboardButton('Помогаете ли вы с покупкой авиабилетов?', callback_data='faq_2'))
    murkupF.add(types.InlineKeyboardButton('Можно ли поехать в одиночку?', callback_data='faq_3'))
    murkupF.add(types.InlineKeyboardButton('Сколько человек в туре?', callback_data='faq_4'))
    murkupF.add(types.InlineKeyboardButton('Можно ли в тур с детьми?', callback_data='faq_5'))
    murkupF.add(types.InlineKeyboardButton('Насколько безопасно на Кавказе девушкам?', callback_data='faq_6'))

    bot.send_message(message.chat.id, "<b>Выберете вопрос который вас интересует?</b> 💬 ⤵️", reply_markup=murkupF, parse_mode='HTML')

    bot.send_message(message.chat.id,'Если не нашли <b>ответ на свой вопрос</b> - напишите @mary_travel_manager', parse_mode='HTML')


if __name__ == '__main__':
    try:
        logger.info("Запуск бота...")
        logger.info(f"Используемый токен: {config.BOT_TOKEN[:10]}...")
        bot.polling(none_stop=True, timeout=30, long_polling_timeout=5)
    except Exception as e:
        logger.error(f"Ошибка при запуске бота: {e}")
        logger.info("Перезапуск бота через 5 секунд...")
        import time
        time.sleep(5)
        bot.polling(none_stop=True, timeout=30, long_polling_timeout=5)