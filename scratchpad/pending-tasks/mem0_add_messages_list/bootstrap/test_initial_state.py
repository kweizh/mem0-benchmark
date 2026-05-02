import os
import shutil
import pytest

PROJECT_DIR = "/home/user/mem0-project"

def test_project_dir_exists():
    assert os.path.isdir(PROJECT_DIR), f"Project directory {PROJECT_DIR} does not exist."

def test_mem0_installed():
    # Since mem0 is a python package, we can check if it's importable or if pip shows it
    import importlib.util
    spec = importlib.util.find_spec("mem0")
    assert spec is not None, "mem0 package is not installed."
