import openai
import streamlit as st

import os


with st.sidebar:
    st.title('🤖💬 OpenAI Chatbot')
    
    # Check if the API key is available as an environment variable
    api_key = os.environ.get('OPENAI_API_KEY') #export OPENAI_API_KEY="YOUR_API_KEY" / set OPENAI_API_KEY=YOUR_API_KEY / $env:OPENAI_API_KEY="YOUR_API_KEY"

    
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
        else:
            st.success('Proceed to entering your prompt message!', icon='👉')

    # Dropdown menu to select the model
    model_choice = st.selectbox(
        'Choose the model:',
        ['gpt-3.5-turbo', 'gpt-4-turbo-preview','gpt-4o'],
        index=0  # Default selection is gpt-3.5-turbo
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
            model=model_choice,  # Use the selected model from the dropdown
            messages=[{"role": m["role"], "content": m["content"]}
                      for m in st.session_state.messages], stream=True):
            full_response += response.choices[0].delta.get("content", "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
