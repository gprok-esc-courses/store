import sqlite3
import os

def create():
    if not os.path.isfile('store.db'):
        conn = sqlite3.connect('store.db')
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS products
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT,
                           price NUMERIC)
                       """)
        conn.commit()
        conn.close()


def get_connection():
    conn = sqlite3.connect('store.db')
    return conn