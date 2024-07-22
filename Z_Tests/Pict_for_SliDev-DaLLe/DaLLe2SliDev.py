import openai #0.28.1
import requests
import os

# Set your OpenAI API key here
openai.api_key = 'sk-proj-...'

# Define the prompt for the image generation
#prompt = "A futuristic cityscape with flying cars and neon lights"
prompt = "A calm city with parks. Realistic look."

# Generate the image
response = openai.Image.create(
    prompt=prompt,
    n=1,  # Number of images to generate
    size="1024x1024",  # Size of the image
)

# Get the URL of the generated image
image_url = response['data'][0]['url']

# Download the image
image_data = requests.get(image_url).content
with open('generated_image.png', 'wb') as handler:
    handler.write(image_data)

print("Image generated and saved as 'generated_image.png'")