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

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are an expert business analyst and will provide a detailed jira ticket content with the sections: context, story, acceptance criteria and references.",
        },
        {"role": "user", "content": "I need you to create a development ticket that: will improve current version of our L2B component to handle properly ingestion files with duplicated column names. The proposal is add some postfix with a number if there're repeated column names. "}

    ],
    model="gpt-4o-mini",
    temperature=0.3,
)

# print(chat_completion)
# Extract and print the content of the completed message
completed_message = chat_completion.choices[0].message.content
print(completed_message)

# Generate a .txt file for each EXPRESSIE value in the first 3 rows
   # Define the filename based on the row index
filename = f"./Ticket/DLH.txt"  # Start with 1.txt, 2.txt, etc.

# Write the EXPRESSIE value to the file
with open(filename, 'w', encoding='utf-8') as file:
    #file.write(row['EXPRESSIE'])
    # # print(chat_completion)
    # # Extract and print the content of the completed message
    completed_message = chat_completion.choices[0].message.content
    print(completed_message)
    file.write(completed_message)