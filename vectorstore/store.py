import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


class VectorStore:

    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = faiss.IndexFlatL2(384)
        self.text_chunks = []

    def add_chunks(self, chunks):
        embeddings = self.model.encode(chunks)
        embeddings = np.array(embeddings).astype("float32")

        self.index.add(embeddings)
        self.text_chunks.extend(chunks)

    def search(self, query, top_k=5):
        query_embedding = self.model.encode([query])
        query_embedding = np.array(query_embedding).astype("float32")

        distances, indices = self.index.search(query_embedding, top_k)

        results = []
        for i in indices[0]:
            if i < len(self.text_chunks):
                results.append(self.text_chunks[i])

        return results