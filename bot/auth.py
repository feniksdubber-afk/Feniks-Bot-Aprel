from telebot.types import Message
from bot.database import cursor, conn
from bot.state import user_states, user_sessions

def register(bot):
    @bot.message_handler(commands=['start'])
    def start_command(message: Message):
        print(f"📩 DEBUG: {message.chat.id} start bosdi")
        user_states[message.chat.id] = 'waiting_pin'
        bot.send_message(message.chat.id, "👋 Xush kelibsiz! Iltimos, PIN-kodingizni kiriting:")

    @bot.message_handler(func=lambda m: user_states.get(m.chat.id) == 'waiting_pin')
    def check_pin(message: Message):
        pin = message.text
        print(f"🔑 DEBUG: PIN tekshirilmoqda: {pin}")
        
        cursor.execute("SELECT * FROM users WHERE pin=?", (pin,))
        user = cursor.fetchone()

        if user:
            # user['name'] ishlashi uchun database.py da row_factory bo'lishi shart
            user_sessions[message.chat.id] = dict(user)
            user_states[message.chat.id] = 'logged_in'
            bot.send_message(message.chat.id, f"✅ Salom {user['name']}! Tizimga kirdingiz.")
        else:
            bot.send_message(message.chat.id, "❌ PIN noto'g'ri. Qaytadan urinib ko'ring:")
