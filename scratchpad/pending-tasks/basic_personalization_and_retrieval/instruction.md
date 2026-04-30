Mem0 acts as a long-term memory layer for AI agents, allowing them to persistently remember facts across sessions. The Mem0 Platform API handles memory extraction and retrieval seamlessly.

You need to write a Python script that initializes the Mem0 Platform client, adds a specific user fact ("I am allergic to peanuts"), and executes a search query for "What are my dietary restrictions?". 

**Constraints:**
- Must use the official `MemoryClient` from `mem0ai`.
- You must tie both the `add` and `search` operations to the `user_id` set to `alice_123`.
- Output the `memory` text of the highest-scoring search result.