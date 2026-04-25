import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

# HANDLER IMPORTS
from bot.handlers import auth, admin, worker, projects, support

# REGISTER
auth.register(bot)
admin.register(bot)
worker.register(bot)
projects.register(bot)
support.register(bot)

def start_bot():
    print("🚀 Bot ishga tushdi")
    bot.infinity_polling(skip_pending=True)