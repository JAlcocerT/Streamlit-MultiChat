![CI/CD Pipeline Status](https://github.com/JAlcocerT/streamlitmultichat/actions/workflows/streamlit_GH_Actions.yml/badge.svg)

[![CI/CD Pipeline](https://github.com/JAlcocerT/streamlitmultichat/actions/workflows/streamlit_GH_Actions.yml/badge.svg)](https://github.com/JAlcocerT/streamlit-multiChat/actions/workflows/streamlit_GH_Actions.yml)

<div align="center" style="line-height: 1;">
  <a href="https://github.com/JAlcocerT/Streamlit-MultiChat?tab=GPL-3.0-1-ov-file" style="margin: 2px;">
    <img alt="Code License" src="https://img.shields.io/badge/Code_License-MIT-f5de53?&color=f5de53" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://github.com/JAlcocerT/Streamlit-MultiChat?tab=GPL-3.0-1-ov-file" style="margin: 2px;">
    <img alt="Code License" src="https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://github.com/JAlcocerT/Streamlit-MultiChat/actions/workflows/streamlit_GH_Actions.yml" style="margin: 2px;">
    <img alt="Model License" src="https://github.com/JAlcocerT/streamlitmultichat/actions/workflows/streamlit_GH_Actions.yml/badge.svg" style="display: inline-block; vertical-align: middle;"/>
  </a>
</div>

[![CI/CD Pipeline](https://github.com/JAlcocerT/openai-chatbot/actions/workflows/GithubActions-CICD.yml/badge.svg)](https://github.com/JAlcocerT/openai-chatbot/actions/workflows/GithubActions-CICD.yml)

# Streamlit-MultiChat

Use commercial models: OpenAI / Anthropic or Open and Local LLMs with one Streamlit Web App.

## Getting Started 

<details>
  <summary>Clone and Run 👇</summary>
  &nbsp;

Try the Project quickly with [Python Venv's](https://fossengineer.com/python-dependencies-for-ai/):

```sh
git clone https://github.com/JAlcocerT/Streamlit-MultiChat
python -m venv multichat #create it

multichat\Scripts\activate #activate venv (windows)
source multichat/bin/activate #(linux)
```

```sh
pip install -r requirements.txt #all at once
streamlit run Z_multichat.py
```

* Make sure to have [Ollama ready](https://fossengineer.com/selfhosting-llms-ollama/) and running your desired model!
* Prepare the **API Keys** in any of:
    * .streamlit/secrets.toml
    * As Environment Variables
        * Linux - export OPENAI_API_KEY="YOUR_API_KEY"
        * CMD - set OPENAI_API_KEY=YOUR_API_KEY
        * PS - $env:OPENAI_API_KEY="YOUR_API_KEY"
        * In the [Docker-Compose](https://github.com/JAlcocerT/Streamlit-MultiChat/tree/main/Z_DeployMe)
    * Through the Streamlit UI
</details>


## Thanks to ❤️

* https://github.com/dataprofessor/openai-chatbot

* https://github.com/AIDevBytes/Streamlit-Ollama-Chatbot

* https://github.com/JAlcocerT/groq_streamlit_demo
* https://github.com/TirendazAcademy/Streamlit-Tutorials/blob/main/Blog-Generator-App-with-Claude-API/app.py
* https://www.youtube.com/watch?v=ximj9QWle-g

* https://github.com/siddhardhan23/gemini-pro-streamlit-chatbot