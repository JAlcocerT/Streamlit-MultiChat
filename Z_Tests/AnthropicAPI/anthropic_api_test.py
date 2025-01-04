import anthropic

#https://docs.anthropic.com/en/api/messages
#https://docs.anthropic.com/en/api/messages-examples

import os
# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()  # This loads all environment variables from the .env file


message = anthropic.Anthropic().messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude, could you explain different ways to deploy python streamlit web apps?. Simply List them in bullet points"}
    ]
)
print(message)

print(message.content)