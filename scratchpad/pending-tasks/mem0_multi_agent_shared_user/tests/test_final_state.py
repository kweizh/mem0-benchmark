import os
import subprocess
import json
import pytest

PROJECT_DIR = "/home/user/mem0-project"
COACH_RESULTS = os.path.join(PROJECT_DIR, "coach_results.json")
NUTRIBOT_RESULTS = os.path.join(PROJECT_DIR, "nutribot_results.json")

@pytest.fixture(scope="module", autouse=True)
def run_script():
    script_path = os.path.join(PROJECT_DIR, "multi_agent.py")
    assert os.path.isfile(script_path), f"Script {script_path} does not exist."
    
    result = subprocess.run(
        ["python3", "multi_agent.py"],
        cwd=PROJECT_DIR,
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, f"Script execution failed:\nSTDOUT: {result.stdout}\nSTDERR: {result.stderr}"

def test_coach_results():
    assert os.path.isfile(COACH_RESULTS), f"{COACH_RESULTS} was not created."
    with open(COACH_RESULTS, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            pytest.fail(f"{COACH_RESULTS} is not valid JSON.")
    
    assert isinstance(data, list), "Expected coach_results.json to contain a JSON array."
    
    texts = " ".join(data).lower()
    
    assert "vegetarian" in texts and "allergic to nuts" in texts, \
        "Alice's user memory was not found in coach_results.json."
    assert "fitness coach" in texts and "push their limits" in texts, \
        "Coach's agent memory was not found in coach_results.json."
    assert "nutritionist" not in texts, \
        "NutriBot's agent memory should NOT be in coach_results.json."

def test_nutribot_results():
    assert os.path.isfile(NUTRIBOT_RESULTS), f"{NUTRIBOT_RESULTS} was not created."
    with open(NUTRIBOT_RESULTS, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            pytest.fail(f"{NUTRIBOT_RESULTS} is not valid JSON.")
    
    assert isinstance(data, list), "Expected nutribot_results.json to contain a JSON array."
    
    texts = " ".join(data).lower()
    
    assert "vegetarian" in texts and "allergic to nuts" in texts, \
        "Alice's user memory was not found in nutribot_results.json."
    assert "nutritionist" in texts and "high-protein" in texts, \
        "NutriBot's agent memory was not found in nutribot_results.json."
    assert "fitness coach" not in texts, \
        "Coach's agent memory should NOT be in nutribot_results.json."
