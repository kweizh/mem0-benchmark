import os
import subprocess
import pytest

SCRIPT_PATH = "/home/user/myproject/run.py"

def test_script_exists():
    assert os.path.isfile(SCRIPT_PATH), f"Script not found at {SCRIPT_PATH}"

def test_script_execution_and_output():
    """Run the script and verify it outputs the retrieved memory."""
    env = os.environ.copy()
    # MEM0_API_KEY must be provided in the verifier environment.
    assert "MEM0_API_KEY" in env, "MEM0_API_KEY environment variable is not set in the verifier environment."
    
    result = subprocess.run(
        ["python3", SCRIPT_PATH],
        capture_output=True,
        text=True,
        cwd="/home/user/myproject",
        env=env
    )
    
    assert result.returncode == 0, f"Script execution failed with error: {result.stderr}"
    
    output = result.stdout.lower()
    assert "learning" in output and "mem0" in output, \
        f"Expected the output to contain the retrieved memory about learning Mem0, got: {result.stdout}"
