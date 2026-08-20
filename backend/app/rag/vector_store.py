import faiss
import numpy as np


class VectorStore:
    def __init__(self, dimension: int = 384):
        self.index = faiss.IndexFlatIP(dimension)
        self.texts = []

    def add_embeddings(self, embeddings, texts):
        embeddings = np.asarray(
            embeddings,
            dtype="float32"
        )

        self.index.add(embeddings)

        self.texts.extend(texts)

    def search(self, query_embedding, top_k: int = 3):

        query_embedding = np.asarray(
            query_embedding,
            dtype="float32"
        )

        scores, indices = self.index.search(
            query_embedding,
            top_k
        )

        results = []

        for score, index in zip(scores[0], indices[0]):

            if index == -1:
                continue

            results.append({
                "text": self.texts[index],
                "score": float(score)
            })

        return results