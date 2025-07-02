import telebot
from bot_token import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, f"Я получил сообщение '{message.text}'")


if __name__ == '__main__':
    print("Лабораторный гном варит зелье...")
    bot.infinity_polling()