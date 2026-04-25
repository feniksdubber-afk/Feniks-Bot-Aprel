import telebot
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# Modullarni import qilish (Circular import bo'lmasligi uchun pastda)
from bot import auth
auth.register(bot)

def start_bot():
    try:
        print("✅ Bot pollingni boshlamoqda...")
        # skip_pending=True - bot o'chib qolgan vaqtda yozilgan eski xabarlarga javob bermasligi uchun
        bot.infinity_polling(skip_pending=True)
    except Exception as e:
        print(f"❌ Bot pollingda xatolik: {e}")

if __name__ == "__main__":
    start_bot()
