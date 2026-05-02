import os
import subprocess
import json
import pytest

PROJECT_DIR = "/home/user"
APP_FILE = os.path.join(PROJECT_DIR, "app.py")
RESULTS_FILE = os.path.join(PROJECT_DIR, "results.json")

def test_app_script_exists():
    """Priority 3: Check if the app script was created."""
    assert os.path.isfile(APP_FILE), f"Script not found at {APP_FILE}"

def test_app_execution_and_results():
    """Priority 1/3: Run the script and verify the output file."""
    # Run the script
    result = subprocess.run(
        ["python3", "app.py"],
        cwd=PROJECT_DIR,
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, f"Script execution failed with error: {result.stderr}"

    # Verify the results file exists
    assert os.path.isfile(RESULTS_FILE), f"Results file not found at {RESULTS_FILE}"

    # Verify the results content
    with open(RESULTS_FILE, "r") as f:
        try:
            results = json.load(f)
        except json.JSONDecodeError:
            pytest.fail(f"Failed to parse {RESULTS_FILE} as JSON.")

    assert isinstance(results, list), "Expected results to be a JSON array."
    assert len(results) >= 2, f"Expected at least 2 results, got {len(results)}."

    # Check if both memories are present in the results
    found_knee_injury = False
    found_swimming = False

    for item in results:
        # Depending on the exact structure returned by Mem0, the text might be in 'memory' or 'text'
        memory_text = ""
        if isinstance(item, dict):
            memory_text = str(item.get("memory", item.get("text", ""))).lower()
        elif isinstance(item, str):
            memory_text = item.lower()

        if "knee" in memory_text or "injury" in memory_text:
            found_knee_injury = True
        if "swim" in memory_text:
            found_swimming = True

    assert found_knee_injury, "Could not find the 'knee injury' memory in the search results."
    assert found_swimming, "Could not find the 'swimming' memory in the search results."
