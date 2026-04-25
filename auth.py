from telebot.types import Message
from bot.database import cursor, conn

user_sessions = {}


def register(bot):

    @bot.message_handler(commands=['start'])
    def start(message: Message):
        bot.send_message(message.chat.id, "👋 PIN kiriting")

    @bot.message_handler(func=lambda m: True)
    def login(message: Message):
        pin = message.text

        cursor.execute("SELECT id, name, balance FROM users WHERE pin=?", (pin,))
        user = cursor.fetchone()

        if user:
            user_sessions[message.chat.id] = user
            bot.send_message(message.chat.id, f"Xush kelibsiz {user[1]}")
        else:
            bot.send_message(message.chat.id, "❌ PIN xato")