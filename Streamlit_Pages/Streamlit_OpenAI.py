# #https://github.com/dataprofessor/openai-chatbot

### See new models over time
#https://github.com/JAlcocerT/Streamlit-MultiChat/blob/main/Z_Tests/OpenAI/list_models.py

import streamlit as st
import os 
from openai import OpenAI


def page_three():

    client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    #api_key="private",
                )
    
    # Define a default list of models
    default_models = ['gpt-4.1-nano', 'gpt-4o-mini', 'gpt-4.1', 'gpt-4o']

    # Try to get models from the environment variable
    models_from_env = os.environ.get("OPENAI_MODELS")

    # Use models from environment variable if it's a non-empty comma-separated string,
    # otherwise use the default list
    if models_from_env:
        model_list = [model.strip() for model in models_from_env.split(',')]
    else:
        model_list = default_models    
    
    with st.sidebar:
        st.title('🤖💬 OpenAI Chatbot')
        if 'OPENAI_API_KEY' in st.secrets and len(st.secrets['OPENAI_API_KEY']) > 30:
            st.success('API key already provided!', icon='✅')
            OpenAI.api_key = st.secrets['OPENAI_API_KEY']
        else:
            OpenAI.api_key = st.text_input('Enter OpenAI API token:', type='password')
            if not (OpenAI.api_key.startswith('sk-') and len(OpenAI.api_key) > 30):
                st.warning('Please, enter your credentials', icon='⚠️')
            else:
                st.success('Proceed with your Prompts!', icon='👉')

        model_choice = st.selectbox(
            'Choose the model:',
            model_list,
            index=0 if 'gpt-4.1-nano' in model_list else 0 # Set default to the first available model
        )

        temperature = st.slider(
            'Select temperature for the model:',
            min_value=0.0,
            max_value=1.0,
            value=0.7,
            step=0.01
        )

    system_prompt = os.getenv("SYSTEM_PROMPT", "You are a helpful assistant.")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Insert system prompt if provided
    if system_prompt:
        system_message = system_prompt
    else:
        system_message = "You are a helpful assistant."

    # Add system message if not already included
    if not any(msg["role"] == "system" for msg in st.session_state.messages):
        st.session_state.messages.insert(0, {
            "role": "system",
            "content": system_message
        })

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User input for additional questions or messages
    if prompt := st.chat_input("Ask something to the assistant..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Processing your question..."):
                message_placeholder = st.empty()
                full_response = ""
                for response in client.chat.completions.create(
                    model=model_choice,
                    temperature=temperature,
                    messages=[{"role": m["role"], "content": m["content"]}
                              for m in st.session_state.messages], stream=True):
                    content = response.choices[0].delta.content
                    if content:
                        full_response += content
                        message_placeholder.markdown(full_response + "▌")
                message_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})