from backend.app.llm.groq_client import generate_answer


def analyze_paper(text: str) -> str:
    """
    Analyze a research paper and extract
    important research information.
    """

    if not text or not text.strip():
        return "No paper text was provided."

    prompt = f"""
You are an expert research assistant.

Analyze the following research paper text.

Extract the following five sections:

1. Research Problem
2. Main Methodology
3. Key Findings
4. Limitations
5. Future Work

Use ONLY the information provided in the paper.
Do not invent information.

If a section is not clearly available in the provided text,
write:

Not clearly stated in the provided text.

IMPORTANT:
You MUST return all five sections.
Never return an empty response.

Return EXACTLY in this format:

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

    result = generate_answer(prompt)

    if not result or not result.strip():

        retry_prompt = f"""
Analyze this research paper text and provide a concise
research analysis.

You MUST provide all five sections:

Research Problem:
Main Methodology:
Key Findings:
Limitations:
Future Work:

Use only the provided text.
If information is missing, write:
Not clearly stated in the provided text.

Do not return an empty response.

Paper:
{text}
"""

        result = generate_answer(retry_prompt)

    if not result or not result.strip():
        return (
            "Research Problem:\n"
            "Not clearly stated in the provided text.\n\n"
            "Main Methodology:\n"
            "Not clearly stated in the provided text.\n\n"
            "Key Findings:\n"
            "Not clearly stated in the provided text.\n\n"
            "Limitations:\n"
            "Not clearly stated in the provided text.\n\n"
            "Future Work:\n"
            "Not clearly stated in the provided text."
        )

    return result.strip()