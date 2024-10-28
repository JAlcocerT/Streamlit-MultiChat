#https://github.com/AssemblyAI/youtube-tutorials/blob/main/pandas-dataframe-agent/Interesting%20examples%20for%20Pandas%20Dataframe%20Agent.ipynb

from langchain.chat_models import ChatOpenAI
from langchain.agents import create_pandas_dataframe_agent

import pandas as pd

openai_api_key="sk-proj-"


amsterdam_airbnb = pd.read_csv('amsterdam_airbnb.csv', index_col=0)


#amsterdam_airbnb['price'] = amsterdam_airbnb['price'].replace('[\$,]', '', regex=True).astype(float)

chat = ChatOpenAI(openai_api_key = openai_api_key, model_name='gpt-4', temperature=0.0)
agent = create_pandas_dataframe_agent(chat, amsterdam_airbnb, verbose=True)

agent.run("Which listing has the best value for money?")