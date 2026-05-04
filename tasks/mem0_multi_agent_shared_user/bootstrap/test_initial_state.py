import os
import shutil
import subprocess
import pytest

PROJECT_DIR = "/home/user/mem0-project"

def test_mem0_installed():
    # Mem0 provides a CLI, or we can check if it's importable
    result = subprocess.run(["python3", "-c", "import mem0"], capture_output=True)
    assert result.returncode == 0, "mem0 Python package is not installed."

def test_project_dir_exists():
    assert os.path.isdir(PROJECT_DIR), f"Project directory {PROJECT_DIR} does not exist."
