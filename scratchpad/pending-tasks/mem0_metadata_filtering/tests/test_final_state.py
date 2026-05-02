import os
import json
import subprocess
import pytest

PROJECT_DIR = "/home/user/myproject"
OUTPUT_FILE = os.path.join(PROJECT_DIR, "output.json")
SCRIPT_FILE = os.path.join(PROJECT_DIR, "run.py")

@pytest.fixture(scope="module", autouse=True)
def run_script():
    """Run the user's script to generate the output."""
    assert os.path.isfile(SCRIPT_FILE), f"Script {SCRIPT_FILE} does not exist."
    result = subprocess.run(
        ["python3", "run.py"],
        cwd=PROJECT_DIR,
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, f"Script execution failed: {result.stderr}"

def test_output_file_exists():
    assert os.path.isfile(OUTPUT_FILE), f"Output file {OUTPUT_FILE} was not created."

def test_output_contains_correct_memories():
    with open(OUTPUT_FILE, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            pytest.fail(f"Output file {OUTPUT_FILE} is not valid JSON.")
    
    assert isinstance(data, list), "Output should be a list of memories."
    assert len(data) >= 2, f"Expected at least 2 memories in output, found {len(data)}."
    
    # Mem0 extracts facts, so the exact string might vary slightly, but key phrases should be present.
    # We check if the core concepts are in the memories.
    found_marathon = False
    found_stretch = False
    
    for memory in data:
        # The memory text is usually in a 'memory' or 'text' field, depending on the exact format returned.
        # We'll convert the whole dictionary to a string for a robust check.
        mem_str = json.dumps(memory).lower()
        
        if "marathon" in mem_str or "training" in mem_str:
            found_marathon = True
        if "stretch" in mem_str or "remind" in mem_str:
            found_stretch = True
            
    assert found_marathon, "Memory about training for a marathon was not found in the output."
    assert found_stretch, "Memory about stretching before running was not found in the output."