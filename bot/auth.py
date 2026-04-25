from telebot import types
from bot.database import cursor, conn
from bot.state import user_states, user_sessions

def register(bot):
    @bot.message_handler(commands=['start'])
    def start_command(message):
        print(f"📩 DEBUG: {message.chat.id} start bosdi")
        user_states[message.chat.id] = 'waiting_pin'
        bot.send_message(message.chat.id, "👋 Salom! PIN-kodni kiriting (Masalan: 7777):")

    @bot.message_handler(func=lambda m: user_states.get(m.chat.id) == 'waiting_pin')
    def check_pin(message):
        pin = message.text.strip()
        print(f"🔑 DEBUG: Kiritilgan PIN: {pin}")
        
        cursor.execute("SELECT * FROM users WHERE pin=?", (pin,))
        user = cursor.fetchone()

        if user:
            user_sessions[message.chat.id] = dict(user)
            user_states[message.chat.id] = 'logged_in'
            
            # Asosiy menyu tugmalari
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("🎬 Kinolar")
            btn2 = types.KeyboardButton("💰 Balans")
            btn3 = types.KeyboardButton("👤 Profil")
            markup.add(btn1, btn2, btn3)
            
            bot.send_message(
                message.chat.id, 
                f"✅ Salom {user['name']}! Fenix TV tizimiga xush kelibsiz.",
                reply_markup=markup
            )
        else:
            print(f"❌ DEBUG: PIN {pin} bazadan topilmadi.")
            bot.send_message(message.chat.id, "❌ PIN noto'g'ri. Qaytadan urinib ko'ring:")
