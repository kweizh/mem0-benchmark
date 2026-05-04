import os
import json
import pytest

PROJECT_DIR = "/home/user/mem0_project"
ALICE_FILE = os.path.join(PROJECT_DIR, "alice_memories.json")
BOB_FILE = os.path.join(PROJECT_DIR, "bob_memories.json")

def test_alice_memories_file_exists():
    """Priority 3: Check if alice_memories.json exists."""
    assert os.path.isfile(ALICE_FILE), f"Expected file {ALICE_FILE} does not exist."

def test_bob_memories_file_exists():
    """Priority 3: Check if bob_memories.json exists."""
    assert os.path.isfile(BOB_FILE), f"Expected file {BOB_FILE} does not exist."

def test_alice_memories_content():
    """Priority 3: Verify Alice's memories contain peanut allergy but not vegetarianism."""
    with open(ALICE_FILE, "r") as f:
        raw_content = f.read()
    
    try:
        data = json.loads(raw_content)
        content = json.dumps(data).lower()
    except json.JSONDecodeError:
        content = raw_content.lower()
    
    assert "peanut" in content, "Expected Alice's memories to contain 'peanut'."
    assert "vegetarian" not in content, "Alice's memories should NOT contain 'vegetarian'."

def test_bob_memories_content():
    """Priority 3: Verify Bob's memories contain vegetarianism but not peanut allergy."""
    with open(BOB_FILE, "r") as f:
        raw_content = f.read()
        
    try:
        data = json.loads(raw_content)
        content = json.dumps(data).lower()
    except json.JSONDecodeError:
        content = raw_content.lower()
    
    assert "vegetarian" in content, "Expected Bob's memories to contain 'vegetarian'."
    assert "peanut" not in content, "Bob's memories should NOT contain 'peanut'."
