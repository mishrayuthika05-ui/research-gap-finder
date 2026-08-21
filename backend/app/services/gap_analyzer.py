from backend.app.llm.groq_client import generate_answer


def compare_papers(paper_analyses: list[str]) -> str:
    """
    Compare multiple research paper analyses
    and identify potential research gaps.
    """

    if len(paper_analyses) < 2:
        return "At least two research papers are required for comparison."

    papers_text = ""

    for i, analysis in enumerate(paper_analyses, start=1):
        papers_text += (
            f"\n\n--- PAPER {i} ---\n"
            f"{analysis}"
        )

    prompt = f"""
Compare the following research papers.

Find:
- common limitations
- future work
- possible research gaps

Use only the information provided.

{papers_text}

Give a concise research-gap analysis.
"""

    result = generate_answer(prompt)

    return result