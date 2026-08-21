import os

from dotenv import load_dotenv
from groq import Groq


# Load environment variables from .env
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
    Send a prompt to the Groq LLM and return the generated answer.
    """

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_tokens=500
    )

    return response.choices[0].message.content