import os
import subprocess
import pytest

PROJECT_DIR = "/home/user/mem0-project"
SCRIPT_PATH = os.path.join(PROJECT_DIR, "delete_memories.py")
LOG_PATH = os.path.join(PROJECT_DIR, "output.log")

def test_script_exists():
    assert os.path.isfile(SCRIPT_PATH), f"Script {SCRIPT_PATH} does not exist."

def test_script_execution_and_output():
    # Run the script
    result = subprocess.run(
        ["python", "delete_memories.py"],
        cwd=PROJECT_DIR,
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, f"Script execution failed: {result.stderr}"

    # Check the log file
    assert os.path.isfile(LOG_PATH), f"Log file {LOG_PATH} does not exist after running the script."
    
    with open(LOG_PATH, "r") as f:
        content = f.read().strip()
    
    # The support agent memories should be at least 1
    try:
        count = int(content)
        assert count > 0, f"Expected remaining support agent memories to be > 0, got {count}"
    except ValueError:
        pytest.fail(f"Log file content is not a valid integer: '{content}'")

def test_travel_agent_memories_deleted():
    # We can use a short python snippet to verify using mem0
    verify_script = """
from mem0 import Memory
memory = Memory()
travel_mems = memory.get_all(agent_id='travel-agent')
support_mems = memory.get_all(agent_id='support-agent')

if travel_mems:
    print(f"FAILED: Found travel agent memories: {travel_mems}")
    exit(1)
if not support_mems:
    print("FAILED: No support agent memories found")
    exit(1)
print("SUCCESS")
"""
    verify_path = os.path.join(PROJECT_DIR, "verify_memories.py")
    with open(verify_path, "w") as f:
        f.write(verify_script)

    result = subprocess.run(
        ["python", "verify_memories.py"],
        cwd=PROJECT_DIR,
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, f"Verification of memories failed: {result.stdout} {result.stderr}"
    assert "SUCCESS" in result.stdout, "Verification script did not output SUCCESS."
