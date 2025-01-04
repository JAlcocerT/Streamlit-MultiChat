from openai import OpenAI
#https://platform.openai.com/docs/guides/speech-to-text

import os
from dotenv import load_dotenv

load_dotenv()
# Initialize OpenAI client
#client = openai.OpenAI()
client = OpenAI()


# Path to the file containing the transcribed text
input_file_path = "transcription.txt"
speech_file_path = "OpenAI_API_Audio_from_Text.mp3"

# Read the contents of the file
with open(input_file_path, "r") as file:
    input_text = file.read()

# Use OpenAI's API to convert the text to speech
response = client.audio.speech.create(
    model="tts-1",         # specify the TTS model
    voice="onyx",          # specify the voice
    input=input_text       # use the text read from the file
)

# Save the speech to a file
response.stream_to_file(speech_file_path)


# import openai

# client = openai.OpenAI()
# speech_file_path = "Cloudflare.mp3"
# response = client.audio.speech.create(
#     model="tts-1",
#     voice="onyx",
#     input="Let me know in the comments which workloads you cant wait to monitor with Netdata."
# )
# response.stream_to_file(speech_file_path)