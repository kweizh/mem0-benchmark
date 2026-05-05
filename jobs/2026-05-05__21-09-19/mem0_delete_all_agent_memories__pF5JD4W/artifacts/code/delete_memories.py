import os
from mem0 import Memory

def main():
    # Initialize Mem0 Memory instance
    # Specify a model that supports max_tokens to avoid the error
    config = {
        "llm": {
            "provider": "openai",
            "config": {
                "model": "gpt-4o-mini",
            }
        }
    }
    memory = Memory.from_config(config)

    # Add memories for travel-agent
    print("Adding memories for travel-agent...")
    memory.add("I like window seats", agent_id="travel-agent")
    memory.add("I prefer vegetarian meals", agent_id="travel-agent")
    
    # Add memories for support-agent
    print("Adding memories for support-agent...")
    memory.add("User prefers email support", agent_id="support-agent")
    memory.add("User is located in New York", agent_id="support-agent")

    # Delete all memories for the travel agent
    print("Deleting all memories for travel-agent...")
    memory.delete_all(agent_id="travel-agent")

    # Small sleep to allow for indexing/deletion to propagate if needed
    import time
    time.sleep(1)

    # Get all memories for the support agent
    print("Verifying support-agent memories...")
    # Use filters as required by Mem0 v2.x
    support_mems_dict = memory.get_all(filters={"agent_id": "support-agent"})
    support_mems = support_mems_dict.get("results", [])
    support_count = len(support_mems)
    
    # Verify travel agent memories are gone
    travel_mems_dict = memory.get_all(filters={"agent_id": "travel-agent"})
    travel_mems = travel_mems_dict.get("results", [])
    travel_count = len(travel_mems)
    
    print(f"Support agent memories: {support_mems}")
    print(f"Travel agent memories: {travel_mems}")
    print(f"Support agent memories count: {support_count}")
    print(f"Travel agent memories count: {travel_count}")

    # Write the number of remaining support agent memories to output.log
    log_path = "/home/user/mem0-project/output.log"
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    with open(log_path, "w") as f:
        f.write(str(support_count))
    
    print(f"Logged support agent memory count to {log_path}")

if __name__ == "__main__":
    main()
