import os
import pytest

PROJECT_DIR = "/home/user/mem0_project"
CONFIG_FILE = os.path.join(PROJECT_DIR, "config.py")

def test_project_dir_exists():
    assert os.path.isdir(PROJECT_DIR), f"Project directory {PROJECT_DIR} does not exist."

def test_config_file_exists():
    assert os.path.isfile(CONFIG_FILE), f"Config file {CONFIG_FILE} does not exist."

def test_mem0_config_is_valid():
    import sys
    sys.path.insert(0, PROJECT_DIR)
    try:
        from config import MEM0_CONFIG
    except ImportError:
        pytest.fail("Could not import MEM0_CONFIG from config.py")
    
    assert "vector_store" in MEM0_CONFIG, "MEM0_CONFIG missing 'vector_store' key."
    assert MEM0_CONFIG["vector_store"]["provider"] == "qdrant", "Expected qdrant vector store."
