FROM python:3.11  
#https://hub.docker.com/_/python

# LABEL org.opencontainers.image.source https://github.com/JAlcocerT/Streamlit-MultiChat
# LABEL maintainer="Jesus Alcocer Tagua"

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME

COPY . ./


RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    nano \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages
RUN pip install scrapegraphai==0.9.0b7 \
    nest_asyncio \
    playwright

# Run Playwright commands to install browser dependencies and browsers
RUN playwright install-deps \
    && playwright install

EXPOSE 8501


###podman build -t scrapegraph_cont:latest .
#docker build -t scrapegraph_cont:latest .