import os
import subprocess
import pytest

PROJECT_DIR = "/home/user"
SCRIPT_FILE = os.path.join(PROJECT_DIR, "test_update.py")
OUTPUT_FILE = os.path.join(PROJECT_DIR, "output.txt")

def test_script_exists():
    """Priority 3: Check if the script exists."""
    assert os.path.isfile(SCRIPT_FILE), f"Script not found at {SCRIPT_FILE}"

def test_script_execution_and_output():
    """Priority 3: Run the script and check output file."""
    # Run the script to generate the output
    result = subprocess.run(
        ["python3", "test_update.py"],
        cwd=PROJECT_DIR,
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, f"Script execution failed: {result.stderr}"
    
    assert os.path.isfile(OUTPUT_FILE), f"Output file not found at {OUTPUT_FILE}"
    
    with open(OUTPUT_FILE, "r") as f:
        content = f.read().strip()
        
    assert len(content) > 0, "Output file is empty. Expected exception message or return value."
