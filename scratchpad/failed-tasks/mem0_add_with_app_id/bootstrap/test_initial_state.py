import os
import shutil
import pytest

PROJECT_DIR = "/home/user"

def test_mem0_binary_available():
    assert shutil.which("mem0") is not None, "mem0 binary not found in PATH."

def test_working_directory_exists():
    assert os.path.isdir(PROJECT_DIR), f"Project directory {PROJECT_DIR} does not exist."

def test_openai_api_key_set():
    assert "OPENAI_API_KEY" in os.environ, "OPENAI_API_KEY environment variable is not set."