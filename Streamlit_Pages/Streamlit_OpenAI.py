# #https://github.com/dataprofessor/openai-chatbot

import streamlit as st

from openai import OpenAI

def page_three():

    client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    #api_key="private",
                )
    
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
            ['gpt-4o-mini','gpt-3.5-turbo', 'gpt-4-turbo-preview', 'gpt-4o'],
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
            for response in client.chat.completions.create(
                                                        model=model_choice,
                                                        messages=[{"role": m["role"], "content": m["content"]}
                                                                for m in st.session_state.messages], 
                                                        temperature=temperature,  # Use the selected temperature here
                                                        stream=True):
                                                        full_response += response.choices[0].delta.get("content", "")
                                                        message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})

#---

# import streamlit as st

# import openai

# def page_three():
#     with st.sidebar:
#         st.title('🤖💬 OpenAI Chatbot')
#         if 'OPENAI_API_KEY' in st.secrets and len(st.secrets['OPENAI_API_KEY']) > 30:
#             st.success('API key already provided!', icon='✅')
#             openai.api_key = st.secrets['OPENAI_API_KEY']
#         else:
#             openai.api_key = st.text_input('Enter OpenAI API token:', type='password')
#             if not (openai.api_key.startswith('sk-') and len(openai.api_key) > 30):
#                 st.warning('Please, enter your credentials', icon='⚠️')
#             else:
#                 st.success('Proceed with your Prompts!', icon='👉')

#         model_choice = st.selectbox(
#             'Choose the model:',
#             ['gpt-3.5-turbo', 'gpt-4-turbo-preview', 'gpt-4o', 'gpt-4o-mini'],
#             index=0
#         )

#         temperature = st.slider(
#             'Select temperature for the model:',
#             min_value=0.0,
#             max_value=1.0,
#             value=0.7,
#             step=0.01
#         )

#     if "messages" not in st.session_state:
#         st.session_state.messages = []

#     for message in st.session_state.messages:
#         with st.chat_message(message["role"]):
#             st.markdown(message["content"])

#     if prompt := st.chat_input("What is up?"):
#         st.session_state.messages.append({"role": "user", "content": prompt})
#         with st.chat_message("user"):
#             st.markdown(prompt)
#         with st.chat_message("assistant"):
#             message_placeholder = st.empty()
#             full_response = ""
#             for response in openai.ChatCompletion.create(
#                 model=model_choice,
#                 messages=[{"role": m["role"], "content": m["content"]}
#                           for m in st.session_state.messages], 
#                 temperature=temperature,  # Use the selected temperature here
#                 stream=True):
#                 full_response += response.choices[0].delta.get("content", "")
#                 message_placeholder.markdown(full_response + "▌")
#             message_placeholder.markdown(full_response)
#         st.session_state.messages.append({"role": "assistant", "content": full_response})