from backend.app.rag.chunker import chunk_text


text = """
Research papers are an important source of scientific knowledge.
Machine learning is widely used in research.
Researchers often identify limitations and future research directions.
A research gap represents an area that has not been sufficiently explored.
"""


chunks = chunk_text(text)

print("Number of chunks:", len(chunks))

for i, chunk in enumerate(chunks, start=1):
    print(f"\n--- Chunk {i} ---")
    print(chunk)