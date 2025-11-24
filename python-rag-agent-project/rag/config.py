import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration for the project
class Config:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    EMBEDDINGS_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
    FAISS_INDEX_PATH = "data/faiss_index"  # Path to save the FAISS index