from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
import os

# Initialize global FAISS index
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
faiss_index = FAISS(embedding_function=embeddings)

def ingest_document(file_path):
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter()
    split_docs = text_splitter.split_documents(documents)
    faiss_index.add_documents(split_docs)

def query_document(query):
    results = faiss_index.similarity_search(query)
    return results