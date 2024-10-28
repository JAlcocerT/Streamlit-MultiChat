* Working!!!
    * llamaindex_readmd.py
    * llamaindex_readtxt.py
    
* https://www.youtube.com/watch?v=MeCnOzz8vnM
    * https://github.com/anthropics/anthropic-cookbook/tree/main/third_party/LlamaIndex
    * https://github.com/JAlcocerT/anthropic-cookbook/blob/main/third_party/LlamaIndex/Multi_Document_Agents.ipynb
> Data Agents And Multi-Document Agents with LlamaIndex And Anthropic Claude-3

---

* https://docs.llamaindex.ai/en/stable/

```sh
python -m venv llamaind #create the venv

llamaind\Scripts\activate #activate venv (windows)
source llamaind/bin/activate #(linux)
```

```sh
pip install -r requirements.txt #all at once
```

## colab examples

* https://github.com/anthropics/anthropic-cookbook/blob/main/third_party/LlamaIndex/Basic_RAG_With_LlamaIndex.ipynb
    * https://colab.research.google.com/github/anthropics/anthropic-cookbook/blob/main/third_party/LlamaIndex/Basic_RAG_With_LlamaIndex.ipynb
    * https://colab.research.google.com/github/JAlcocerT/anthropic-cookbook/blob/main/third_party/LlamaIndex/Multi_Document_Agents.ipynb

```sh
!pip install llama-index==0.10.56
!pip install llama-index-llms-anthropic==0.1.15
!pip install llama-index-embeddings-huggingface==0.2.2

os.environ['ANTHROPIC_API_KEY'] = 'sk-
```

### ReAct Agent (LLamaIndex)

A React Agent in LlamaIndex, also known as ReAct Agent (short for Reasoning and Acting), is an agent-based chat mode built on top of a query engine over your data. It essentially acts as an intelligent assistant that can interact with users through a chat interface by leveraging LlamaIndex's capabilities.

Here's a breakdown of its key aspects:

Functionality:

Reasoning Loop: The React Agent operates in a continuous reasoning loop. It first analyzes user input to determine if it can be answered using the query engine.
Query Engine Integration: If the question is suitable, the agent selects the appropriate query engine tool and formulates a query based on the user's input.
Data Retrieval and Processing: The chosen query engine tool then retrieves and processes relevant data from your connected data sources.
Response Generation: Based on the processed data, the agent generates a response for the user. This response could be factual information, summaries, or even insights derived from the data.