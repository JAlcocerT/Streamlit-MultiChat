import json
import os
import requests
from datetime import datetime
import pytz
import re  # For regular expressions

# Ensure Ollama is running and accessible

def get_current_weather(location):
    """Gets the current weather in a given location."""
    print(f"Calling get_current_weather for {location}")
    if location.lower() == "warsaw":
        return {"temperature": 20, "conditions": "sunny", "location": "Warsaw, Poland"}
    elif location.lower() == "london":
        return {"temperature": 17, "conditions": "cloudy", "location": "London, UK"}
    else:
        return {"temperature": "unknown", "conditions": "unknown", "location": location}

def get_current_time(location):
    """Gets the current time in a given location."""
    print(f"Calling get_current_time for {location}")
    if location.lower() == "warsaw":
        warsaw_tz = pytz.timezone('Europe/Warsaw')
        now_warsaw = datetime.now(warsaw_tz)
        return {"time": now_warsaw.strftime("%H:%M"), "location": "Warsaw, Poland"}
    elif location.lower() == "london":
        london_tz = pytz.timezone('Europe/London')
        now_london = datetime.now(london_tz)
        return {"time": now_london.strftime("%H:%M"), "location": "London, UK"}
    else:
        return {"time": "unknown", "location": location}

OLLAMA_API_URL = "http://192.168.0.12:11434/api/chat"
MODEL_NAME = "llama3.2"  # Choose an appropriate Ollama model

tools_description = """
You have access to the following tools:

1.  get_current_weather(location: string) - Gets the current weather in a specific location.
2.  get_current_time(location: string) - Gets the current time in a specific location.

When the user asks a question that requires using one of these tools, respond with a JSON object indicating which tool to use and the necessary parameters. For example:

{"tool_name": "get_current_weather", "parameters": {"location": "London"}}

or

{"tool_name": "get_current_time", "parameters": {"location": "Warsaw"}}

If the user's request doesn't require any tool, respond in a natural language.
"""

user_queries = [
    "What's the weather like in London?",
    "What time is it in Warsaw?",
    "Tell me about the weather and time in Warsaw.",
    "Is it sunny right now in Warsaw?",
    "What's the current hour in London?",
    "Give me an update on London."
]

for user_query in user_queries:
    print(f"\nUser query: {user_query}")

    prompt = f"{tools_description}\n\nUser Query: {user_query}"

    data = {
        "model": MODEL_NAME,
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(OLLAMA_API_URL, json=data)
    response.raise_for_status()
    ai_response_text = response.json()['choices'][0]['message']['content'].strip()
    print(f"Ollama's initial response text: {ai_response_text}")

    tool_call = None
    try:
        # Attempt to find JSON within the response using regex
        json_match = re.search(r'\{.*\}', ai_response_text, re.DOTALL)
        if json_match:
            json_string = json_match.group(0)
            tool_call = json.loads(json_string)
        else:
            raise json.JSONDecodeError("No JSON found via regex", ai_response_text, 0)
    except json.JSONDecodeError as e:
        print(f"JSONDecodeError: {e}")
        print("Could not parse tool call. Proceeding with natural language response.")
        print(f"Ollama's natural language response: {ai_response_text}")

    if tool_call:
        tool_name = tool_call.get("tool_name")
        parameters = tool_call.get("parameters")

        if tool_name == "get_current_weather" and parameters and "location" in parameters:
            weather_data = get_current_weather(parameters["location"])
            print(f"Tool Result: {weather_data}")
            final_prompt = f"You called the 'get_current_weather' tool with the location '{parameters['location']}'. The result was: {weather_data}. Respond to the user in a natural language."
            final_data = {
                "model": MODEL_NAME,
                "messages": [
                    {"role": "user", "content": prompt},
                    {"role": "assistant", "content": ai_response_text},
                    {"role": "user", "content": final_prompt}
                ]
            }
            final_response = requests.post(OLLAMA_API_URL, json=final_data).json()['choices'][0]['message']['content'].strip()
            print(f"Final answer from Ollama: {final_response}")

        elif tool_name == "get_current_time" and parameters and "location" in parameters:
            time_data = get_current_time(parameters["location"])
            print(f"Tool Result: {time_data}")
            final_prompt = f"You called the 'get_current_time' tool with the location '{parameters['location']}'. The result was: {time_data}. Respond to the user in a natural language."
            final_data = {
                "model": MODEL_NAME,
                "messages": [
                    {"role": "user", "content": prompt},
                    {"role": "assistant", "content": ai_response_text},
                    {"role": "user", "content": final_prompt}
                ]
            }
            final_response = requests.post(OLLAMA_API_URL, json=final_data).json()['choices'][0]['message']['content'].strip()
            print(f"Final answer from Ollama: {final_response}")

        else:
            print("Could not parse tool call or unrecognized tool.")