#https://github.com/AssemblyAI/youtube-tutorials/blob/main/pandas-dataframe-agent/Using%20Pandas%20Dataframe%20Agent.ipynb

from langchain.chat_models import ChatOpenAI
from langchain.agents import create_pandas_dataframe_agent

import pandas as pd

openai_api_key="sk-proj-"

iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

chat = ChatOpenAI(openai_api_key = openai_api_key, model_name='gpt-4', temperature=0.0)
agent = create_pandas_dataframe_agent(chat, iris, verbose=True)

agent.run("What is the average sepal_length?")
