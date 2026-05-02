import os
import pytest
from mem0 import Memory

APP_FILE = "/home/user/app.py"
OUTPUT_FILE = "/home/user/output.txt"

def test_app_file_exists():
    """Priority 3: Check if the app.py script was created."""
    assert os.path.isfile(APP_FILE), f"app.py not found at {APP_FILE}"

def test_output_file_content():
    """Priority 3: Check if the output.txt file exists and contains the correct memory text."""
    assert os.path.isfile(OUTPUT_FILE), f"output.txt not found at {OUTPUT_FILE}"
    with open(OUTPUT_FILE, "r") as f:
        content = f.read().lower()
    assert "hiking" in content, f"Expected 'hiking' in output.txt, but got: {content}"

def test_qdrant_contains_memory():
    """Priority 1/3: Verify the memory was actually saved to the local Qdrant instance using Mem0."""
    config = {
        "vector_store": {
            "provider": "qdrant",
            "config": {
                "host": "localhost",
                "port": 6333
            }
        },
        "llm": {
            "provider": "openai",
            "config": {
                "model": "gpt-4o-mini"
            }
        }
    }
    
    try:
        memory = Memory.from_config(config)
        memories = memory.get_all(user_id="bob")
        
        found = False
        if memories and isinstance(memories, list):
            for mem in memories:
                if isinstance(mem, dict) and "memory" in mem:
                    if "hiking" in mem["memory"].lower():
                        found = True
                        break
        
        assert found, f"Memory about 'hiking' for user 'bob' was not found in the Qdrant vector store. Retrieved memories: {memories}"
    except Exception as e:
        pytest.fail(f"Failed to connect to Qdrant or retrieve memories via Mem0: {e}")
