import os
import pytest

PROJECT_DIR = "/home/user/mem0_project"

def test_project_directory_exists():
    assert os.path.isdir(PROJECT_DIR), f"Project directory {PROJECT_DIR} does not exist."

def test_mem0_installed():
    try:
        import mem0
    except ImportError:
        pytest.fail("mem0ai library is not installed.")
