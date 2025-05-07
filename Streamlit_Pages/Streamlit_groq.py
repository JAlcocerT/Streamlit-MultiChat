#https://github.com/tonykipkemboi/groq_streamlit_demo

from typing import Generator
from groq import Groq

import streamlit as st
from Streamlit_Pages.config import Config

models = {
    "gemma-7b-it": {"name": "Gemma-7b-it via Groq", "tokens": 8192, "developer": "Google"},
    "llama3-70b-8192": {"name": "LLaMA3-70b-8192  via Groq", "tokens": 8192, "developer": "Meta"},
    "llama3-8b-8192": {"name": "LLaMA3-8b-8192 via Groq", "tokens": 8192, "developer": "Meta"},
    "mixtral-8x7b-32768": {"name": "Mixtral-8x7b-Instruct-v0.1 via Groq", "tokens": 32768, "developer": "Mistral"},
}

# Allow flexible Groq API key loading: from Streamlit secrets or .env/environment
import os
from dotenv import load_dotenv
load_dotenv()

# Determine Groq API key from Streamlit secrets or environment
_groq_api_key = None
try:
    _groq_api_key = st.secrets.get("GROQ_API_KEY")
except Exception:
    _groq_api_key = None
if not _groq_api_key:
    _groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize client if key is provided
client = None
if _groq_api_key:
    try:
        client = Groq(api_key=_groq_api_key)
    except Exception as _e:
        # Initialization failed; client remains None
        client = None
        # Defer error reporting to the page
        print(f"[Groq] Error initializing client: {_e}")

def generate_chat_responses(chat_completion) -> Generator[str, None, None]:
    for chunk in chat_completion:
        if chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content

def page_one():
    # Ensure Groq client is initialized
    if client is None:
        st.sidebar.error(
            "Groq API key is not configured. Please set GROQ_API_KEY in Streamlit secrets or environment."
        )
        return
    with st.sidebar:
        st.title('🤖💬 Groq Chatbot')

        model_option = st.selectbox(
            "Choose a model:",
            options=list(models.keys()),
            format_func=lambda x: models[x]["name"],
            index=3  # Default to mixtral
        )

        if 'selected_model' not in st.session_state or st.session_state.selected_model != model_option:
            st.session_state.messages = []
            st.session_state.selected_model = model_option

        max_tokens_range = models[model_option]["tokens"]

        max_tokens = st.slider(
            "Max Tokens:",
            min_value=512,  # Minimum value to allow some flexibility
            max_value=max_tokens_range,
            value=min(32768, max_tokens_range),
            step=512,
            help=f"Adjust the maximum number of tokens (words) for the model's response. Max for selected model: {max_tokens_range}"
        )

        temperature = st.slider(
            "Temperature:",
            min_value=0.0,
            max_value=1.0,
            value=0.6,
            step=0.1,
            help="Adjust the temperature for the model's response. Higher values will result in more random responses, while lower values will result in more deterministic responses."
        )

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        avatar = '🤖' if message["role"] == "assistant" else '👨‍💻'
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])

    if prompt := st.chat_input("Enter your prompt here..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user", avatar='👨‍💻'):
            st.markdown(prompt)
        with st.chat_message("assistant", avatar="🤖"):
            message_placeholder = st.empty()
            full_response = ""
            try:
                if model_option in Config.OLLAMA_MODELS:
                    llm_stream = chat(prompt,
                                      model=model_option,
                                      temperature=0.7)
                    stream_output = st.write_stream(stream_parser(llm_stream))
                else:
                    chat_completion = client.chat.completions.create(
                        model=model_option,
                        messages=[
                            {
                                "role": m["role"],
                                "content": m["content"]
                            }
                            for m in st.session_state.messages
                        ],
                        max_tokens=max_tokens,
                        temperature=0.6,
                        stream=True
                    )
                    chat_responses_generator = generate_chat_responses(chat_completion)
                    for response in chat_responses_generator:
                        full_response += response
                        message_placeholder.markdown(full_response + "▌")
            except Exception as e:
                st.error(e, icon="🚨")

            message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})