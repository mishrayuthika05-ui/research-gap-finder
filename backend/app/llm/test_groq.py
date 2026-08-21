from backend.app.llm.groq_client import generate_answer


prompt = """
Explain in two simple sentences what a research gap is.
"""


answer = generate_answer(prompt)

print("\nLLM Response:\n")
print(answer)