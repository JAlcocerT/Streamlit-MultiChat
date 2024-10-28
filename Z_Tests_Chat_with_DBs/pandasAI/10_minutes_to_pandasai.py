from pandasai import SmartDataframe


import pandas as pd

df = pd.DataFrame({
    "country": [
        "United States",
        "United Kingdom",
        "France",
        "Germany",
        "Italy",
        "Spain",
        "Canada",
        "Australia",
        "Japan",
        "China",
    ],
    "gdp": [
        19294482071552,
        2891615567872,
        2411255037952,
        3435817336832,
        1745433788416,
        1181205135360,
        1607402389504,
        1490967855104,
        4380756541440,
        14631844184064,
    ],
    "happiness_index": [6.94, 7.16, 6.66, 7.07, 6.38, 6.4, 7.23, 7.22, 5.87, 5.12],
})


import os

os.environ['PANDASAI_API_KEY'] = "sk-proj-"

sdf = SmartDataframe(df)


sdf.chat("Return the top 5 countries by GDP")

sdf.chat("What's the sum of the gdp of the 2 unhappiest countries?")

print(sdf.last_code_generated)

# sdf.chat("Plot a chart of the gdp by country")

# sdf.chat("Plot a histogram of the gdp by country, using a different color for each bar")


# from pandasai import SmartDatalake


# employees_df = pd.DataFrame(
#     {
#         "EmployeeID": [1, 2, 3, 4, 5],
#         "Name": ["John", "Emma", "Liam", "Olivia", "William"],
#         "Department": ["HR", "Sales", "IT", "Marketing", "Finance"],
#     }
# )

# salaries_df = pd.DataFrame(
#     {
#         "EmployeeID": [1, 2, 3, 4, 5],
#         "Salary": [5000, 6000, 4500, 7000, 5500],
#     }
# )

# lake = SmartDatalake([employees_df, salaries_df])
# lake.chat("What's the name of the employee that gets paid the most?")

# print(lake.last_code_executed)

# users_df = pd.DataFrame(
#     {
#         "id": [1, 2, 3, 4, 5],
#         "name": ["John", "Emma", "Liam", "Olivia", "William"]
#     }
# )
# users = SmartDataframe(users_df, name="users")

# photos_df = pd.DataFrame(
#     {
#         "id": [31, 32, 33, 34, 35],
#         "user_id": [1, 1, 2, 4, 5]
#     }
# )
# photos = SmartDataframe(photos_df, name="photos")

# lake = SmartDatalake([users, photos])
# lake.chat("How many photos has been uploaded by John?")

# print(lake.last_code_executed)

# from pandasai import SmartDataframe
# from pandasai.llm import OpenAI
# from pandasai.llm import AzureOpenAI
# from pandasai.llm import GoogleVertexAI

# openai_llm = OpenAI(
#     api_token="my-openai-api-key",
# )

# azure_llm = AzureOpenAI(
#     api_token="my-azure-openai-api-key",
#     azure_endpoint="my-azure-openai-api-endpoint",
#     api_version="2023-05-15",
#     deployment_name="my-deployment-name"
# )

# vertexai_llm = GoogleVertexAI(
#   project_id="generative-ai-training",
#   location="us-central1",
#   model="text-bison@001"
# )

# df1 = SmartDataframe(df, config={"llm": openai_llm})
# df2 = SmartDataframe(df, config={"llm": azure_llm})
# df3 = SmartDataframe(df, config={"llm": vertexai_llm})

# print(df1.chat("Which country has the highest GDP?"))
# print(df2.chat("Which one is the unhappiest country?"))
# print(df3.chat("What is the sum of the GDP of the 2 unhappiest countries?"))


# from pandasai import SmartDataframe
# from langchain.llms import OpenAI
# # from langchain.llms import Anthropic
# # from langchain.llms import LlamaCpp

# langchain_llm = OpenAI(openai_api_key="YOUR TOKEN", max_tokens=1000)
# langchain_sdf = SmartDataframe(df, config={"llm": langchain_llm})
# langchain_sdf.chat("Which are the top 5 countries by GPD?")