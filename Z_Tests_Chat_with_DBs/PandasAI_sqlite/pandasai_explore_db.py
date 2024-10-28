# from pandasai import SmartDataframe
# from pandasai.connectors import SqliteConnector

import pandas as pd 
from pandasai import PandasAI 
from pandasai.llm.openai import OpenAI

import ssqlite3

# storing the API Token in Open AI environment 
# replace "YOUR_API_KEY" with your generated API key 
llm = OpenAI(api_token='sk-proj-') 
#initializing an instance of Pandas AI with openAI environment 
pandas_ai = PandasAI(llm, verbose=True, conversational=False)


# connector = SqliteConnector(config={
#     "database" : "example.db",
#     "table" : "actor",
#     "where" :[
#         ["name","!=","PENELOPE"]
#     ]
# })

# df = SmartDataframe(connector)
# df.chat('How many records are there ?')

# Create a connection to the SQLite database
conn = sqlite3.connect('example.db')

# Write the query
query = "SELECT * FROM employees"

# Use pandas to pass sql query using connection form SQLite3
df = pd.read_sql_query(query, conn)


response = pandas_ai(df, "How many records do we have?") 
print(response)
