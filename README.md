# Personal RAG Concierge 📚

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-121212?style=for-the-badge&logo=chainlink&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

> **Kaggle Community Hackathon:** Agents Intensive - Capstone Project  
> *Chat securely with your own documents—fast, local, private.*

## 📖 Overview

Personal RAG Concierge is a privacy-first RAG agent for conversational Q&A over PDF documents. It uses a Streamlit UI for uploads, HuggingFace MiniLM embeddings (all-MiniLM-L6-v2) for local vectorization, FAISS for fast similarity search, and Google Gemini Flash for generation. Documents are chunked and embedded locally; only compact query text and retrieved snippets are sent to the LLM.

## ✨ Key Features

- Multi-agent LangChain tools for ingestion and retrieval
- Session memory for natural follow-ups
- Fast generation via Google Gemini Flash
- Clean Streamlit UI with upload, chat, and history
- Privacy-first design: local embeddings and secure API keys

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Frontend | Streamlit |
| LLM | Google Gemini Flash |
| Embeddings | HuggingFace MiniLM |
| Vector Store | FAISS |
| Orchestration | LangChain |

## 🚀 Quick Start

### Prerequisites
- Python 3.11 or higher
- Google API Key from [Google AI Studio](https://aistudio.google.com/app/apikey)

### Installation Steps

```bash
# Clone the repository
git clone https://github.com/THEN01EXPLORER/personal-rag-agent.git
cd capstone

# Create and activate virtual environment
python -m venv venv

# Windows (Git Bash)
source venv/Scripts/activate

# Windows (Command Prompt)
venv\Scripts\activate.bat

# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create environment file
echo "GOOGLE_API_KEY=your_api_key_here" > .env

# Run the application
streamlit run agent.py
```

The app will open automatically at `http://localhost:8501`

### Usage Workflow

1. **Upload Document:** Use the sidebar file uploader to select a PDF document
2. **Ingest Content:** Click "📥 Ingest Document" to process and embed the content
3. **Ask Questions:** Type your questions in the chat input at the bottom
4. **Get Answers:** The agent retrieves relevant context and provides grounded responses

### Example Session
```
User: What are the main findings in this research paper?
Agent: Based on the document, the main findings include...

User: Can you elaborate on the methodology?
Agent: The methodology section describes a three-phase approach...
```

## 🎥 Demo

🚀 **[Try Live App](https://agentpy-gzmxf4kwamofut5acnf3v5.streamlit.app/)**  
🎬 **[Watch Video](https://youtu.be/1U8ETtSHhR4)**

![Personal RAG Concierge UI](image.png)

## 🌐 Deployment to Streamlit Cloud

### Deployment Steps

1. **Push your code to GitHub:**
```bash
git add .
git commit -m "Ready for deployment"
git push origin main
```

2. **Deploy to Streamlit Cloud:**
   - Navigate to [share.streamlit.io](https://share.streamlit.io/)
   - Click "New app"
   - Select your repository, branch (`main`), and main file (`agent.py`)
   - Click "Deploy"

3. **Configure API Key as Secret:**
   - In your Streamlit Cloud dashboard, access app settings
   - Navigate to "Secrets" section
   - Add your API key in TOML format:
   ```toml
   GOOGLE_API_KEY = "your_google_api_key_here"
   ```
   - Save and reboot the application

4. **Access your deployed app:**
   - Your live app will be available at `https://[your-app-name].streamlit.app`

**Note:** For local development, use a `.env` file. For Streamlit Cloud, always use the Secrets management feature to keep your API keys secure.

## 📁 Project Structure

```
capstone/
├── agent.py                      # Main Streamlit application
├── requirements.txt               # Python dependencies
├── .env                          # Environment variables (local only)
├── .gitignore                    # Git ignore rules
├── README.md                     # Project documentation
├── python-rag-agent-project/     # Additional RAG modules
│   ├── agent.py                  # Alternative implementation
│   ├── tools/
│   │   └── document_tool.py      # Document processing tools
│   └── rag/
│       ├── embeddings.py         # Embedding utilities
│       ├── vectorstore.py        # Vector store management
│       ├── loader.py             # Document loaders
│       ├── chain.py              # RAG chain implementation
│       └── config.py             # Configuration management
└── tools/
    └── document_tool.py          # Shared document utilities
```

## 🔒 Security & Privacy

### Data Handling Philosophy
- **Local Processing:** PDF documents are processed locally and temporarily stored only during ingestion
- **Embedding Storage:** Only vectorized embeddings are retained—no raw document text is stored long-term
- **API Communication:** Only user queries and retrieved context snippets are sent to Google Gemini API
- **No Cloud Storage:** Documents never leave your machine except as processed query context

### Best Practices
- Never commit your `.env` file or API keys to version control
- Use environment variables for all sensitive credentials
- For production deployments, consider adding authentication, rate limiting, and encrypted storage
- Be mindful of sensitive documents—this is a demonstration prototype

⚠️ **Compliance Note:** Do not ingest regulated documents (HIPAA, GDPR-protected, classified information) without implementing additional safeguards.

## 🎯 Use Cases

- **Academic Research:** Query research papers, theses, and academic literature for instant insights
- **Legal Document Review:** Search through contracts, case files, and legal briefs efficiently
- **Technical Documentation:** Navigate API docs, user manuals, and technical specifications
- **Personal Knowledge Management:** Build a searchable archive of articles, notes, and reports
- **Business Intelligence:** Analyze market reports, financial statements, and business plans

## 🔮 Future Enhancements

### Planned Features
- [ ] **Persistent Vector Store:** Save FAISS index to disk for cross-session document retention
- [ ] **Multi-format Support:** Add support for DOCX, TXT, Markdown, and web scraping
- [ ] **Source Citations:** Display page numbers and document names in answers
- [ ] **Advanced Reranking:** Implement hybrid search (BM25 + semantic) for improved retrieval
- [ ] **Multi-user Authentication:** Add user login and document isolation for shared deployments
- [ ] **REST API Endpoint:** Expose programmatic access for integrations
- [ ] **Batch Processing:** Support folder uploads and bulk document ingestion
- [ ] **Observability:** Integrate tracing and metrics (LangSmith, Weights & Biases)

### Extensibility Options
The modular architecture makes it easy to swap components:
- **LLM:** Replace Gemini with Groq, OpenAI, Anthropic, or local models
- **Embeddings:** Use OpenAI embeddings, Cohere, or custom fine-tuned models
- **Vector Store:** Migrate to Pinecone, Weaviate, or Qdrant for production scale
- **UI:** Build a React frontend or mobile app using the core RAG logic

## 🏆 Hackathon Submission

**Competition:** Kaggle Community Hackathon - Agents Intensive Capstone Project

### Why Personal RAG Concierge Stands Out

1. **Real User Value:** Solves a genuine pain point—instant Q&A over personal documents without cloud upload friction
2. **High Performance:** Google Gemini Flash delivers sub-second responses with high-quality reasoning
3. **Privacy-First Design:** Documents stay local; only embeddings are generated for search
4. **Production-Ready Architecture:** Modular design with clear separation of concerns
5. **Zero Learning Curve:** Intuitive Streamlit interface requires no technical expertise

### Technical Highlights

- **Complete RAG Pipeline:** Full implementation of chunking, embedding, retrieval, and generation workflow
- **LangChain Integration:** Leverages industry-standard orchestration framework for robust agent behavior
- **Local Embeddings:** HuggingFace SentenceTransformers run on CPU—no GPU required
- **Session Context Management:** Maintains conversation history for natural follow-up questions
- **Smart Output Parsing:** Automatically cleans nested response structures from LLM API
- **Cost-Effective Solution:** Uses free Google Gemini API and local embeddings (no paid vector database)
- **Extensible Design:** Easy to swap LLMs, embeddings, or vector stores for different use cases
- **Educational Value:** Clean, well-documented code demonstrating RAG best practices

### Innovation Points

- **Zero-config Setup:** Works out of the box with just an API key—no complex configuration needed
- **Privacy Without Compromise:** Maintains data privacy while delivering cloud-level performance
- **Deployment Ready:** One-click deployment to Streamlit Cloud with full documentation
- **Real-world Application:** Immediately useful for researchers, professionals, and students

## 🐛 Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| `GOOGLE_API_KEY not found` | Missing or incorrect `.env` file | Verify `.env` exists in project root with valid key |
| Slow first run | Model downloads on initial use | Subsequent runs are much faster; models are cached locally |
| Empty/irrelevant answers | Document not properly ingested | Re-upload PDF and ensure "✅ Successfully ingested" message appears |
| Unicode errors during load | Malformed or encrypted PDF | Try re-saving the PDF or converting to text-based format |
| Out of memory error | Very large PDF files | Split document into smaller files or increase system RAM |
| Model not found (404) | Outdated model name in code | Verify code uses `gemini-flash-latest` model identifier |

### Getting Additional Help
- Check the [Issues](https://github.com/THEN01EXPLORER/personal-rag-agent/issues) page for known problems and solutions
- Review [LangChain documentation](https://python.langchain.com/) for RAG pipeline details
- Consult [Streamlit docs](https://docs.streamlit.io/) for UI customization options
- Refer to [Google AI Studio](https://aistudio.google.com/) for API key and model information

## 🤝 Contributing

Contributions are welcome! To contribute:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please ensure your code follows existing style conventions and includes appropriate documentation.

## 📧 Contact

**Repository:** [personal-rag-agent](https://github.com/THEN01EXPLORER/personal-rag-agent)  
**GitHub:** [@THEN01EXPLORER](https://github.com/THEN01EXPLORER)

---

**Built with ❤️ for Kaggle Agents Intensive Capstone Project**

*Star ⭐ this repo if you find it useful!*
