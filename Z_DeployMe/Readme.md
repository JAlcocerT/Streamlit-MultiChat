## Deploy Streamlit MultiChat


* [The Project is documented **here** →](https://jalcocert.github.io/JAlcocerT/create-streamlit-chatgpt/)
* [See more **AI Projects** (with Docker) **here** →](https://github.com/JAlcocerT/Docker/tree/main/AI_Gen/Project_MultiChat)
* GHCR Package: <https://github.com/JAlcocerT/Streamlit-MultiChat/pkgs/container/streamlit-multichat>

<div align="center">

[![GitHub Release](https://img.shields.io/github/release/JAlcocerT/Streamlit-MultiChat/all.svg)](https://github.com/JAlcocerT/Streamlit-MultiChat/releases)
[![GitHub Release Date](https://img.shields.io/github/release-date-pre/JAlcocerT/Streamlit-MultiChat.svg)](https://github.com/JAlcocerT/Streamlit-MultiChat/releases)

</div>

> Using [Github Actions](https://fossengineer.com/docker-github-actions-cicd/) with [MultiArch Images](https://jalcocert.github.io/JAlcocerT/create-streamlit-chatgpt/#conclusion---and-what-i-learnt)


Clone the repository and use the **Docker-Compose with your API credentials**.

The **architectures** supported by this **container image** are:

| Architecture | Available | Tag |
| :----: | :----: | ---- |
| x86-64 | ✅ | Multi-Arch |
| arm64 | ✅ | Multi-Arch |
| armhf | N/A | Not Supported |

1. Get your **APIs Keys**

* https://console.anthropic.com/workbench/
* https://console.groq.com/keys
* https://platform.openai.com/api-keys
* [Deploy Ollama](https://fossengineer.com/selfhosting-llms-ollama/)

2. Pull the **container image**

```sh
docker pull ghcr.io/jalcocert/streamlit-multichat #:v1.1  #:latest
```
3. Get [docker ready](https://jalcocert.github.io/JAlcocerT/docs/dev/dev-interesting-it-concepts/#containers) and Use the **docker compose** of this folder:

```sh
git clone https://github.com/JAlcocerT/Streamlit-MultiChat

cd Z_DeployMe
#input your API credentials in the command part of the docker-compose (or through the UI)
docker-compose up -d
```

By default, it will use the Docker Image built with GH Actions and [available at ghcr](https://github.com/JAlcocerT/Streamlit-MultiChat/pkgs/container/streamlit-multichat)

> Go to `localhost:8501` to interact with the bots via Streamlit UI

### Optional

By default, Im using **buildx to create ARM64 and x86** images, but you can Build your own Image:


<details>
  <summary>Why would I want to build it? 👇</summary>
  &nbsp;


* You want to run it on a different architecture
* You want to build the image from the source, because why not

</details>

```sh
git clone https://github.com/JAlcocerT/Streamlit-MultiChat
cd Streamlit-MultiChat

docker build -t streamlitmultichat .
#cd Z_DeployMe
#docker-compose up -d

# docker run -d \
#   --name streamlit_multichat \
#   -v ai_streamlit_multichat:/app \
#   -w /app \
#   -p 8501:8501 \
#   streamlitmultichat \
#   /bin/sh -c "mkdir -p /app/.streamlit && \
#               echo 'OPENAI_API_KEY = \"sk-proj-openaiAPIhere\"' > /app/.streamlit/secrets.toml && \
#               echo 'GROQ_API_KEY = \"gsk_groqAPIhere\"' >> /app/.streamlit/secrets.toml && \
#               streamlit run Z_multichat.py"

# podman run -d --name=phidata_yt_groq -p 8502:8501 -e GROQ_API_KEY=your_api_key_here streamlitmultichat tail -f /dev/null
```

Once built, your image will be visible: `docker images`