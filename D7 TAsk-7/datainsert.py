import sqlite3

conn = sqlite3.connect('sales_data.db')
cur = conn.cursor()

#Sample data
sales_data = [
    ('Product A', 10, 2.5),
    ('Product B', 5, 5.0),
    ('Product A', 7, 2.5),
    ('Product C', 3, 10.0),
    ('Product B', 8, 5.0),
]

#Insert data
cur.executemany('INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)', sales_data)
conn.commit()
conn.close()