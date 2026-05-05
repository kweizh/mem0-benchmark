from mem0 import Memory
import os

def test_update_nonexistent():
    m = Memory()
    memory_id = "nonexistent_memory_id_999"
    data = "I like green apples"
    
    try:
        result = m.update(memory_id, data)
        output = str(result)
    except Exception as e:
        output = str(e)
    
    with open("/home/user/output.txt", "w") as f:
        f.write(output)

if __name__ == "__main__":
    test_update_nonexistent()
