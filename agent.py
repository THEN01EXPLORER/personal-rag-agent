"""
Personal RAG Concierge - Streamlit UI with Google Gemini and HuggingFace Embeddings.
"""

import os
import tempfile
from dotenv import load_dotenv
import streamlit as st

# Load environment variables from .env file
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Initialize Google Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-flash-latest",
    temperature=0,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# System prompt for the agent
system_prompt = (
    "You are a helpful assistant that answers questions based on ingested PDF documents. "
    "When the user asks a question, search the vector database and provide a grounded answer. "
    "If no document has been ingested yet, politely ask the user to upload a PDF first."
)


def ingest_document_streamlit(uploaded_file) -> str:
    """
    Ingest a PDF file uploaded via Streamlit into the FAISS vector store.
    
    Args:
        uploaded_file: Streamlit UploadedFile object
        
    Returns:
        Success message with statistics
    """
    try:
        # Save uploaded file to temporary location
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_path = tmp_file.name
        
        # Load the PDF document
        loader = PyPDFLoader(tmp_path)
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
        
        # Create or update FAISS vector store in session state
        if st.session_state.vector_db is None:
            st.session_state.vector_db = FAISS.from_documents(chunks, embeddings)
        else:
            # Add to existing vector store
            new_db = FAISS.from_documents(chunks, embeddings)
            st.session_state.vector_db.merge_from(new_db)
        
        # Clean up temp file
        os.unlink(tmp_path)
        
        return f"✅ Successfully ingested **{uploaded_file.name}**: {len(chunks)} chunks from {len(documents)} pages."
    
    except Exception as e:
        return f"❌ Error ingesting document: {str(e)}"


def query_agent(user_message: str) -> str:
    """
    Query the agent with a user message. Retrieves context from vector DB and uses LLM.
    
    Args:
        user_message: The user's query
        
    Returns:
        The agent's response
    """
    try:
        # Check if vector database exists
        if st.session_state.vector_db is None:
            return "📄 Please upload a PDF document first using the file uploader above."
        
        # Retrieve relevant context from vector store
        results = st.session_state.vector_db.similarity_search(user_message, k=3)
        
        if not results:
            return "🔍 No relevant information found in the ingested documents."
        
        # Combine retrieved chunks
        context = "\n\n---\n\n".join([doc.page_content for doc in results])
        
        # Build prompt with context
        augmented_prompt = f"""Context from ingested documents:
{context}

---

User question: {user_message}

Please answer the question based on the context provided above. If the context doesn't contain relevant information, say so."""
        
        # Get LLM response
        response = llm.invoke([
            ("system", system_prompt),
            ("user", augmented_prompt)
        ])
        
        return getattr(response, "content", str(response))
    
    except Exception as e:
        return f"❌ Error querying agent: {str(e)}"


def main():
    """Main Streamlit application."""
    
    st.set_page_config(
        page_title="Personal RAG Concierge",
        page_icon="📚",
        layout="centered"
    )
    
    st.title("📚 Personal RAG Concierge")
    st.markdown("*Chat securely with your own documents—fast, local, private.*")
    
    # Check API key
    if not os.getenv('GOOGLE_API_KEY'):
        st.error("⚠️ GOOGLE_API_KEY not found in environment variables. Please add it to your .env file.")
        st.stop()
    
    # Initialize session state
    if 'vector_db' not in st.session_state:
        st.session_state.vector_db = None
    
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    # Sidebar for file upload
    with st.sidebar:
        st.header("📄 Document Upload")
        uploaded_file = st.file_uploader(
            "Upload a PDF document",
            type=['pdf'],
            help="Upload a PDF to ingest into the RAG system"
        )
        
        if uploaded_file is not None:
            if st.button("📥 Ingest Document"):
                with st.spinner("Processing document..."):
                    result = ingest_document_streamlit(uploaded_file)
                    st.success(result)
        
        st.divider()
        st.markdown("### 🔧 Tech Stack")
        st.markdown("""
        - **LLM:** Google Gemini Flash (latest)
        - **Embeddings:** HuggingFace MiniLM
        - **Vector Store:** FAISS
        - **Framework:** LangChain
        """)
        
        if st.button("🗑️ Clear Chat History"):
            st.session_state.chat_history = []
            st.rerun()
    
    # Display chat history
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if user_input := st.chat_input("Ask a question about your documents..."):
        # Add user message to history
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(user_input)
        
        # Get agent response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = query_agent(user_input)
                st.markdown(response)
        
        # Add assistant response to history
        st.session_state.chat_history.append({"role": "assistant", "content": response})


if __name__ == "__main__":
    main()
