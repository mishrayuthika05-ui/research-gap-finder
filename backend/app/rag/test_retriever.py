from backend.app.rag.retriever import Retriever


texts = [
    "The study uses a small dataset collected from social media.",
    "The proposed model achieves high accuracy on the test dataset.",
    "One limitation is the lack of multilingual evaluation.",
    "The model requires significant computational resources.",
    "Future work should investigate real-time misinformation detection."
]


retriever = Retriever(texts)


query = "What are the limitations of this research?"


results = retriever.retrieve(
    query,
    top_k=3
)


print("\nRetrieved Results:")

for i, result in enumerate(results, start=1):

    print(f"\n--- Result {i} ---")
    print("Score:", result["score"])
    print("Text:", result["text"])