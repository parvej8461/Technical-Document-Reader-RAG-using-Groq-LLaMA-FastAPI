
# Technical Document Reader (RAG) using Groq + LLaMA + FastAPI

A production-ready **Retrieval-Augmented Generation (RAG)** system that allows you to upload technical documents (PDFs) and ask natural-language questions. The system retrieves relevant context using vector search (FAISS) and generates accurate answers using **Groq-hosted LLaMA models** via a **FastAPI** backend.

---

##  Features

* Upload and index technical PDF documents
* Semantic search using embeddings + FAISS
* Ultra-low-latency LLM inference via Groq
* REST API built with FastAPI
* Dockerized for easy local and cloud deployment
* Swagger UI for testing

---

##  Architecture Overview

```
Client
  ↓
FastAPI Backend
  ↓
Document Loader → Chunking → Embeddings
  ↓
FAISS Vector Store (Similarity Search)
  ↓
Groq API (LLaMA Models)
  ↓
Final Answer
```

---

##  Tech Stack

* **Backend:** FastAPI, Python 3.10
* **LLM Inference:** Groq API (LLaMA 3)
* **Embeddings:** sentence-transformers
* **Vector DB:** FAISS (CPU)
* **Document Parsing:** PyPDF2
* **Containerization:** Docker, Docker Compose

---

##  Project Structure

```
doc-reader-llm/
│
├── app/
│   ├── main.py              # FastAPI entrypoint
│   ├── llm.py               # Groq LLM integration
│   ├── embeddings.py        # Embedding generation
│   ├── vector_store.py      # FAISS index logic
│   ├── document_loader.py  # PDF loader
│
├── data/
│   └── uploaded_docs/       # Persisted uploaded documents
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

##  Prerequisites

* Docker & Docker Compose installed
* Groq API key

---

##  Setup & Run

### 1️ Clone the repository

```bash
git clone <your-repo-url>
cd doc-reader-llm
```

### 2️ Set Groq API Key

```bash
export GROQ_API_KEY="your_groq_api_key"
```

### 3️ Build and Run with Docker

```bash
docker-compose up --build
```

The API will be available at:

```
http://localhost:8000
```

---

##  API Usage

### Swagger UI

```
http://localhost:8000/docs
```

###  Upload Document

**Endpoint:** `POST /upload`

Upload a PDF file to index it for retrieval.

###  Ask a Question

**Endpoint:** `POST /ask?question=...`

Returns an LLM-generated answer grounded in the uploaded documents.

---

##  How RAG Works Here

1. Document text is extracted from PDFs
2. Text is chunked into manageable segments
3. Each chunk is embedded into a vector
4. FAISS performs similarity search on query
5. Relevant context is injected into the LLM prompt
6. Groq-hosted LLaMA generates the final answer

---

##  Production Considerations

* Add API key authentication
* Implement rate limiting
* Enable request logging & monitoring
* Add Redis caching for frequent queries
* Move FAISS to a managed vector DB for scale
* Deploy using Kubernetes with GPU nodes

---

---

##  Future Enhancements

* Multi-document metadata filtering
* Streaming responses
* UI (Streamlit / React)
* Versioned embeddings
* Fine-tuned domain models

---

##  License

MIT License

---

##  Author

Parvej

