Testing [GPT4All](https://fossengineer.com/genai-with-python-gpt4all/)

<https://www.youtube.com/watch?v=GRvQ5u63GBk>


```py
#pip install gpt4all

#pip install gpt4all==1.0.0
#pip show gpt4all

#https://huggingface.co/TheBloke/orca_mini_3B-GGML/tree/main
#https://github.com/nomic-ai/gpt4all
#https://gpt4all.io/index.html
#https://github.com/nomic-ai/gpt4all/blob/main/gpt4all-bindings/python/README.md

#https://pypi.org/project/gpt4all/


from gpt4all import GPT4All

model = GPT4All("/home/.../orca-mini-3b.ggmlv3.q4_0.bin")
#model = GPT4All("./orca-mini-3b.ggmlv3.q4_0.bin")

#output = model.generate("The capital of France is ", max_tokens=3)
output = model.generate("what is a framework?", max_tokens=100)

print(output)
```


```py
from gpt4all import GPT4All
model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf", device='gpu') # device='amd', device='intel'
output = model.generate("The capital of France is ", max_tokens=3)
print(output)
```