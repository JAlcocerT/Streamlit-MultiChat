
* https://github.com/JAlcocerT/Streamlit-AIssistant/tree/main/Z_Tests/Grok_API

* https://jalcocert.github.io/JAlcocerT/how-to-use-grok-api
* https://pypi.org/project/xai-sdk/

```sh
pip install xai-sdk
```


```sh
curl https://api.x.ai/v1/chat/completions \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $XAI_API_KEY" \
-d '{
  "messages": [
    {
      "role": "system",
      "content": "You are a test assistant."
    },
    {
      "role": "user",
      "content": "Testing. Which model are you?."
    }
  ],
  "model": "grok-2-latest",
  "stream": false,
  "temperature": 0
}'
```