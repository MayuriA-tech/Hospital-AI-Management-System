import sqlite3
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database", "hospital.db")


def get_connection():
    """
    Create and return a database connection.
    """
    return sqlite3.connect(DB_PATH)


def execute_query(query):
    """
    Execute any SELECT query and return results as a DataFrame.
    """

    conn = get_connection()

    try:
        df = pd.read_sql_query(query, conn)
        return df

    except Exception as e:
        print(f"Database Error: {e}")
        return None

    finally:
        conn.close()


def get_patients(limit=20):
    """
    Return first 'limit' patient records.
    """

    query = f"""
    SELECT *
    FROM patients
    LIMIT {limit}
    """

    return execute_query(query)