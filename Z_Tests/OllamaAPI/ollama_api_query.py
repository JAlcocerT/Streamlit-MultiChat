import requests
import json
import re

OLLAMA_API_URL = "http://192.168.0.12:11434/api/chat"
MODEL_NAME = "llama3.2"

def query_ollama(prompt):
    """Sends a query to the specified Ollama model and returns the response."""
    data = {
        "model": MODEL_NAME,
        "messages": [{"role": "user", "content": prompt}]
    }
    try:
        response = requests.post(OLLAMA_API_URL, json=data)
        response.raise_for_status()
        ai_response_text = response.text.strip()
        try:
            json_data = json.loads(ai_response_text)
            return json_data['choices'][0]['message']['content'].strip()
        except json.JSONDecodeError:
            # Attempt to find JSON within the response using regex
            json_match = re.search(r'\{.*\}', ai_response_text, re.DOTALL)
            if json_match:
                json_string = json_match.group(0)
                try:
                    json_data = json.loads(json_string)
                    return json_data['choices'][0]['message']['content'].strip()
                except json.JSONDecodeError:
                    print("Error: Could not parse JSON even after regex extraction.")
                    print("Raw response:", ai_response_text)
                    return None
            else:
                print("Error: Could not find valid JSON in the Ollama response.")
                print("Raw response:", ai_response_text)
                return None
    except requests.exceptions.RequestException as e:
        print(f"Error communicating with Ollama API: {e}")
        return None

if __name__ == "__main__":
    user_query = input("Enter your query for llama3.2: ")
    if user_query:
        response = query_ollama(user_query)
        if response:
            print(f"\nResponse from {MODEL_NAME}:")
            print(response)