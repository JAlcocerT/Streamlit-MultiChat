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

Build your own Image:

```sh
#docker build -t streamlitmultichat .
#docker run -p 8501:8501 -v ai_streamlit_multichat:/app --name streamlitmultichat streamlitmultichat:latest /bin/sh -c "cd /app && streamlit run streamlit-multichat.py"
#podman run -p .....
```