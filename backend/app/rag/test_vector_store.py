from backend.app.rag.embedder import create_embeddings
from backend.app.rag.vector_store import VectorStore


texts = [
    "Machine learning is used for detecting fake news.",
    "Deep learning models can classify misinformation.",
    "Solar energy is a renewable source of electricity.",
    "Natural language processing helps computers understand text."
]


embeddings = create_embeddings(texts)


store = VectorStore()

store.add_embeddings(
    embeddings,
    texts
)


query = "How can AI detect fake news?"

query_embedding = create_embeddings([query])


results = store.search(
    query_embedding,
    top_k=2
)


print("\nSearch Results:")

for result in results:
    print("\nScore:", result["score"])
    print("Text:", result["text"])