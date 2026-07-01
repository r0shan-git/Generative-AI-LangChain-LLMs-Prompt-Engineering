# from langchain_openai   import OpenAIEmbeddings

# embeddings = OpenAIEmbeddings(model="text-embedding-3-large",dimensions=64)

# texts=["Hello this is ROshan gupta",
#        "I am learning Gen AI",
#        "Gen AI is the future"]

# vectors=embeddings.embed_documents(texts)
# print(vectors)

### huggingface embedding model

from langchain_huggingface import HuggingFaceEmbeddings