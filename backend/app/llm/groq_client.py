import os

from dotenv import load_dotenv
from groq import Groq


# Load environment variables
load_dotenv()


# Get Groq API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError(
        "GROQ_API_KEY is not set in the .env file."
    )


# Create Groq client
client = Groq(api_key=api_key)


def generate_answer(prompt: str) -> str:
    """
    Send a prompt to the Groq LLM and return
    a stable generated answer.
    """

    try:

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",

            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a careful research analysis assistant. "
                        "Use only the information provided in the prompt. "
                        "Do not invent facts or evidence. "
                        "Give consistent and concise answers."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            # Lower temperature = more consistent output
            temperature=0.0,

            # Allow enough space for research analysis
            max_tokens=1200
        )

        answer = response.choices[0].message.content

        if not answer:
            return ""

        return answer.strip()

    except Exception as e:

        print("LLM Error:", str(e))

        return ""