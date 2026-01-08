import psutil
import threading
import telebot
import config
import datetime
import os

print(os.getcwd())

isStart = True

bot = telebot.TeleBot(config.BOT_TOKEN)

file = open(f'{os.getcwd()}\cfg.txt', 'r')
cfgName = file.readline()
file.close()


def check_file(nameExe):
    global isStart
    for proc in psutil.process_iter():
        name = proc.name()
        if name == nameExe:
            isStart = True
            print(name)
            return True


def f():
    global isStart
    threading.Timer(60.0, f).start()  # Перезапуск через 2 минуты


    if check_file(cfgName) != True and isStart == True:
        print('-' * 20)
        print('Файл выключен', '!' * 5)
        print('-' * 20)

        isStart = False
        os.startfile(fr"D:\MaryTravelBot\main\dist\{cfgName}")
        if check_file(cfgName) == True:
            bot.send_message(config.adminChat, 'Файл перезапущен (произошел рестарт файла)')
        else:
            bot.send_message(config.adminChat, 'Файл выключен')
    print(f"[{datetime.datetime.now()}] Проверка ")

f()