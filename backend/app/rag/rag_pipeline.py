from backend.app.rag.retriever import Retriever
from backend.app.llm.groq_client import generate_answer


class RAGPipeline:

    def __init__(self, texts):
        """
        Initialize the RAG pipeline with document chunks.
        """

        self.retriever = Retriever(texts)

    def answer(self, query: str, top_k: int = 3) -> str:
        """
        Retrieve relevant chunks and generate an answer.
        """

        results = self.retriever.retrieve(
            query,
            top_k=top_k
        )

        if not results:
            return "I could not find relevant information in the document."

        context = "\n\n".join(
            result["text"]
            for result in results
        )

        prompt = f"""
You are a research assistant.

Answer the user's question using ONLY the provided
research paper context.

If the answer cannot be found in the context,
say that the information is not available in
the provided document.

Research Paper Context:
-----------------------
{context}
-----------------------

Question:
{query}

Answer clearly and concisely.
"""

        return generate_answer(prompt)