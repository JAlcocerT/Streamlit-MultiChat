"""
Documentation Enhancement Plan Generator - Python Version
This script uses direct OpenAI API calls for generating documentation enhancement recommendations
"""

import os
import json
import argparse
from dotenv import load_dotenv
from pathlib import Path
from openai import OpenAI
import sys

# Load environment variables
load_dotenv()

# Get OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY not found. Please set it in your .env file.")

# Create OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

def load_prompt(filename):
    """Load prompt content from a file"""
    with open(Path(__file__).parent / filename, "r", encoding="utf-8") as f:
        return f.read()

def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description="Generate documentation enhancement plan")
    parser.add_argument(
        "--doc-path", 
        type=str,
        default=os.environ.get("DOC_PATH", "/path/to/default/documentation.md"),
        help="Full path to documentation file to analyze"
    )
    parser.add_argument(
        "--model",
        type=str,
        default="gpt-4o-mini",
        help="OpenAI model to use (default: gpt-4o-mini)"
    )
    return parser.parse_args()

def enhance_documentation(doc_content, system_message, prompt, model_name):
    """
    Generate enhancement recommendations using OpenAI
    
    This function mimics what we'd do with BAML but using direct API calls
    """
    # Format the prompt with the documentation content
    full_prompt = f"{prompt}\n\nDocumentation content:\n{doc_content}"
    
    # Create messages for the API call
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": full_prompt}
    ]
    
    # Make the API call with JSON response format
    response = client.chat.completions.create(
        model=model_name,
        messages=messages,
        response_format={"type": "json_object"},
        temperature=0.2
    )
    
    # Get the response content
    result = response.choices[0].message.content
    
    # Parse the JSON response
    try:
        return json.loads(result)
    except json.JSONDecodeError:
        print("Error: Failed to parse JSON response from the model")
        print("Raw response:", result)
        return {"recommendations": [{"recommendation": "Error parsing model response"}]}

def main():
    """Generate documentation enhancement plan"""
    try:
        # Parse command line arguments
        args = parse_arguments()
        doc_path = args.doc_path
        model_name = args.model
        
        # Load system message and prompt
        system_message = load_prompt("./plan_enhancement_system.md")
        prompt = load_prompt("./plan_enhancement_prompt.md")
        
        # Check if documentation file exists
        doc_path_obj = Path(doc_path)
        if not doc_path_obj.exists():
            print(f"Error: Documentation file not found at {doc_path}")
            print("Using sample documentation for demonstration...")
            doc_content = "This is sample documentation content."
        else:
            print(f"Reading documentation from: {doc_path}")
            # Read the documentation file
            with open(doc_path_obj, "r", encoding="utf-8") as f:
                doc_content = f.read()

        print(f"Generating documentation enhancement plan using {model_name}...")
        
        # Call the enhance_documentation function
        result = enhance_documentation(doc_content, system_message, prompt, model_name)
        
        # Output results
        print("\n===== DOCUMENTATION ENHANCEMENT PLAN =====\n")
        if "recommendations" in result:
            for i, rec in enumerate(result["recommendations"], 1):
                print(f"{i}. {rec.get('recommendation', '')}")
        else:
            print("Error: Unexpected response format")
            print("Raw result:", result)
        
        # Save results to JSON file
        output_file = "enhancement_plan.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2)
        print(f"\nEnhancement plan saved to {output_file}")
        
        return result
        
    except Exception as e:
        print(f"Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    main()
