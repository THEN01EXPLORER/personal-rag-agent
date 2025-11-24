"""
Document processing tool using LangChain for PDF ingestion and querying.
"""

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.tools import tool

# Global variable to store the vector database
vector_db = None


@tool
def ingest_document(file_path: str) -> str:
    """
    Load a PDF document, split it into chunks, and create a FAISS vector store.
    
    Args:
        file_path: Path to the PDF file to ingest
        
    Returns:
        Success message with document statistics
    """
    global vector_db
    
    try:
        # Load the PDF document
        loader = PyPDFLoader(file_path)
        documents = loader.load()
        
        # Split documents into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        chunks = text_splitter.split_documents(documents)
        
        # Initialize embeddings (runs locally on CPU)
        embeddings = HuggingFaceEmbeddings(
            model_name='sentence-transformers/all-MiniLM-L6-v2'
        )
        
        # Create FAISS vector store
        vector_db = FAISS.from_documents(chunks, embeddings)
        
        return f"Successfully ingested document: {file_path}. Created {len(chunks)} chunks from {len(documents)} pages."
    
    except Exception as e:
        return f"Error ingesting document: {str(e)}"


@tool
def query_document(query: str) -> str:
    """
    Query the ingested document and return the top 3 most relevant results.
    
    Args:
        query: The search query string
        
    Returns:
        Combined content from the top 3 matching document chunks
    """
    global vector_db
    
    # Check if vector database is initialized
    if vector_db is None:
        return "No document has been ingested yet. Please use ingest_document first."
    
    try:
        # Search for top 3 similar documents
        results = vector_db.similarity_search(query, k=3)
        
        if not results:
            return "No relevant results found for your query."
        
        # Combine the content from all results
        combined_content = "\n\n---\n\n".join([doc.page_content for doc in results])
        
        return f"Found {len(results)} relevant chunks:\n\n{combined_content}"
    
    except Exception as e:
        return f"Error querying document: {str(e)}"
