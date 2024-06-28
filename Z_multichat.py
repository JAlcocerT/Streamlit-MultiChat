import streamlit as st

from config import Config

import os

from Streamlit_Pages.Streamlit_groq import page_one
from Streamlit_Pages.Streamlit_Ollama import page_two
from Streamlit_Pages.Streamlit_OpenAI import page_three
from Streamlit_Pages.Streamlit_Anthropic import page_four

st.set_page_config(page_icon="💬", layout="wide", page_title="Multi-Chat Bot")

# Initialize chat history and selected model
if "messages" not in st.session_state:
    st.session_state.messages = []

if "selected_model" not in st.session_state:
    st.session_state.selected_model = None

# Choose page
pages = {'Groq API': page_one, 'Local with Ollama': page_two, 'OpenAI API': page_three, 'Anthropic API': page_four}
selected_page = st.sidebar.selectbox("Choose the Model Provider:", options=list(pages.keys()))
pages[selected_page]()