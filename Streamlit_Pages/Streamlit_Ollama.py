#https://github.com/AIDevBytes/Streamlit-Ollama-Chatbot

from Streamlit_Pages.config import Config
import streamlit as st

from helpers.llm_helper import chat, stream_parser


def page_two():
    with st.sidebar:
        st.title('🤖💬 LLaMA Chatbot')

        # if 'LLAMA_API_KEY' in st.secrets and len(st.secrets['LLAMA_API_KEY']) > 30:
        #     st.success('API key already provided!', icon='✅')
        # else:
        #     st.warning('Please, enter your credentials', icon='⚠️')

        model = st.selectbox(
            'What model would you like to use?', 
            Config.OLLAMA_MODELS
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

    if user_prompt := st.chat_input("What would you like to ask?"):
        st.session_state.messages.append({"role": "user", "content": user_prompt})
        with st.chat_message("user"):
            st.markdown(user_prompt)
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            try:
                llm_stream = chat(user_prompt, model=model, temperature=temperature)
                full_response = st.write_stream(stream_parser(llm_stream))
            except Exception as e:
                st.error(e, icon="🚨")
            message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})