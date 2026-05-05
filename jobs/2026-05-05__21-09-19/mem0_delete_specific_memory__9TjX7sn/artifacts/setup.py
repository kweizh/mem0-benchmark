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
    m.add("Charlie loves playing tennis", user_id="charlie")
    m.add("Charlie is allergic to strawberries", user_id="charlie")
    m.add("Charlie works as a software engineer", user_id="charlie")
    print("Memories added successfully.")

if __name__ == "__main__":
    main()
