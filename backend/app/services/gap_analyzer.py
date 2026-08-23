from backend.app.llm.groq_client import generate_answer


def compare_papers(paper_analyses: list[str]) -> str:
    """
    Compare multiple research paper analyses and identify
    well-supported potential research gaps.
    """

    if len(paper_analyses) < 2:
        return "At least two research papers are required for comparison."

    # Prepare papers
    papers_text = ""

    for i, analysis in enumerate(paper_analyses, start=1):

        if not analysis or not analysis.strip():
            analysis = "No analysis available for this paper."

        papers_text += (
            f"\n\n================ PAPER {i} ================\n"
            f"{analysis.strip()}"
        )

    prompt = f"""
You are an expert research-gap analysis assistant.

Your task is to compare the research papers below and identify
potential research gaps supported by the information provided.

IMPORTANT RULES:

1. Use ONLY information present in the paper analyses.
2. Do NOT invent facts, datasets, methods, results, or limitations.
3. Do NOT claim that a research gap is definitively novel.
4. If evidence is insufficient, clearly say so.
5. Prefer gaps that appear across multiple papers.
6. Pay special attention to:
   - limitations
   - future work
   - unresolved problems
   - missing evaluations
   - missing datasets or domains
   - scalability issues
   - generalization issues
   - evaluation limitations
7. Do not create a gap simply because information is missing
   from the provided analysis.
8. Distinguish between an actual research gap and a limitation
   of the provided paper analysis.

For each paper identify:

PAPER:
MAIN FOCUS:
LIMITATIONS:
FUTURE WORK:
OPEN PROBLEMS:

Then compare the papers.

Return the following sections:

COMMON THEMES:
...

COMMON LIMITATIONS:
...

FUTURE WORK OVERLAP:
...

OPEN RESEARCH PROBLEMS:
...

POTENTIAL RESEARCH GAPS:
1. ...
2. ...
3. ...

STRONGEST POTENTIAL GAP:
...

WHY THIS GAP IS SUPPORTED:
...

EVIDENCE COVERAGE:
Paper 1: ...
Paper 2: ...
Paper 3: ...

CONFIDENCE:
High / Medium / Low

Research papers:
{papers_text}
"""

    result = generate_answer(prompt)

    if not result or not result.strip():
        return (
            "Unable to generate a cross-paper analysis. "
            "The LLM returned an empty response."
        )

    return result.strip()