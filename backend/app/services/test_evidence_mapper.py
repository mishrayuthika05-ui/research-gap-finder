from backend.app.services.evidence_mapper import map_gap_evidence


paper_analyses = [

    """
    Research Problem:
    Detecting misinformation on social media.

    Main Methodology:
    Machine learning classification using English-language
    Twitter posts.

    Key Findings:
    The model achieved good classification performance.

    Limitations:
    The dataset contains only English-language posts.
    The study focuses only on Twitter.

    Future Work:
    Evaluate the model on multilingual datasets and other
    social media platforms.
    """,

    """
    Research Problem:
    Detecting misinformation using deep learning.

    Main Methodology:
    A transformer-based model trained on multilingual data.

    Key Findings:
    The model performs well on multilingual misinformation.

    Limitations:
    The experiments were performed mainly on static datasets.
    Real-time detection was not evaluated.

    Future Work:
    Investigate real-time misinformation detection.
    """,

    """
    Research Problem:
    Real-time misinformation detection.

    Main Methodology:
    Deep learning model evaluated on social media streams.

    Key Findings:
    The model can detect misinformation quickly.

    Limitations:
    The dataset contains limited languages and platforms.

    Future Work:
    Evaluate the approach across more languages and social
    media platforms.
    """
]


candidate_gap = """
Real-time, multilingual and cross-platform misinformation
detection has not been evaluated together across the papers.
"""


result = map_gap_evidence(
    candidate_gap,
    paper_analyses
)


print("\nEvidence Mapping")
print("=" * 60)
print(result)