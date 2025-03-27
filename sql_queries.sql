-- Total Revenue
SELECT SUM(Sales) AS Total_Revenue FROM sales;

-- Top 5 Best-Selling Products
SELECT "Product Name", SUM(Sales) AS Total_Sales
FROM sales
GROUP BY "Product Name"
ORDER BY Total_Sales DESC
LIMIT 5;

-- Monthly Sales Trend
SELECT strftime('%Y-%m', "Order Date") AS Month, SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Month
ORDER BY Month;
