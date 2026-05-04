import os
import sys
import pytest

PROJECT_DIR = "/home/user/mem0_project"
SCRIPT_FILE = os.path.join(PROJECT_DIR, "process_memories.py")

def test_script_exists():
    assert os.path.isfile(SCRIPT_FILE), f"Script file {SCRIPT_FILE} does not exist."

def test_final_memories():
    sys.path.insert(0, PROJECT_DIR)
    
    try:
        from config import MEM0_CONFIG
        from mem0 import Memory
    except ImportError as e:
        pytest.fail(f"Failed to import required modules: {e}")
        
    try:
        m = Memory.from_config(MEM0_CONFIG)
        memories = m.get_all(user_id="bob")
    except Exception as e:
        pytest.fail(f"Failed to initialize Memory or retrieve memories: {e}")
        
    if isinstance(memories, dict) and "results" in memories:
        mem_list = memories["results"]
    else:
        mem_list = memories
        
    if not mem_list:
        pytest.fail("No memories found for user 'bob'.")
        
    texts = []
    for mem in mem_list:
        if isinstance(mem, dict):
            if "memory" in mem:
                texts.append(mem["memory"])
            elif "text" in mem:
                texts.append(mem["text"])
            else:
                texts.append(str(mem))
        else:
            texts.append(str(mem))
            
    joined_texts = " ".join(texts)
    
    assert "allergic to peanuts and shellfish" in joined_texts, \
        f"Expected updated memory about peanut and shellfish allergy. Found: {joined_texts}"
        
    assert "hates Monday mornings" not in joined_texts, \
        "Expected memory about Monday mornings to be deleted, but it was found."
        
    assert "loves to play tennis" in joined_texts, \
        f"Expected new memory about playing tennis. Found: {joined_texts}"
        
    assert "works as a software engineer" in joined_texts, \
        f"Expected original memory about software engineer to be preserved. Found: {joined_texts}"
