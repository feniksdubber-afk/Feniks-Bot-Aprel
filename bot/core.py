import telebot
import os
from dotenv import load_dotenv

load_dotenv()

# Variables bo'limidan BOT_TOKEN ni oladi
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

# Webhookni tozalash (muammolarni oldini olish uchun)
bot.remove_webhook()

# Handlerlarni ulash (auth.py ni ro'yxatdan o'tkazish)
from bot import auth
auth.register(bot)

def start_bot():
    try:
        me = bot.get_me()
        print(f"✅ Telegram bilan aloqa o'rnatildi! Bot: @{me.username}")
        print("🚀 Bot polling (xabarlarni kutish) boshlandi...")
        bot.infinity_polling(skip_pending=True)
    except Exception as e:
        print(f"❌ Bot ishga tushishida xatolik: {e}")
