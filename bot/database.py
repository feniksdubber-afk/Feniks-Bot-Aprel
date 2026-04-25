import sqlite3
import os

# Bazaga ulanish
db_path = os.path.join(os.getcwd(), "feniks.db")
conn = sqlite3.connect(db_path, check_same_thread=False)
conn.row_factory = sqlite3.Row  # Natijalarni dictionary ko'rinishida olish uchun
cursor = conn.cursor()

def init_db():
    # Foydalanuvchilar jadvalini yaratish
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER UNIQUE,
            name TEXT,
            pin TEXT,
            balance REAL DEFAULT 0,
            role TEXT DEFAULT 'user'
        )
    ''')
    
    # SIZNI ADMIN SIFATIDA QO'SHISH
    # PIN-kod: 7777 deb belgilandi
    cursor.execute('''
        INSERT OR IGNORE INTO users (telegram_id, name, pin, balance, role) 
        VALUES (?, ?, ?, ?, ?)
    ''', (6761276533, "Shohruxxon", "7777", 0.0, "admin"))
    
    conn.commit()
    print("✅ Ma'lumotlar bazasi tayyor va Admin tekshirildi.")

# Dastur boshlanishida jadvalni va adminni yaratish
init_db()
