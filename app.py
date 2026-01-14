import sqlite3
from flask import Flask, request, render_template, flash, redirect, url_for
from create_db import create_db
from werkzeug.security import generate_password_hash, check_password_hash

create_db()
DB_NAME = "tradecraft.db"
# app.py


app = Flask(__name__)


@app.route("/")
def home():
    return "TradeCraft Running"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("tradecrafts.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT password_hash FROM users WHERE username=?", (username,)
        )
        result = cursor.fetchone()
        conn.close()

        if result and check_password_hash(result[0], password):
            flash("Login successful!", "success")
            return redirect(url_for('news'))
        else:

            flash('Invalid credentials', "error")
            return redirect(url_for('login'))

    return render_template("login.html")


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

            flash('Account created. You can now log in.', "success")
            return redirect(url_for('login'))

        except sqlite3.IntegrityError:
            flash('Username taken .', "error")
            return redirect(url_for('signup'))

    return render_template("signup.html")


if __name__ == "__main__":
    app.run(debug=True)
