<div align="center">
  <h1>Streamlit-MultiChat</h1>
</div>

<div align="center">
  <h3>Many LLMs - One Streamlit Web App</h3>
</div>

<div align="center">
  <h4>OpenAI | Anthropic | Ollama | Groq</h3>
</div>


<div align="center">
  <a href="https://github.com/JAlcocerT/Streamlit-MultiChat?tab=GPL-3.0-1-ov-file" style="margin-right: 5px;">
    <img alt="Code License" src="https://img.shields.io/badge/License-GPLv3-blue.svg" />
  </a>
  <a href="https://github.com/JAlcocerT/Streamlit-MultiChat/actions/workflows/Streamlit_GHA_MultiArch.yml" style="margin-right: 5px;">
    <img alt="GH Actions Workflow" src="https://github.com/JAlcocerT/Streamlit-MultiChat/actions/workflows/Streamlit_GHA_MultiArch.yml/badge.svg" />
  </a>

  <a href="https://www.python.org/downloads/release/python-312">
    <img alt="Python Version" src="https://img.shields.io/badge/python-3.12-blue.svg" />
  </a>
</div>

<div align="center">

[![GitHub Release](https://img.shields.io/github/release/JAlcocerT/Streamlit-MultiChat/all.svg)](https://github.com/JAlcocerT/Streamlit-MultiChat/releases)
[![GitHub Release Date](https://img.shields.io/github/release-date-pre/JAlcocerT/Streamlit-MultiChat.svg)](https://github.com/JAlcocerT/Streamlit-MultiChat/releases)

</div>

<p align="center">

  <a href="https://youtube.com/@JAlcocerTech">
    <img alt="YouTube Channel" src="https://img.shields.io/badge/YouTube-Channel-red" />
  </a>
  <a href="https://GitHub.com/JAlcocerT/Streamlit-MultiChat/graphs/commit-activity" style="margin-right: 5px;">
    <img alt="Maintained" src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" />
  </a>
  <a href="https://github.com/JAlcocerT/Streamlit-MultiChat">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/JAlcocerT/Streamlit-MultiChat" />
  </a>
  <a href="https://github.com/JAlcocerT/Streamlit-MultiChat">
    <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/JAlcocerT/Streamlit-MultiChat" />
  </a>
</p>

A custom Streamlit Web App to Chat with the latest LLMs and get a *per use cost* instead of a fixed monthly price.



## Features

Use **many large language models**: OpenAI, Anthropic, Open / Local LLM's with **one Streamlit Web App**.

* LLM Support
  * Ollama - Open Source Models
  * OpenAI - GPT 3.5 / GPT4 / GPT4o / GPT4o-mini
  * Anthropic - Claude 3 (Opus / Sonnet) / Claude 3.5
  * Groq API - LlaMa models using quick LPU inference
* Extended explanation
  * [**SliDev presentation** of the Streamlit-MultiChat](https://jalcocert.github.io/Streamlit-MultiChat/1)
  * [This **blog post** →](https://jalcocert.github.io/JAlcocerT/create-streamlit-chatgpt/#a-multichat-with-streamlit)
  * Deploy as per [Z_DeployMe](https://github.com/JAlcocerT/Streamlit-MultiChat/tree/main/Z_DeployMe)

During the process, I also explored: [SliDev PPTs](https://github.com/JAlcocerT/Streamlit-MultiChat/tree/main/slidev), [ScrapeGraph](https://github.com/JAlcocerT/Streamlit-MultiChat/blob/main/Z_Tests/ScrapeGraph/test_scrapegraph_stv2.py), [DaLLe](https://github.com/JAlcocerT/Streamlit-MultiChat/tree/main/Z_Tests/Pict_for_SliDev-DaLLe), [Streamlit Auth](https://github.com/JAlcocerT/Streamlit-MultiChat/tree/main/Z_Tests/Auth_sqlite) and [OpenAI as Custom Agents](https://github.com/JAlcocerT/Streamlit-MultiChat/tree/main/Z_Tests/OpenAI)

## Getting Started 

[The Project is documented **here** →](https://jalcocert.github.io/JAlcocerT/create-streamlit-chatgpt/)



> [!IMPORTANT]
> You have few alternatives to run this project locally:

```sh
uv sync #as per pyproject.toml
cp ./streamlit/secrets_sample.toml ./streamlit/secrets.toml #add your APIs
uv run streamlit run Z_multichat.py
```


<details>
  <summary>Clone the repository and Run with your API keys 👇</summary>
  &nbsp;

  * OpenAI API Keys - <https://platform.openai.com/api-keys>
  * Anthropic - <https://console.anthropic.com/settings/keys>
  * Groq - <https://console.groq.com/keys>
  * For Ollama, you need [this setup](https://fossengineer.com/selfhosting-llms-ollama/)

Try the Project quickly with [**Python Venv's**](https://fossengineer.com/python-dependencies-for-ai/):


1. Get [Python Installed](https://jalcocert.github.io/JAlcocerT/guide-python/#installing-python-)
2. Prepare a [Venv](https://jalcocert.github.io/JAlcocerT/useful-python-stuff/#python-apps-reliability)

```sh
git clone https://github.com/JAlcocerT/Streamlit-MultiChat
#python -m venv multichat_venv #create the venv
python3 -m venv multichat_venv #linux

#multichat_venv\Scripts\activate #activate venv (windows)
source multichat_venv/bin/activate #(linux)
```

Then, provide the API Keys and run the Streamlit Web App:

```sh
#uv pip install -r requirements.txt
pip install -r requirements.txt #all at once, ~2min
#pip freeze > requirements-output.txt

cp ./.streamlit/secrets_sample.toml ./.streamlit/secrets.toml #fill the API Keys
#streamlit run Z_multichat.py
streamlit run Z_multichat_Auth.py
```

* Make sure to have [Ollama ready](https://fossengineer.com/selfhosting-llms-ollama/) and running your desired model!
* Prepare the **API Keys** in any of:
    * .streamlit/secrets.toml
    * As Environment Variables
        * Linux - `export OPENAI_API_KEY="YOUR_API_KEY"`
        * CMD - `set OPENAI_API_KEY=YOUR_API_KEY`
        * PS - `$env:OPENAI_API_KEY="YOUR_API_KEY"`
        * In the [Docker-Compose](https://github.com/JAlcocerT/Streamlit-MultiChat/tree/main/Z_DeployMe)
    * Through the Streamlit UI
</details>


<div align="center">
  <img src="streamlit-multichat.png" alt="MultiChat" style="width:100%;"/>
  <p><em>Chat with Several Models with Streamlit</em></p>
</div>

* **Alternatively** - Use the [Docker Image](https://github.com/JAlcocerT/Streamlit-MultiChat/pkgs/container/streamlit-multichat)

```sh
docker pull ghcr.io/jalcocert/streamlit-multichat:latest #x86/ARM64
make up #downloads and configures the docker-compose
```

> You will need [Docker](https://jalcocert.github.io/JAlcocerT/docs/dev/dev-interesting-it-concepts/#containers) ready. And *optionally [Portainer](https://fossengineer.com/selfhosting-portainer-docker/)*

---

## Thanks to ❤️

Projects I got inspiration from / consolidated in this App were [tested here](https://github.com/JAlcocerT/Streamlit-MultiChat/tree/main/Z_Tests): `./Z_Tests`

<details>
  <summary>Check the Projects 👈</summary>
  &nbsp;

* https://github.com/dataprofessor/openai-chatbot

* https://github.com/AIDevBytes/Streamlit-Ollama-Chatbot

* https://github.com/tonykipkemboi/groq_streamlit_demo -> Groq + Streamlit Chat

* https://github.com/TirendazAcademy/Streamlit-Tutorials/blob/main/Blog-Generator-App-with-Claude-API/app.py
  * https://www.youtube.com/watch?v=ximj9QWle-g

* https://github.com/siddhardhan23/gemini-pro-streamlit-chatbot

</details>

<div align="center">
  <a href="https://ko-fi.com/Z8Z1QPGUM">
    <img src="https://ko-fi.com/img/githubbutton_sm.svg" alt="ko-fi">
  </a>
</div>