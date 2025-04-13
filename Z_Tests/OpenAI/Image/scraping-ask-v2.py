#python3 scraping-ask-v2.py > comments_property_alijares.mdx

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

def get_jpg_urls_from_page(url, num_images=5):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        visorficha_div = soup.find('div', class_='visorficha-miniaturas')

        if not visorficha_div:
            print(f"No 'visorficha-miniaturas' div found on the page: {url}")
            return []

        li_elements = visorficha_div.find_all('li', class_='imagenesComoBackground')
        image_urls = []

        for li in li_elements[:num_images]:  # Limit to the first num_images
            style = li.get('style', '')
            if 'background-image' in style:
                start = style.find('url("') + len('url("')
                end = style.find('")')
                if start != -1 and end != -1:
                    img_url = style[start:end]
                    image_urls.append(img_url)

            cargafoto = li.get('cargafoto', '')
            if cargafoto:
                image_urls.append(cargafoto)

        return image_urls

    except requests.exceptions.RequestException as e:
        print(f"Error retrieving URL {url}: {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

def query_image_from_url(image_url: str, question: str, model: str = "gpt-4o-mini", max_tokens: int = 300):
    """
    Queries an image located at a given URL using the OpenAI Vision API.

    Args:
        image_url: The URL of the image to analyze.
        question: The question to ask about the image.
        model: The OpenAI Vision model to use (default: "gpt-4o-mini").
        max_tokens: The maximum number of tokens for the model's response (default: 300).

    Returns:
        str: The answer from the OpenAI model, or None if an error occurs.
    """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": question},
                        {
                            "type": "image_url",
                            "image_url": {"url": image_url},
                        },
                    ],
                }
            ],
            max_tokens=max_tokens,
        )
        answer = response.choices[0].message.content
        return answer
    except Exception as e:
        print(f"Error querying image from URL: {e}")
        return None

def analyze_first_n_images(url: str, question: str, num_images_to_analyze: int = 5, model: str = "gpt-4o-mini"):
    """
    Finds the URLs of the first n images on a webpage and asks the OpenAI model
    a question about each of them.

    Args:
        url: The URL of the webpage to scrape.
        question: The question to ask about each image.
        num_images_to_analyze: The number of images to analyze (default: 5).
        model: The OpenAI Vision model to use (default: "gpt-4o-mini").
    """
    image_urls = get_jpg_urls_from_page(url, num_images_to_analyze)

    if image_urls:
        print(f"Found {len(image_urls)} image URLs to analyze:")
        for i, img_url in enumerate(image_urls):
            print(f"[{i+1}] {img_url}")
            answer = query_image_from_url(img_url, question, model)
            if answer:
                print(f"Analysis for image [{i+1}]: {answer}\n")
            else:
                print(f"Could not get analysis for image [{i+1}].\n")
    else:
        print("No image URLs found on the page.")

if __name__ == "__main__":
    target_url = "https://www.viviendasylocalesgranada.com/ficha/chalet/otura/urbanizacion-los-alijares/4348/13194834/es/"
    analysis_question = "Describe the key features and the overall impression of this property."
    num_analyze = 5  # You can change the number of images to analyze

    analyze_first_n_images(target_url, analysis_question, num_analyze)