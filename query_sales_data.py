import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Get Total Revenue
cursor.execute("SELECT SUM(Sales) FROM sales")
total_revenue = cursor.fetchone()[0]
print(f"💰 Total Revenue: ${total_revenue:,.2f}")

# Fix column name based on check_columns.py output
cursor.execute("""
SELECT "Product Name", SUM(Sales) AS Total_Sales
FROM sales
GROUP BY "Product Name"
ORDER BY Total_Sales DESC
LIMIT 5;
""")
top_products = cursor.fetchall()

print("\n🏆 Top 5 Best-Selling Products:")
for product, sales in top_products:
    print(f"{product}: ${sales:,.2f}")

conn.close()
