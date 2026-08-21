from backend.app.rag.rag_pipeline import RAGPipeline


texts = [
    """
    The study proposes a machine learning model for detecting
    misinformation on social media platforms.
    """,

    """
    The dataset used in this study contains only English-language
    social media posts, which limits the generalizability of the model.
    """,

    """
    Another limitation is that the model was evaluated on a relatively
    small dataset and may not perform well on unseen platforms.
    """,

    """
    Future research should investigate multilingual misinformation
    detection and evaluate the model across different social media platforms.
    """,

    """
    The proposed model achieved promising results on the experimental dataset.
    """
]


rag = RAGPipeline(texts)


question = "What are the main limitations of this research?"


answer = rag.answer(
    question,
    top_k=3
)


print("\nRAG Answer:")
print("----------------------------")
print(answer)