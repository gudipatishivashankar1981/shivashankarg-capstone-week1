
"""
hello_llm.py

Simple OpenAI API example for Week 1 of the capstone.

Usage:
   labsuser@vscode:~$ python shivashankarg-capstone-week1/src/hello_llm.py shivashankarg-capstone-week1/runs/run1.md

Question:
Explain the difference between Rehost and Refactor.

Answer:Rehosting and refactoring are two approaches to modernizing or migrating applications:

    1. **Rehosting** (also known as "lift and shift"):
    - Involves moving an application from one environment to another (e.g., on-premises to cloud) with minimal changes.
    - The architecture and code remain largely intact.
    - Focuses on quick migration to reduce costs and time.

    2. **Refactoring**:
    - Involves modifying the application’s code and architecture to improve performance, scalability, or maintainability.
    - Often entails rewriting parts of the application, using modern frameworks or technologies.
    - Aims for long-term benefits and better alignment with current business needs.

    In summary, rehosting is about moving as-is, while refactoring is about improving and optimizing.
labsuser@vscode:~$ 

The OPENAI_API_KEY should be stored in a .env file.
"""

import os
import sys

from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI


# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

MODEL_NAME = "gpt-4o-mini"
SYSTEM_PROMPT = "You are concise."


# ---------------------------------------------------------
# Environment Setup
# ---------------------------------------------------------

def load_api_key() -> str:
    """Load and validate the OpenAI API key."""
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY not found. Check your .env file."
        )

    return api_key


# ---------------------------------------------------------
# OpenAI Client
# ---------------------------------------------------------

def create_client() -> OpenAI:
    """Create and return an OpenAI client."""
    api_key = load_api_key()
    return OpenAI(api_key=api_key)


# ---------------------------------------------------------
# LLM Interaction
# ---------------------------------------------------------

def ask(client: OpenAI, question: str) -> str:
    """
    Send a question to the LLM and return the generated answer.
    """
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": question,
            },
        ],
    )

    return response.choices[0].message.content


# ---------------------------------------------------------
# Main Program
# ---------------------------------------------------------

def main() -> None:
    """Run the application."""
    client = create_client()

    #question = " ".join(sys.argv[1:]).strip()
    if len(sys.argv) > 1:
        question = read_markdown(sys.argv[1])
    else:
        question = "Say hello."

    if not question:
        question = "Say hello."

    answer = ask(client, question)

    print("\nQuestion:")
    print(question)

    print("\nAnswer:")
    print(answer)
# ---------------------------------------------------------
# Read a Markdown file
# ---------------------------------------------------------
def read_markdown(filename: str) -> str:
    """Read a markdown file and return its contents."""
    return Path(filename).read_text(encoding="utf-8")
# ---------------------------------------------------------
# Entry Point
# ---------------------------------------------------------

if __name__ == "__main__":
    main()
 