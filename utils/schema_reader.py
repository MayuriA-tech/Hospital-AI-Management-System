import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database", "hospital.db")


def get_schema():
    """
    Reads the SQLite database schema and returns it as text.
    """

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.execute("PRAGMA table_info(patients);")

    columns = cursor.fetchall()

    conn.close()

    schema = "Table: patients\n\nColumns:\n"

    for column in columns:
        schema += f"- {column[1]}\n"

    return schema