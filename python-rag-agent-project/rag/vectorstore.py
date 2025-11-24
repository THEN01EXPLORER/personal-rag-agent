from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

class VectorStore:
    def __init__(self, model_name="sentence-transformers/all-MiniLM-L6-v2"):
        self.embeddings = HuggingFaceEmbeddings(model_name=model_name)
        # Initialize empty FAISS; create on first add
        self.faiss_index = None

    def add_documents(self, documents):
        if self.faiss_index is None:
            self.faiss_index = FAISS.from_documents(documents, self.embeddings)
        else:
            tmp = FAISS.from_documents(documents, self.embeddings)
            self.faiss_index.merge_from(tmp)

    def similarity_search(self, query):
        if self.faiss_index is None:
            return []
        return self.faiss_index.similarity_search(query)