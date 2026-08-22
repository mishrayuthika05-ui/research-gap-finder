from backend.app.rag.retriever import Retriever


def precision_at_k(retrieved_indices, relevant_indices, k):
    """
    Precision@K:
    Retrieved relevant items / total retrieved items
    """

    retrieved = retrieved_indices[:k]

    if not retrieved:
        return 0.0

    relevant_retrieved = len(
        set(retrieved) & set(relevant_indices)
    )

    return relevant_retrieved / len(retrieved)


def recall_at_k(retrieved_indices, relevant_indices, k):
    """
    Recall@K:
    Retrieved relevant items / total relevant items
    """

    if not relevant_indices:
        return 0.0

    retrieved = retrieved_indices[:k]

    relevant_retrieved = len(
        set(retrieved) & set(relevant_indices)
    )

    return relevant_retrieved / len(relevant_indices)


def f1_at_k(precision, recall):
    """
    F1 score from precision and recall.
    """

    if precision + recall == 0:
        return 0.0

    return (
        2 * precision * recall
        / (precision + recall)
    )


def evaluate_retrieval(
    retriever,
    queries,
    ground_truth,
    k=5
):
    """
    Evaluate retriever using manually labelled
    relevant chunk indices.
    """

    results = []

    for query in queries:

        retrieved = retriever.retrieve(
            query,
            top_k=k
        )

        retrieved_texts = [
            result["text"]
            for result in retrieved
        ]

        retrieved_indices = []

        for text in retrieved_texts:

            if text in retriever.texts:
                retrieved_indices.append(
                    retriever.texts.index(text)
                )

        relevant_indices = ground_truth.get(
            query,
            []
        )

        precision = precision_at_k(
            retrieved_indices,
            relevant_indices,
            k
        )

        recall = recall_at_k(
            retrieved_indices,
            relevant_indices,
            k
        )

        f1 = f1_at_k(
            precision,
            recall
        )

        results.append({
            "query": query,
            "precision": precision,
            "recall": recall,
            "f1": f1
        })

    return results