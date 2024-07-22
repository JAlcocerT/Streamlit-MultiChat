import openai
import requests
import os
import toml
from dotenv import load_dotenv

# Function to load the API key
def load_openai_api_key():
    # First, check if the API key is provided as an environment variable
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key:
        return api_key

    # If not found, try to load it from the .env file
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key:
        return api_key

    # If still not found, try to load it from the .toml file
    try:
        config = toml.load('../../.streamlit/secrets.toml')
        api_key = config['OPENAI_API_KEY'] #config['openai']['api_key']
        return api_key
    except FileNotFoundError:
        print("Error: secrets.toml file not found.")
    except KeyError:
        print("Error: API key not found in secrets.toml.")

    # If the API key is still not found, raise an error
    raise ValueError("OpenAI API key is not set. Please set it as an environment variable, in the .env file, or in the .toml file.")


# Set your OpenAI API key here
#openai.api_key = 'sk-proj-'
# config = toml.load('../../.streamlit/secrets.toml')
# #config['openai']['api_key']

# # Create an OpenAI client
# #client = openai.OpenAI()
client = openai.OpenAI(api_key=load_openai_api_key())

# Define the prompt for the image generation
prompt = "A futuristic cityscape with flying cars and neon lights"

# Generate the image using a specific model #https://platform.openai.com/docs/guides/images/generations
response = client.images.generate(
    model="dall-e-3",  # Specify the model here
    prompt=prompt,
    size="1024x1024",  # Size of the image
    quality="standard",  # Quality of the image
    n=1  # Number of images to generate
)

# Get the URL of the generated image
image_url = response.data[0].url

# Download and save the image
image_data = requests.get(image_url).content
with open('generated_image22.png', 'wb') as handler:
    handler.write(image_data)

print("Image generated and saved as 'generated_image22.png'")