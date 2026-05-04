import os
import subprocess
import pytest

PROJECT_DIR = "/home/user/mem0_project"
MAIN_FILE = os.path.join(PROJECT_DIR, "main.py")

def test_main_file_exists_and_contains_model():
    """Priority 3 fallback: basic file existence and content check."""
    assert os.path.isfile(MAIN_FILE), f"main.py not found at {MAIN_FILE}"
    
    with open(MAIN_FILE, "r") as f:
        content = f.read()
        
    assert "gpt-4o-mini" in content, "Expected 'gpt-4o-mini' to be configured in main.py"
    assert "qdrant" in content, "Expected 'qdrant' to be configured as vector store provider in main.py"

def test_memory_stored_in_qdrant():
    """Priority 1: Use Python script to query Mem0 and verify the database state."""
    test_script = os.path.join(PROJECT_DIR, "verify_mem0.py")
    script_content = \"\"\"
import json
import sys
from mem0 import Memory

config = {
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "path": "/home/user/mem0_project/qdrant_db"
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
    results = memory.search("learning", user_id="alice")
    # Print results as JSON for the test to parse
    print(json.dumps(results))
except Exception as e:
    print(json.dumps({"error": str(e)}))
    sys.exit(1)
\"\"\"
    with open(test_script, "w") as f:
        f.write(script_content)
        
    result = subprocess.run(
        ["python3", "verify_mem0.py"],
        capture_output=True,
        text=True,
        cwd=PROJECT_DIR
    )
    
    assert result.returncode == 0, f"Verification script failed: {result.stderr}"
    
    import json
    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError:
        pytest.fail(f"Failed to parse output as JSON: {result.stdout}")
        
    if isinstance(data, dict) and "error" in data:
        pytest.fail(f"Mem0 search raised an error: {data['error']}")
        
    assert isinstance(data, list), f"Expected list of results, got: {data}"
    assert len(data) > 0, "No memories found for query 'learning' and user 'alice'"
    
    # Check if the memory contains the expected string
    found = False
    for item in data:
        memory_text = item.get("memory", "")
        if "learning how to build AI agents" in memory_text.lower() or "learning" in memory_text.lower():
            found = True
            break
            
    assert found, f"Expected to find memory about learning to build AI agents, got: {data}"