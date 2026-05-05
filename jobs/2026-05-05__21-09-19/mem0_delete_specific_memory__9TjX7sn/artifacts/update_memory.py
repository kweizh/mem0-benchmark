import os
from mem0 import Memory

config = {
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "path": "/home/user/project/qdrant_db"
        }
    },
    "llm": {
        "provider": "openai",
        "config": {
            "model": "gpt-4o",
            "max_tokens": 1000
        }
    }
}

def main():
    m = Memory.from_config(config)
    
    # 1. Search for the memory related to "allergic to strawberries"
    response = m.search("allergic to strawberries", filters={"user_id": "charlie"})
    print(f"Search results: {response}")
    
    search_results = response.get("results", []) if isinstance(response, dict) else response
    
    memory_id = None
    for result in search_results:
        # Depending on mem0 version, result might be a dict or an object
        content = result.get("memory") if isinstance(result, dict) else getattr(result, "memory", "")
        if "strawberry" in content.lower() or "strawberries" in content.lower():
            memory_id = result.get("id") if isinstance(result, dict) else getattr(result, "id", None)
            break
            
    if memory_id:
        print(f"Found memory_id: {memory_id}")
        # 2. Delete that specific memory using its ID
        m.delete(memory_id)
        print(f"Deleted memory: {memory_id}")
        
        # 3. Add a new memory
        m.add("Charlie is no longer allergic to strawberries", user_id="charlie")
        print("Added new memory: Charlie is no longer allergic to strawberries")
    else:
        print("Memory not found.")

if __name__ == "__main__":
    main()
