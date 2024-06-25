import streamlit as st
from typing import Generator

from groq import Groq
import openai

from config import Config
from helpers.llm_helper import chat, stream_parser

import os

st.set_page_config(page_icon="💬", layout="wide", page_title="Multi-Chat Bot")

client = Groq(api_key=st.secrets["GROQ_API_KEY"],)

# Initialize chat history and selected model
if "messages" not in st.session_state:
    st.session_state.messages = []

if "selected_model" not in st.session_state:
    st.session_state.selected_model = None

models = {
    "gemma-7b-it": {"name": "Gemma-7b-it via Groq", "tokens": 8192, "developer": "Google"},
    "llama3-70b-8192": {"name": "LLaMA3-70b-8192  via Groq", "tokens": 8192, "developer": "Meta"},
    "llama3-8b-8192": {"name": "LLaMA3-8b-8192 via Groq", "tokens": 8192, "developer": "Meta"},
    "mixtral-8x7b-32768": {"name": "Mixtral-8x7b-Instruct-v0.1 via Groq", "tokens": 32768, "developer": "Mistral"},
}

def generate_chat_responses(chat_completion) -> Generator[str, None, None]:
    for chunk in chat_completion:
        if chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content

def page_one():
    # Layout for model selection and max_tokens slider
    col1, col2 = st.columns(2)

    with col1:
        model_option = st.selectbox(
            "Choose a model:",
            options=list(models.keys()),
            format_func=lambda x: models[x]["name"],
            index=3  # Default to mixtral
        )

    if st.session_state.selected_model != model_option:
        st.session_state.messages = []
        st.session_state.selected_model = model_option

    max_tokens_range = models[model_option]["tokens"]

    with col2:
        max_tokens = st.slider(
            "Max Tokens:",
            min_value=512,  # Minimum value to allow some flexibility
            max_value=max_tokens_range,
            value=min(32768, max_tokens_range),
            step=512,
            help=f"Adjust the maximum number of tokens (words) for the model's response. Max for selected model: {max_tokens_range}"
        )

    for message in st.session_state.messages:
        avatar = '🤖' if message["role"] == "assistant" else '👨‍💻'
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])

    if prompt := st.chat_input("Enter your prompt here..."):
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user", avatar='👨‍💻'):
            st.markdown(prompt)

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

                with st.chat_message("assistant", avatar="🤖"):
                    chat_responses_generator = generate_chat_responses(chat_completion)
                    full_response = st.write_stream(chat_responses_generator)
        except Exception as e:
            st.error(e, icon="🚨")

        if isinstance(full_response, str):
            st.session_state.messages.append(
                {"role": "assistant", "content": full_response})
        else:
            combined_response = "\n".join(str(item) for item in full_response)
            st.session_state.messages.append(
                {"role": "assistant", "content": combined_response})

def page_two():
    st.title(Config.PAGE_TITLE)

    with st.sidebar:   
        st.markdown("# Chat Options")

        model = st.selectbox('What model would you like to use?', Config.OLLAMA_MODELS)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if user_prompt := st.chat_input("What would you like to ask?"):
        with st.chat_message("user"):
            st.markdown(user_prompt)

        st.session_state.messages.append({"role": "user", "content": user_prompt})

        with st.spinner('Generating response...'):
            llm_stream = chat(user_prompt, model=model)

            stream_output = st.write_stream(stream_parser(llm_stream))

            st.session_state.messages.append({"role": "assistant", "content": stream_output})


# import openai
# import streamlit as st

def page_three():
    with st.sidebar:
        st.title('🤖💬 OpenAI Chatbot')
        if 'OPENAI_API_KEY' in st.secrets and len(st.secrets['OPENAI_API_KEY']) > 30:
            st.success('API key already provided!', icon='✅')
            openai.api_key = st.secrets['OPENAI_API_KEY']
        else:
            openai.api_key = st.text_input('Enter OpenAI API token:', type='password')
            if not (openai.api_key.startswith('sk-') and len(openai.api_key) > 30):
                st.warning('Please, enter your credentials', icon='⚠️')
            else:
                st.success('Proceed with your Prompts!', icon='👉')

        model_choice = st.selectbox(
            'Choose the model:',
            ['gpt-3.5-turbo', 'gpt-4-turbo-preview', 'gpt-4o'],
            index=0
        )

        temperature = st.slider(
            'Select temperature for the model:',
            min_value=0.0,
            max_value=1.0,
            value=0.7,
            step=0.01
        )

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is up?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            for response in openai.ChatCompletion.create(
                model=model_choice,
                messages=[{"role": m["role"], "content": m["content"]}
                          for m in st.session_state.messages], 
                temperature=temperature,  # Use the selected temperature here
                stream=True):
                full_response += response.choices[0].delta.get("content", "")
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})


# Choose page
pages = {'Groq API': page_one, 'Local with Ollama': page_two, 'OpenAI API': page_three}
selected_page = st.sidebar.selectbox("Choose the Model Provider:", options=list(pages.keys()))
pages[selected_page]()