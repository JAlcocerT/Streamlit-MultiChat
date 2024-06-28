import os
import requests
from bs4 import BeautifulSoup
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.llms import OpenAI
from langchain import PromptTemplate

#https://github.com/TirendazAcademy/LangChain-Tutorials/tree/main
#https://github.com/TirendazAcademy/LangChain-Tutorials/blob/main/Creating-a-Vector-Store.ipynb
#pip install -q langchain==0.2.0 openai==1.0.0 chromadb==0.4.8 tiktoken

#export OPENAI_API_KEY="YOUR_API_KEY"
os.environ["OPENAI_API_KEY"] = "..."

# URL of the Wikipedia page to scrape
url = 'https://en.wikipedia.org/wiki/Prime_Minister_of_the_United_Kingdom'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the text on the page
text = soup.get_text()
text = text.replace('\n', '')

# Save the text to a file
with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(text)

# Load the document
with open('./output.txt', encoding='utf-8') as f:
    text = f.read()

# Define the text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
    length_function=len,
)

# Split the text into chunks
texts = text_splitter.split_text(text)

# Define the embeddings model
embeddings = OpenAIEmbeddings()

# Create a Chroma vector store from the text chunks and embeddings
db = Chroma.from_texts(texts, embeddings)

# User's question
users_question = "Who is the current Prime Minister of the UK?"

# Use the vector store to find similar text chunks
results = db.similarity_search(users_question, k=5)

# Define the prompt template
template = """
You are a chat bot who loves to help people! Given the question using only the given context. If you are unsure and the answer is not explicitly written in the documentation, say "Sorry, I don't know how to help with that."

Context sections: {context}

Question: {question}

Answer: """

prompt = PromptTemplate(template=template, input_variables=["context", "question"])

#Fill the prompt template
context = "\n".join([doc.page_content for doc in results])
prompt_text = prompt.format(context=context, question=users_question)

#Ask the defined LLM
llm = OpenAI(temperature=0.7)
answer = llm(prompt_text)

print(answer)