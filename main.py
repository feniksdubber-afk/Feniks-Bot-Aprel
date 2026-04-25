import threading
import uvicorn
import os
from fastapi import FastAPI
from bot.core import start_bot

app = FastAPI()

@app.get("/")
def home():
    return {"status": "ok", "message": "Fenix TV server ishlamoqda"}

if __name__ == "__main__":
    # 1. Botni alohida oqimda (Thread) boshlaymiz
    print("🤖 Bot tayyorlanmoqda...")
    bot_thread = threading.Thread(target=start_bot, daemon=True)
    bot_thread.start()
    
    # 2. FastAPI ni asosiy oqimda ishga tushiramiz
    # Port 8080 - loglarda ko'ringan port
    print("🌐 FastAPI port 8080 da ishga tushmoqda...")
    uvicorn.run(app, host="0.0.0.0", port=8080)
