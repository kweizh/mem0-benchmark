import json
import os
from mem0 import Memory

def main():
    # Initialize Memory with a configuration that ensures compatibility
    # with the environment's OpenAI API (avoiding o1-series models that don't support max_tokens)
    config = {
        "llm": {
            "provider": "openai",
            "config": {
                "model": "gpt-4o",
            }
        }
    }
    m = Memory.from_config(config)

    user_id = "alice"
    
    # Facts to store
    facts = [
        "I am allergic to peanuts.",
        "I love hiking."
    ]

    print(f"Adding facts for user: {user_id}...")
    # Add facts
    for fact in facts:
        m.add(fact, user_id=user_id)
    
    # Search for relevant context
    query = "What should I avoid eating?"
    print(f"Searching for: '{query}'...")
    results = m.search(query, filters={"user_id": user_id})

    # Save results to JSON
    output_path = "/home/user/mem0_project/search_results.json"
    with open(output_path, "w") as f:
        json.dump(results, f, indent=4)
    
    print(f"Search results saved to {output_path}")

if __name__ == "__main__":
    main()
