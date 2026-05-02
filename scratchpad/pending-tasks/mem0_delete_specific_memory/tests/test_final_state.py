import os
import subprocess
import json
import pytest

PROJECT_DIR = "/home/user/project"

def test_update_memory_script_exists():
    script_path = os.path.join(PROJECT_DIR, "update_memory.py")
    assert os.path.isfile(script_path), f"update_memory.py not found at {script_path}"

def test_mem0_final_state():
    # We will write a small python script to check the memory state
    # using the same config as setup.py
    checker_script = os.path.join(PROJECT_DIR, "verify_state.py")
    with open(checker_script, "w") as f:
        f.write("""
import json
from mem0 import Memory

config = {
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "path": "/home/user/project/qdrant_db"
        }
    }
}

def main():
    m = Memory.from_config(config)
    memories = m.get_all(user_id="charlie")
    # memories is typically a list of dicts, or a dict containing a list
    # Let's extract the text of the memories
    results = []
    if isinstance(memories, list):
        items = memories
    elif isinstance(memories, dict) and "results" in memories:
        items = memories["results"]
    else:
        items = memories
        
    for item in items:
        if isinstance(item, dict) and "memory" in item:
            results.append(item["memory"])
        elif hasattr(item, "memory"):
            results.append(item.memory)
        else:
            results.append(str(item))
            
    print(json.dumps(results))

if __name__ == "__main__":
    main()
""")
    
    result = subprocess.run(
        ["python3", "verify_state.py"],
        capture_output=True, text=True, cwd=PROJECT_DIR
    )
    assert result.returncode == 0, f"Failed to run verification script: {result.stderr}"
    
    try:
        memories = json.loads(result.stdout)
    except json.JSONDecodeError:
        pytest.fail(f"Failed to parse memories JSON: {result.stdout}")
        
    # Check that the deleted memory is gone
    assert not any("is allergic to strawberries" in m for m in memories if "no longer" not in m), \
        "The memory 'Charlie is allergic to strawberries' should have been deleted."
        
    # Check that the new memory is present
    assert any("no longer allergic to strawberries" in m.lower() for m in memories), \
        "The new memory 'Charlie is no longer allergic to strawberries' was not found."
        
    # Check that the preserved memory is still there
    assert any("tennis" in m.lower() for m in memories), \
        "The preserved memory 'Charlie loves playing tennis' was not found."
