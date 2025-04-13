import openai
import yaml
from datetime import datetime
import re  # For creating URL slugs
import os
from dotenv import load_dotenv
from openai import OpenAI
import requests
from bs4 import BeautifulSoup

# Load environment variables from the .env file
load_dotenv()

# Get the OpenAI API key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("Error: OPENAI_API_KEY environment variable not set.")
    exit()

client = OpenAI(api_key=api_key)

def generate_slug(title):
    """Generates a URL-friendly slug from a title."""
    slug = title.lower().replace(" ", "-")
    slug = re.sub(r"[^\w-]", "", slug)
    return slug

def generate_image(prompt, image_filepath):
    """Generates an image based on the prompt using DALL-E."""
    try:
        response = client.images.generate(
            model="dall-e-3",  # Or another DALL-E model
            prompt=prompt,
            n=1,
            size="1024x1024",  # Adjust size as needed
        )
        image_url = response.data[0].url
        image_response = requests.get(image_url)
        image_response.raise_for_status()  # Raise an exception for bad status codes

        with open(image_filepath, "wb") as f:
            f.write(image_response.content)
        return True
    except Exception as e:
        print(f"Error generating image: {e}")
        return False

def generate_blog_post(topic, base_front_matter):
    """Generates a blog post with front matter and an image URL using OpenAI."""

    # Generate dynamic parts of the front matter
    title = f"[AI] Exploring the Wonders of {topic.capitalize()}"
    slug = generate_slug(title)
    today = datetime.now().strftime("%Y-%m-%d")
    description = f"A deep dive into the fascinating world of {topic}."
    tags = [topic.capitalize(), "AI Generated"] # Example tags
    image_filename = f"{slug}.png"
    image_path = f"/images/{image_filename}" # Relative path for Hugo

    front_matter = {
        "title": title,
        "date": today,
        "draft": False,
        "tags": tags,
        "description": description,
        "url": slug,
        "image": image_path, # Add image path to front matter
        **base_front_matter  # Merge with any other base front matter you provide
    }

    prompt = f"""Write a comprehensive blog post about the topic: "{topic}".

    The blog post should cover various aspects of {topic}, provide examples where relevant, and aim to be informative and engaging for readers interested in learning more.

    Please structure the blog post with appropriate headings and subheadings to improve readability.
    """

    image_prompt = f"A visually appealing image representing the topic: '{topic}'. It should be suitable as a featured image for a blog post."

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=2000,  # Adjust as needed
            n=1,
            stop=None,
            temperature=0.7,
        )
        content = response.choices[0].message.content.strip()

        # Generate the image
        image_dir = "./"  # Assuming your Hugo static images are here
        os.makedirs(image_dir, exist_ok=True)
        image_filepath = os.path.join(image_dir, image_filename)
        if generate_image(image_prompt, image_filepath):
            return front_matter, content
        else:
            print("Warning: Image generation failed. Blog post will be created without an image URL.")
            front_matter.pop("image", None) # Remove image from front matter if generation fails
            return front_matter, content

    except Exception as e:
        print(f"Error generating content: {e}")
        return None, None

def create_hugo_post(front_matter, content, filepath):
    """Creates a Hugo .md post from front matter and content."""
    with open(filepath, 'w') as f:
        f.write("---\n")
        yaml.dump(front_matter, f, sort_keys=False)
        f.write("---\n\n")
        f.write(content)

if __name__ == "__main__":
    topic = "the impact of AI on creative industries"
    base_front_matter = {} # You can add any static front matter here

    front_matter, content = generate_blog_post(topic, base_front_matter)

    if front_matter and content:
        filename = f"./{front_matter['url']}.md"
        create_hugo_post(front_matter, content, filename)
        print(f"Hugo post created at: {filename}")