import os
import subprocess
import pytest

PROJECT_DIR = "/home/user/project"

def test_scripts_run_successfully():
    """Priority 1: Run the setup and search scripts to verify they work."""
    setup_result = subprocess.run(
        ["python3", "setup_memories.py"],
        capture_output=True, text=True, cwd=PROJECT_DIR
    )
    assert setup_result.returncode == 0, f"setup_memories.py failed: {setup_result.stderr}"

    search_result = subprocess.run(
        ["python3", "search_mem0.py"],
        capture_output=True, text=True, cwd=PROJECT_DIR
    )
    assert search_result.returncode == 0, f"search_mem0.py failed: {search_result.stderr}"

def test_output_file_exists_and_contains_correct_memory():
    """Priority 3: Verify the output file contains the correct filtered memory."""
    output_file = os.path.join(PROJECT_DIR, "high_score_memories.txt")
    assert os.path.isfile(output_file), f"Output file {output_file} does not exist."

    with open(output_file, "r") as f:
        content = f.read()

    assert "I am allergic to peanuts" in content, \
        f"Expected 'I am allergic to peanuts' in {output_file}, got: {content}"
    assert "I love hiking" not in content, \
        f"Did not expect 'I love hiking' in {output_file}, but it was present."
    assert "My favorite color is blue" not in content, \
        f"Did not expect 'My favorite color is blue' in {output_file}, but it was present."
