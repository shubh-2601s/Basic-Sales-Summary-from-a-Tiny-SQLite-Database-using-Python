
## 📊 Sales Data Visualization with SQLite and Python

This project uses **SQLite**, **SQL queries**, **Pandas**, and **Matplotlib** to analyze and visualize sales data. It automatically generates a small database, runs analysis, and plots bar and pie charts to summarize the results.

---

### 🧾 Features

* 🗃️ Creates a sales database with 50+ rows of product data
* 🔍 Executes SQL queries to aggregate quantity and revenue
* 📊 Uses Pandas to manipulate and analyze data
* 📈 Visualizes insights with Matplotlib (saved as PNG)

---

### 🗃️ Tech Stack

| Tool       | Purpose                  |
| ---------- | ------------------------ |
| Python     | Core programming         |
| SQLite3    | Lightweight SQL database |
| Pandas     | Data analysis            |
| Matplotlib | Visualizations           |

---

### 🧑‍💻 How to Run

1. **Install Dependencies**

   ```bash
   pip install pandas matplotlib
   ```

2. **Run the Script**

   ```bash
   python sales_visualization.py
   ```

---

## ✅ Step-by-Step Code Explanation

### 📌 1. **Connect to SQLite and Create Table**

```python
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product TEXT,
        quantity INTEGER,
        price REAL
    )
""")
```

* Connects to `sales_data.db` (creates if not exists)
* Defines a table `sales` with columns: `product`, `quantity`, `price`

---

### 📌 2. **Generate and Insert Random Sample Data**

```python
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sample_data = []

for _ in range(50):
    product = random.choice(products)
    quantity = random.randint(1, 10)
    price = random.choice([15.0, 20.0, 25.0, 30.0, 35.0])
    sample_data.append((product, quantity, price))

cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sample_data)
conn.commit()
```

* Generates 50 records with random `product`, `quantity`, and `price`
* Inserts them into the database

---

### 📌 3. **Run SQL to Get Aggregated Results**

```python
query = """
    SELECT product,
           SUM(quantity) AS total_qty,
           SUM(quantity * price) AS revenue
    FROM sales
    GROUP BY product
"""
df = pd.read_sql_query(query, conn)
```

* Executes an SQL query to compute:

  * Total quantity (`SUM(quantity)`)
  * Total revenue (`SUM(quantity * price)`)
* Groups by product
* Loads result into a Pandas DataFrame

---

### 📌 4. **Plot Revenue Bar Chart with Labels**

```python
ax = df.plot(kind='bar', x='product', y='revenue', color='mediumseagreen', legend=False)
for i, v in enumerate(df['revenue']):
    ax.text(i, v + 30, f"₹{v:.0f}", ha='center', fontweight='bold')
plt.savefig("final_revenue_by_product.png")
```

* Plots a bar chart of revenue per product
* Adds ₹ labels above each bar
* Saves chart as `final_revenue_by_product.png`

---

### 📌 5. **Plot Quantity Bar Chart**

```python
ax = df.plot(kind='bar', x='product', y='total_qty', color='steelblue', legend=False)
for i, v in enumerate(df['total_qty']):
    ax.text(i, v + 2, str(v), ha='center', fontweight='bold')
plt.savefig("final_quantity_by_product.png")
```

* Similar to above, but for quantity sold

---

### 📌 6. **Combined Bar + Line Chart**

```python
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
df.plot(kind='bar', x='product', y='revenue', ax=ax1, color='coral')
df.plot(kind='line', x='product', y='total_qty', ax=ax2, color='navy', marker='o')
plt.savefig("final_revenue_vs_quantity.png")
```

* Plots revenue as bars
* Plots quantity as a line on a second Y-axis
* Useful for comparing value vs volume

---

### 📌 7. **Plot Pie Chart of Quantity Share**

```python
plt.pie(df['total_qty'], labels=df['product'], autopct='%1.1f%%', startangle=140)
plt.savefig("final_quantity_pie_chart.png")
```

* Visualizes the share of quantity sold by each product as a pie chart

---

### 📌 8. **Close DB Connection**

```python
conn.close()
```

* Always good practice to close database connections

---

## 📊 Example Sales Summary

| Product   | Total Quantity | Total Revenue |
| --------- | -------------- | ------------- |
| Product A | 109            | ₹2735.0       |
| Product B | 116            | ₹3020.0       |
| Product C | 126            | ₹3280.0       |
| Product D | 84             | ₹1745.0       |
| Product E | 146            | ₹3325.0       |

---

## 🖼️ Sample Charts

| Chart                          | Preview                            |
| ------------------------------ | ---------------------------------- |
| Revenue by Product             |![final_revenue_by_product](https://github.com/user-attachments/assets/4e306d0f-4d3f-44b7-81b7-b30fb1c08f7d) |
| Quantity by Product            | ![final_quantity_by_product](https://github.com/user-attachments/assets/44f26173-4ad4-488d-8333-9afe64412619) |
| Revenue vs Quantity (Combined) | ![final_revenue_vs_quantity](https://github.com/user-attachments/assets/9e617686-bec5-4de8-a314-e79d932c30b6) |
| Quantity Share (Pie Chart)     | ![final_quantity_pie_chart](https://github.com/user-attachments/assets/0006f57a-cfe5-4d3f-852e-62b6f69fe12b)  |


---

## 👨‍💻 Author

**Shubham S**
📧 Email: [10221shubham.s@gmail.com](mailto:10221shubham.s@gmail.com)

🔗 [LinkedIn](https://www.linkedin.com/in/shubham-s-14ba6a283/)

🐙 [GitHub](https://github.com/shubh-2601s)

---
