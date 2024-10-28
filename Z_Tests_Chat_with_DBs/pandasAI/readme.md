* PandasAI works for me with Python 3.10

```sh
python -m venv pandasaidb #create the venv
pandasaidb\Scripts\activate #activate venv (windows)
source pandasaidb/bin/activate #(linux)
pip install pandasai==2.0.37 openpyxl langchain_groq langchain_community
```

```sh
export GROQ_API_KEY=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
$env:GROQ_API_KEY="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"
set GROQ_API_KEY=YOUR_API_KEY
```