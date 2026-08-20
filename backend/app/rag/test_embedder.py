from backend.app.rag.embedder import create_embeddings


texts = [
    "Machine learning is used for detecting fake news.",
    "Deep learning models can classify misinformation."
]


embeddings = create_embeddings(texts)


print("Embedding shape:", embeddings.shape)
print("Embedding type:", type(embeddings))