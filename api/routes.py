from retrieval.retriever import RAGService
from ingestion.loader import read_pdf
from processing.chunker import chunk_text
from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel

router = APIRouter()

rag_service = RAGService()


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):

    contents = await file.read()
    text = read_pdf(contents)

    if not text:
        return {"error": "Could not extract text from PDF"}

    chunks = chunk_text(text)

    rag_service.ingest(chunks)

    return {
        "message": "Resume uploaded and indexed successfully",
        "total_chunks": len(chunks)
    }


class JobRequest(BaseModel):
    job_description: str


@router.post("/analyze")
async def analyze_resume(request: JobRequest):

    result = rag_service.ask(request.job_description)

    return result