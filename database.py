import sqlite3

conn = sqlite3.connect("feniks.db", check_same_thread=False)
cursor = conn.cursor()

def init_db():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
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