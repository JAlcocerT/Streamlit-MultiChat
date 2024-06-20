# ### https://github.com/TirendazAcademy/Streamlit-Tutorials/blob/main/Blog-Generator-App-with-Claude-API/app.py

# from dotenv import load_dotenv 
import anthropic
import streamlit as st

# load_dotenv()

def get_response(user_content, temperature, model): 
    # client = anthropic.Anthropic()
    client = anthropic.Anthropic(api_key=api_key)
    response = client.messages.create(
        model=model,
        max_tokens=1024,
        temperature=temperature,
        system="Generate 5 attention-grabbing blog titles based on user-provived keywords",
        messages=[{"role":"user", "content":user_content}],
    )
    return response.content[0].text

st.title("Blog Title Generator")
api_key = st.text_input("Enter your Anthropic API Key:", type="password")
user_content = st.text_input("Enter the keyword for blog titles:")
temperature = st.slider("Select Temperature", min_value=0.0, max_value=1.0, value=0.5, step=0.1)
model = st.selectbox("Select Model", ("claude-3-opus-20240229", "claude-3-sonnet-20240229","claude-3.5-sonnet-20240620"))

if st.button("Generate Titles"):
    if not user_content:
        st.warning("Please enter a keyword before generating titles.", icon = "⚠️")
    else:
        generated_titles = get_response(user_content, temperature, model)
        st.success("Titles generated successfully!")
        st.text_area("", value=generated_titles, height=300)


# #from dotenv import load_dotenv 
# import anthropic
# import streamlit as st

# #load_dotenv()

# def get_response(user_content): 
#     #client = anthropic.Anthropic()
#     client = anthropic.Anthropic(api_key=api_key)
#     response = client.messages.create(
#         model="claude-3-opus-20240229", #claude-3-sonnet-20240229
#         max_tokens=1024,
#         temperature=0.5,
#         system="Generate 5 attention-grabbing blog titles based on user-provived keywords",
#         messages=[{"role":"user", "content":user_content}],
#     )
#     return response.content[0].text

# st.title("Blog Title Generator")
# api_key = st.text_input("Enter your Anthropic API Key:", type="password")
# user_content = st.text_input("Enter the keyword for blog titles:")

# if st.button("Generate Titles"):
#     if not user_content:
#         st.warning("Please enter a keyword before generating titles.", icon = "⚠️")
#     generated_titles = get_response(user_content)
#     st.success("Titles generated successfully!")
#     st.text_area("", value=generated_titles, height=300)