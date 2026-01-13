import sqlite3

def create_db(db_name="tradecraft.db"):
    with sqlite3.connect(db_name) as conn:
        _create_tables(conn)

def create_db_connection(conn):
    _create_tables(conn)