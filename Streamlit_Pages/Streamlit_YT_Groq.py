import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv

from Z_Tests.PhiData.phi.tools.youtube_tools import YouTubeTools
from Z_Tests.PhiData.assistant import get_chunk_summarizer, get_video_summarizer

# from phidata.utils.youtube import YouTubeTools
# from phidata.llm.groq import GroqChatCompletion
# import streamlit as st
# import os
# from groq import Groq
# from dotenv import load_dotenv

# Dummy imports for this example, replace by your actual implementations
# from your_module import YouTubeTools, get_video_summarizer, get_chunk_summarizer

def get_available_groq_models_from_env():
    load_dotenv()
    model_string = os.getenv("AVAILABLE_LLM_MODELS")
    return [model.strip() for model in model_string.split(',')] if model_string else None

def page_six():
    st.title("Youtube Video Summaries 🎥")

    with st.sidebar:
        st.title('🔑 Groq API Key')
        groq_api_key = os.getenv("GROQ_API_KEY")
        api_key_provided = False

        if 'GROQ_API_KEY' in st.secrets and len(st.secrets['GROQ_API_KEY']) > 30:
            st.success('API key already provided via Streamlit secrets!', icon='✅')
            #groq_client = Groq(api_key=st.secrets['GROQ_API_KEY'])
            api_key_provided = True
        elif groq_api_key and len(groq_api_key) > 30:
            st.success('API key already provided via .env or environment variables!', icon='✅')
            #groq_client = Groq(api_key=groq_api_key)
            api_key_provided = True
        else:
            groq_api_key_input = st.text_input('Enter your Groq API Key:', type='password', key="groq_api_key_input")
            if groq_api_key_input.startswith('gsk') and len(groq_api_key_input) > 30:
                st.success('Groq API Key provided!', icon='✅')
                #groq_client = Groq(api_key=groq_api_key_input)
                api_key_provided = True
            else:
                st.warning('Please enter your Groq API Key.', icon='⚠️')
                #groq_client = None

    available_models_env = get_available_groq_models_from_env()
    model_list = available_models_env if available_models_env else ["llama3-70b-8192", "llama3-8b-8192", "mixtral-8x7b-32768"]

    llm_model = st.selectbox(
        'Choose the Groq model:',
        model_list,
        index=0 if "llama3-70b-8192" in model_list else 0,
        key="llm_model_select"
    )

    chunker_limit = st.sidebar.slider(
        ":heart_on_fire: Words in chunk", 1000, 10000, 4500, 500,
        help="Set the number of words to chunk the text into.",
        key="chunker_slider"
    )

    video_url = st.sidebar.text_input(":video_camera: Video URL", key="video_url_input")
    generate_report = st.sidebar.button("Generate Summary", key="generate_button")

    st.sidebar.markdown("---")
    st.sidebar.markdown("##### Powered by Groq & YouTube")
    if st.sidebar.button("Restart", key="restart_button"):
        st.session_state.pop("youtube_url", None)
        st.rerun()

    ### ---- Insert your logic here ---- ###
    if api_key_provided and generate_report and video_url:
        st.session_state["youtube_url"] = video_url

    st.sidebar.markdown("##### Forked with :orange_heart: from [phidata](https://github.com/JAlcocerT/phidata)")

    if "youtube_url" in st.session_state:
        _url = st.session_state["youtube_url"]
        youtube_tools = YouTubeTools(languages=["en"])  # you should define YouTubeTools
        video_captions = None
        video_summarizer = get_video_summarizer(model=llm_model)  # you should define this

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
            chunks.append(" ".join(words[i:(i + chunker_limit)]))

        if num_chunks > 1:
            chunk_summaries = []
            for i in range(num_chunks):
                with st.status(f"Summarizing chunk: {i+1}", expanded=False) as status:
                    chunk_summary = ""
                    chunk_container = st.empty()
                    chunk_summarizer = get_chunk_summarizer(model=llm_model)  # you should define this
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