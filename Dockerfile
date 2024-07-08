FROM python:3.12.4-slim  
#https://hub.docker.com/_/python

LABEL org.opencontainers.image.source https://github.com/JAlcocerT/Streamlit-MultiChat
LABEL maintainer="Jesus Alcocer Tagua"

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME

COPY . ./

# RUN apt-get update && apt-get install -y \
#     build-essential \
#     curl \
#     software-properties-common \
#     git \
#     && rm -rf /var/lib/apt/lists/*

# Install production dependencies.
RUN pip install -r requirements.txt

EXPOSE 8501