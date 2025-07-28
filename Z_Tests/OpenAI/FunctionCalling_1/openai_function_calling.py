"""
Example of OpenAI function calling without BAML.
This script demonstrates how to use OpenAI's function calling capabilities
with direct API calls, showing both the standard approach and the structured output approach.
"""

import os
import json
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv(dotenv_path=Path(__file__).parent / ".env")

# Initialize OpenAI client
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY not found in environment")

client = OpenAI(api_key=api_key)

# Example 1: Traditional Function Calling
print("\n=== Example 1: Traditional Function Calling ===")

# Define the available functions
def get_current_weather(location, unit="celsius"):
    """Get the current weather in a given location"""
    # This would typically call a weather API
    # For this example, we'll just return mock data
    weather_data = {
        "location": location,
        "temperature": 22 if unit == "celsius" else 72,
        "unit": unit,
        "forecast": ["sunny", "windy"]
    }
    return json.dumps(weather_data)

# Define the function for the API to use
functions = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the current weather in a location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA"
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "The temperature unit to use"
                    }
                },
                "required": ["location"]
            }
        }
    }
]

# Make the API call with function definitions
response = client.chat.completions.create(
    model="gpt-4o",  # Use a model that supports function calling
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What's the weather like in Boston?"}
    ],
    tools=functions,
    tool_choice="auto"  # Let the model decide when to call the function
)

# Print the initial response
print("\nInitial Response:")
message = response.choices[0].message
print(f"Role: {message.role}")
print(f"Content: {message.content}")

# Check if the model wants to call a function
if message.tool_calls:
    # Process the function call
    for tool_call in message.tool_calls:
        function_name = tool_call.function.name
        function_args = json.loads(tool_call.function.arguments)
        
        print(f"\nFunction Call:")
        print(f"Name: {function_name}")
        print(f"Arguments: {function_args}")
        
        # Execute the function
        if function_name == "get_current_weather":
            function_response = get_current_weather(
                location=function_args.get("location"),
                unit=function_args.get("unit", "celsius")
            )
            print(f"\nFunction Response: {function_response}")
            
            # Send the function result back to the API
            second_response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": "What's the weather like in Boston?"},
                    message,
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "name": function_name,
                        "content": function_response
                    }
                ]
            )
            
            # Print the final response
            print("\nFinal Response:")
            print(second_response.choices[0].message.content)

# Example 2: JSON Mode for Structured Output
print("\n\n=== Example 2: JSON Mode for Structured Output ===")

# Define the structure we want
json_response_format = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"},
        "has_pets": {"type": "boolean"},
        "hobbies": {"type": "array", "items": {"type": "string"}}
    }
}

try:
    # Make an API call with JSON mode
    structured_response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that returns JSON."}, 
            {"role": "user", "content": "Generate a profile for a fictional person named Alice. Return the result as JSON."}
        ],
        response_format={"type": "json_object"},
    )
    
    # Parse and print the JSON response
    print("\nJSON Mode Response:")
    response_content = structured_response.choices[0].message.content
    print(f"Raw response: {response_content}")
    
    # Parse the JSON
    person_data = json.loads(response_content)
    print("\nParsed JSON data:")
    for key, value in person_data.items():
        print(f"{key}: {value}")
    
except Exception as e:
    print(f"Error with JSON mode: {e}")

if __name__ == "__main__":
    print("\nScript completed successfully!")
