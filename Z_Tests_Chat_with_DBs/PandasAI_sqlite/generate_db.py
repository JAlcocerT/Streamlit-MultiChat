import sqlite3
import pandas as pd

# Create a connection to the SQLite database
# Doesn't matter if the database doesn't yet exist
conn = sqlite3.connect('example.db')

# Create a cursor object
cursor = conn.cursor()

# Execute some SQL commands to create a table and insert some data
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    position TEXT NOT NULL,
    office TEXT NOT NULL
)
""")
cursor.execute("""
INSERT INTO employees (name, position, office) VALUES
('John Doe', 'Manager', 'London'),
('Jane Doe', 'Engineer', 'New York')
""")

# Commit the transactions and close the connection
conn.commit()
conn.close()

# Now we can use pandas to easily query the database
conn = sqlite3.connect('example.db')
df = pd.read_sql_query("SELECT * FROM employees", conn)

print(df)