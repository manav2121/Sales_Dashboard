import pandas as pd

# Load dataset
df = pd.read_csv("data/Superstore.csv")

# Drop unnecessary columns
df.drop(['Row ID', 'Postal Code'], axis=1, inplace=True)

# Convert date columns (Handling DD/MM/YYYY format)
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True, errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True, errors='coerce')

# Handle missing values
df.dropna(inplace=True)

# Save cleaned data
df.to_csv("data/Cleaned_Sales_Data.csv", index=False)

print("✅ Data cleaned and saved successfully!")
