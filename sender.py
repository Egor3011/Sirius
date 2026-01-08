import openpyxl
import telebot
from telebot import types
import config
import datetime


max_range_sheet = 259


bot = telebot.TeleBot(config.BOT_TOKEN)

book = openpyxl.open("example (1).xlsx", read_only=True)
sheet = book.active

a = []

print(sheet[5][1].value)

for i in range(6, 294):
    nn = sheet[i][1].value
    print(i)
    print(nn)
    if nn in a:
        pass
    else:
        a.append(nn)

print(a)


#bot.send_message(config.adminChat, str(a))
bot.send_message(config.adminChat, "❗️ Рассылка запущенна")

for i in a:
    try:
        bot.copy_message(i, config.adminChat, 2559)
        bot.copy_message(i, config.adminChat, 2563)
        bot.copy_message(i, config.adminChat, 2564)

    except Exception as ex:
        print(ex)
    finally:
        print(i)

bot.send_message(config.adminChat, f"✅ Рассылка завершена\nВсе пользователи участвующие в рассылке:{str(a)}")