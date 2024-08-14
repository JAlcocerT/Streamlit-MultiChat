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

pain_opportunities= """ Understanding your client’s “pain points,” or the problem that your client needs to solve, is crucial. Your knowledge of the problem from the client’s perspective and the opportunity for growth or improvement guides the path you and your colleagues take as you begin your work.

The pain points and opportunities help you understand the client’s needs and the end goal.
Here are some examples of client “pain points”:

* To enhance security and comply with regulations
* To generate more revenue
* To reduce costs
* To offer a new service
* To improve customer engagement
* To increase the company’s competitive advantage
* To meet organizational or business goals: increase market shares, add value-add services, or develop the customer base

* make the sentences aiming to: polarize, arose amotions, be risque be unconventional and encourage the action
* avoid pain
* Why, what, how structure
"""

purpose="""
i am building a SaaS called xyzabc - to help people to book appointments online.

Please write me few call to actions.

Keep in mind the following:

* make the sentences aiming to: polarize, arose emotions, be risque be unconventional and encourage the action
* avoid pain
* make a story that will make the reader see why he needs this service
"""

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": """You are an expert neuro-marketer. Very aware of the following:
                                
                        """,
        },
        {"role": "user", "content": "Make a story that will make the reader see why he needs AI into his business"}

    ],
    model="gpt-4o-mini",
    temperature=0.7,
)

# print(chat_completion)
# Extract and print the content of the completed message
completed_message = chat_completion.choices[0].message.content
print(completed_message)