import os
import subprocess
import pytest
import json

def test_alice_memories_deleted_and_bob_intact():
    script = """
import sys
import json
from mem0 import Memory

try:
    m = Memory()
    alice_memories = m.get_all(user_id="alice")
    bob_memories = m.get_all(user_id="bob")
    
    # get_all might return a list or a dict with 'results'
    if isinstance(alice_memories, dict) and "results" in alice_memories:
        alice_count = len(alice_memories["results"])
    else:
        alice_count = len(alice_memories) if alice_memories else 0

    if isinstance(bob_memories, dict) and "results" in bob_memories:
        bob_count = len(bob_memories["results"])
    else:
        bob_count = len(bob_memories) if bob_memories else 0

    print(json.dumps({"alice_count": alice_count, "bob_count": bob_count}))
except Exception as e:
    print(json.dumps({"error": str(e)}))
    sys.exit(1)
"""
    script_path = "/tmp/verify_memories.py"
    with open(script_path, "w") as f:
        f.write(script)

    result = subprocess.run(["python3", script_path], capture_output=True, text=True)
    assert result.returncode == 0, f"Failed to run verification script. stderr: {result.stderr}\nstdout: {result.stdout}"
    
    try:
        output = json.loads(result.stdout)
    except json.JSONDecodeError:
        pytest.fail(f"Failed to parse JSON output. stdout: {result.stdout}")
        
    if "error" in output:
        pytest.fail(f"Error checking memories: {output['error']}")
        
    assert output["alice_count"] == 0, f"Expected 0 memories for alice, but found {output['alice_count']}."
    assert output["bob_count"] > 0, f"Expected >0 memories for bob, but found {output['bob_count']}. Bob's memories should not have been deleted."
