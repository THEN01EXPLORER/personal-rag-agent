# Personal RAG Concierge

> Track: **A. Concierge Agents**  
> Tagline: *Chat securely with your own documents—fast, local, private.*

## 1. Project Description
Personal RAG Concierge is a secure, local AI agent that lets users chat with their own PDF documents using Retrieval Augmented Generation (RAG). Instead of sending your files to a remote black box, documents stay local while only lightweight text embeddings are generated for semantic search. The system:
- Ingests PDF documents, chunks and embeds them
- Uses a FAISS vector store for similarity search
- Streams grounded answers powered by Groq's high-speed Llama-3.3-70B Versatile model
- Employs HuggingFace `all-MiniLM-L6-v2` embeddings for efficiency
- Provides a simple terminal interface for loading and querying documents

Designed for hackathon speed but architected for extensibility: add authentication, swap embedding models, or expose an API endpoint.

## 2. Tech Stack
- **Language:** Python 3.11+
- **Framework / Orchestration:** LangChain
- **LLM:** Groq API (Model: `llama-3.3-70b-versatile`)
- **Embeddings:** HuggingFace SentenceTransformers (`all-MiniLM-L6-v2`)
- **Vector Store:** FAISS (in-memory / local persistence capable)
- **Document Handling:** PyPDF / custom loader utilities
- **Environment Management:** `python -m venv`

## 3. Installation
```bash
# 1. Clone the repository
git clone <YOUR_REPO_URL>
cd capstone

# 2. Create and activate a virtual environment
python -m venv venv
# Windows PowerShell
venv\Scripts\Activate.ps1
# Or Git Bash / bash on Windows
source venv/Scripts/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your Groq API key
echo "GROQ_API_KEY=your_api_key_here" > .env
```
Ensure the `.env` file is in the project root and is NOT committed (covered by `.gitignore`).

## 4. Usage
```bash
# Start the agent
python agent.py
```
Interactive flow:
1. At the prompt, provide a PDF path (local only). Example:
   ```
   Load the PDF file at D:/docs/your_resume.pdf
   ```
2. Ask grounded questions:
   ```
   What are the main strengths highlighted?
   Summarize the experience section.
   ```
3. Type `exit` or `quit` to end the session.

### Example Session
```
You: Load the PDF file at D:/docs/whitepaper.pdf
Agent: Ingestion successful. Ready for questions.
You: Summarize the methodology.
Agent: The document outlines a three-phase approach... (grounded answer)
```

## 5. Demo
[Insert Video Link Here]

## 6. Architecture Overview
```
User Prompt → LangChain ChatGroq → (Tool Decision?) →
  Ingest PDF → Chunk + Embed (MiniLM) → Store in FAISS → Retrieve Similar Chunks →
    Augmented Context → Groq LLM → Grounded Response
```
Key Points:
- Two-pass pattern: initial reasoning may trigger a tool; second pass integrates observation.
- Embeddings cached locally; no raw document text sent to external LLM provider.

## 7. Security & Privacy
- Documents remain on local disk; only embeddings (dense vectors) are stored.
- `.env` secures your `GROQ_API_KEY` (never commit this value).
- Add OS-level encryption or containerization for sensitive deployments.

## 8. Extensibility Ideas
- Web UI (FastAPI + React)
- Multi-document semantic merging & source citation
- Persistent FAISS index on disk
- Role-based access or JWT auth
- Advanced reranking (ColBERT or hybrid BM25 + embeddings)
- Observability (tracing, token & latency metrics)

## 9. Hackathon Pitch Highlights
- Real user value: instant Q&A over personal knowledge assets
- Performance: Groq + lightweight embeddings = fast iteration
- Privacy-first: local processing of raw PDFs
- Modular design: easy to swap components (LLM, embeddings, store)

## 10. Troubleshooting
| Issue | Cause | Fix |
|-------|-------|-----|
| `GROQ_API_KEY missing` | `.env` not loaded | Confirm `.env` and restart shell |
| Slow first run | Model & embedding downloads | Subsequent runs are fast |
| Empty answers | Document not ingested | Re-run ingestion command |
| Unicode errors | Problematic PDF extraction | Try OCR preprocessing |

## 11. License
Add your preferred license (e.g., MIT) before submission.

## 12. Disclaimer
Do not ingest sensitive, proprietary, or regulated documents without appropriate safeguards. This prototype is for hackathon demonstration.

---
**Ready for judging?** Run `python agent.py`, ingest a sample PDF, and record a short demo showing a few grounded queries.
