#https://www.youtube.com/watch?v=aqdWSYWC_LI
#https://raw.githubusercontent.com/daveebbelaar/langchain-experiments/main/openai-functions/openai_function_calling.py

# --------------------------------------------------------------
# Import Modules
# --------------------------------------------------------------

import os
import json
#import openai

import os
from dotenv import load_dotenv
from openai import OpenAI  # pip install openai==1.30.5

# Load environment variables from the .env file
load_dotenv()

from datetime import datetime, timedelta
from dotenv import load_dotenv
# from langchain.chat_models import ChatOpenAI
# from langchain.schema import HumanMessage, AIMessage, ChatMessage


# --------------------------------------------------------------
# Load OpenAI API Token From the .env File
# --------------------------------------------------------------


# Get the OpenAI API key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client
client = OpenAI(
    api_key=api_key,
)


# --------------------------------------------------------------
# Use OpenAI’s Function Calling Feature
# --------------------------------------------------------------

function_descriptions = [
    {
        "name": "get_flight_info",
        "description": "Get flight information between two locations",
        "parameters": {
            "type": "object",
            "properties": {
                "loc_origin": {
                    "type": "string",
                    "description": "The departure airport, e.g. DUS",
                },
                "loc_destination": {
                    "type": "string",
                    "description": "The destination airport, e.g. HAM",
                },
            },
            "required": ["loc_origin", "loc_destination"],
        },
    }
]

user_prompt = "When's the next flight from Amsterdam to New York?"

completion = client.chat.completions.create( #openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",
    messages=[{"role": "user", "content": user_prompt}],
    # Add function calling
    functions=function_descriptions,
    function_call="auto",  # specify the function call
)

# It automatically fills the arguments with correct info based on the prompt
# Note: the function does not exist yet

output = completion.choices[0].message
print(output)

print('the function does not exists, but we passed the description already')

# --------------------------------------------------------------
# Add a Function
# --------------------------------------------------------------


def get_flight_info(loc_origin, loc_destination):
    """Get flight information between two locations."""

    # Example output returned from an API or database
    flight_info = {
        "loc_origin": loc_origin,
        "loc_destination": loc_destination,
        "datetime": str(datetime.now() + timedelta(hours=2)),
        "airline": "KLM",
        "flight": "KL643",
    }

    return json.dumps(flight_info)


# Use the LLM output to manually call the function
# The json.loads function converts the string to a Python object

origin = json.loads(output.function_call.arguments).get("loc_origin")
destination = json.loads(output.function_call.arguments).get("loc_destination")
params = json.loads(output.function_call.arguments)
type(params)

# print('.........these are the params...')
# print(origin)
# print(destination)
# print(params)

# Call the function with arguments

chosen_function = eval(output.function_call.name)
flight = chosen_function(**params)

print('These are the details:',flight)

# --------------------------------------------------------------
# Add function result to the prompt for a final answer
# --------------------------------------------------------------
print('.........now we USE IT WITH FUNCTION......')
# The key is to add the function output back to the messages with role: function
second_completion = client.chat.completions.create( #openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",
    messages=[
        {"role": "user", "content": user_prompt},
        {"role": "function", "name": output.function_call.name, "content": flight},
    ],
    functions=function_descriptions,
)
response = second_completion.choices[0].message.content
print(response)