
import os
from dotenv import load_dotenv
from openai import OpenAI  # pip install openai>0.28

# Load environment variables from the .env file
load_dotenv()

# Get the OpenAI API key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    api_key=api_key,
)

#
#from openai import OpenAI
#pip install --upgrade openai
#1.73.0
import os

# Get your OpenAI API key from environment variables or hardcode it (not recommended for production)
openai_api_key = os.environ.get("OPENAI_API_KEY")
if not openai_api_key:
    print("Error: OPENAI_API_KEY environment variable not set.")
    exit()

client = OpenAI(api_key=openai_api_key)

prompt = "A vibrant cyberpunk cityscape at sunset with flying vehicles."

try:
    response = client.images.generate(
        model="dall-e-3",  # Or "dall-e-2"
        prompt=prompt,
        n=1,  # Number of images to generate (default is 1 for DALL·E 3)
        size="1024x1024",  # Available sizes vary by model
        # quality="standard", # For DALL·E 3, can be "standard" or "hd" (default is "standard")
        # style="vivid",     # For DALL·E 3, can be "vivid" or "natural" (default is "vivid")
    )

    image_url = response.data[0].url
    print(f"Generated image URL: {image_url}")

    # You can then download the image from the URL or handle the response data differently
    # If you want the base64 encoded image data instead of the URL:
    # response = client.images.generate(
    #     model="dall-e-3",
    #     prompt=prompt,
    #     n=1,
    #     size="1024x1024",
    #     response_format="b64_json"
    # )
    # import base64
    # from io import BytesIO
    # from PIL import Image
    # b64_image = response.data[0].b64_json
    # image_bytes = base64.b64decode(b64_image)
    # image = Image.open(BytesIO(image_bytes))
    # image.save("generated_image.png")
    # print("Image saved as generated_image.png")

except Exception as e:
    print(f"Error generating image: {e}")