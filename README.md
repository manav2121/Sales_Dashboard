# 📊 Sales Dashboard

This is a **Sales Dashboard** built with **Streamlit**, **SQLite**, **Matplotlib**, and **Seaborn** to visualize sales data effectively.

---

## 🚀 Features
- **Total Revenue Display** 💰
- **Top 5 Best-Selling Products** 🏆
- **Sales Distribution by Region** 🌍
- **Monthly Sales Trend Visualization** 📈
- **Filters for Region Selection** 🔍
- **Interactive & Dynamic Dashboard** ⚡

---

## 🛠️ Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/manav2121/Sales_Dashboard.git
cd Sales_Dashboard
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Dashboard
```bash
streamlit run dashboard.py
```

---

## 📂 Project Structure
```
Sales_Dashboard/
│-- dashboard.py          # Main Streamlit app
│-- db/sales_data.db      # SQLite database (Ensure this file exists)
│-- requirements.txt      # Required Python packages
│-- README.md             # Project documentation
```

---

## 📦 Dependencies
- **Streamlit**
- **SQLite3**
- **Pandas**
- **Matplotlib**
- **Seaborn**

Install all dependencies using:
```bash
pip install -r requirements.txt
```

---

## 🔧 Environment Variables
Ensure you have a **valid database path** in your environment:
```bash
export DATABASE_URL="sqlite:///db/sales_data.db"
```

---

## 📝 Usage
- Open the dashboard in your browser after running the app.
- Explore sales trends, top products, and revenue.
- Use filters to analyze specific regions.

---

## 🔗 Deployment
You can deploy this dashboard on **Railway, Vercel, or Streamlit Cloud**.

**Example for Railway Deployment:**
1. Upload your project to GitHub.
2. Create a new project on [Railway](https://railway.app/).
3. Connect your GitHub repository.
4. Set environment variables (`DATABASE_URL`).
5. Deploy and get your live dashboard!

---

## 📌 Notes
- Ensure that `db/sales_data.db` exists before running the app.
- If you face **ModuleNotFoundError**, install missing packages using `pip install <package>`.

---

## 🎯 Future Improvements
- Add user authentication for secured access.
- Implement **more data visualizations** using **Altair**.
- Export reports as **PDF/CSV**.

---

## 📞 Support
For any issues, feel free to create an **Issue** in the repository or contact me. 🚀

