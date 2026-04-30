Agent memories can contain temporary states (like a short-term illness or a temporary address) that should not persist indefinitely. Mem0 allows attaching metadata to stored facts for lifecycle management.

You need to implement a Python cleanup script that fetches all memories for a given user, checks their attached metadata for an `expires_at` Unix timestamp, and deletes the memory if the timestamp is in the past. 

**Constraints:**
- Must use `get_all(user_id="athlete_01")` to retrieve the user's memories.
- Must use the `delete(memory_id)` core primitive to remove expired entries.
- Do NOT delete memories that lack the `expires_at` metadata field.