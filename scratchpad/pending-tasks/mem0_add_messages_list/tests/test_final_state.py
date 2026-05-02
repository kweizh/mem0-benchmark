import os
import json
import pytest

PROJECT_DIR = "/home/user/mem0-project"
SCRIPT_FILE = os.path.join(PROJECT_DIR, "add_messages.py")
OUTPUT_FILE = os.path.join(PROJECT_DIR, "output.json")

def test_script_exists():
    assert os.path.isfile(SCRIPT_FILE), f"Script file not found at {SCRIPT_FILE}"

def test_output_file_exists_and_contains_vegetarian_fact():
    assert os.path.isfile(OUTPUT_FILE), f"Output file not found at {OUTPUT_FILE}"
    
    with open(OUTPUT_FILE, "r") as f:
        try:
            results = json.load(f)
        except json.JSONDecodeError:
            pytest.fail("output.json is not valid JSON")
            
    assert isinstance(results, list), "output.json should contain a JSON array"
    assert len(results) > 0, "output.json array is empty"
    
    # Verify that the fact about being a vegetarian is in the results
    found_vegetarian = False
    for item in results:
        # mem0 search results usually have 'memory' or 'text' field
        memory_text = item.get("memory", "")
        if not memory_text:
            memory_text = item.get("text", "") # fallback if schema varies
            
        if "vegetarian" in memory_text.lower():
            found_vegetarian = True
            break
            
    assert found_vegetarian, "No memory found in output.json indicating that Alice is a vegetarian."
