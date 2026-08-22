from backend.app.services.research_pipeline import ResearchPipeline


papers = [

    """
    This study focuses on detecting misinformation
    on social media.

    The model was trained using English-language
    Twitter posts.

    The study achieved good classification performance.

    However, the dataset contains only English-language
    posts and the study focuses only on Twitter.

    Future work should evaluate multilingual datasets
    and other social media platforms.
    """,

    """
    This research investigates misinformation detection
    using a transformer-based deep learning model.

    The model was trained using multilingual data.

    The experiments achieved promising results.

    However, the experiments mainly used static datasets
    and real-time detection was not evaluated.

    Future work should investigate real-time detection.
    """,

    """
    This study investigates real-time misinformation
    detection using deep learning.

    The model was evaluated on social media streams.

    The model achieved fast detection performance.

    However, the dataset contains limited languages
    and platforms.

    Future work should evaluate the approach across
    more languages and social media platforms.
    """
]


pipeline = ResearchPipeline()


result = pipeline.analyze_papers(papers)


if "error" in result:

    print("ERROR:")
    print(result["error"])

else:

    print("\n")
    print("=" * 70)
    print("RESEARCH GAP FINDER RESULT")
    print("=" * 70)

    print("\n\nPAPER ANALYSES")
    print("-" * 70)

    for i, analysis in enumerate(
        result["paper_analyses"],
        start=1
    ):
        print(f"\n--- PAPER {i} ---")
        print(analysis)

    print("\n\nCROSS-PAPER COMPARISON")
    print("-" * 70)
    print(result["comparison"])

    print("\n\nCANDIDATE RESEARCH GAP")
    print("-" * 70)
    print(result["candidate_gap"])

    print("\n\nGAP SCORE")
    print("-" * 70)
    print(result["gap_score"])

    print("\n\nEVIDENCE")
    print("-" * 70)
    print(result["evidence"])