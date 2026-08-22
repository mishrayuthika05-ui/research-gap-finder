from backend.app.utils.pdf_processor import extract_text_from_pdf
from backend.app.rag.chunker import chunk_text
from backend.app.rag.retriever import Retriever
from backend.app.rag.evaluation import evaluate_retrieval


# ==========================================
# SETTINGS
# ==========================================

PDF_PATH = "data/papers/paper1.pdf"

TOP_K = 5


# ==========================================
# LOAD PAPER
# ==========================================

print("=" * 60)
print("RETRIEVAL METRICS EVALUATION")
print("=" * 60)

text = extract_text_from_pdf(PDF_PATH)

print("Characters:", len(text))

chunks = chunk_text(text)

print("Total chunks:", len(chunks))


# ==========================================
# CREATE RETRIEVER
# ==========================================

retriever = Retriever(chunks)


# ==========================================
# EVALUATION QUERIES
# ==========================================

queries = [
    "limitations of the research",
    "future work and research directions",
    "methodology used in the study",
    "main findings and results",
    "research problem"
]


# ==========================================
# GROUND TRUTH
# ==========================================
#
# NOTE:
# These indices should be manually checked
# against the paper chunks.
#
# For initial testing we select a few chunks.
# Later we can create a proper labelled
# evaluation dataset.
#

ground_truth = {

    "limitations of the research": [80, 81, 82],

    "future work and research directions": [83, 84, 85],

    "methodology used in the study": [10, 11, 12],

    "main findings and results": [20, 21, 22],

    "research problem": [0, 1, 2]
}


# ==========================================
# CALCULATE METRICS
# ==========================================

results = evaluate_retrieval(
    retriever,
    queries,
    ground_truth,
    k=TOP_K
)


# ==========================================
# DISPLAY RESULTS
# ==========================================

print("\n")
print("=" * 60)
print("PRECISION / RECALL / F1 RESULTS")
print("=" * 60)

total_precision = 0
total_recall = 0
total_f1 = 0


for result in results:

    print("\nQuery:")
    print(result["query"])

    print(
        "Precision@5:",
        round(result["precision"], 3)
    )

    print(
        "Recall@5:",
        round(result["recall"], 3)
    )

    print(
        "F1@5:",
        round(result["f1"], 3)
    )

    total_precision += result["precision"]
    total_recall += result["recall"]
    total_f1 += result["f1"]


# ==========================================
# AVERAGE METRICS
# ==========================================

count = len(results)

print("\n")
print("=" * 60)
print("AVERAGE METRICS")
print("=" * 60)

print(
    "Average Precision@5:",
    round(total_precision / count, 3)
)

print(
    "Average Recall@5:",
    round(total_recall / count, 3)
)

print(
    "Average F1@5:",
    round(total_f1 / count, 3)
)