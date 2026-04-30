When a user's facts change fundamentally (e.g., moving to a new city), the system needs to update the existing record to prevent conflicting context retrieval in future interactions.

You need to add an initial memory ("I currently live in New York") for a user. Then, simulate processing a new message ("I just moved from NY to SF") by retrieving the original memory's ID via search, and explicitly updating it with the new city. 

**Constraints:**
- Must use the `search` method to dynamically find the `memory_id` of the New York fact.
- Must use the `update(memory_id, data)` method to change the memory's text to reflect San Francisco.
- Do NOT simply use `delete` and `add`; you must modify the record in place.