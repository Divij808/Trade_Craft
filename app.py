from create_db import create_db
from werkzeug.security import generate_password_hash, check_password_hash
create_db()
def signup_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    password_hash = generate_password_hash(password)
