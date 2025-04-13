import openai
import json
import os
from datetime import datetime

# # Replace with your actual OpenAI API key (or ensure it's in your .env file)
# openai.api_key = os.environ.get("OPENAI_API_KEY")

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

#pip install python-dotenv==1.0.1

# Get API keys and other environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY  # Temporary for debugging


def get_current_weather(location):
    """Gets the current weather in a given location."""
    print(f"Calling get_current_weather for {location}")
    if location.lower() == "warsaw":
        return {"temperature": 18, "conditions": "partly cloudy", "location": "Warsaw, Poland"}
    elif location.lower() == "london":
        return {"temperature": 15, "conditions": "rainy", "location": "London, UK"}
    else:
        return {"temperature": "unknown", "conditions": "unknown", "location": location}

def get_current_time(location):
    """Gets the current time in a given location."""
    print(f"Calling get_current_time for {location}")
    if location.lower() == "warsaw":
        now_utc = datetime.utcnow()
        # Approximate UTC+2 for Warsaw in April (Daylight Saving Time)
        warsaw_time = now_utc.hour + 2, now_utc.minute
        return {"time": f"{warsaw_time[0]:02}:{warsaw_time[1]:02}", "location": "Warsaw, Poland"}
    elif location.lower() == "london":
        now_utc = datetime.utcnow()
        london_time = now_utc.hour + 1, now_utc.minute # Approximate UTC+1 for London in April
        return {"time": f"{london_time[0]:02}:{london_time[1]:02}", "location": "London, UK"}
    else:
        return {"time": "unknown", "location": location}

functions = [
    {
        "name": "get_current_weather",
        "description": "Get the current weather in a specific location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The city and state, e.g. San Francisco, CA",
                },
            },
            "required": ["location"],
        },
    },
    {
        "name": "get_current_time",
        "description": "Get the current time in a specific location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The city and state, e.g. San Francisco, CA",
                },
            },
            "required": ["location"],
        },
    },
]

# Example user queries
user_queries = [
    "What's the weather like in London?",
    "What time is it in Warsaw?",
    "Tell me about the weather and time in Warsaw.",
    "Is it sunny right now in Warsaw?",
    "What's the current hour in London?",
    "Give me an update on London." # Could be ambiguous, might lean towards weather
]

for user_query in user_queries:
    print(f"\nUser query: {user_query}")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_query}],
        functions=functions,
        function_call="auto",
    )

    response_message = response["choices"][0]["message"]

    if response_message.get("function_call"):
        function_name = response_message["function_call"]["name"]
        function_args_str = response_message["function_call"]["arguments"]
        function_args = json.loads(function_args_str)
        location = function_args.get("location")

        print(f"LLM decided to call function: {function_name} with arguments: {function_args}")

        if function_name == "get_current_weather":
            weather_data = get_current_weather(location=location)
            tool_response = json.dumps(weather_data)
        elif function_name == "get_current_time":
            time_data = get_current_time(location=location)
            tool_response = json.dumps(time_data)
        else:
            tool_response = "Function not recognized."

        second_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": user_query},
                response_message,
                {"role": "function", "name": function_name, "content": tool_response},
            ],
        )
        final_answer = second_response["choices"][0]["message"]["content"]
        print(f"Final answer from LLM: {final_answer}")

    else:
        print(f"LLM response: {response_message['content']}")