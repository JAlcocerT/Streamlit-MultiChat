* https://jalcocert.github.io/JAlcocerT/photo-video-tinkering/#shorts

---

```sh
#git clone https://github.com/JAlcocerT/Streamlit-MultiChat
#python -m venv oaiaudio_venv #create the venv
python3 -m venv oaiaudio_venv #linux

#oaiaudio_venv\Scripts\activate #activate venv (windows)
source oaiaudio_venv/bin/activate #(linux)
```

Then, provide the API Keys and run the scripts:

```sh
#uv pip install -r requirements.txt
sudo apt install libportaudio2
pip install -r requirements.txt
#pip freeze > requirements-output.txt
python3 openai-tts.py

sox -r 24000 -b 16 -e signed-integer -c 1 -t raw audio_reply.pcm audio_reply.wav
#sox -r 24000 -b 16 -e signed-integer -c 1 -t raw audio_reply.pcm audio_reply.mp3
```