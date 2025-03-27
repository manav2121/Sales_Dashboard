import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

# Connect to SQLite database
conn = sqlite3.connect("sales_data.db")

# Load data
df = pd.read_sql("SELECT * FROM sales", conn)

# Close connection
conn.close()

# ---- Streamlit UI ----
st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("📊 Sales Dashboard")

# ---- Total Revenue ----
total_revenue = df["Sales"].sum()
st.metric(label="💰 Total Revenue", value=f"${total_revenue:,.2f}")

# ---- Top 5 Best-Selling Products ----
top_products = df.groupby("Product Name")["Sales"].sum().reset_index()
top_products = top_products.sort_values(by="Sales", ascending=False).head(5)

fig_top_products = px.bar(
    top_products, x="Sales", y="Product Name", 
    orientation="h", title="🏆 Top 5 Best-Selling Products",
    color="Sales", height=400
)
st.plotly_chart(fig_top_products, use_container_width=True)

# ---- Sales by Region ----
region_sales = df.groupby("Region")["Sales"].sum().reset_index()
fig_region = px.pie(
    region_sales, values="Sales", names="Region", 
    title="🌍 Sales Distribution by Region"
)
st.plotly_chart(fig_region, use_container_width=True)

# ---- Sales Trend Over Time ----
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df = df.dropna(subset=["Order Date"])  # Drop rows with invalid dates
df["Year-Month"] = df["Order Date"].dt.to_period("M").astype(str)

sales_trend = df.groupby("Year-Month")["Sales"].sum().reset_index()
fig_trend = px.line(
    sales_trend, x="Year-Month", y="Sales", 
    title="📈 Monthly Sales Trend"
)
st.plotly_chart(fig_trend, use_container_width=True)

# ---- Filters (Optional) ----
st.sidebar.header("🔍 Filters")
selected_region = st.sidebar.multiselect("Select Region:", df["Region"].unique())

if selected_region:
    df = df[df["Region"].isin(selected_region)]

st.dataframe(df.head(50))  # Display filtered data

