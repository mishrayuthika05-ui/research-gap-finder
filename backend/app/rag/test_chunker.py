from backend.app.utils.pdf_processor import extract_text_from_pdf
from backend.app.rag.chunker import chunk_text


pdf_path = "data/papers/paper1.pdf"


# Extract text from PDF
text = extract_text_from_pdf(pdf_path)

print("Total characters:", len(text))


# Split extracted text into chunks
chunks = chunk_text(text)

print("Number of chunks:", len(chunks))


# Show first 3 chunks
for i, chunk in enumerate(chunks[:3], start=1):

    print(f"\n--- Chunk {i} ---")
    print(chunk)