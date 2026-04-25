import telebot
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# Handlerlarni ro'yxatdan o'tkazish
from bot import auth
auth.register(bot)

def start_bot():
    try:
        # skip_pending=True - bot o'chiq vaqtida kelgan xabarlarni e'tiborsiz qoldiradi
        # Bu bot yoqilganda "spam" bo'lib ketmasligi uchun kerak
        print("✅ Bot polling boshlandi...")
        bot.infinity_polling(skip_pending=True)
    except Exception as e:
        print(f"❌ Botda xatolik: {e}")

if __name__ == "__main__":
    start_bot()
