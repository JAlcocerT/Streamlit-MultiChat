import yaml

def create_hugo_post(data, filepath):
    """Creates a Hugo .md post from structured data."""
    front_matter = {
        "title": data["title"],
        "date": data["date"],
        "draft": data.get("draft", False),  # Use .get() with a default value
        "tags": data.get("tags", []),
        "description": data.get("description", ""),
        "url": data.get("url", "")
    }

    content = data.get("content", "")

    with open(filepath, 'w') as f:
        f.write("---\n")
        yaml.dump(front_matter, f, sort_keys=False)
        f.write("---\n\n")
        f.write(content)

# Example usage:
openai_data = {
    "title": "[AI] Using LiteLLM to unify LLMs calls. Applied to AIssistant.",
    "date": "2025-04-12",
    "draft": False,
    "tags": ["Gen-AI", "Python"],
    "description": "How to use LiteLLM with different APIs - From OpenAI to Mistral APIs",
    "url": "how-to-use-lite-llm",
    "content": "## Introduction\n\nThis post explores how to leverage LiteLLM..."
}

output_filepath = "./how-to-use-lite-llm.md"
create_hugo_post(openai_data, output_filepath)

print(f"Hugo post created at: {output_filepath}")