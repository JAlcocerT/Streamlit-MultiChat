* https://docs.pandas-ai.com/llms#langchain-models

pip install pandasai[langchain]


from pandasai import SmartDataframe
from langchain_openai import OpenAI

langchain_llm = OpenAI(openai_api_key="my-openai-api-key")
df = SmartDataframe("data.csv", config={"llm": langchain_llm})


PandasAI will automatically detect that you are using a LangChain LLM and will convert it to a PandasAI LLM.

