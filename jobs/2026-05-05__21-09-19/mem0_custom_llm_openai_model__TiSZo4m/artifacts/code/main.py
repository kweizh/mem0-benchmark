import os
from mem0 import Memory

def main():
    config = {
        "llm": {
            "provider": "openai",
            "config": {
                "model": "gpt-4o-mini"
            }
        },
        "vector_store": {
            "provider": "qdrant",
            "config": {
                "path": "/home/user/mem0_project/qdrant_db",
                "collection_name": "memories"
            }
        }
    }

    # Initialize Memory
    m = Memory.from_config(config)

    # Add memory
    print("Adding memory for user 'alice'...")
    result = m.add("I am learning how to build AI agents.", user_id="alice")
    print("Memory added successfully.")
    print(result)

    # Verify memory
    all_memories = m.get_all(filters={"user_id": "alice"})
    print("\nAll memories for alice:")
    memories = all_memories.get('results', [])
    for memory in memories:
        text = memory.get('memory')
        print(f"- {text}")

if __name__ == "__main__":
    main()
