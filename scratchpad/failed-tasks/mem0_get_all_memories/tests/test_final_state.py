import os
import json
import pytest

WORKSPACE_DIR = "/home/user/workspace"
OUTPUT_FILE = os.path.join(WORKSPACE_DIR, "alice_memories.json")

def test_output_file_exists():
    """Priority 3: Check if the JSON output file exists."""
    assert os.path.isfile(OUTPUT_FILE), f"Output file not found at {OUTPUT_FILE}"

def test_memories_in_output_file():
    """Priority 3: Check if the output file contains the required memories."""
    with open(OUTPUT_FILE, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            pytest.fail(f"Failed to parse {OUTPUT_FILE} as JSON")
    
    # mem0 get_all returns a dictionary with 'results' key containing the memories in newer versions,
    # or a list of dictionaries in older versions. Let's handle both or just search the strings in the dump.
    # We can just convert the whole JSON to string and check if the texts are in it.
    json_str = json.dumps(data)
    
    expected_texts = [
        "Alice is allergic to peanuts.",
        "Alice loves hiking.",
        "Alice's favorite color is blue."
    ]
    
    for text in expected_texts:
        assert text in json_str, f"Expected memory text '{text}' not found in {OUTPUT_FILE}"
