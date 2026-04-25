from telebot import types # Tugmalar uchun

# ... (eski kodlar) ...

        if user:
            user_sessions[message.chat.id] = dict(user)
            user_states[message.chat.id] = 'logged_in'
            
            # Asosiy menyu tugmalarini yaratish
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
