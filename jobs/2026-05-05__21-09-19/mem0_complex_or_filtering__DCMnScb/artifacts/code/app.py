import json
import os
from mem0 import Memory

def main():
    # Initialize Mem0 client
    # Using explicit model to avoid max_tokens issue with some newer OpenAI models
    config = {
        "llm": {
            "provider": "openai",
            "config": {
                "model": "gpt-4o",
            }
        }
    }
    m = Memory.from_config(config)

    # 1. Add memory for user_id="alice"
    print("Adding memory for Alice...")
    m.add("Alice has a knee injury", user_id="alice")

    # 2. Add memory for agent_id="coach"
    print("Adding memory for Coach...")
    m.add("The coach recommends swimming for recovery", agent_id="coach")

    # 3. Search using compound $or filter
    # To satisfy Mem0's validation (which requires at least one of user_id, agent_id, or run_id),
    # we use the wildcard "*" for user_id which Mem0's Qdrant implementation treats as "skip filter".
    # This allows us to perform a pure OR search across different entities.
    print("Searching for 'recovery' with $or filter...")
    filters = {
        "user_id": "*", 
        "$or": [
            {"user_id": "alice"},
            {"agent_id": "coach"}
        ]
    }
    
    # Perform the search
    results = m.search("recovery", filters=filters)

    # Handle both list and dict return types depending on Mem0 version
    if isinstance(results, dict) and "results" in results:
        results_list = results["results"]
    else:
        results_list = results

    print(f"Found {len(results_list)} results.")
    for r in results_list:
        print(f" - {r.get('memory')} (user_id={r.get('user_id')}, agent_id={r.get('agent_id')})")

    # 4. Save results to /home/user/results.json
    print("Saving results to /home/user/results.json...")
    # Convert results to a serializable format if they are not already
    # (they are usually dictionaries in Mem0)
    with open("/home/user/results.json", "w") as f:
        json.dump(results_list, f, indent=4)

if __name__ == "__main__":
    main()
