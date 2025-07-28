import os
from dotenv import load_dotenv
from openai import OpenAI
from pathlib import Path

import sys

# Path to the documentation index file
DOC_PATH = Path(__file__).parent.parent / "docs/src/content/docs/reference/index.md"

# Load .env from one folder above this script
load_dotenv(dotenv_path=Path(__file__).parent.parent / ".env")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY not found in environment. Please set it in the .env file one level above the Orchestrator folder.")

client = OpenAI(api_key=OPENAI_API_KEY)

def load_prompt(filename):
    with open(Path(__file__).parent / filename, "r", encoding="utf-8") as f:
        return f.read()

SYSTEM_MESSAGE = load_prompt("./plan_enhancement_system.md")
PROMPT = load_prompt("./plan_enhancement_prompt.md")

def main(model_name="gpt-4o-mini"):
    # Read the documentation file
    with open(DOC_PATH, "r", encoding="utf-8") as f:
        doc_content = f.read()

    # Prepare the prompt
    user_prompt = PROMPT + doc_content

    messages = [
        {"role": "system", "content": SYSTEM_MESSAGE},
        {"role": "user", "content": user_prompt}
    ]

    if model_name.startswith("o"):
        print(f"Using model '{model_name}' WITHOUT temperature parameter...")
        chat_completion = client.chat.completions.create(
            messages=messages,
            model=model_name,
        )
    else:
        print(f"Using model '{model_name}' with temperature=0.3...")
        chat_completion = client.chat.completions.create(
            messages=messages,
            model=model_name,
            temperature=0.3,
        )
    plan = chat_completion.choices[0].message.content
    print("\n--- PLAN TO ENHANCE DOCUMENTATION DEPTH ---\n")
    print(plan)


if __name__ == "__main__":
    
    model_name = sys.argv[1] if len(sys.argv) > 1 else "gpt-4o-mini"
    main(model_name)