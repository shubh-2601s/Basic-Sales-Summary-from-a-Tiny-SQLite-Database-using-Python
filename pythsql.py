import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import random

# Step 1: Connect to SQLite DB
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Step 2: Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product TEXT,
        quantity INTEGER,
        price REAL
    )
""")

# Step 3: Insert 50+ records
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sample_data = []

for _ in range(50):
    product = random.choice(products)
    quantity = random.randint(1, 10)
    price = random.choice([15.0, 20.0, 25.0, 30.0, 35.0])
    sample_data.append((product, quantity, price))

cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sample_data)
conn.commit()

# Step 4: SQL Query
query = """
    SELECT product,
           SUM(quantity) AS total_qty,
           SUM(quantity * price) AS revenue
    FROM sales
    GROUP BY product
"""
df = pd.read_sql_query(query, conn)
print("📊 Sales Summary:\n", df)

# Step 5A: Revenue Bar Chart
plt.figure(figsize=(8, 5))
ax = df.plot(kind='bar', x='product', y='revenue', color='mediumseagreen', legend=False)
for i, v in enumerate(df['revenue']):
    ax.text(i, v + 30, f"₹{v:.0f}", ha='center', fontweight='bold')
plt.title("Total Revenue by Product", fontsize=14)
plt.xlabel("Product")
plt.ylabel("Revenue (₹)")
plt.tight_layout()
plt.savefig("final_revenue_by_product.png")
plt.show()

# Step 5B: Quantity Bar Chart
plt.figure(figsize=(8, 5))
ax = df.plot(kind='bar', x='product', y='total_qty', color='steelblue', legend=False)
for i, v in enumerate(df['total_qty']):
    ax.text(i, v + 2, str(v), ha='center', fontweight='bold')
plt.title("Total Quantity Sold by Product", fontsize=14)
plt.xlabel("Product")
plt.ylabel("Quantity")
plt.tight_layout()
plt.savefig("final_quantity_by_product.png")
plt.show()

# Step 5C: Combined Revenue vs Quantity Chart
fig, ax1 = plt.subplots(figsize=(10, 6))
ax2 = ax1.twinx()

df.plot(kind='bar', x='product', y='revenue', ax=ax1, color='coral', width=0.4, position=0, legend=False)
df.plot(kind='line', x='product', y='total_qty', ax=ax2, color='navy', marker='o', linewidth=2, legend=False)

ax1.set_ylabel("Revenue (₹)", color='coral')
ax2.set_ylabel("Quantity", color='navy')
ax1.set_xlabel("Product")
plt.title("Revenue vs Quantity by Product", fontsize=14)
plt.tight_layout()
plt.savefig("final_revenue_vs_quantity.png")
plt.show()

# Step 5D: Pie Chart – Quantity Share
plt.figure(figsize=(6, 6))
plt.pie(df['total_qty'], labels=df['product'], autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Share of Quantity Sold by Product', fontsize=13)
plt.tight_layout()
plt.savefig("final_quantity_pie_chart.png")
plt.show()

# Step 6: Close connection
conn.close()
