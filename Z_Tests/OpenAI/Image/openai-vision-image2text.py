import os
from dotenv import load_dotenv
from openai import OpenAI
import base64

# Load environment variables from the .env file
load_dotenv()

# Get the OpenAI API key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("Error: OPENAI_API_KEY environment variable not set.")
    exit()

client = OpenAI(api_key=api_key)

image_path = "cyberpunk_cityscape.png"  # Path to the image you want to query
question = "Describe the main elements and atmosphere of this image."

try:
    # Function to encode the image to base64
    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")

    base64_image = encode_image(image_path)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        #model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": question},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{base64_image}",
                        },
                    },
                ],
            }
        ],
        max_tokens=300,  # Adjust as needed
    )

    answer = response.choices[0].message.content
    print(f"Question: {question}")
    print(f"Answer: {answer}")

except FileNotFoundError:
    print(f"Error: Image file not found at {image_path}")
except Exception as e:
    print(f"Error querying image: {e}")