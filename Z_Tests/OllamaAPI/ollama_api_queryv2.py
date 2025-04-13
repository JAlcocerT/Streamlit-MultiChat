import requests
import json
import re

OLLAMA_API_URL = "http://192.168.0.12:11434/api/chat"
MODEL_NAME = "llama3.2"

def query_ollama(prompt):
    """Sends a query to the specified Ollama model and yields the response chunks."""
    data = {
        "model": MODEL_NAME,
        "messages": [{"role": "user", "content": prompt}],
        "stream": True  # Enable streaming
    }
    try:
        response = requests.post(OLLAMA_API_URL, json=data, stream=True)
        response.raise_for_status()
        for line in response.iter_lines():
            if line:
                try:
                    decoded_line = line.decode('utf-8')
                    json_chunk = json.loads(decoded_line)
                    content = json_chunk.get('message', {}).get('content')
                    done = json_chunk.get('done', False)
                    if content:
                        yield content
                    if done:
                        break
                except json.JSONDecodeError as e:
                    print(f"JSONDecodeError: {e} - Line: {line.decode('utf-8')}")
                    continue
    except requests.exceptions.RequestException as e:
        print(f"Error communicating with Ollama API: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    user_query = input("Enter your query for llama3.2: ")
    if user_query:
        print(f"\nResponse from {MODEL_NAME}:")
        full_response = ""
        for chunk in query_ollama(user_query):
            print(chunk, end="", flush=True)
            full_response += chunk
        print()
        # You can now work with the full_response if needed