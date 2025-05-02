import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


#Run and print these queries:
with sqlite3.connect("sales_data.db") as conn:
    query_total = """
    SELECT 
        SUM(quantity) AS total_quantity, 
        SUM(quantity * price) AS total_revenue
    FROM sales;
    """
    total_sales = pd.read_sql_query(query_total, conn)
    

    query_apples = """
    SELECT 
        product, 
        SUM(quantity) AS total_qty, 
        SUM(quantity * price) AS revenue
    FROM sales
    WHERE product = 'Apples'
    GROUP BY product;
    """
    apples_sales = pd.read_sql_query(query_apples, conn)
    

    query_product_summary = """
    SELECT 
        product, 
        SUM(quantity) AS total_qty, 
        SUM(quantity * price) AS revenue
    FROM sales
    GROUP BY product
    """
    df_product_summary = pd.read_sql_query(query_product_summary, conn)
    

#Print All Statements 
print("01) Sales for 'Apples':")
print(apples_sales)
print("\n02) Total Sales (All Products):")
print(total_sales)
print("\n03) Sales Summary per Product:")
print(df_product_summary)



# #Bar_Chart total revenue per product
# ax = df_product_summary.plot(kind='bar', x='product', y='revenue', legend=False)
# ax.set_ylabel('Revenue')
# ax.set_title('Total Revenue per Product')
# plt.savefig("sales_revenue_chart.png")
# plt.show()


#Line chart of revenue per product
ax = df_product_summary.plot(kind='line', x='product', y='revenue', marker='o')
ax.set_ylabel('Revenue')
ax.set_xlabel('Product')
ax.set_title('Revenue per Product (Line Chart)')
plt.tight_layout()
plt.savefig("sales_revenue_line_chart.png")
plt.show()