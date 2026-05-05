from mem0 import Memory

def delete_alice_memories():
    # Initialize the Mem0 Memory client
    m = Memory()
    
    # Delete all memories associated with user_id="alice"
    m.delete_all(user_id="alice")
    print("Deleted all memories for user: alice")

if __name__ == "__main__":
    delete_alice_memories()
