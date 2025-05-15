import streamlit as st
from streamlit_webrtc import webrtc_streamer
import io
from pydub import AudioSegment  # Requires ffmpeg to be installed
#pip install pydub

def save_audio_as_mp3(audio_bytes, filename="recorded_audio.mp3"):
    try:
        audio_segment = AudioSegment.from_wav(io.BytesIO(audio_bytes))
        audio_segment.export(filename, format="mp3")
        return True, filename
    except Exception as e:
        return False, str(e)

audio_value = st.audio_input("Record a voice message")

if audio_value:
    st.audio(audio_value)  # Display the recorded audio

    if st.button("Save as MP3"):
        success, message = save_audio_as_mp3(audio_value.getvalue())
        if success:
            st.success(f"Audio saved as: {message}")
            with open(message, "rb") as f:
                st.download_button(
                    label="Download MP3",
                    data=f,
                    file_name="recorded_audio.mp3",
                    mime="audio/mp3",
                )
        else:
            st.error(f"Error saving as MP3: {message}")