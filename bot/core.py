import telebot
import os
from dotenv import load_dotenv

load_dotenv() # .env faylini o'qiydi

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

from bot import auth
auth.register(bot)

def start_bot():
    print("🚀 Bot ishga tushdi")
    bot.infinity_polling(skip_pending=True)
