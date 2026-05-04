import os
import pytest

PROJECT_DIR = "/home/user/mem0_project"

def test_mem0_library_importable():
    try:
        import mem0
    except ImportError as e:
        pytest.fail(f"Failed to import mem0: {e}")

def test_project_directory_exists():
    assert os.path.isdir(PROJECT_DIR), f"Project directory {PROJECT_DIR} does not exist."
