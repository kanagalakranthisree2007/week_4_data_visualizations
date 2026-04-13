"""
Week 4 Project – Data Visualization & Analysis
Author: Kranthi
Description: Complete pipeline for loading, cleaning, analyzing, and visualizing sales data.
"""

import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

# Step 1: Load Data
def load_data(filepath):
    try:
        df = pd.read_csv(filepath)
        print("Data loaded successfully!")
        print("Available columns:", df.columns.tolist())
        return df
    except FileNotFoundError:
        print("Error: File not found at given path:", filepath)
        sys.exit()

# Step 2: Clean Data
def clean_data(df):
    df = df.dropna()
    return df

# Step 3: Analyze Data
def analyze_data(df):
    # Sales by Product
    sales_by_product = df.groupby("Product")["Total_Sales"].sum()

    # Monthly Sales Trend
    if "Date" in df.columns:
        df["Month"] = pd.to_datetime(df["Date"]).dt.month
        monthly_sales = df.groupby("Month")["Total_Sales"].sum()
    else:
        print("⚠️ No 'Date' column found. Skipping monthly trend.")
        monthly_sales = None

    return sales_by_product, monthly_sales

# Step 4: Visualizations
def create_visualizations(sales_by_product, monthly_sales):
    os.makedirs("visualizations", exist_ok=True)

    # Bar Chart – Sales by Product
    plt.figure(figsize=(8,6))
    sales_by_product.plot(kind="bar", color="skyblue")
    plt.title("Sales by Product")
    plt.xlabel("Product")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("visualizations/bar_chart.png")
    plt.close()

    # Line Chart – Monthly Sales Trend
    if monthly_sales is not None:
        plt.figure(figsize=(8,6))
        monthly_sales.plot(kind="line", marker="o", color="green")
        plt.title("Monthly Sales Trend")
        plt.xlabel("Month")
        plt.ylabel("Total Sales")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig("visualizations/line_chart.png")
        plt.close()

    # Pie Chart – Product Share
    plt.figure(figsize=(6,6))
    sales_by_product.plot(kind="pie", autopct="%1.1f%%", startangle=90)
    plt.title("Sales Distribution by Product")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig("visualizations/pie_chart.png")
    plt.close()

    print(" Visualizations saved in visualizations/ folder.")

# Step 5: Insights
def print_insights(sales_by_product, monthly_sales):
    print("\n--- Insights ---")
    print(f"⭐ Highest sales product: {sales_by_product.idxmax()} ({sales_by_product.max()})")
    print(f"🔻 Lowest sales product: {sales_by_product.idxmin()} ({sales_by_product.min()})")
    if monthly_sales is not None:
        print(" Monthly trend shows peaks and dips – possible seasonal patterns.")

# Main Execution
if __name__ == "__main__":
    filepath = r"C:\Users\kanag\OneDrive\Desktop\intenship\sales_analysis\sales_data.csv"
    df = load_data(filepath)
    df = clean_data(df)
    sales_by_product, monthly_sales = analyze_data(df)
    create_visualizations(sales_by_product, monthly_sales)
    print_insights(sales_by_product, monthly_sales)