import os
import pytest
import subprocess

PROJECT_DIR = "/home/user/mem0_project"

def test_project_directory_exists():
    assert os.path.isdir(PROJECT_DIR), f"Project directory {PROJECT_DIR} does not exist."

def test_mem0_installed():
    result = subprocess.run(
        ["python3", "-c", "import mem0"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, "mem0 is not installed or cannot be imported in Python."

def test_openai_api_key_set():
    assert "OPENAI_API_KEY" in os.environ, "OPENAI_API_KEY environment variable is not set."