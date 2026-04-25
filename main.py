from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import threading

from core import start_bot

if __name__ == "__main__":
    start_bot()

app = FastAPI()

app.mount("/assets", StaticFiles(directory="frontend/dist/assets"), name="assets")

@app.get("/")
def home():
    return FileResponse("frontend/dist/index.html")

# BOT RUN
threading.Thread(target=start_bot, daemon=True).start()
