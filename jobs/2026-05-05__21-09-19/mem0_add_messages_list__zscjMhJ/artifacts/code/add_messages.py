import json
import os
from mem0 import Memory

def main():
    # Initialize the Memory client
    # It uses default OpenAI models and in-memory Qdrant
    # Explicitly setting model to gpt-4o-mini to avoid max_tokens issue with some models
    config = {
        "llm": {
            "provider": "openai",
            "config": {
                "model": "gpt-4o-mini",
            }
        }
    }
    m = Memory.from_config(config)

    # Define the messages
    messages = [
        {"role": "user", "content": "Hi, I'm Alice. I am planning a trip to Japan next month."},
        {"role": "assistant", "content": "That's exciting! Japan is beautiful."},
        {"role": "user", "content": "I am a vegetarian, so I need to find good food options."}
    ]

    # Add messages for user_id="alice"
    # The add method returns a list of dictionaries containing the extracted facts
    m.add(messages, user_id="alice")

    # Search for food preferences
    # The search method returns a list of memory dictionaries (or a dict containing them in v2)
    # Use filters for user_id in search
    search_results = m.search("food preferences", filters={"user_id": "alice"})

    # Extract the list if it's in the v2 format
    if isinstance(search_results, dict) and "results" in search_results:
        search_results = search_results["results"]

    # Write results to output.json
    output_path = "/home/user/mem0-project/output.json"
    with open(output_path, "w") as f:
        json.dump(search_results, f, indent=4)

if __name__ == "__main__":
    main()
