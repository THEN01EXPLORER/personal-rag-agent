from langchain_huggingface import HuggingFaceEmbeddings

class Embeddings:
    def __init__(self, model_name="sentence-transformers/all-MiniLM-L6-v2"):
        self.embeddings = HuggingFaceEmbeddings(model_name=model_name)

    def embed_text(self, text):
        return self.embeddings.embed_query(text)

    def embed_texts(self, texts):
        return self.embeddings.embed_documents(texts)