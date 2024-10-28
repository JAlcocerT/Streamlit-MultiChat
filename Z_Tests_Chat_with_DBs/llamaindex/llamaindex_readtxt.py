import os
os.environ['ANTHROPIC_API_KEY'] = 'sk-ant-api03-'

from llama_index.llms.anthropic import Anthropic
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

llm = Anthropic(temperature=0.0, model='claude-3-opus-20240229')
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

from llama_index.core import Settings
Settings.llm = llm
Settings.embed_model = embed_model
Settings.chunk_size = 512

# !mkdir -p 'data/paul_graham/'
# !wget 'https://raw.githubusercontent.com/run-llama/llama_index/main/docs/examples/data/paul_graham/paul_graham_essay.txt' -O 'data/paul_graham/paul_graham_essay.txt'

from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
)

documents = SimpleDirectoryReader("./data").load_data()

index = VectorStoreIndex.from_documents(
    documents,
)

query_engine = index.as_query_engine(similarity_top_k=3)

response = query_engine.query("What properties do you have available?")

print(response)

response_specif = query_engine.query("What properties could you recommend if i want to live in spain?")

print(response_specif)

response_specif = query_engine.query("What properties could be interesting if my budget is maximum 300k $?")

print(response_specif)