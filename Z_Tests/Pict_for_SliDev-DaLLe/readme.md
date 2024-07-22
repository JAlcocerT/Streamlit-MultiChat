* https://platform.openai.com/docs/guides/images/usage?context=python

```sh
export OPENAI_API_KEY=your-api-key-here
set OPENAI_API_KEY="your-api-key-here"
```

* Get it from the server with:

```sh
sftp serveruser@192.168.3.200
get /home/serveruser/dalle/generated_image22.png C:\Users\desktopuser\Desktop\Streamlit-MultiChat\Z_Tests\generated_image.png
```

* Or with:

```sh
python3 -m http.server 8000

Invoke-WebRequest -Uri http://192.168.3.200:8000/generated_image22.png -OutFile C:\Users\Jesus_Alcocer\Desktop\Streamlit-MultiChat\Z_Tests\generated_image22.png


curl http://192.168.3.200:8000/generated_image22.png --output C:\Users\Jesus_Alcocer\Desktop\Streamlit-MultiChat\Z_Tests\generated_image.png
```