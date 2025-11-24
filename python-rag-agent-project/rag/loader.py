from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os

# Initialize global FAISS index (lazy create)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
faiss_index = None

def ingest_document(file_path):
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter()
    split_docs = text_splitter.split_documents(documents)
    global faiss_index
    if faiss_index is None:
        faiss_index = FAISS.from_documents(split_docs, embeddings)
    else:
        tmp = FAISS.from_documents(split_docs, embeddings)
        faiss_index.merge_from(tmp)

def query_document(query):
    if faiss_index is None:
        return []
    results = faiss_index.similarity_search(query)
    return results