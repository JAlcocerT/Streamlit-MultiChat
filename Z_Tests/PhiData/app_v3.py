import streamlit as st

from phi.tools.youtube_tools import YouTubeTools
from assistant import get_chunk_summarizer, get_video_summarizer  # type: ignore

#from Z_Functions import Auth_functions as af
import Auth_functions as af

# Load environment variables from .env file
from dotenv import load_dotenv
import os
load_dotenv()  # This loads all environment variables from the .env file

st.set_page_config(
    page_title="Youtube Video Summaries",
    page_icon=":orange_heart:",
)
st.title("Youtube Video Summaries 🎥")
# st.markdown("##### :orange_heart: built using [phidata](https://github.com/phidatahq/phidata)")


from groq import Groq

# Load environment variables (already done above, but for clarity if this snippet is used alone)
load_dotenv()

def get_available_groq_models_from_env():
    """
    Reads available Groq models from the AVAILABLE_LLM_MODELS environment variable.
    Returns a list of model names or None if the variable is not set.
    """
    model_string = os.getenv("AVAILABLE_LLM_MODELS")
    if model_string:
        return [model.strip() for model in model_string.split(',')]
    return None

def main() -> None:
    if af.login():

        # Get LLMs via Groq API or from .env
        available_models_env = get_available_groq_models_from_env()

        if available_models_env:
            llm_model = st.sidebar.selectbox(
                "Select Model", options=available_models_env
            )
        else:
            llm_model = st.sidebar.selectbox(
                "Select Model", options=["llama3-70b-8192", "llama3-8b-8192", "mixtral-8x7b-32768"],
                help="AVAILABLE_LLM_MODELS not found in .env, using default list."
            )
            st.sidebar.info(
                "To load models from .env, define a comma-separated list like:\n"
                "AVAILABLE_LLM_MODELS=llama3-70b-8192,llama3-8b-8192,mixtral-8x7b-32768"
            )

        # Set assistant_type in session state
        if "llm_model" not in st.session_state:
            st.session_state["llm_model"] = llm_model
        # Restart the assistant if assistant_type has changed
        elif st.session_state["llm_model"] != llm_model:
            st.session_state["llm_model"] = llm_model
            st.rerun()

        # Get chunker limit
        chunker_limit = st.sidebar.slider(
            ":heart_on_fire: Words in chunk",
            min_value=1000,
            max_value=10000,
            value=4500,
            step=500,
            help="Set the number of characters to chunk the text into.",
        )

        # Get video url
        video_url = st.sidebar.text_input(":video_camera: Video URL")
        # Button to generate report
        generate_report = st.sidebar.button("Generate Summary")
        if generate_report:
            st.session_state["youtube_url"] = video_url

        # st.sidebar.markdown("## Trending Videos")
        st.sidebar.markdown("##### Forked with :orange_heart: from [phidata](https://github.com/JAlcocerT/phidata)")

        if "youtube_url" in st.session_state:
            _url = st.session_state["youtube_url"]
            youtube_tools = YouTubeTools(languages=["en"])
            video_captions = None
            video_summarizer = get_video_summarizer(model=llm_model)

            with st.status("Parsing Video", expanded=False) as status:
                with st.container():
                    video_container = st.empty()
                    video_container.video(_url)

                video_data = youtube_tools.get_youtube_video_data(_url)
                with st.container():
                    video_data_container = st.empty()
                    video_data_container.json(video_data)
                status.update(label="Video", state="complete", expanded=False)

            with st.status("Reading Captions", expanded=False) as status:
                video_captions = youtube_tools.get_youtube_video_captions(_url)
                with st.container():
                    video_captions_container = st.empty()
                    video_captions_container.write(video_captions)
                status.update(label="Captions processed", state="complete", expanded=False)

            if not video_captions:
                st.write("Sorry could not parse video. Please try again or use a different video.")
                return

            chunks = []
            num_chunks = 0
            words = video_captions.split()
            for i in range(0, len(words), chunker_limit):
                num_chunks += 1
                chunks.append(" ".join(words[i : (i + chunker_limit)]))

            if num_chunks > 1:
                chunk_summaries = []
                for i in range(num_chunks):
                    with st.status(f"Summarizing chunk: {i+1}", expanded=False) as status:
                        chunk_summary = ""
                        chunk_container = st.empty()
                        chunk_summarizer = get_chunk_summarizer(model=llm_model)
                        chunk_info = f"Video data: {video_data}\n\n"
                        chunk_info += f"{chunks[i]}\n\n"
                        for delta in chunk_summarizer.run(chunk_info):
                            chunk_summary += delta  # type: ignore
                            chunk_container.markdown(chunk_summary)
                        chunk_summaries.append(chunk_summary)
                        status.update(label=f"Chunk {i+1} summarized", state="complete", expanded=False)

                with st.spinner("Generating Summary"):
                    summary = ""
                    summary_container = st.empty()
                    video_info = f"Video URL: {_url}\n\n"
                    video_info += f"Video Data: {video_data}\n\n"
                    video_info += "Summaries:\n\n"
                    for i, chunk_summary in enumerate(chunk_summaries, start=1):
                        video_info += f"Chunk {i}:\n\n{chunk_summary}\n\n"
                        video_info += "---\n\n"

                    for delta in video_summarizer.run(video_info):
                        summary += delta  # type: ignore
                        summary_container.markdown(summary)
            else:
                with st.spinner("Generating Summary"):
                    summary = ""
                    summary_container = st.empty()
                    video_info = f"Video URL: {_url}\n\n"
                    video_info += f"Video Data: {video_data}\n\n"
                    video_info += f"Captions: {video_captions}\n\n"

                    for delta in video_summarizer.run(video_info):
                        summary += delta  # type: ignore
                        summary_container.markdown(summary)
        else:
            st.write("Please provide a video URL or click on one of the trending videos.")

        st.sidebar.markdown("---")
        if st.sidebar.button("Restart"):
            st.rerun()


# main()

if __name__ == "__main__":
    main()