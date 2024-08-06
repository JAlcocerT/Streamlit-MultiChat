import streamlit as st
import os
import json
from scrapegraphai.graphs import SmartScraperGraph

def run_smart_scraper():
    # Streamlit page configuration
    st.set_page_config(page_title="Smart Scraper", layout="wide")

    # Fetch environment variables
    api_key = os.getenv('MODEL_API_KEY', 'default_api_key')
    model = os.getenv('MODEL', 'gpt-4o-mini')
    temperature = float(os.getenv('TEMPERATURE', 0))

    # Define the configuration for the scraping pipeline
    graph_config = {
        "llm": {
            "api_key": api_key,
            "model": model,
            "temperature": temperature
        },
        "verbose": True,
        "headless": True  # Important if you don't have a screen
    }

    # Streamlit user interface
    st.title("Smart Scraper")
    url = st.text_input("Enter the URL:", "https://scrapegraphai.com/")
    prompt = st.text_area("Enter the prompt:", "Find some information about what does the company do, the name and a contact email.")
    run_button = st.button("Run Scraper")

    if run_button:
        if url and prompt:
            # Create the SmartScraperGraph instance
            smart_scraper_graph = SmartScraperGraph(
                prompt=prompt,
                source=url,
                config=graph_config
            )

            # Run the pipeline
            result = smart_scraper_graph.run()
            
            # Display results
            st.json(result)
        else:
            st.warning("Please enter both a URL and a prompt.")

# To run the function when the script is executed
# if __name__ == "__main__":
#     run_smart_scraper()