import telebot
import datetime
from bot_token import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):

    text = (
        "/time - Показать текущее время\n"
        "/date - Показать текущую дату"
    )
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['time'])
def time(message):

    time_now = datetime.datetime.now().strftime("%H:%M:%S")
    bot.send_message(message.chat.id, f"Текущее время: {time_now}")

@bot.message_handler(commands=['date'])
def date(message):

    date_now = datetime.datetime.now().strftime("%d.%m.%Y")
    bot.send_message(message.chat.id, f"Текущая дата: {date_now}")

if __name__ == '__main__':
    print("Лабораторный гном варит зелье...")
    bot.infinity_polling()