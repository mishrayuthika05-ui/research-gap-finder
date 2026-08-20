from backend.app.rag.embedder import create_embeddings
from backend.app.rag.vector_store import VectorStore


class Retriever:

    def __init__(self, texts):
        self.texts = texts

        embeddings = create_embeddings(texts)

        self.vector_store = VectorStore(
            dimension=embeddings.shape[1]
        )

        self.vector_store.add_embeddings(
            embeddings,
            texts
        )

    def retrieve(self, query: str, top_k: int = 3):

        query_embedding = create_embeddings([query])

        return self.vector_store.search(
            query_embedding,
            top_k=top_k
        )