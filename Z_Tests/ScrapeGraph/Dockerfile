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
RUN pip install -r requirements.txt

# RUN pip install scrapegraphai==0.9.0b7 \
#     streamlit==1.37.1 \
#     nest_asyncio \
#     playwright

# Run Playwright commands to install browser dependencies and browsers
RUN playwright install-deps \
    && playwright install

EXPOSE 8501


###podman build -t scrapegraph_st:latest .
#docker build -t scrapegraph_streamv2 .

#docker run -it --name my_scrapegraph_container scrapegraph_stream
#podman run -it --name my_scrapegraph_container scrapegraph_st:latest

#docker run -it --name my_scrapegraph_container scrapegraph_stream
#docker exec -it my_scrapegraph_container bash

#docker exec -it my_scrapegraph_container /bin/bash
#podman exec -it my_scrapegraph_container /bin/bash