
FROM python:3.10-slim

# Install git
RUN apt-get update && apt-get install -y git nano

# Set up the working directory
WORKDIR /app

# Clone the repository
#RUN git clone https://github.com/JAlcocerT/openai-chatbot

#WORKDIR /openai-chatbot

# Install Python requirements
#RUN pip install -r requirements.txt

# Set the entrypoint to a bash shell
CMD ["/bin/bash"]