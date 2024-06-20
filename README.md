# Streamlit-MultiChat

[![CI/CD Pipeline](https://github.com/JAlcocerT/openai-chatbot/actions/workflows/GithubActions-CICD.yml/badge.svg)](https://github.com/JAlcocerT/openai-chatbot/actions/workflows/GithubActions-CICD.yml)


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
streamlit run multichat.py
```

* Make sure to have [ollama ready](https://fossengineer.com/selfhosting-llms-ollama/) and running your desired model!
* Prepare the API Keys in any of:
    * .streamlit/secrets.toml
    * As environment Variable
        * Linux
        * CMD
        * PS
        * Docker-Compose
    * Through the Streamlit UI
</details>


## Thanks to ❤️

* https://github.com/dataprofessor/openai-chatbot
* https://github.com/AIDevBytes/Streamlit-Ollama-Chatbot