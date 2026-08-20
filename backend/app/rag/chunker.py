def chunk_text(
    text: str,
    chunk_size: int = 1000,
    overlap: int = 150
) -> list[str]:
    """
    Split text into overlapping chunks.
    """

    if not text.strip():
        return []

    chunks = []

    start = 0
    text_length = len(text)

    while start < text_length:

        end = start + chunk_size

        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks