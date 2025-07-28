"""
Documentation Enhancement Plan Generator using BAML
This script uses BAML for type-safe OpenAI API interactions
"""

import os
import json
import argparse
from dotenv import load_dotenv
from pathlib import Path

# Import BAML client
from baml_client.sync_client import b
from baml_client.types import EnhancementInput, EnhancementPlan

# Load .env file
load_dotenv()

# Setup argument parser for flexibility
def parse_arguments():
    parser = argparse.ArgumentParser(description="Generate documentation enhancement plan using BAML")
    parser.add_argument(
        "--doc-path", 
        type=str,
        default=os.environ.get("DOC_PATH", "/path/to/default/documentation.md"),
        help="Full path to documentation file to analyze"
    )
    return parser.parse_args()

def load_prompt(filename):
    """Load prompt content from a file"""
    with open(Path(__file__).parent / filename, "r", encoding="utf-8") as f:
        return f.read()

def main():
    """Generate documentation enhancement plan using BAML"""
    try:
        # Parse command line arguments
        args = parse_arguments()
        doc_path = args.doc_path
        
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

        # Create BAML input
        enhancement_input = EnhancementInput(
            documentation=doc_content,
            prompt=prompt,
            system_message=system_message
        )

        print("Generating documentation enhancement plan...")
        # Call BAML function with type-safe input
        result = b.EnhanceDocumentation(enhancement_input)
        
        # Output results
        print("\n===== DOCUMENTATION ENHANCEMENT PLAN =====\n")
        for i, rec in enumerate(result.recommendations, 1):
            # Check if priority and rationale exist
            if hasattr(rec, 'priority') and hasattr(rec, 'rationale') and rec.priority and rec.rationale:
                print(f"{i}. {rec.recommendation}")
                print(f"   Priority: {rec.priority}")
                print(f"   Rationale: {rec.rationale}\n")
            elif hasattr(rec, 'priority') and rec.priority:
                print(f"{i}. {rec.recommendation} (Priority: {rec.priority})")
            elif hasattr(rec, 'rationale') and rec.rationale:
                print(f"{i}. {rec.recommendation}")
                print(f"   Rationale: {rec.rationale}\n")
            else:
                print(f"{i}. {rec.recommendation}")
            
        # Save results to JSON file
        output_file = "enhancement_plan_baml.json"
        with open(output_file, "w", encoding="utf-8") as f:
            # Convert to dictionary with all available fields
            recommendations = []
            for rec in result.recommendations:
                recommendation_dict = {"recommendation": rec.recommendation}
                if hasattr(rec, 'priority') and rec.priority:
                    recommendation_dict["priority"] = rec.priority
                if hasattr(rec, 'rationale') and rec.rationale:
                    recommendation_dict["rationale"] = rec.rationale
                recommendations.append(recommendation_dict)
            
            json.dump({"recommendations": recommendations}, f, indent=2)
        print(f"\nEnhancement plan saved to {output_file}")
        
        return result
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

if __name__ == "__main__":
    main()
