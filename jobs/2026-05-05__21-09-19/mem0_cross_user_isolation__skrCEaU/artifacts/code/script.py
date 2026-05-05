#!/usr/bin/env python3
import os
import json
from mem0 import Memory

def main():
    # Initialize Mem0 Memory instance
    # Default configuration uses OpenAI and in-memory Qdrant
    # We specify gpt-4o-mini to avoid issues with models that don't support max_tokens
    config = {
        "llm": {
            "provider": "openai",
            "config": {
                "model": "gpt-4o-mini",
            }
        }
    }
    m = Memory.from_config(config)

    # Add a memory for user_id="alice"
    print("Adding memory for Alice...")
    m.add("I am highly allergic to peanuts.", user_id="alice")

    # Add a memory for user_id="bob"
    print("Adding memory for Bob...")
    m.add("I am a vegetarian.", user_id="bob")

    # Search for "What are my dietary restrictions?" for user_id="alice"
    query = "What are my dietary restrictions?"
    
    print(f"Searching for Alice: '{query}'")
    alice_results = m.search(query, filters={"user_id": "alice"})
    
    # Save Alice's results
    alice_file = "/home/user/mem0_project/alice_memories.json"
    with open(alice_file, "w") as f:
        json.dump(alice_results.get("results", alice_results), f, indent=4)
    print(f"Alice's memories saved to {alice_file}")

    # Search for the same query for user_id="bob"
    print(f"Searching for Bob: '{query}'")
    bob_results = m.search(query, filters={"user_id": "bob"})
    
    # Save Bob's results
    bob_file = "/home/user/mem0_project/bob_memories.json"
    with open(bob_file, "w") as f:
        json.dump(bob_results.get("results", bob_results), f, indent=4)
    print(f"Bob's memories saved to {bob_file}")

    print("Task completed successfully.")

if __name__ == "__main__":
    main()
