> [Post](https://jalcocert.github.io/JAlcocerT/how-to-use-openai-function-calling/)



---


## Setup

```sh
#python -m venv openaifcall_venv #create the venv
python3 -m venv openaifcall_venv #create the venv

#openaifcall_venv\Scripts\activate #activate venv (windows)
source openaifcall_venv/bin/activate #(linux)
```

**Install dependencies** with:

```sh
#pip install beautifulsoup4 openpyxl pandas numpy==2.0.0
pip install -r requirements.txt #all at once
#pip freeze | grep langchain

#pip show beautifulsoup4
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