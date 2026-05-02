import os

WORKSPACE_DIR = "/home/user/workspace"
OUTPUT_FILE = os.path.join(WORKSPACE_DIR, "alice_memories.json")
SCRIPT_FILE = os.path.join(WORKSPACE_DIR, "run.py")

def test_workspace_exists():
    assert os.path.isdir(WORKSPACE_DIR), f"Workspace directory {WORKSPACE_DIR} should exist"

def test_output_file_does_not_exist():
    assert not os.path.exists(OUTPUT_FILE), f"Output file {OUTPUT_FILE} should not exist initially"

def test_script_file_does_not_exist():
    assert not os.path.exists(SCRIPT_FILE), f"Script file {SCRIPT_FILE} should not exist initially"
