# import streamlit as st
# import streamlit.components.v1 as components

#https://mermaid.js.org/syntax/stateDiagram.html
#https://mermaid.js.org/syntax/mindmap.html
#https://mermaid.js.org/syntax/flowchart.html


import streamlit as st
import streamlit.components.v1 as components
import os
from dotenv import load_dotenv

from openai import OpenAI  # pip install openai==1.30.5

# Load environment variables from the .env file
load_dotenv()

# Get the OpenAI API key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client
client = OpenAI(
    api_key=api_key,
)

def get_mermaid_code_from_openai(prompt: str, api_key: str) -> str:
    #openai.api_key = api_key
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": """You are an expert developer in MermaidJS Charts that it is able to understand user requirements and provide highlevel diagrams.
                              Your favourite ones are: mindmap and basic flowchart:
                              graph LR
                                  A[Square Rect] -- Link text --> B((Circle))
                                  A --> C(Round Rect)
                                  B --> D{Rhombus}
                                  C --> D
                              """,
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.3,
    )
    completed_message = response.choices[0].message.content #response.choices[0].message["content"]
    return completed_message

def mermaid(code: str) -> None:
    components.html(
        f"""
        <pre class="mermaid">
            {code}
        </pre>

        <script type="module">
            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
            mermaid.initialize({{ startOnLoad: true }});
        </script>
        """,
        height=500,
    )

# Load OpenAI API key
#api_key = load_openai_api_key()

# Streamlit app title
st.title("Mermaid Diagram in Streamlit")

# User input for OpenAI prompt
st.write("Enter your prompt for the OpenAI API below:")
prompt = st.text_area("OpenAI Prompt", height=100, value="Describe a simple flowchart for a login process.")

# Generate Mermaid code from OpenAI
if st.button("Generate Mermaid Code"):
    if prompt and api_key:
        mermaid_code = get_mermaid_code_from_openai(prompt, api_key)
        st.write("Generated Mermaid code:")
        st.text_area("Mermaid Code", value=mermaid_code, height=200)
        st.write("Rendered Mermaid diagram:")
        mermaid(mermaid_code)
    else:
        st.write("Please enter a valid prompt and ensure API key is set.")

# User input for Mermaid code
st.write("Or manually enter your Mermaid diagram code below:")
user_mermaid_code = st.text_area("Mermaid Code", height=200, value="graph LR\n    A --> B --> C")

# Render the Mermaid diagram from user input
if user_mermaid_code:
    mermaid(user_mermaid_code)
else:
    st.write("Please enter a valid Mermaid diagram code.")