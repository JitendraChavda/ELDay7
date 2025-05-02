import sqlite3

#Connect to (or create) the database
conn = sqlite3.connect('sales_data.db')

#Create a cursor object
cur = conn.cursor()

#Create sales table
cur.execute('''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    product TEXT,
    quantity INTEGER,
    price REAL
)
''')
conn.commit()
conn.close()