import threading
import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from bot.core import start_bot

# Lifespan - bu FastAPI ishga tushganda botni ham qo'shib ishga tushiradi
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🤖 Bot alohida oqimda ishga tushmoqda...")
    bot_thread = threading.Thread(target=start_bot, daemon=True)
    bot_thread.start()
    yield
    print("🛑 Server to'xtatilmoqda...")

app = FastAPI(lifespan=lifespan)

@app.get("/")
def home():
    return {"status": "ok", "message": "Fenix TV server is live"}

if __name__ == "__main__":
    # Faqat uvicorn'ni ishga tushiramiz, bot lifespan orqali o'zi yonadi
    uvicorn.run(app, host="0.0.0.0", port=8080)
