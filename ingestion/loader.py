import pdfplumber
from io import BytesIO

def read_pdf(contents: bytes) -> str:
    """Read PDF from uploaded file bytes"""

    text = ""

    try:
        with pdfplumber.open(BytesIO(contents)) as pdf:
            for page in pdf.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"

        return text.strip()

    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""