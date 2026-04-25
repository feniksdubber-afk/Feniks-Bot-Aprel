import threading
import time

def safe_delete(bot, chat_id, message_id):
    try:
        bot.delete_message(chat_id, message_id)
    except:
        pass


def delete_later(bot, chat_id, message_id, delay=3):
    def task():
        time.sleep(delay)
        safe_delete(bot, chat_id, message_id)
    threading.Thread(target=task).start()
