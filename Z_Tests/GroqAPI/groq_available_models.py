#https://console.groq.com/docs/api-reference#models

import requests
from dotenv import load_dotenv
import os
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Get the GROQ API key from environment variables
api_key = os.getenv("GROQ_API_KEY")

# API endpoint and headers
url = "https://api.groq.com/openai/v1/models"
headers = {
    "Authorization": f"Bearer {api_key}"
}

# Make the API request
response = requests.get(url, headers=headers)

# Check if the response was successful
if response.status_code == 200:
    data = response.json()  # Parse the JSON response

    # Sort models by 'created' date in descending order (newest first)
    sorted_models = sorted(data['data'], key=lambda x: x['created'], reverse=True)

    # Prepare the final output with relevant details
    output = []
    for model in sorted_models:
        model_name = model['id']
        created_date = datetime.utcfromtimestamp(model['created']).strftime('%Y-%m-%d %H:%M:%S')
        context_window = model['context_window']
        
        # Collect the model details
        output.append(f"Model: {model_name}\nCreated: {created_date}\nContext Window: {context_window}\n")
    
    # Print the final output
    print("\n".join(output))
else:
    print("Error fetching data:", response.status_code)



# import requests
# from dotenv import load_dotenv
# import os

# # Load environment variables from .env file
# load_dotenv()

# # Get the GROQ API key from environment variables
# api_key = os.getenv("GROQ_API_KEY")

# # API endpoint and headers
# url = "https://api.groq.com/openai/v1/models"
# headers = {
#     "Authorization": f"Bearer {api_key}"
# }

# # Make the API request
# response = requests.get(url, headers=headers)

# # Check if the response was successful
# if response.status_code == 200:
#     data = response.json()  # Parse the JSON response
#     model_names = [model['id'] for model in data['data']]  # Extract model names
    
#     # Print the model names
#     for model_name in model_names:
#         print(model_name)
# else:
#     print("Error fetching data:", response.status_code)