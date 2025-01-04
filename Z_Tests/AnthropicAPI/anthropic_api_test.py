import streamlit as st
import anthropic
import os

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()  # This loads all environment variables from the .env file

# Create the Anthropi client
api_key = os.getenv("ANTHROPIC_API_KEY")
client = anthropic.Anthropic(api_key=api_key)

# Get user input


message = client.messages.create(
    model="claude-3-sonnet-20240229",
    max_tokens=689,
    temperature=0,
    messages=[
        {"role": "user", "content": f"What are the alternatives to selfhost a streamlit app?"}
    ]
)

    
mood_analysis = ''.join(block.text for block in message.content)  # Adjusted line