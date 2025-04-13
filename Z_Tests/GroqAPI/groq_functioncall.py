import os
import json
from datetime import datetime
from groq import Groq
from dotenv import load_dotenv  # Import load_dotenv

# Load environment variables
load_dotenv()

# Get the Groq API key from the environment variable
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize the Groq client
client = Groq(api_key=GROQ_API_KEY)

# ... rest of your code ...

# import os
# import json
# from datetime import datetime
# from groq import Groq

# # Replace with your actual Groq API key
# GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
# client = Groq(api_key=GROQ_API_KEY)

def get_current_weather(location):
    """Gets the current weather in a given location."""
    print(f"Calling get_current_weather for {location}")
    if location.lower() == "warsaw":
        return {"temperature": 19, "conditions": "sunny", "location": "Warsaw, Poland"}
    elif location.lower() == "london":
        return {"temperature": 16, "conditions": "partly cloudy", "location": "London, UK"}
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

    prompt = f"{tools_description}\n\nUser Query: {user_query}"

    response = client.chat.completions.create(
        model="llama3-8b-8192",  # Or another capable Groq model
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300,
    )

    ai_response = response.choices[0].message.content.strip()
    print(f"Groq's initial response: {ai_response}")

    try:
        tool_call = json.loads(ai_response)
        tool_name = tool_call.get("tool_name")
        parameters = tool_call.get("parameters")

        if tool_name == "get_current_weather" and parameters and "location" in parameters:
            weather_data = get_current_weather(parameters["location"])
            print(f"Tool Result: {weather_data}")
            final_prompt = f"You called the 'get_current_weather' tool with the location '{parameters['location']}'. The result was: {weather_data}. Respond to the user in a natural language."
            final_response = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[
                    {"role": "user", "content": prompt},
                    {"role": "assistant", "content": ai_response},
                    {"role": "user", "content": final_prompt}
                ],
                max_tokens=300,
            ).choices[0].message.content.strip()
            print(f"Final answer from Groq: {final_response}")

        elif tool_name == "get_current_time" and parameters and "location" in parameters:
            time_data = get_current_time(parameters["location"])
            print(f"Tool Result: {time_data}")
            final_prompt = f"You called the 'get_current_time' tool with the location '{parameters['location']}'. The result was: {time_data}. Respond to the user in a natural language."
            final_response = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[
                    {"role": "user", "content": prompt},
                    {"role": "assistant", "content": ai_response},
                    {"role": "user", "content": final_prompt}
                ],
                max_tokens=300,
            ).choices[0].message.content.strip()
            print(f"Final answer from Groq: {final_response}")

        else:
            print("Could not parse tool call or unrecognized tool.")

    except json.JSONDecodeError:
        print(f"Final answer from Groq: {ai_response}")