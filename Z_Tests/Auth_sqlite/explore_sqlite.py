# ### python explore_sqlite.py

import sqlite3

# Connect to the database
conn = sqlite3.connect('./data.db')
c = conn.cursor()

# Get the list of tables in the database
c.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = c.fetchall()

# Print the table names
print("Tables in the database:")
for table in tables:
    print(table[0])

# Iterate over each table and retrieve its structure and data
for table in tables:
    table_name = table[0]
    print(f"\nTable: {table_name}")
    
    # Get the table structure (column names and types)
    c.execute(f"PRAGMA table_info({table_name})")
    columns = c.fetchall()
    print("Columns:")
    for column in columns:
        print(f"- {column[1]} ({column[2]})")
    
    # Get the data from the table
    c.execute(f"SELECT * FROM {table_name}")
    rows = c.fetchall()
    print("Data:")
    for row in rows:
        print(row)

# Close the database connection
conn.close()

# # import sqlite3

# # conn = sqlite3.connect('../../data.db')
# # c = conn.cursor()

# # c.execute("SELECT * FROM userstable")
# # rows = c.fetchall()
# # for row in rows:
# #     print(row)

# import sqlite3

# conn = sqlite3.connect('data.db')
# c = conn.cursor()

# # Create the 'userstable' if it doesn't exist
# # c.execute('''CREATE TABLE IF NOT EXISTS userstable
# #              (username TEXT, password TEXT)''')

# # Execute your SELECT query
# c.execute("SELECT * FROM userstable")
# rows = c.fetchall()
# for row in rows:
#     print(row)

# conn.close()