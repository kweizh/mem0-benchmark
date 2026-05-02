import os
import subprocess
import json
import pytest

PROJECT_DIR = "/home/user/mem0_project"
SCRIPT_PATH = os.path.join(PROJECT_DIR, "memory_ops.py")
RESULTS_PATH = os.path.join(PROJECT_DIR, "search_results.json")

def test_script_exists():
    assert os.path.isfile(SCRIPT_PATH), f"Script not found at {SCRIPT_PATH}"

def test_script_execution():
    result = subprocess.run(
        ["python3", "memory_ops.py"],
        capture_output=True, text=True, cwd=PROJECT_DIR
    )
    assert result.returncode == 0, f"Script execution failed: {result.stderr}"

def test_results_file_exists():
    assert os.path.isfile(RESULTS_PATH), f"Results file not found at {RESULTS_PATH}"

def test_results_contain_memory():
    with open(RESULTS_PATH, 'r') as f:
        try:
            results = json.load(f)
        except json.JSONDecodeError:
            pytest.fail(f"{RESULTS_PATH} is not valid JSON.")
    
    content_str = json.dumps(results).lower()
    assert "peanut" in content_str, "Expected search results to contain information about peanuts."
