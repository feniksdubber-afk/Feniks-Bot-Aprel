import telebot
import os
import time
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
# Agar token bo'sh bo'lsa, xato berishi uchun
if not TOKEN:
    raise ValueError("❌ XATOLIK: BOT_TOKEN topilmadi! Variables bo'limini tekshiring.")

bot = telebot.TeleBot(TOKEN)

# Webhookni tozalash va handlerlarni ulash
from bot import auth
bot.remove_webhook()
auth.register(bot)

def start_bot():
    while True: # Bot o'chib qolsa qayta yonishi uchun
        try:
            me = bot.get_me()
            print(f"✅ BOT TAYYOR: @{me.username}")
            bot.infinity_polling(skip_pending=True, timeout=60)
        except Exception as e:
            print(f"⚠️ Botda uzilish: {e}. 5 soniyadan so'ng qayta urinish...")
            time.sleep(5)
