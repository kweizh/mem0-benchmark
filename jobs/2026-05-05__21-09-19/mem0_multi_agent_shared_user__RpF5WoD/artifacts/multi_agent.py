from mem0 import Memory
import json
import os

def main():
    # Initialize Memory
    config = {
        "llm": {
            "provider": "openai",
            "config": {
                "model": "gpt-4o-mini",
            }
        }
    }
    m = Memory.from_config(config)

    # Add User memory
    print("Adding user memory for Alice...")
    m.add("I am a vegetarian and allergic to nuts.", user_id="alice")

    # Add Agent memories
    print("Adding agent memory for Coach...")
    m.add("You are a fitness coach. Always encourage the user to push their limits.", agent_id="coach")
    
    print("Adding agent memory for NutriBot...")
    m.add("You are a nutritionist. Recommend high-protein plant-based meals.", agent_id="nutribot")

    query = "Suggest a dinner plan"

    # Search for Alice's user memory
    print(f"Searching for query: '{query}' for Alice...")
    alice_memories = m.search(query, filters={"user_id": "alice"}).get('results', [])
    
    # Search for Coach's agent memory
    print(f"Searching for query: '{query}' for Coach...")
    coach_memories = m.search(query, filters={"agent_id": "coach"}).get('results', [])
    if not coach_memories:
        print("Coach search returned nothing, using get_all...")
        coach_memories = m.get_all(filters={"agent_id": "coach"}).get('results', [])

    # Combine results for Coach + Alice
    coach_results = [mem['memory'] for mem in alice_memories] + [mem['memory'] for mem in coach_memories]
    print(f"Coach results: {coach_results}")
    with open("/home/user/mem0-project/coach_results.json", "w") as f:
        json.dump(coach_results, f, indent=2)

    # Search for NutriBot's agent memory
    print(f"Searching for query: '{query}' for NutriBot...")
    nutribot_memories = m.search(query, filters={"agent_id": "nutribot"}).get('results', [])
    if not nutribot_memories:
        print("NutriBot search returned nothing, using get_all...")
        nutribot_memories = m.get_all(filters={"agent_id": "nutribot"}).get('results', [])

    # Combine results for NutriBot + Alice
    nutribot_results = [mem['memory'] for mem in alice_memories] + [mem['memory'] for mem in nutribot_memories]
    print(f"NutriBot results: {nutribot_results}")
    with open("/home/user/mem0-project/nutribot_results.json", "w") as f:
        json.dump(nutribot_results, f, indent=2)

    print("Done.")

if __name__ == "__main__":
    main()
