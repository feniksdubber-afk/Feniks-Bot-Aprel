import sqlite3

# check_same_thread=False - bir vaqtning o'zida ham FastAPI, 
# ham Bot bazaga ulanishi uchun shart.
conn = sqlite3.connect("feniks.db", check_same_thread=False)

# row_factory - bazadan ma'lumotni 'user[1]' emas, 
# balki 'user["name"]' ko'rinishida olish imkonini beradi.
conn.row_factory = sqlite3.Row 
cursor = conn.cursor()

def init_db():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER UNIQUE,
        name TEXT,
        balance INTEGER DEFAULT 0,
        card TEXT,
        pin TEXT UNIQUE,
        role TEXT
    )
    """)
    conn.commit()

init_db()
