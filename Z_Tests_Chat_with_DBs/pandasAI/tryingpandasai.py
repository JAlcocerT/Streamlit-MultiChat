import pandas as pd
from pandasai import SmartDataframe
from langchain_groq.chat_models import ChatGroq
from langchain_community.llms import Ollama 
import sqlite3
import os

llm = ChatGroq(model_name="llama3-70b-8192", api_key = os.environ["GROQ_API_KEY"])

df = pd.read_csv('happiness.csv') #pd.read_excel('data.xlsx')
df = SmartDataframe(df, config={"llm": llm})

print( df.chat('Which are the 5 happiest countries?'))
print( df.chat('What is the sum of the GDPs of the 2 happiest countries?'))