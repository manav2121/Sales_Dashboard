import sqlite3
import pandas as pd

# Load cleaned CSV data
df = pd.read_csv("data/Cleaned_Sales_Data.csv")

# Connect to SQLite database
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Create a table if it doesn’t exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    Order_ID TEXT,
    Order_Date TEXT,
    Ship_Date TEXT,
    Ship_Mode TEXT,
    Customer_ID TEXT,
    Customer_Name TEXT,
    Segment TEXT,
    Country TEXT,
    City TEXT,
    State TEXT,
    Region TEXT,
    Category TEXT,
    Sub_Category TEXT,
    Product_ID TEXT,
    Product_Name TEXT,
    Sales REAL,
    Quantity INTEGER,
    Discount REAL,
    Profit REAL
)
""")

# Insert data into the table
df.to_sql("sales", conn, if_exists="replace", index=False)

# Commit and close connection
conn.commit()
conn.close()

print("✅ Data successfully stored in SQLite!")
