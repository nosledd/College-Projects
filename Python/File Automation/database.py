import sqlite3
from datetime import datetime


def connect_db():
    conn = sqlite3.connect("E:/Git/College-Projects/Python/File Automation/database.db")
    cursor = conn.cursor()
    return conn, cursor



def create_table():
    conn, cursor = connect_db()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_name TEXT,
            subject TEXT,
            path TEXT,
            upload_date TEXT
        )
    """)

    conn.commit()
    conn.close()



def insert_record(file_name, subject, path):
    conn, cursor = connect_db()

    upload_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(upload_date)

    cursor.execute("""
        INSERT INTO notes (file_name, subject, path, upload_date)
        VALUES (?, ?, ?, ?)
    """, (file_name, subject, path, upload_date))

    conn.commit()
    conn.close()
