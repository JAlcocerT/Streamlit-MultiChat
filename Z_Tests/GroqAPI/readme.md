```sh
pip install groq==0.13.1
#https://www.youtube.com/watch?v=WaRjHz9ErO4
```

> https://console.groq.com/keys

---

## Venv Setup


```sh
python3 -m venv TestGroqAPI_venv

#Unix
source TestGroqAPI_venv/bin/activate
#.\TestGroqAPI_venv\Scripts\activate #Windows

pip install -r requirements.txt

source .env
#export GROQ_API_KEY="your-api-key-here"
#set GROQ_API_KEY=your-api-key-here
#$env:GROQ_API_KEY="your-api-key-here"
echo $GROQ_API_KEY

python3 groq_api_query.py
```

See all **[models available](https://jalcocert.github.io/JAlcocerT/how-to-use-lite-llm/) via Groq API** with:

```sh
curl https://api.groq.com/openai/v1/models \
-H "Authorization: Bearer $GROQ_API_KEY"
```