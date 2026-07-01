from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
texts=["Hello this is ROshan gupta",
       "I am learning Gen AI",
       "Gen AI is the future"]

vectors=embeddings.embed_documents(texts)
print(vectors)

