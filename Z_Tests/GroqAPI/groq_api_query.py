###QUERIES TO API AS PER THE GROQ API, DEFAULT###
from groq import Groq

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()  # This loads all environment variables from the .env file

client = Groq()

# Adding a sample message in the `messages` list
messages = [
    {"role": "user", "content": "Hello, what it is the fastest LLM inference in the market?"}
]

completion = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    #model="llama-3.2-90b-vision-preview",
    #model="llama3-groq-70b-8192-tool-use-preview",
    messages=messages,  # Now the messages list contains one message
    temperature=0.5,
    max_tokens=1024,
    top_p=0.65,
    stream=True,
    stop=None,
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")


#######
# https://console.groq.com/playground?model=llama3-groq-70b-8192-tool-use-preview
#####

# from groq import Groq

# # Load environment variables from .env file
# from dotenv import load_dotenv
# load_dotenv()  # This loads all environment variables from the .env file


# client = Groq()
# completion = client.chat.completions.create(
#     model="llama3-groq-70b-8192-tool-use-preview",
#     messages=[],
#     temperature=0.5,
#     max_tokens=1024,
#     top_p=0.65,
#     stream=True,
#     stop=None,
# )

# for chunk in completion:
#     print(chunk.choices[0].delta.content or "", end="")
