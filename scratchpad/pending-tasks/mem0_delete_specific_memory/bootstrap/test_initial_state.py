import os
import shutil
import subprocess
import pytest

PROJECT_DIR = "/home/user/project"

def test_project_dir_exists():
    assert os.path.isdir(PROJECT_DIR), f"Project directory {PROJECT_DIR} does not exist."

def test_setup_script_exists():
    setup_path = os.path.join(PROJECT_DIR, "setup.py")
    assert os.path.isfile(setup_path), f"Setup script {setup_path} does not exist."

def test_mem0_installed():
    # Verify mem0ai is installed by trying to import it
    result = subprocess.run(
        ["python3", "-c", "import mem0"],
        capture_output=True, text=True
    )
    assert result.returncode == 0, f"mem0 package is not installed: {result.stderr}"
