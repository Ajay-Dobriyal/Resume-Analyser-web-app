from ingestion.loader import read_pdf
from processing.chunker import clean_text, chunk_text

text=read_pdf(r"C:\Users\ajayd\Downloads\Ajay_Dobriyal_Resume AI.pdf")
cleaned = clean_text(text)

chunks = chunk_text(cleaned)

print("Total chunks:", len(chunks))
print("First chunk:", chunks[0])


# test_embedder.py
from embeddings.embedder import get_embedding

vector = get_embedding("I am a Spark developer")

print(len(vector))
print(vector[:5])
