from backend.app.llm.groq_client import generate_answer


prompt = """
You are a research assistant.

Compare these two research findings:

Paper 1:
The study uses only English-language data.

Paper 2:
The study supports multilingual data but does not evaluate
real-time detection.

Identify one possible research gap based only on these facts.

Give a short answer.
"""


answer = generate_answer(prompt)


print("\nGroq Response:")
print("=" * 50)
print("TYPE:", type(answer))
print("LENGTH:", len(answer) if answer else 0)
print("ANSWER:", repr(answer))