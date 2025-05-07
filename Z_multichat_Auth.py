import streamlit as st

from Streamlit_Pages.config import Config

import os

from Streamlit_Pages.Streamlit_groq import page_one
from Streamlit_Pages.Streamlit_Ollama import page_two
from Streamlit_Pages.Streamlit_OpenAI import page_three
from Streamlit_Pages.Streamlit_Anthropic import page_four
#from Streamlit_Pages.Streamlit_ScrapeGraph import page_five
from Streamlit_Pages.Streamlit_YT_Groq import page_six

from Streamlit_Pages import Auth_functions as af

st.set_page_config(page_icon="💬", layout="wide", page_title="Multi-Chat Bot")

if af.login(): #Simple Auth Layer

    # Initialize chat history and selected model
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "selected_model" not in st.session_state:
        st.session_state.selected_model = None

    # Choose a streamlit page
    #pages = {'OpenAI API': page_three, 'Groq API': page_one, 'Local with Ollama': page_two, 'Anthropic API': page_four, 'ScrapeGraph': page_five, 'YT Summaries':page_six}
    pages = {'OpenAI API': page_three, 'Groq API': page_one, 'Local with Ollama': page_two, 'Anthropic API': page_four, 'YT Summaries':page_six}
    selected_page = st.sidebar.selectbox("Choose the Model Provider:", options=list(pages.keys()))
    pages[selected_page]()