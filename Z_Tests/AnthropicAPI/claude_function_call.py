import anthropic #0.49.0
import json
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Replace with your actual Anthropic API key
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

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
    now_utc = datetime.utcnow()
    timezones = {"warsaw": 2, "london": 1}
    timezone_offset = timezones.get(location.lower(), 0)
    local_hour = (now_utc.hour + timezone_offset) % 24
    local_minute = now_utc.minute
    return {"time": f"{local_hour:02}:{local_minute:02}", "location": f"{location.capitalize()}"}

tools_description = """
You have access to the following tools:

1.  get_current_weather(location: string) - Gets the current weather in a specific location.
2.  get_current_time(location: string) - Gets the current time in a specific location.

When the user asks a question that requires using one of these tools, please respond with a JSON object indicating which tool to use and the necessary parameters. For example:

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

    messages = [
        {"role": "user", "content": f"{tools_description}\n\nUser Query: {user_query}"}
    ]

    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=300,
        messages=messages
    )

    ai_response = response.content[0].text.strip()
    print(f"Claude's initial response: {ai_response}")

    try:
        tool_call = json.loads(ai_response)
        tool_name = tool_call.get("tool_name")
        parameters = tool_call.get("parameters")

        if tool_name == "get_current_weather" and parameters and "location" in parameters:
            weather_data = get_current_weather(parameters["location"])
            print(f"Tool Result: {weather_data}")
            final_prompt = f"You called the 'get_current_weather' tool with the location '{parameters['location']}'. The result was: {weather_data}. Respond to the user in a natural language."
            final_messages = [
                {"role": "user", "content": f"{tools_description}\n\nUser Query: {user_query}"},
                {"role": "assistant", "content": ai_response},
                {"role": "user", "content": final_prompt}
            ]
            final_response = client.messages.create(
                model="claude-3-opus-20240229",
                max_tokens=300,
                messages=final_messages
            ).content[0].text.strip()
            print(f"Final answer from Claude: {final_response}")

        elif tool_name == "get_current_time" and parameters and "location" in parameters:
            time_data = get_current_time(parameters["location"])
            print(f"Tool Result: {time_data}")
            final_prompt = f"You called the 'get_current_time' tool with the location '{parameters['location']}'. The result was: {time_data}. Respond to the user in a natural language."
            final_messages = [
                {"role": "user", "content": f"{tools_description}\n\nUser Query: {user_query}"},
                {"role": "assistant", "content": ai_response},
                {"role": "user", "content": final_prompt}
            ]
            final_response = client.messages.create(
                model="claude-3-opus-20240229",
                max_tokens=300,
                messages=final_messages
            ).content[0].text.strip()
            print(f"Final answer from Claude: {final_response}")

        else:
            print("Could not parse tool call or unrecognized tool.")

    except json.JSONDecodeError:
        print(f"Final answer from Claude: {ai_response}")