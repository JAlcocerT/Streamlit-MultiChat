# import openai

# # Retrieve the list of available models
# models = openai.Model.list()

# # Print the ID of each model
# for model in models['data']:
#   print(model['id'])

#https://stackoverflow.com/questions/78122648/openai-api-how-do-i-get-a-list-of-all-available-openai-models

import os
from dotenv import load_dotenv
from openai import OpenAI  # pip install openai>0.28

# Load environment variables from the .env file
load_dotenv()

# from openai import OpenAI
# import os
# client = OpenAI(
#     api_.key = os.getenv('OPENAI_API_KEY')
# )

client = OpenAI()
models = client.models.list()
for model in models:
    print(model.id)