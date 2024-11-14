## Deploy Streamlit MultiChat

<div align="center" style="line-height: 1;">
  <a href="https://opensource.org/license/gpl-3-0" style="margin: 2px;">
    <img alt="Code License" src="https://img.shields.io/badge/License-GPLv3-blue.svg" style="display: inline-block; vertical-align: middle;"/>
  </a>


</div>

[![GitHub release](https://img.shields.io/github/release/xmrig/xmrig-proxy/all.svg)](https://github.com/xmrig/xmrig-proxy/releases)
[![GitHub Release Date](https://img.shields.io/github/release-date-pre/xmrig/xmrig-proxy.svg)](https://github.com/xmrig/xmrig-proxy/releases)

Clone the repository and use the **Docker-Compose with your credentials**.

1. Get your **APIs Keys**
  * https://console.anthropic.com/workbench/
  * https://console.groq.com/keys
  * https://platform.openai.com/api-keys

2. Pull the container image

```sh
docker pull ghcr.io/jalcocert/streamlit-multichat:latest
```
3. Use the docker compose of this folder
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

```sh
#git clone https://github.com/JAlcocerT/Streamlit-MultiChat
#cd Streamlit-MultiChat

#docker build -t streamlitmultichat .
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

* Why would I want to build it?
  * You want to run it on a different architecture (Any other SBC: ARM32, ...)
  * You want to build the image from the source, because why not