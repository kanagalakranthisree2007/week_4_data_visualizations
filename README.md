# week_4_data_visualization
# Sales Analysis Project

## 📌 Project Overview
This project demonstrates a complete data analysis workflow using Python.  
It covers loading data, cleaning, analyzing, visualizing, and writing insights.  
Charts are created with **Matplotlib**, and data is handled with **Pandas**.

---

## 🧩 Code Explanation (Step by Step)

### 1. Imports
```python
import pandas as pd
import matplotlib.pyplot as plt

# explanation
- pandas → for data loading, cleaning, and analysis.
- matplotlib → for creating charts.

### 2. Load Data
def load_data(filepath):
    df = pd.read_csv(filepath)
    print("✅ Data loaded successfully!")
    print("Available columns:", df.columns.tolist())
    return df

- Reads the CSV file from the given path.
- Prints available columns to avoid errors.

### 3.clean data
   def clean_data(df):
    return df.dropna()

- Removes missing values.
- Ensures dataset is clean before analysis.

### 4.Analyze data
     def analyze_data(df):
    sales_by_product = df.groupby("Product")["Amount"].sum()
    df["Month"] = pd.to_datetime(df["Date"]).dt.month
    monthly_sales = df.groupby("Month")["Amount"].sum()
    return sales_by_product, monthly_sales

- Groups data by Product → calculates total sales.
- Converts Date column to month → finds monthly trend.
- Returns two results:
            sales_by_product
            monthly_sales

### 5.Visualizations
def create_visualizations(sales_by_product, monthly_sales):
    sales_by_product.plot(kind="bar", color="skyblue")
    plt.savefig("visualizations/bar_chart.png")

    monthly_sales.plot(kind="line", marker="o", color="green")
    plt.savefig("visualizations/line_chart.png")

    sales_by_product.plot(kind="pie", autopct="%1.1f%%")
    plt.savefig("visualizations/pie_chart.png")

- Bar chart → Sales by product.
- Line chart → Monthly sales trend.
- Pie chart → Product share.



