#python3 pyopen.py > output.mdx

import os
from openai import OpenAI # pip install openai==1.30.5

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "What it is Python?",
        }
    ],
    model="gpt-4o-mini",
    temperature=0.3,
)

# print(chat_completion)
# Extract and print the content of the completed message
completed_message = chat_completion.choices[0].message.content
print(completed_message)