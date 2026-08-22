from backend.app.llm.groq_client import generate_answer


def map_gap_evidence(
    gap: str,
    paper_analyses: list[str]
) -> str:
    """
    Map a candidate research gap to supporting
    evidence from individual research papers.
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
You are a research evidence mapping assistant.

Candidate Research Gap:
{gap}

Below are analyses of multiple research papers:

{papers_text}

Determine how each paper supports, contradicts,
or leaves open the candidate research gap.

For each paper provide:

PAPER:
RELATION:
EVIDENCE:
IMPLICATION:

RELATION must be one of:
- Supports
- Partially Supports
- Does Not Address
- Contradicts

Use ONLY the information provided.
Do not invent evidence.

Finally provide:

OVERALL EVIDENCE:
...

IMPORTANT:
Do not claim that the gap is definitively novel.
"""

    return generate_answer(prompt)