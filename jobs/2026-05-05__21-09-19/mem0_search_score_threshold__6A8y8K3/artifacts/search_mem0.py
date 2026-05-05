from mem0 import Memory

def main():
    # Initialize Memory from mem0 using the default configuration
    memory = Memory()
    
    # Search for the query "What are my dietary restrictions?" for user_id="bob"
    query = "What are my dietary restrictions?"
    
    # Search for memories. In mem0ai 2.x, user_id should be passed in filters.
    # We use a try-except or check for compatibility if needed, but here we 
    # follow the error message recommendation from earlier.
    try:
        search_results = memory.search(query, filters={"user_id": "bob"})
    except ValueError:
        # Fallback for older versions if filters is not supported
        search_results = memory.search(query, user_id="bob")
    
    # Handle the return type which can be a dict {'results': [...]} or a list
    if isinstance(search_results, dict):
        results = search_results.get('results', [])
    else:
        results = search_results
    
    # Filter search results, keeping only memories with a score strictly greater than 0.6
    high_score_memories = []
    for res in results:
        score = res.get('score', 0)
        if score > 0.6:
            # The memory text is typically stored in the 'memory' key
            mem_text = res.get('memory')
            if mem_text:
                high_score_memories.append(mem_text)
    
    # Write the memory text of the matched results to high_score_memories.txt, one per line
    output_path = "/home/user/project/high_score_memories.txt"
    with open(output_path, "w") as f:
        for mem in high_score_memories:
            f.write(mem + "\n")

if __name__ == "__main__":
    main()
