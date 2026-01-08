import telebot
import config

bot = telebot.TeleBot(config.BOT_TOKEN)

a = [7990032679,286381491,1138606967]

for i in a:
    try:
        bot.copy_message(i, config.adminChat, 1488)
    except Exception as ex:
        print(ex)
    finally:
        print(i)