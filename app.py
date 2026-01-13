import sqlite3

from create_db import create_db
from werkzeug.security import generate_password_hash, check_password_hash
create_db()
DB_NAME = "tradecraft.db"
def signup_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    password_hashed = generate_password_hash(password)

    try:
        with sqlite3.connect(DB_NAME) as conn:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO users (username, password_hash, cash) VALUES (?, ?, ?)",
                (username, generate_password_hash(password), 10000.0)
            )
            conn.commit()
            print("✅ User created successfully!")
    except sqlite3.IntegrityError:
        print("❌ Username already exists.")


