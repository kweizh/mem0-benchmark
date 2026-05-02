import os
import shutil
import subprocess
import pytest

PROJECT_DIR = "/home/user"

def test_python_available():
    assert shutil.which("python") is not None, "python binary not found in PATH."

def test_mem0_installed():
    result = subprocess.run(["python", "-c", "import mem0"], capture_output=True)
    assert result.returncode == 0, "mem0ai is not installed in the Python environment."

def test_project_dir_exists():
    assert os.path.isdir(PROJECT_DIR), f"Project directory {PROJECT_DIR} does not exist."

def test_setup_script_exists():
    script_path = os.path.join(PROJECT_DIR, "setup_memories.py")
    assert os.path.isfile(script_path), f"Setup script {script_path} does not exist."
