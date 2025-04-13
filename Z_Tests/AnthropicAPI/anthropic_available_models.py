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

# 
# import anthropic
# import os

# # You need to have your Anthropic API key set as an environment variable
# # For example: export ANTHROPIC_API_KEY="your_api_key_here"
# ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
if not ANTHROPIC_API_KEY:
    print("Error: ANTHROPIC_API_KEY environment variable not set.")
else:
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    try:
        models_response = client.models.list()
        print("Available Claude Models:")
        for model in models_response.data:
            print(f"- ID: {model.id}")
            print(f"  Display Name: {model.display_name}")
            print(f"  Type: {model.type}")
            print(f"  Created At: {model.created_at}")
            # The 'updated_at' attribute does not exist in the ModelInfo object
            # print(f"  Updated At: {model.updated_at}")
            print()

    except anthropic.APIStatusError as e:
        print(f"Anthropic API Status Error: {e}")
    except anthropic.APIConnectionError as e:
        print(f"Anthropic API Connection Error: {e}")
    except anthropic.APIError as e:
        print(f"Anthropic API Error: {e}")