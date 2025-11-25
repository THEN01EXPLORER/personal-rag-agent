# Personal RAG Concierge 📚

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-121212?style=for-the-badge&logo=chainlink&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

> **Kaggle Community Hackathon:** Agents Intensive - Capstone Project  
> *Chat securely with your own documents—fast, local, private.*

## 📖 Overview

**Personal RAG Concierge** is a privacy-first AI agent enabling users to chat with PDF documents using Retrieval-Augmented Generation (RAG). Powered by **Google Gemini Flash** and **FAISS** vector storage, it provides instant, grounded answers while keeping documents local.

**Key Workflow:**
1. Upload PDFs via Streamlit UI
2. Documents chunked and embedded locally (HuggingFace `all-MiniLM-L6-v2`)
3. FAISS stores embeddings in-memory
4. Ask questions—agent retrieves context and generates answers via Gemini
5. Only queries sent to API, never raw documents

## ✨ Features

- **Multi-Agent Tooling:** Custom LangChain tools for ingestion and retrieval
- **Session Memory:** Maintains conversation context for follow-ups
- **Google Gemini Flash:** Sub-second reasoning with `gemini-flash-latest`
- **Clean Streamlit UI:** Drag-and-drop upload, real-time chat, history persistence
- **Privacy-First:** Local embeddings, in-memory vector store, secure API keys

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Frontend** | Streamlit |
| **LLM** | Google Gemini Flash |
| **Embeddings** | HuggingFace MiniLM |
| **Vector Store** | FAISS |
| **Framework** | LangChain |

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- [Google API Key](https://aistudio.google.com/app/apikey)

### Installation

```bash
# Clone repository
git clone https://github.com/THEN01EXPLORER/personal-rag-agent.git
cd capstone

# Create virtual environment
python -m venv venv
source venv/Scripts/activate  # Windows Git Bash
# OR: venv\Scripts\activate.bat (Windows CMD)

# Install dependencies
pip install -r requirements.txt

# Create .env file
echo "GOOGLE_API_KEY=your_key_here" > .env

# Run application
streamlit run agent.py
```

App opens at `http://localhost:8501`

## 🎥 Demo

🚀 **[Try Live App](https://agentpy-gzmxf4kwamofut5acnf3v5.streamlit.app/)**  
🎬 **[Watch Video](https://youtu.be/1U8ETtSHhR4)**

![Personal RAG Concierge UI](image.png)

## 🌐 Deployment

Deploy to Streamlit Cloud in minutes:
1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io/) → "New app"
3. Select repo, branch (`main`), file (`agent.py`)
4. Add API key in Settings → Secrets:
   ```toml
   GOOGLE_API_KEY = "your_key_here"
   ```
5. Deploy and access at `https://[app-name].streamlit.app`

## 📁 Project Structure

```
capstone/
├── agent.py              # Main Streamlit app
├── requirements.txt      # Dependencies
├── .env                  # API keys (local)
├── python-rag-agent-project/
│   ├── agent.py          # Alternative implementation
│   ├── tools/            # Document processing
│   └── rag/              # RAG components
└── tools/                # Shared utilities
```

## 🎯 Use Cases

- Academic research papers and theses
- Legal contracts and case files
- Technical documentation and APIs
- Personal knowledge management
- Business reports and market analysis

## 🔮 Future Enhancements

- [ ] Persistent vector store for cross-session retention
- [ ] Multi-format support (DOCX, TXT, Markdown)
- [ ] Source citations with page numbers
- [ ] Hybrid search (BM25 + semantic)
- [ ] Multi-user authentication
- [ ] REST API endpoint
- [ ] Batch folder uploads

## 🏆 Hackathon Submission

**Competition:** Kaggle Agents Intensive - Capstone Project

### Why This Project Stands Out

1. **Real User Value:** Instant Q&A over personal documents without cloud upload
2. **High Performance:** Gemini Flash delivers sub-second responses
3. **Privacy-First:** Documents stay local; only embeddings generated
4. **Production-Ready:** Modular architecture with clean separation
5. **Zero Learning Curve:** Intuitive Streamlit interface

### Technical Highlights

- **Complete RAG Pipeline:** Chunking, embedding, retrieval, and generation
- **LangChain Integration:** Industry-standard orchestration
- **Local Embeddings:** CPU-only, no GPU required
- **Session Context:** Follow-up question support
- **Smart Parsing:** Automatic cleanup of nested LLM responses
- **Cost-Effective:** Free Gemini API + local embeddings
- **Extensible:** Easy to swap LLMs, embeddings, or vector stores

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| `GOOGLE_API_KEY not found` | Add key to `.env` file |
| Slow first run | Models download once, then cached |
| Empty answers | Re-upload PDF, check ingestion success |
| Unicode errors | Re-save PDF as text-based |
| Model 404 error | Code uses `gemini-flash-latest` |

## 📧 Contact

**Repository:** [personal-rag-agent](https://github.com/THEN01EXPLORER/personal-rag-agent)  
**GitHub:** [@THEN01EXPLORER](https://github.com/THEN01EXPLORER)

---

**Built with ❤️ for Kaggle Agents Intensive Capstone Project**

*Star ⭐ this repo if you find it useful!*
