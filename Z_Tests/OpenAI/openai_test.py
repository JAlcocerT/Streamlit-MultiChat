import openai
import os
from dotenv import load_dotenv

load_dotenv()

def is_openai_api_key_valid(api_key):
    openai.api_key = api_key
    try:
        openai.models.list()  # A simple, inexpensive API call
        return True
    except openai.AuthenticationError:
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

# Example usage:
api_key = os.getenv("OPENAI_API_KEY")  # Or replace with your actual API key string

if api_key:
    if is_openai_api_key_valid(api_key):
        print("OpenAI API key is valid.")
    else:
        print("OpenAI API key is invalid.")
else:
    print("OpenAI API key not found in environment variables.")

print(api_key)