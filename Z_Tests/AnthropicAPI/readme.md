> It all started during streamlit multichat...

[The Test is documented **here** →](https://jalcocert.github.io/JAlcocerT/how-to-use-lite-llm/#anthropic)


* https://github.com/JAlcocerT/Streamlit-MultiChat/blob/main/Z_Tests/streamlit_anthropic2.py


```sh
python3 -m venv Z_AnthropicTests_venv

#Unix
source Z_AnthropicTests_venv/bin/activate
#.\Z_AnthropicTests_venv\Scripts\activate #Windows

pip install -r requirements.txt


source .env
#export GROQ_API_KEY="your-api-key-here"
#set GROQ_API_KEY=your-api-key-here
#$env:GROQ_API_KEY="your-api-key-here"
echo $GROQ_API_KEY $OPENAI_API_KEY $ANTHROPIC_API_KEY

python3 anthropic_api_test.py

# git add .
# git commit -m "better st offer analyzer"
# git push
```