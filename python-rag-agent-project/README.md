# python-rag-agent-project/README.md

# RAG Agent Project

This project implements a Retrieval-Augmented Generation (RAG) agent using Python, LangChain, Groq (LLM), HuggingFace (Embeddings), and FAISS (Vector Store). The agent can ingest PDF documents, process them, and respond to user queries based on the ingested content.

## Project Structure

```
python-rag-agent-project
├── agent.py               # Main agent script
├── tools
│   └── document_tool.py   # Document processing tools
├── rag
│   ├── __init__.py       # Package initialization
│   ├── embeddings.py      # Embedding utilities
│   ├── vectorstore.py     # Vector store utilities
│   ├── loader.py          # Document loader utilities
│   ├── chain.py           # Chain utilities
│   └── config.py          # Configuration settings
├── data
│   └── source_documents    # Directory for source documents
├── requirements.txt       # Project dependencies
├── .env                   # Environment variables
└── README.md              # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd python-rag-agent-project
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the project root and add your GROQ API key:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

## Usage

1. **Ingest a PDF document:**
   Call the `ingest_document` function from `document_tool.py` with the path to your PDF file:
   ```python
   from tools.document_tool import ingest_document
   ingest_document("path/to/your/document.pdf")
   ```

2. **Run the agent:**
   Execute the `agent.py` script to start the agent:
   ```bash
   python agent.py
   ```

3. **Interact with the agent:**
   Type your queries in the terminal, and the agent will respond based on the ingested documents.

## Example

```bash
You: What is the main topic of the document?
Agent: The main topic of the document is...
```

## License

This project is licensed under the MIT License. See the LICENSE file for more details.