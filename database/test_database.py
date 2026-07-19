import sqlite3
import pandas as pd

conn = sqlite3.connect("database/hospital.db")

# Display all column names
cursor = conn.execute("PRAGMA table_info(patients);")

print("Columns in the table:\n")

for column in cursor.fetchall():
    print(column[1])

conn.close()