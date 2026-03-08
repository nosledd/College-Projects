import sqlite3
from datetime import datetime


def connect_db():
    conn = sqlite3.connect("E:/Git/College-Projects/Python/File Automation/database.db")
    cursor = conn.cursor()
    return conn, cursor


def create_table():
    conn, cursor = connect_db()

    cursor.execute("""
        create table if not exists notes (
            id int primary key autoincrement,
            file_name varchar(20),
            subject varchar(20),
            path varchar(100),
            upload_date varchar(20)
        )
    """)

    conn.commit()
    conn.close()


def insert_record(file_name, subject, path):
    conn, cursor = connect_db()

    upload_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")        #pending
    print(upload_date)

    cursor.execute("insert into notes (file_name, subject, path, upload_date) values (?, ?, ?, ?) ", (file_name, subject, path, upload_date))

    conn.commit()
    conn.close()
