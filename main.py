import threading
import uvicorn
from fastapi import FastAPI
from bot.core import start_bot # Botni ishga tushirish funksiyasi

app = FastAPI()

@app.get("/")
def home():
    return {"status": "ok", "message": "Fenix TV API is running"}

if __name__ == "__main__":
    # DIQQAT: Botni alohida oqimda (Thread) boshlash
    # Bu FastAPI va Bot bir vaqtda ishlashini ta'minlaydi
    print("🤖 Bot ishga tushirilmoqda...")
    bot_thread = threading.Thread(target=start_bot, daemon=True)
    bot_thread.start()
    
    # FastAPI serverni ishga tushirish
    print("🌐 FastAPI server ishga tushmoqda...")
    uvicorn.run(app, host="0.0.0.0", port=8080)
