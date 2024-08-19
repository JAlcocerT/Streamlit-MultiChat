import os
from dotenv import load_dotenv
from openai import OpenAI  # pip install openai==1.30.5

# Load environment variables from the .env file
load_dotenv()



from datetime import datetime, timedelta


# Get the OpenAI API key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client
client = OpenAI(
    api_key=api_key,
)

from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o",
  #model="gpt-4o-mini",
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "what it is the weather in london?\n"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": ""
        }
      ],
      "tool_calls": [
        {
          "id": "call_pPvXPKckphpr0TEFgz0HFVfL",
          "type": "function",
          "function": {
            "name": "get_weather",
            "arguments": "{\"location\":\"London, UK\",\"unit\":\"c\"}"
          }
        }
      ]
    },
    {
      "role": "tool",
      "content": [
        {
          "type": "text",
          "text": ""
        }
      ],
      "tool_call_id": "call_pPvXPKckphpr0TEFgz0HFVfL"
    }
  ],
  temperature=0.3,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  tools=[
    {
      "type": "function",
      "function": {
        "name": "get_weather",
        "description": "Determine weather in my location",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "The city and state e.g. San Francisco, CA"
            },
            "unit": {
              "type": "string",
              "enum": [
                "c",
                "f"
              ]
            }
          },
          "required": [
            "location",
            "unit"
          ],
          "additionalProperties": False
        },
        "strict": True #To ensure the model's response always follows this schema.
      }
    }
  ],
  response_format={
    "type": "text"
  }
)

output = response.choices[0].message
print(output)