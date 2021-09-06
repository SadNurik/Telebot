import telebot
import configure


bot = telebot.TeleBot(configure.config)

@bot.message_handler(commands=['go'])
def welcome(message):
    bot.send_message(
        message.chat.id, "Дбро пожаловать в калькулятор")

@bot.message_handler(content_types=['text'])
def funnc(message):
    a = message.text
    try:
        bot.send_message(message.chat.id, a + " = " + str(eval(a)))
    except NameError:
        bot.send_message(message.chat.id, "число, один из знаков, число")
    except SyntaxError:
        bot.send_message(message.chat.id, "число, один из знаков, число")
    except ZeroDivisionError:
        bot.send_message(message.chat.id, "На ноль делить нельзя")

bot.polling(non_stop=True)
