import sqlite3
import pandas as pan

class pann:
    connect=sqlite3.connect("E:/Git/College-Projects/Python/File Automation/database.db")
    df = pan.read_sql("SELECT * FROM notes", connect)
    print(df)
    connect.close()

    python_notes = df[df["subject"] == "python"]
    print(":",python_notes)
