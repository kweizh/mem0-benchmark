import os
import json
import pytest

PROJECT_DIR = "/home/user"
QDRANT_DB_DIR = os.path.join(PROJECT_DIR, "qdrant_db")
PROFILE_JSON = os.path.join(PROJECT_DIR, "bob_profile.json")

def test_qdrant_db_exists():
    assert os.path.isdir(QDRANT_DB_DIR), f"Qdrant DB directory {QDRANT_DB_DIR} does not exist."

def test_profile_json_exists():
    assert os.path.isfile(PROFILE_JSON), f"Profile JSON {PROFILE_JSON} does not exist."

def test_profile_json_contents():
    with open(PROFILE_JSON, "r") as f:
        data = json.load(f)
    
    assert "hobbies" in data, "Key 'hobbies' not found in bob_profile.json."
    assert "profession" in data, "Key 'profession' not found in bob_profile.json."
    assert "all_memories" in data, "Key 'all_memories' not found in bob_profile.json."
    
    hobbies = " ".join(data["hobbies"]).lower()
    assert "hiking" in hobbies or "photography" in hobbies, "Expected 'hiking' or 'photography' in hobbies."
    
    profession = " ".join(data["profession"]).lower()
    assert "software engineer" in profession or "developer" in profession, "Expected 'software engineer' or 'developer' in profession."

def test_mem0_api_verify_memories():
    from mem0 import Memory
    
    config = {
        "vector_store": {
            "provider": "qdrant",
            "config": {
                "path": QDRANT_DB_DIR
            }
        }
    }
    
    try:
        m = Memory.from_config(config)
    except Exception as e:
        pytest.fail(f"Failed to initialize Mem0 Memory from {QDRANT_DB_DIR}: {e}")
        
    memories = m.get_all(user_id="bob")
    assert isinstance(memories, list), "Expected m.get_all() to return a list."
    assert len(memories) > 0, "No memories found for user_id='bob'."
    
    all_text = " ".join([mem.get("memory", "").lower() for mem in memories])
    assert "software engineer" in all_text, "Expected 'software engineer' in stored memories."
    assert "hiking" in all_text, "Expected 'hiking' in stored memories."
