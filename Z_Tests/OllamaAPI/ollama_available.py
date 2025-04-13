import requests
import json

OLLAMA_API_URL = "http://192.168.0.12:11434/api/tags"

try:
    response = requests.get(OLLAMA_API_URL)
    response.raise_for_status()  # Raise an exception for bad status codes

    data = response.json()
    if "models" in data:
        print("Available Ollama Models:")
        for model_info in data["models"]:
            name = model_info.get("name")
            modified_at = model_info.get("modified_at")
            size = model_info.get("size")
            print(f"- Name: {name}")
            if modified_at:
                print(f"  Modified At: {modified_at}")
            if size:
                print(f"  Size: {size / (1024 * 1024):.2f} MB")
    else:
        print("Could not find 'models' in the API response.")

except requests.exceptions.RequestException as e:
    print(f"Error communicating with Ollama API: {e}")
except json.JSONDecodeError:
    print("Error decoding JSON response from Ollama API.")