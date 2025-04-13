import os
from dotenv import load_dotenv
from openai import OpenAI
import requests  # To download the image

# Load environment variables from the .env file
load_dotenv()

# Get the OpenAI API key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("Error: OPENAI_API_KEY environment variable not set.")
    exit()

client = OpenAI(api_key=api_key)

prompt = "A vibrant cyberpunk cityscape at sunset with flying vehicles."
output_filename = "cyberpunk_cityscape.png"  # Define the name for the downloaded image

try:
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size="1024x1024",
        response_format="url",  # Ensure you get the URL
    )

    image_url = response.data[0].url
    print(f"Generated image URL: {image_url}")

    # Download the image
    image_response = requests.get(image_url)
    image_response.raise_for_status()  # Raise an exception for bad status codes

    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, output_filename)

    with open(output_path, "wb") as f:
        f.write(image_response.content)

    print(f"Image downloaded successfully to: {output_path}")

except Exception as e:
    print(f"Error generating or downloading image: {e}")