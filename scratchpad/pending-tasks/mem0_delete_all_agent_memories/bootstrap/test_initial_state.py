import os
import subprocess
import pytest

PROJECT_DIR = "/home/user/mem0-project"

def test_project_dir_exists():
    assert os.path.isdir(PROJECT_DIR), f"Project directory {PROJECT_DIR} does not exist."

def test_mem0_installed():
    try:
        # Check if mem0 is installed in the python environment
        subprocess.run(["python", "-c", "import mem0"], check=True, capture_output=True)
    except subprocess.CalledProcessError:
        pytest.fail("mem0 library is not installed in the Python environment.")
