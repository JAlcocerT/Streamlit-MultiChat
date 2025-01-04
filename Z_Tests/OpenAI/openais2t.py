from openai import OpenAI
#https://platform.openai.com/docs/guides/speech-to-text

import os
from dotenv import load_dotenv

load_dotenv()

# # # Get the OpenAI API key from the environment variables
# # api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

audio_file= open("/home/jalcocert/Desktop/Streamlit-MultiChat/Z_Tests/OpenAI/OpenAI_API_Audio_from_Text.mp3", "rb")
transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file
)

print(transcription.text)

text_to_write = transcription.text

# Open the text file in write mode ('w') and write the content
with open("transcription_speech2text.txt", "w") as text_file:
  text_file.write(text_to_write)

print("Transcription written to transcription_speech2text.txt")