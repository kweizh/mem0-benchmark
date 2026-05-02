import os
import subprocess
import pytest

PROJECT_DIR = "/home/user/project"

def test_mem0_installed():
    result = subprocess.run(["python3", "-c", "import mem0"], capture_output=True)
    assert result.returncode == 0, "mem0 package is not installed."

def test_project_dir_exists():
    assert os.path.isdir(PROJECT_DIR), f"Project directory {PROJECT_DIR} does not exist."
