import threading
import uvicorn
from fastapi import FastAPI
from bot.core import start_bot  # core.py ichidagi funksiya

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "running"}

if __name__ == "__main__":
    # 1. Botni alohida oqimda ishga tushiramiz
    # daemon=True - FastAPI to'xtaganda bot ham avtomatik to'xtashi uchun
    bot_thread = threading.Thread(target=start_bot, daemon=True)
    bot_thread.start()
    print("🤖 Bot oqimi ishga tushirildi...")

    # 2. FastAPI ni asosiy oqimda ishga tushiramiz
    # Port 8080 - konteyneringiz shu portda ishlayotganini loglarda ko'rdik
    uvicorn.run(app, host="0.0.0.0", port=8080)
