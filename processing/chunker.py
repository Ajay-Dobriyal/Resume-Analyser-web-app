def clean_text(text: str) -> str:
    text = text.replace("\n", " ")
    text = " ".join(text.split())  # remove extra spaces
    return text


def chunk_text(text: str, chunk_size: int = 500, overlap: int = 100) -> list:

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)

        start = end - overlap

    return chunks
