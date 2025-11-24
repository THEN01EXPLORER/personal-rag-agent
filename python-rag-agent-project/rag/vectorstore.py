from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

class VectorStore:
    def __init__(self, model_name="sentence-transformers/all-MiniLM-L6-v2"):
        self.embeddings = HuggingFaceEmbeddings(model_name=model_name)
        self.faiss_index = FAISS(embedding_function=self.embeddings)

    def add_documents(self, documents):
        self.faiss_index.add_documents(documents)

    def similarity_search(self, query):
        return self.faiss_index.similarity_search(query)