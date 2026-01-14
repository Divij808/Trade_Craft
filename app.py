import sqlite3
from flask import Flask, request, render_template
from create_db import create_db
from werkzeug.security import generate_password_hash, check_password_hash

create_db()
DB_NAME = "tradecraft.db"
# app.py


app = Flask(__name__)


@app.route("/")
def home():
    return "TradeCraft Running"


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
    try:
        conn = sqlite3.connect("tradecrafts.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, password_hash,cash) VALUES (?, ?, ?)",
            (username, generate_password_hash(password), 10000.0)
        )
        conn.commit()
        conn.close()

        return "User created"
    except:

        print("Error creating user because there is already a user with that name")

    return render_template("signup.html")


if __name__ == "__main__":
    app.run(debug=True)
