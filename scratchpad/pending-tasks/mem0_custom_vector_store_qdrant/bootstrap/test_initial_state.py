import os
import subprocess
import pytest
import urllib.request
import urllib.error

PROJECT_DIR = "/home/user"

def test_mem0_installed():
    try:
        import mem0
    except ImportError:
        pytest.fail("mem0 is not installed in the Python environment.")

def test_qdrant_running():
    try:
        response = urllib.request.urlopen("http://localhost:6333/")
        assert response.getcode() == 200, "Qdrant is not returning 200 OK."
    except urllib.error.URLError as e:
        pytest.fail(f"Failed to connect to Qdrant on port 6333: {e}")

def test_project_dir_exists():
    assert os.path.isdir(PROJECT_DIR), f"Project directory {PROJECT_DIR} does not exist."
