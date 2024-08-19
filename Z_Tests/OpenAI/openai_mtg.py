#python3 pyopen.py > output.mdx

import os
from dotenv import load_dotenv
from openai import OpenAI  # pip install openai==1.30.5

# Load environment variables from the .env file
load_dotenv()

# Get the OpenAI API key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client
client = OpenAI(
    api_key=api_key,
)

mtg_must_have= """
* Purpose - Every meeting should have an objective—the reason why you're having the meeting. Before you schedule a meeting be sure you know what it is that you want out of the meeting.
* Agenda - An agenda outlines the plan for the meeting and lets participants know what to expect. It allows them to be prepared so they can actively participate and bring their expertise to the table.  
* preparation - Before the meeting all participants should take some time to review the agenda and prepare any questions they may have. 
"""

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": f"""You are an expert meeting assistant. Very aware of the following:
                              {mtg_must_have}  
                        """,
        },
        {"role": "user", "content": "Who are you and what can you do?"}

    ],
    model="gpt-4o-mini",
    temperature=0.7,
)

# print(chat_completion)
# Extract and print the content of the completed message
completed_message = chat_completion.choices[0].message.content
print(completed_message)