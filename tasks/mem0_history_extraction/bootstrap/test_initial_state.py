import os
import json
import pytest
import subprocess

PROJECT_DIR = "/home/user"
CHAT_LOGS_DIR = os.path.join(PROJECT_DIR, "chat_logs")
SESSION1_PATH = os.path.join(CHAT_LOGS_DIR, "session1.json")
SESSION2_PATH = os.path.join(CHAT_LOGS_DIR, "session2.json")

def test_openai_api_key_set():
    assert "OPENAI_API_KEY" in os.environ, "OPENAI_API_KEY environment variable is not set."

def test_chat_logs_exist():
    assert os.path.isdir(CHAT_LOGS_DIR), f"Chat logs directory {CHAT_LOGS_DIR} does not exist."
    assert os.path.isfile(SESSION1_PATH), f"Chat log file {SESSION1_PATH} does not exist."
    assert os.path.isfile(SESSION2_PATH), f"Chat log file {SESSION2_PATH} does not exist."

def test_session1_content():
    with open(SESSION1_PATH, "r") as f:
        data = json.load(f)
    assert isinstance(data, list)
    assert len(data) > 0
    assert "software engineer" in data[0].get("content", ""), "Expected 'software engineer' in session1.json content."

def test_session2_content():
    with open(SESSION2_PATH, "r") as f:
        data = json.load(f)
    assert isinstance(data, list)
    assert len(data) > 0
    assert "hiking" in data[0].get("content", ""), "Expected 'hiking' in session2.json content."

def test_mem0_installed():
    result = subprocess.run(
        ["python3", "-c", "import mem0"],
        capture_output=True, text=True
    )
    assert result.returncode == 0, f"mem0 package is not installed or import failed: {result.stderr}"
