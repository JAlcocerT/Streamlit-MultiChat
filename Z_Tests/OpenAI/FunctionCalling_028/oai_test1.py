import openai
import json
import os

# Replace with your actual OpenAI API key
#openai.api_key = os.environ.get("OPENAI_API_KEY")

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

#pip install python-dotenv==1.0.1

# Get API keys and other environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY  # Temporary for debugging


# 1. Define the function the LLM can call
def get_current_weather(location):
    """Gets the current weather in a given location. For demonstration purposes,
    we'll just return a fixed response. In a real application, you'd call a weather API.
    """
    if location.lower() == "warsaw":
        return {"temperature": 15, "conditions": "sunny", "location": "Warsaw, Poland"}
    elif location.lower() == "london":
        return {"temperature": 12, "conditions": "cloudy", "location": "London, UK"}
    else:
        return {"temperature": "unknown", "conditions": "unknown", "location": location}

# 2. Define the function schema for OpenAI
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
    }
]

# 3. User query
user_query = "What's the weather like in Warsaw right now?"

# 4. First API call to get the LLM's response and potential function call
response = openai.ChatCompletion.create(
    model= "gpt-3.5-turbo",  # Or another capable model
        #"gpt-4o-mini",
    messages=[{"role": "user", "content": user_query}],
    functions=functions,
    function_call="auto",  # Let the LLM decide when to call the function
)

response_message = response["choices"][0]["message"]

# 5. Check if the LLM decided to call a function
if response_message.get("function_call"):
    function_name = response_message["function_call"]["name"]
    function_args_str = response_message["function_call"]["arguments"]
    function_args = json.loads(function_args_str)

    print(f"LLM decided to call function: {function_name} with arguments: {function_args}")

    # 6. Call the actual function
    if function_name == "get_current_weather":
        weather_data = get_current_weather(location=function_args.get("location"))

        # 7. Send the function result back to the LLM
        second_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": user_query},
                response_message,  # The LLM's function call response
                {
                    "role": "function",
                    "name": function_name,
                    "content": json.dumps(weather_data),
                },
            ],
        )
        final_answer = second_response["choices"][0]["message"]["content"]
        print(f"\nFinal answer from LLM: {final_answer}")

else:
    # If the LLM didn't call a function, just print its response
    print(f"LLM response: {response_message['content']}")