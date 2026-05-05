from mem0 import Memory
from config import MEM0_CONFIG
import json

def main():
    # 1. Initialize the Memory instance using the configuration provided in config.py.
    print("Initializing Memory instance...")
    m = Memory.from_config(MEM0_CONFIG)

    user_id = "bob"

    # 2. Add the following initial memories for user_id="bob":
    # - "Bob is allergic to peanuts"
    # - "Bob hates Monday mornings"
    # - "Bob works as a software engineer"
    print(f"Adding initial memories for user_id='{user_id}'...")
    m.add("Bob is allergic to peanuts", user_id=user_id)
    m.add("Bob hates Monday mornings", user_id=user_id)
    m.add("Bob works as a software engineer", user_id=user_id)

    # 3. Search for the memory containing the fact about Bob's peanut allergy.
    print("Searching for peanut allergy memory...")
    search_response = m.search(query="Bob is allergic to peanuts", filters={"user_id": user_id})
    search_results = search_response.get("results", []) if isinstance(search_response, dict) else search_response
    
    allergy_memory_id = None
    for res in search_results:
        txt = res.get("memory") or res.get("text", "")
        if "peanuts" in txt.lower():
            allergy_memory_id = res.get("id")
            break
    
    if allergy_memory_id:
        print(f"Found allergy memory ID: {allergy_memory_id}")
        # 4. Update that specific memory to say "Bob is allergic to peanuts and shellfish"
        print("Updating memory...")
        m.update(memory_id=allergy_memory_id, data="Bob is allergic to peanuts and shellfish")
        print("Updated memory successfully.")
    else:
        print("Could not find peanut allergy memory.")

    # 5. Search for the memory containing the fact that Bob hates Monday mornings.
    print("Searching for Monday mornings memory...")
    search_response_monday = m.search(query="Bob hates Monday mornings", filters={"user_id": user_id})
    search_results_monday = search_response_monday.get("results", []) if isinstance(search_response_monday, dict) else search_response_monday
    
    monday_memory_id = None
    for res in search_results_monday:
        txt = res.get("memory") or res.get("text", "")
        if "monday" in txt.lower():
            monday_memory_id = res.get("id")
            break

    if monday_memory_id:
        print(f"Found Monday morning memory ID: {monday_memory_id}")
        # 6. Delete that specific memory using the delete(memory_id) method.
        print("Deleting memory...")
        m.delete(memory_id=monday_memory_id)
        print("Deleted memory successfully.")
    else:
        print("Could not find Monday morning memory.")

    # 7. Add a new memory "Bob loves to play tennis" for user_id="bob".
    print("Adding tennis memory...")
    m.add("Bob loves to play tennis", user_id=user_id)
    print("Added tennis memory successfully.")

    print("\nProcess completed successfully.")
    
    # Optional: list final memories to verify
    print("Final memories for Bob:")
    get_all_response = m.get_all(filters={"user_id": user_id})
    final_memories = get_all_response.get("results", []) if isinstance(get_all_response, dict) else get_all_response
    for mem in final_memories:
        txt = mem.get("memory") or mem.get("text")
        print(f"- {txt} (ID: {mem.get('id')})")

if __name__ == "__main__":
    main()
