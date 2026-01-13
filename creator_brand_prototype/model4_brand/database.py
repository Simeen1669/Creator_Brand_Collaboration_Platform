import sqlite3

def create_db():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT,
        password TEXT,
        role TEXT
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS creator_profile(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        niche TEXT,
        platform TEXT,
        followers INTEGER
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS requests(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        creator_id INTEGER,
        campaign TEXT,
        status TEXT
    )""")

    conn.commit()
    conn.close()
