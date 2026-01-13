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


def login_user():
    username = input("Enter username: ")
    password = input("Enter password: ")

    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute(
            "SELECT password_hash FROM users WHERE username = ?",
            (username,)
        )
        row = cur.fetchone()

        if row and check_password_hash(row[0], password):
            print("✅ Login successful!")
        else:
            print("❌ Invalid username or password.")


def forgot_password():
    username = input("Enter your username: ")

    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute(
            "SELECT id FROM users WHERE username = ?",
            (username,)
        )
        row = cur.fetchone()

        if row:
            new_password = input("Enter your new password: ")
            new_password_hashed = generate_password_hash(new_password)
            cur.execute(
                "UPDATE users SET password_hash = ? WHERE id = ?",
                (new_password_hashed, row[0])
            )
            conn.commit()
            print("✅ Password reset successful!")
        else:
            print("❌ Username not found.")
