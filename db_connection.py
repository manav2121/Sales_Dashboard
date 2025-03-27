import os
import sqlite3
from scripts.db_connection import conn, cursor

# Get the database path from the environment variable or use default
db_path = os.getenv("DATABASE_URL", "sqlite:///Sales_Dashboard_Project/sales_data.db").replace("sqlite:///", "")

try:
    # Connect to SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    print(f"Connected to database: {db_path}")

except sqlite3.Error as e:
    print(f"Error connecting to database: {e}")
    exit(1)  # Exit the script if connection fails

# Example query to check if the connection works
try:
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables in database:", tables)
except sqlite3.Error as e:
    print(f"Error executing query: {e}")

# Close connection when done
finally:
    conn.close()
