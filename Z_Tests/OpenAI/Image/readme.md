* https://platform.openai.com/docs/guides/images?api-mode=responses

* https://jalcocert.github.io/JAlcocerT/ai-vision-models/


```sh
python3 scraping-ask-v2.py https://www.viviendasylocalesgranada.com/ficha/chalet/otura/urbanizacion-los-alijares/4348/13194834/es/ "What are your general comments about this property based on the images?" > comments_property_alijares.mdx
```

---

```sh
#python -m venv solvingerror_venv #create the venv
python3 -m venv openaimg_venv #create the venv

#openaimg_venv\Scripts\activate #activate venv (windows)
source openaimg_venv/bin/activate #(linux)
```

**Install dependencies** with:

```sh
#pip install beautifulsoup4 openpyxl pandas numpy==2.0.0
pip install -r requirements.txt #all at once
#pip freeze | grep langchain

#pip show beautifulsoup4
pip list
#pip freeze > requirements_output.txt #generate a txt with the ones you have!
```

```sh
source .env

#export OPENAI_API_KEY="your-api-key-here"
#set OPENAI_API_KEY=your-api-key-here
#$env:OPENAI_API_KEY="your-api-key-here"
echo $OPENAI_API_KEY
```