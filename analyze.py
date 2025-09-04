import pandas as pd

# Load JSON dataset
df = pd.read_json("blinkit.json")

# Preview data
print("🔹 First 5 rows:")
print(df.head(), "\n")

# KPIs
total_sales = df["Total Sales"].sum()
avg_sales = df["Total Sales"].mean()
num_orders = len(df)
avg_rating = df["Rating"].mean()

print("📊 Key Metrics")
print(f"Total Sales       : {total_sales:,.2f}")
print(f"Average Sales     : {avg_sales:,.2f}")
print(f"Number of Orders  : {num_orders}")
print(f"Average Rating    : {avg_rating:.2f}")
