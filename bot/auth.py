from telebot.types import Message
from bot.database import cursor
from bot.state import user_states, user_sessions # Markazlashgan xotira
from bot.utils import delete_later

def register(bot):
    @bot.message_handler(commands=['start'])
    def start(message: Message):
        # Foydalanuvchi holatini 'waiting_pin'ga o'zgartiramiz
        user_states[message.chat.id] = 'waiting_pin'
        bot.send_message(message.chat.id, "👋 PIN kiritishingizni kutmoqdaman...")

    @bot.message_handler(func=lambda m: user_states.get(m.chat.id) == 'waiting_pin')
    def login(message: Message):
        pin = message.text
        cursor.execute("SELECT * FROM users WHERE pin=?", (pin,))
        user = cursor.fetchone()

        if user:
            # Endi user['name'] deb yozishimiz mumkin (row_factory tufayli)
            user_sessions[message.chat.id] = dict(user)
            user_states[message.chat.id] = 'logged_in'
            bot.send_message(message.chat.id, f"✅ Xush kelibsiz {user['name']}")
        else:
            msg = bot.send_message(message.chat.id, "❌ PIN xato")
            # Utils'dan foydalanamiz: xabarni 3 soniyadan keyin o'chirish
            delete_later(bot, message.chat.id, msg.message_id, delay=3)
