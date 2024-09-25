import telebot
from telebot import types
from telebot.types import Message

# zero_tg_web_app_telebot_bot
BOT_TOKEN = "7774799580:AAEO9XoYoNeY6FSQw0a8pqrZGGntM3I02PM"
APP_URL = "https://99657494-48eb-45ba-a660-3121ad7b2c5a-00-36a9202qj6jow.janeway.replit.dev/"

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def start_command(message: Message):
    web_app_info = types.WebAppInfo(APP_URL)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu_button = types.KeyboardButton("Меню", web_app=web_app_info)
    markup.add(menu_button)
    bot.send_message(message.chat.id, "Нажми, чтобы увидеть меню!", reply_markup=markup)


# Срабатывает, если приходят данные из веб-приложения
@bot.message_handler(content_types=["web_app_data"])
def handle_web_app_data(message: Message):
    data = message.web_app_data.data
    bot.send_message(message.chat.id, data)


bot.polling()
