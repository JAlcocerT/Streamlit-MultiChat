# Streamlit-MultiChat

[![CI/CD Pipeline](https://github.com/JAlcocerT/Streamlit-MultiChat/actions/workflows/Streamlit_GH_Actions.yml/badge.svg)](https://github.com/JAlcocerT/JAlcocerT/Streamlit-MultiChat/actions/workflows/Streamlit_GH_Actions.yml)


## Getting Started 

<details>
  <summary>Clone me and Run me 👇</summary>
  &nbsp;

Try the Project quickly with [Python Venv's](https://fossengineer.com/python-dependencies-for-ai/):

```sh
python -m venv multichat #create it

multichat\Scripts\activate #activate venv (windows)
source multichat/bin/activate #(linux)
```

```sh
pip install -r requirements.txt #all at once
streamlit run Z_multichat.py
```

* Make sure to have [ollama ready](https://fossengineer.com/selfhosting-llms-ollama/) and running your desired model!
* Prepare the API Keys in any of:
    * .streamlit/secrets.toml
    * As Environment Variables
        * Linux - export OPENAI_API_KEY="YOUR_API_KEY"
        * CMD - set OPENAI_API_KEY=YOUR_API_KEY
        * PS - $env:OPENAI_API_KEY="YOUR_API_KEY"
        * In the Docker-Compose
    * Through the Streamlit UI
</details>


## Thanks to ❤️

* https://github.com/dataprofessor/openai-chatbot

* https://github.com/AIDevBytes/Streamlit-Ollama-Chatbot

* https://github.com/JAlcocerT/groq_streamlit_demo
* https://github.com/TirendazAcademy/Streamlit-Tutorials/blob/main/Blog-Generator-App-with-Claude-API/app.py
* https://www.youtube.com/watch?v=ximj9QWle-g

* https://github.com/siddhardhan23/gemini-pro-streamlit-chatbot