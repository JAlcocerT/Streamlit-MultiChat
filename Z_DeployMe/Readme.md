## Deploy Streamlit MultiChat

Clone the repository and use the Docker-Compose with your credentials:

```sh
git clone https://github.com/JAlcocerT/Streamlit-MultiChat

cd Z_DeployMe
#input your API credentials in the command part of the docker-compose (or through the UI)
docker-compose up -d
```

By default, it will use the Docker Image built with GH Actions and [available at ghcr](https://github.com/JAlcocerT/Streamlit-MultiChat/pkgs/container/streamlit-multichat)

> Go to `localhost:8501` to interact with the bots via Streamlit UI

### Optional

By default, Im using buildx to create ARM64 and x86 images, but you can Build your own Image:

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

#podman run -p .....
```

Why would I want to build it?

* You want to run it on a Raspberry Pi (Any other SBC, ARM architecture)
* You want to build the image from the source, because why not