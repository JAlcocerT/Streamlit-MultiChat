* https://github.com/daveebbelaar/langchain-experiments/tree/main/openai-functions


---

## Venv Setup for OpenAI Testing

* https://jalcocert.github.io/JAlcocerT/useful-python-stuff/

```sh
python -m venv openaiapi_venv #create the venv
python3 -m venv openaiapi_venv #create the venv

#openaiapi_venv\Scripts\activate #activate venv (windows)
source openaiapi_venv/bin/activate #(linux)
```

Install them with:

```sh
#pip install openai
pip install -r requirements.txt #all at once
#pip freeze | grep openai

pip show openai
pip list
#pip freeze > requirements.txt #generate a txt with the ones you have!
```

```sh
source .env

#export OPENAI_API_KEY="your-api-key-here"
#set OPENAI_API_KEY=your-api-key-here
#$env:OPENAI_API_KEY="your-api-key-here"
echo $OPENAI_API_KEY
```