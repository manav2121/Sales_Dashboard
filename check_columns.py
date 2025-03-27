import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Get table schema
cursor.execute("PRAGMA table_info(sales)")
columns = cursor.fetchall()

# Print column names
print("📌 Columns in 'sales' table:")
for col in columns:
    print(col[1])

conn.close()
