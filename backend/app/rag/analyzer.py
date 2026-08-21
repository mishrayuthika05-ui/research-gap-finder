from backend.app.llm.groq_client import generate_answer


def analyze_paper(text: str) -> str:
    """
    Analyze a research paper and extract
    important research information.
    """

    prompt = f"""
You are an expert research assistant.

Analyze the following research paper text.

Extract the following information:

1. Research Problem
2. Main Methodology
3. Key Findings
4. Limitations
5. Future Work

Use ONLY the information provided in the paper.
Do not invent information.

Return the answer in this format:

Research Problem:
...

Main Methodology:
...

Key Findings:
...

Limitations:
...

Future Work:
...

Research Paper:
----------------
{text}
----------------
"""

    return generate_answer(prompt)