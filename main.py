from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import threading
import uvicorn
from bot.core import start_bot

app = FastAPI()

# Frontend ulash (Xatolik bermasligi uchun tekshiruv bilan)
import os
if os.path.exists("frontend/dist"):
    app.mount("/assets", StaticFiles(directory="frontend/dist/assets"), name="assets")

@app.get("/")
def home():
    if os.path.exists("frontend/dist/index.html"):
        return FileResponse("frontend/dist/index.html")
    return {"message": "Bot ishlamoqda, lekin frontend topilmadi."}

if __name__ == "__main__":
    # Botni parallel oqimda (Thread) boshlaymiz
    threading.Thread(target=start_bot, daemon=True).start()
    
    # FastAPI serverni ishga tushiramiz
    uvicorn.run(app, host="0.0.0.0", port=8000)
