from telebot.types import Message
from bot.database import cursor, conn
from bot.state import user_states, user_sessions

def register(bot):
    @bot.message_handler(commands=['start'])
    def start_command(message: Message):
        print(f"📩 DEBUG: {message.chat.id} start bosdi")
        user_states[message.chat.id] = 'waiting_pin'
        bot.send_message(message.chat.id, "👋 Salom! PIN-kodni kiriting (Masalan: 7777):")

    @bot.message_handler(func=lambda m: user_states.get(m.chat.id) == 'waiting_pin')
    def check_pin(message: Message):
        pin = message.text.strip() # Bo'sh joylarni olib tashlaymiz
        print(f"🔑 DEBUG: Kiritilgan PIN: {pin}")
        
        # Bazadan qidirish
        cursor.execute("SELECT * FROM users WHERE pin=?", (pin,))
        user = cursor.fetchone()

        if user:
            # Bazada ma'lumot topildi
            user_sessions[message.chat.id] = dict(user)
            user_states[message.chat.id] = 'logged_in'
            bot.send_message(message.chat.id, f"✅ Salom {user['name']}! Fenix TV tizimiga xush kelibsiz.")
        else:
            # PIN noto'g'ri bo'lsa
            print(f"❌ DEBUG: PIN {pin} bazadan topilmadi.")
            bot.send_message(message.chat.id, "❌ PIN noto'g'ri. Iltimos, qaytadan urinib ko'ring yoki admin bilan bog'laning.")
