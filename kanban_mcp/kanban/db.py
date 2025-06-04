import sqlite3
import os

DB_FILE = os.path.join(os.path.dirname(__file__), "..", "kanban.sqlite3")

def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            status TEXT CHECK(status IN ('todo', 'in_progress', 'done')) NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
