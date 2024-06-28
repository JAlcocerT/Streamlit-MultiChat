#https://github.com/TirendazAcademy/Streamlit-Tutorials/blob/main/Blog-Generator-App-with-Claude-API/app.py

import anthropic
import streamlit as st

def get_response(user_content, temperature, model):
    client = anthropic.Anthropic(api_key=st.secrets['ANTHROPIC_API_KEY'])
    response = client.messages.create(
        model=model,
        max_tokens=1024,
        temperature=temperature,
        system="You are a helpful assistant",
        #system="Generate 5 attention-grabbing blog titles based on user-provived keywords",
        messages=[{"role":"user", "content":user_content}],
    )
    return response.content[0].text

def page_four():
    with st.sidebar:
        st.title('📝 Chat with Anthropic')

        if 'ANTHROPIC_API_KEY' in st.secrets and len(st.secrets['ANTHROPIC_API_KEY']) > 30:
            st.success('API key already provided!', icon='✅')
        else:
            st.warning('Please, enter your credentials', icon='⚠️')

        model = st.selectbox(
            "Select Model", 
            ("claude-3-opus-20240229", "claude-3-sonnet-20240229","claude-3.5-sonnet-20240620")
        )

        temperature = st.slider(
            "Select Temperature", 
            min_value=0.0, 
            max_value=1.0, 
            value=0.5, 
            step=0.1
        )

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if user_content := st.chat_input("Chat with Claude LLMs:"):
        st.session_state.messages.append({"role": "user", "content": user_content})
        with st.chat_message("user"):
            st.markdown(user_content)
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            try:
                full_response = get_response(user_content, temperature, model)
            except Exception as e:
                st.error(e, icon="🚨")
            message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})