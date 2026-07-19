import pandas as pd
import sqlite3

# Load CSV file
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

csv_path = os.path.join(BASE_DIR, "data", "healthcare_dataset.csv")
db_path = os.path.join(BASE_DIR, "database", "hospital.db")

df = pd.read_csv(csv_path)


# Connect to SQLite database
conn = sqlite3.connect("database/hospital.db")

# Store data into SQL table
df.to_sql("patients", conn, if_exists="replace", index=False)

print("Database created successfully!")
print(f"Total records inserted: {len(df)}")

conn.close()

