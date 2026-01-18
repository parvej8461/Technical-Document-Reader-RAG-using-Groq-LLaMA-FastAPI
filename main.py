from fastapi import FastAPI, UploadFile, File
from app.document_loader import load_pdf
from app.embeddings import embed_text
from app.vector_store import add_to_index, search
from app.llm import ask_llm

app = FastAPI(
    title="Document Reader LLM API",
    version="1.0",
    description="RAG-based Technical Document Reader using Groq"
)

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    path = f"data/uploaded_docs/{file.filename}"
    with open(path, "wb") as f:
        f.write(await file.read())

    text = load_pdf(path)
    chunks = [text[i:i+500] for i in range(0, len(text), 500)]
    embeddings = embed_text(chunks)
    add_to_index(embeddings, chunks)

    return {"status": "Document indexed successfully"}

@app.post("/ask")
def ask(question: str):
    q_embedding = embed_text([question])
    context_chunks = search(q_embedding)
    context = " ".join(context_chunks)
    answer = ask_llm(context, question)
    return {"answer": answer}
