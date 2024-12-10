import os
from dotenv import load_dotenv
from openai import OpenAI  # Ensure you've installed the correct version via pip
from flask import Flask, request, jsonify

# Load environment variables from the .env file
load_dotenv()

# Get the OpenAI API key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client
client = OpenAI(api_key=api_key)

# Create a Flask application
app = Flask(__name__)

mtg_must_have = """
* Purpose - Every meeting should have an objective—the reason why you're having the meeting. Before you schedule a meeting be sure you know what it is that you want out of the meeting.
* Agenda - An agenda outlines the plan for the meeting and lets participants know what to expect. It allows them to be prepared so they can actively participate and bring their expertise to the table.  
* Preparation - Before the meeting all participants should take some time to review the agenda and prepare any questions they may have. 
"""

# Define an endpoint that responds to POST requests
@app.route('/query', methods=['POST'])
def query_openai():
    try:
        # Extract the user input from the request
        user_input = request.json.get('user_input', '')

        # Call the OpenAI Chat Completion with user input
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": f"""You are an expert meeting assistant. Very aware of the following:
                                  {mtg_must_have}  
                            """,
                },
                {"role": "user", "content": user_input}
            ],
            model="gpt-4o-mini",
            temperature=0.7,
        )

        # Extract the response
        completed_message = chat_completion.choices[0].message.content

        # Send response back to the requester
        return jsonify({"response": completed_message})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Run the server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Accessible from other devices in the local network