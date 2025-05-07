Adding **youtube summarizing** capabilities to the MultiChat:

* https://github.com/JAlcocerT/phidata
* https://jalcocert.github.io/JAlcocerT/summarize-yt-videos/

```sh
streamlit run app_v3.py
```

---



```sh
#python -m venv solvingerror_venv #create the venv
python3 -m venv ytgroq_venv #create the venv

#solvingerror_venv\Scripts\activate #activate venv (windows)
source ytgroq_venv/bin/activate #(linux)
```

**Install dependencies** with:

```sh
pip install -r requirements.txt #all at once
#pip freeze | grep langchain

#pip show beautifulsoup4
pip list
pip freeze > requirements-output.txt #generate a txt with the ones you have!
```

```sh
source .env

#export OPENAI_API_KEY="your-api-key-here"
#set OPENAI_API_KEY=your-api-key-here
#$env:OPENAI_API_KEY="your-api-key-here"
echo $OPENAI_API_KEY
```