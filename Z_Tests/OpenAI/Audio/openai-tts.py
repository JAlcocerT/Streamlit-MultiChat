#https://platform.openai.com/docs/models/gpt-4o-mini-tts
#https://platform.openai.com/docs/models/gpt-4o-mini-tts


#cd Z_Tests/OpenAI/Audio/
#python3 openai-tts.py
#sox -r 24000 -b 16 -e signed-integer -c 1 -t raw audio_reply.pcm audio_reply.wav

#https://jalcocert.github.io/JAlcocerT/photo-video-tinkering/#shorts

import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get the OpenAI API key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")

import asyncio
from openai import AsyncOpenAI

openai = AsyncOpenAI()

#input_text = """Ah, you got a package gone missing, huh? Sounds like trouble. Lemme see what I can dig up."""
file_path = "yt.md"

# Read the text content from the file
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        input_text = file.read()
    print(f"Successfully read text from '{file_path}'.")
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
    input_text = None  # Or provide a default value
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
    input_text = None  # Or provide a default value

instructions_text = """Affect: a mysterious noir detective\n\nTone: Cool, detached, but subtly reassuring—like they've seen it all and know how to handle a missing package like it's just another case.\n\nDelivery: Slow and deliberate, with dramatic pauses to build suspense, as if every detail matters in this investigation.\n\nEmotion: A mix of world-weariness and quiet determination, with just a hint of dry humor to keep things from getting too grim.\n\nPunctuation: Short, punchy sentences with ellipses and dashes to create rhythm and tension, mimicking the inner monologue of a detective piecing together clues."""

async def main() -> None:
    output_file = "audio_reply.pcm"  # You can change the filename and extension

    async with openai.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="echo", #onyx
        ##onyx #coral #CHANGE THE VOICE HERE! #🎭 OpenAI TTS voices (alloy, ash, ballad, coral, echo, fable, onyx, nova, sage, shimmer, verse)
        input=input_text,
        instructions=instructions_text,
        response_format="pcm",
    ) as response:
        with open(output_file, "wb") as f:
            async for chunk in response.iter_bytes():  # Changed aiter_bytes() to iter_bytes()
                f.write(chunk)

    print(f"Audio saved to {output_file}")

if __name__ == "__main__":
    asyncio.run(main())

#python3 pyopen.py > output.mdx

# import os
# from dotenv import load_dotenv

# # Load environment variables from the .env file
# load_dotenv()

# # Get the OpenAI API key from the environment variables
# api_key = os.getenv("OPENAI_API_KEY")

# import asyncio

# from openai import AsyncOpenAI
# from openai.helpers import LocalAudioPlayer

# openai = AsyncOpenAI()

# input = """Ah, you got a package gone missing, huh? Sounds like trouble. Lemme see what I can dig up.\n\nI'm chasing a trail of numbers through the system. There it is—shipped two days ago, supposed to land on your doorstep by noon today. But… it's still out there. Somewhere.\n\nMaybe it's stuck at a warehouse, maybe it took a wrong turn down a dark alley. Either way, I'll get to the bottom of it. I'll send you the latest update, and if it doesn't show up soon… well, I'll make some calls.\n\nYou sit tight, kid. I'll keep an eye on it."""

# instructions = """Affect: a mysterious noir detective\n\nTone: Cool, detached, but subtly reassuring—like they've seen it all and know how to handle a missing package like it's just another case.\n\nDelivery: Slow and deliberate, with dramatic pauses to build suspense, as if every detail matters in this investigation.\n\nEmotion: A mix of world-weariness and quiet determination, with just a hint of dry humor to keep things from getting too grim.\n\nPunctuation: Short, punchy sentences with ellipses and dashes to create rhythm and tension, mimicking the inner monologue of a detective piecing together clues."""

# async def main() -> None:

#     async with openai.audio.speech.with_streaming_response.create(
#         model="gpt-4o-mini-tts",
#         voice="coral",
#         input=input,
#         instructions=instructions,
#         response_format="pcm",
#     ) as response:
#         await LocalAudioPlayer().play(response)

# if __name__ == "__main__":
#     asyncio.run(main())