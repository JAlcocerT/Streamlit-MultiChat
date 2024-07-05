<div align="center">
  <h1>Streamlit-MultiChat</h1>
</div>

Use commercial models: OpenAI / Anthropic / Open and Local LLMs with one Streamlit Web App.
<div align="center" style="line-height: 1;">
  <a href="https://github.com/JAlcocerT/Streamlit-MultiChat?tab=GPL-3.0-1-ov-file" style="margin: 2px;">
    <img alt="Code License" src="https://img.shields.io/badge/License-GPLv3-blue.svg" style="display: inline-block; vertical-align: middle;"/>
  </a>

  <a href="https://github.com/JAlcocerT/Streamlit-MultiChat/actions/workflows/streamlit_GH_Actions.yml" style="margin: 2px;">
    <img alt="Model License" src="https://github.com/JAlcocerT/Streamlit-MultiChat/actions/workflows/streamlit_GH_Actions.yml/badge.svg" style="display: inline-block; vertical-align: middle;"/>
  </a>
</div>

[![GitHub release](https://img.shields.io/github/release/xmrig/xmrig-proxy/all.svg)](https://github.com/xmrig/xmrig-proxy/releases)
[![GitHub Release Date](https://img.shields.io/github/release-date-pre/xmrig/xmrig-proxy.svg)](https://github.com/xmrig/xmrig-proxy/releases)

## Getting Started 

<details>
  <summary>Clone and Run 👇</summary>
  &nbsp;

Try the Project quickly with [Python Venv's](https://fossengineer.com/python-dependencies-for-ai/):

```sh
git clone https://github.com/JAlcocerT/Streamlit-MultiChat
python -m venv multichat #create the venv

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


<div align="center">
  <img src="streamlit-multichat.png" alt="MultiChat" style="width:100%;"/>
  <p><em>Chat with Several Models with Streamlit</em></p>
</div>

---

## Thanks to ❤️

Projects I got inspiration from / consolidated in this App were [tested here](https://github.com/JAlcocerT/Streamlit-MultiChat/tree/main/Z_Tests):

* https://github.com/dataprofessor/openai-chatbot

* https://github.com/AIDevBytes/Streamlit-Ollama-Chatbot

* https://github.com/tonykipkemboi/groq_streamlit_demo -> Groq + Streamlit Chat

* https://github.com/TirendazAcademy/Streamlit-Tutorials/blob/main/Blog-Generator-App-with-Claude-API/app.py
* https://www.youtube.com/watch?v=ximj9QWle-g

* https://github.com/siddhardhan23/gemini-pro-streamlit-chatbot