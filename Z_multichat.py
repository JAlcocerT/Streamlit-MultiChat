import streamlit as st
import openai
from config import Config
from helpers.llm_helper import chat, stream_parser
import os

st.set_page_config(
    page_title=Config.PAGE_TITLE,
    initial_sidebar_state="expanded"
)

st.title(Config.PAGE_TITLE)

with st.sidebar:   
    st.markdown("# Chat Options")
    
    model = st.selectbox(
    'What model would you like to use?', 
    Config.OLLAMA_MODELS + tuple(['gpt-3.5-turbo', 'gpt-4-turbo-preview','gpt-4o'])
)

api_key = os.environ.get('OPENAI_API_KEY')

if api_key:
    openai.api_key = api_key
    st.success('API key loaded from environment variable!', icon='✅')
elif 'OPENAI_API_KEY' in st.secrets:
    openai.api_key = st.secrets['OPENAI_API_KEY']
    st.success('API key loaded from Streamlit secrets!', icon='✅')
else:
    openai.api_key = st.text_input('Enter OpenAI API token:', type='password')
    if not (openai.api_key.startswith('sk-')):
        st.warning('Please enter your credentials!', icon='⚠️')

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
        if model in Config.OLLAMA_MODELS:
            llm_stream = chat(user_prompt, model=model)
            stream_output = st.write_stream(stream_parser(llm_stream))
        else:
            message_placeholder = st.empty()
            full_response = ""
            for response in openai.ChatCompletion.create(
                model=model,  
                messages=[{"role": m["role"], "content": m["content"]}
                          for m in st.session_state.messages], stream=True):
                full_response += response.choices[0].delta.get("content", "")
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)

            stream_output = full_response

        st.session_state.messages.append({"role": "assistant", "content": stream_output})