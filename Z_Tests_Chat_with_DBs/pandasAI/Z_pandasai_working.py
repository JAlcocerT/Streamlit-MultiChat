#https://docs.pandas-ai.com/llms#openai-models

from pandasai import SmartDataframe
from pandasai.llm import OpenAI
from pandasai.helpers.openai_info import get_openai_callback
import pandas as pd

llm = OpenAI(api_token="sk-proj-")
#pandas_ai = SmartDataframe("data.csv", config={"llm": llm})

# conversational=False is supposed to display lower usage and cost
df = SmartDataframe("happiness.csv", config={"llm": llm, "conversational": False})

with get_openai_callback() as cb:
    response = df.chat("What it is the happiest country?")

    print(response)
    print(cb)

#https://github.com/thepycoach/pandasai-tutorial/tree/main

# import pandas as pd
# from pandasai import PandasAI
# from pandasai.llm.openai import OpenAI

# df = pd.read_csv("supermarket_sales.csv")
# df = df[['Gender', 'Product line', 'Total']]

# OPENAI_API_KEY = "sk-proj-"
# llm = OpenAI(api_token=OPENAI_API_KEY)

# pandas_ai = PandasAI(llm)

# pandas_ai.run(df, prompt="Which products are in Product Line")

########

# import os
# import pandas as pd
# from pandasai import Agent

# # Sample DataFrame
# sales_by_country = pd.DataFrame({
#     "country": ["United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia", "Japan", "China"],
#     "revenue": [5000, 3200, 2900, 4100, 2300, 2100, 2500, 2600, 4500, 7000]
# })

# # By default, unless you choose a different LLM, it will use BambooLLM.
# # You can get your free API key signing up at https://pandabi.ai (you can also configure it in your .env file)
# os.environ["PANDASAI_API_KEY"] = "sk-proj-"

# agent = Agent(sales_by_country)
# agent.chat('Which are the top 5 countries by sales?')

######

