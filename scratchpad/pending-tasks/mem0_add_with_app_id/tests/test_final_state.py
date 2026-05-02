import os
import subprocess
import pytest

SCRIPT_FILE = "/home/user/add_memory.py"

def test_script_exists():
    """Priority 3 fallback: basic file existence check."""
    assert os.path.isfile(SCRIPT_FILE), f"Script not found at {SCRIPT_FILE}"

def test_memories_added():
    """Priority 3: Check internal state using a verification script."""
    verify_script = "/home/user/verify_memory.py"
    script_content = """import sys
from mem0 import Memory

try:
    m = Memory()
    
    # Check travel-planner
    travel_memories = m.search("Japan", user_id="alice", app_id="travel-planner")
    if not any("Japan" in mem.get("memory", "") for mem in travel_memories):
        print("Error: Japan trip memory not found for travel-planner app")
        sys.exit(1)
        
    # Check recipe-finder
    recipe_memories = m.search("spicy food", user_id="alice", app_id="recipe-finder")
    if not any("spicy food" in mem.get("memory", "") for mem in recipe_memories):
        print("Error: Spicy food memory not found for recipe-finder app")
        sys.exit(1)
        
    print("Success")
except Exception as e:
    print(f"Error: {str(e)}")
    sys.exit(1)
"""
    with open(verify_script, "w") as f:
        f.write(script_content)
        
    result = subprocess.run(
        ["python3", verify_script],
        capture_output=True, text=True, cwd="/home/user"
    )
    
    assert result.returncode == 0, f"Memory verification failed: {result.stdout} {result.stderr}"
    assert "Success" in result.stdout, f"Expected Success in output, got: {result.stdout}"
