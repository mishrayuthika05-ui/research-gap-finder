from backend.app.llm.groq_client import generate_answer


def score_research_gap(
    gap: str,
    paper_analyses: list[str]
) -> str:
    """
    Evaluate a candidate research gap using
    evidence from multiple research papers.
    """

    if len(paper_analyses) < 2:
        return "At least two research papers are required."

    papers_text = ""

    for i, analysis in enumerate(paper_analyses, start=1):
        papers_text += (
            f"\n\n--- PAPER {i} ---\n"
            f"{analysis}"
        )

    prompt = f"""
You are a research evaluation assistant.

A candidate research gap has been identified:

CANDIDATE GAP:
{gap}

Below are analyses of the research papers:

{papers_text}

Evaluate whether the candidate gap is supported
by the provided papers.

Give a score from 0 to 10 based on:

1. Evidence Strength
2. Number of papers supporting the gap
3. Research Coverage
4. Novelty indication

Then provide:

GAP SCORE:
...

CONFIDENCE:
High / Medium / Low

SUPPORTING EVIDENCE:
...

REASONING:
...

IMPORTANT:
Use ONLY the information provided.
Do not invent evidence or claim that the gap is
definitively novel.
"""

    return generate_answer(prompt)