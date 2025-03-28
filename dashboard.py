import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ✅ Set up Streamlit page config
st.set_page_config(page_title="Sales Dashboard", layout="wide")

# Ensure the database file exists
DB_PATH = os.getenv("DATABASE_URL", "/opt/render/project/src/db/sales_data.db")



# Function to get database connection
@st.cache_data
def get_data():
    try:
        conn = sqlite3.connect(DB_PATH)
        df = pd.read_sql("SELECT * FROM sales", conn)
        conn.close()
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()  # Return empty dataframe if there's an issue

# Load data
df = get_data()

st.title("📊 Sales Dashboard")

# If no data is found, show a message
if df.empty:
    st.warning("No sales data available.")
else:
    # ---- Total Revenue ----
    total_revenue = df["Sales"].sum()
    st.metric(label="💰 Total Revenue", value=f"${total_revenue:,.2f}")

    # ---- Top 5 Best-Selling Products ----
    top_products = df.groupby("Product Name")["Sales"].sum().reset_index()
    top_products = top_products.sort_values(by="Sales", ascending=False).head(5)

    fig, ax = plt.subplots()
    sns.barplot(x="Sales", y="Product Name", data=top_products, palette="Blues_r", ax=ax)
    ax.set_title("🏆 Top 5 Best-Selling Products")
    st.pyplot(fig)

    # ---- Sales by Region ----
    region_sales = df.groupby("Region")["Sales"].sum().reset_index()

    fig, ax = plt.subplots()
    ax.pie(region_sales["Sales"], labels=region_sales["Region"], autopct="%1.1f%%", colors=["red", "blue", "green"])
    ax.set_title("🌍 Sales Distribution by Region")
    st.pyplot(fig)

    # ---- Sales Trend Over Time ----
    df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
    df = df.dropna(subset=["Order Date"])  # Drop rows with invalid dates
    df["Year-Month"] = df["Order Date"].dt.to_period("M").astype(str)

    sales_trend = df.groupby("Year-Month")["Sales"].sum().reset_index()

    fig, ax = plt.subplots()
    sns.lineplot(x="Year-Month", y="Sales", data=sales_trend, marker="o", color="purple", ax=ax)
    ax.set_title("📈 Monthly Sales Trend")
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # ---- Filters ----
    st.sidebar.header("🔍 Filters")
    selected_region = st.sidebar.multiselect("Select Region:", df["Region"].unique())

    if selected_region:
        df = df[df["Region"].isin(selected_region)]

    st.dataframe(df.head(50))  # Display filtered data
