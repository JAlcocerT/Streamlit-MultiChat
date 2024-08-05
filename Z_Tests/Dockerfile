FROM python:3.10.12-slim
#https://hub.docker.com/_/python

# LABEL org.opencontainers.image.source https://github.com/JAlcocerT/Streamlit-MultiChat
# LABEL maintainer="Jesus Alcocer Tagua"

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME

#COPY . ./

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    nano \
    g++ 
    # \
    # && rm -rf /var/lib/apt/lists/*

# Install Miniconda
RUN curl -Lo miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && sh miniconda.sh -b -p /miniconda \
    && rm miniconda.sh

ENV PATH=/miniconda/bin:${PATH}    

# Install production dependencies.
#RUN pip install -r requirements.txt

EXPOSE 8501

# docker build -t py_test .
# podman build -t py_test .