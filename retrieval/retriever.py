from vectorstore.store import VectorStore
from llm.generator import generate

vector_store = VectorStore()


class RAGService:

    def ingest(self, chunks):
        vector_store.add_chunks(chunks)

    def ask(self, job_description):

        relevant_chunks = vector_store.search(job_description, top_k=5)

        if not relevant_chunks:
            return {"error": "No resume uploaded yet."}

        resume_context = "\n\n".join(relevant_chunks)

        prompt = f"""
You are an AI resume evaluator.

Analyze the resume against the job description carefully.

Resume Content:
{resume_context}

Job Description:
{job_description}

Return ONLY the result in this structure:

Skill Gap Analysis:
- point

Missing Keywords:
- keyword

Improvement Suggestions:
- suggestion

ATS Score: number between 0 and 100
"""

        result = generate(prompt)

        return {
            "analysis": result.strip(),
            "chunks_used": len(relevant_chunks)
        }