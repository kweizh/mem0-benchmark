import os
import subprocess
import pytest

PROJECT_DIR = "/home/user/myproject"

def test_project_dir_exists():
    assert os.path.isdir(PROJECT_DIR), f"Project directory {PROJECT_DIR} does not exist."

def test_mem0ai_installed():
    try:
        subprocess.run(["python3", "-c", "import mem0"], check=True, capture_output=True)
    except subprocess.CalledProcessError:
        pytest.fail("mem0ai package is not installed.")