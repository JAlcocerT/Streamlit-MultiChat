# # # # # # # # Uses BS4+OpenAI to get the WebRelevant Info
# # # # # # # # Outputs text to markdown and saves images as zip via the streamlit interface
# # # # # # # # ready for SSG migration

# # 1. https://www.viviendasylocalesgranada.com/ficha/chalet/otura/urbanizacion-los-alijares/4348/13194834/es/
# # 2. https://www.viviendasylocalesgranada.com/ficha/casa-con-terreno/gojar/zona-de-gojar/4348/19314363/es/
# # 3. https://www.viviendasylocalesgranada.com/ficha/finca-rustica/moraleda-de-zafayona/moraleda-de-zafayona/4348/22216627/es/
# # 4. https://www.viviendasylocalesgranada.com/ficha/chalet/albolote/parque-del-cubillas/4348/22248092/es/
# # 5. https://www.viviendasylocalesgranada.com/ficha/casa/alhama-de-granada/area-de-alhama-de-granada/4348/22561693/es/

#import streamlit as st
import os
import requests
from bs4 import BeautifulSoup
#from io import BytesIO
#from zipfile import ZipFile  # Correct import
#from PIL import Image

# ... (rest of your code remains the same)

def get_jpg_urls_from_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        visorficha_div = soup.find('div', class_='visorficha-miniaturas')

        if not visorficha_div:
            st.error(f"No 'visorficha-miniaturas' div found on the page: {url}")
            return []

        li_elements = visorficha_div.find_all('li', class_='imagenesComoBackground')
        image_urls = []

        for li in li_elements:
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
        st.error(f"Error retrieving URL {url}: {e}")
        return []
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        return []


#a = get_jpg_urls_from_page('https://www.viviendasylocalesgranada.com/ficha/chalet/otura/urbanizacion-los-alijares/4348/13194834/es/')

#print(a)

#https://fotos15.apinmo.com/4348/13194834/11-3s.jpg

import os
from dotenv import load_dotenv
from openai import OpenAI
import base64
import requests

# Load environment variables from the .env file
load_dotenv()

# Get the OpenAI API key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("Error: OPENAI_API_KEY environment variable not set.")
    exit()

client = OpenAI(api_key=api_key)

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

if __name__ == "__main__":
    image_url_to_query = "https://fotos15.apinmo.com/4348/13194834/11-3s.jpg"  # Example URL
    query_question = "What type of property is shown in this image?"
    selected_model = "gpt-4o-mini"  # You can change this to "gpt-4-vision-preview" or other vision models

    answer = query_image_from_url(image_url_to_query, query_question, selected_model)

    if answer:
        print(f"Question: {query_question}")
        print(f"Model: {selected_model}")
        print(f"Answer: {answer}")