import sqlite3
from flask import Flask
from create_db import create_db
from werkzeug.security import generate_password_hash, check_password_hash

create_db()
DB_NAME = "tradecraft.db"
# app.py


app = Flask(__name__)


@app.route("/")
def home():
    return "TradeCraft Running"


if __name__ == "__main__":
    app.run(debug=True)
