import os
import json
import pytest

RESULTS_FILE = "/home/user/project/results.json"

def test_results_file_exists():
    """Priority 3 fallback: basic file existence check."""
    assert os.path.isfile(RESULTS_FILE), f"Results file not found at {RESULTS_FILE}"

def test_results_length_is_two():
    """Priority 3 fallback: parse JSON output to verify length."""
    with open(RESULTS_FILE, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            pytest.fail(f"File {RESULTS_FILE} is not valid JSON.")
            
    assert isinstance(data, list), f"Expected a JSON list in {RESULTS_FILE}, got {type(data)}."
    assert len(data) == 2, f"Expected exactly 2 results, got {len(data)}."

def test_results_contain_tennis():
    """Priority 3 fallback: parse JSON output to verify content."""
    with open(RESULTS_FILE, "r") as f:
        data = json.load(f)
        
    found_tennis = False
    for item in data:
        # The memory text could be in item['memory'] or item['text'] depending on mem0 version,
        # but we can just check if 'tennis' is in the string representation of the item
        if "tennis" in json.dumps(item).lower():
            found_tennis = True
            break
            
    assert found_tennis, "Expected to find 'tennis' in the search results."
