import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('example.db')

# Create a cursor object
cursor = conn.cursor()

# Execute a query
cursor.execute("SELECT * FROM employees")

# Fetch all the rows
rows = cursor.fetchall()

for row in rows:
    print(row)

# Close the connection
conn.close()