Memories in Mem0 are strictly partitioned by entities (e.g., `user_id`, `agent_id`, `app_id`). A common developer mistake is using an `AND` operator when searching for memories shared between a user and an agent, which results in zero matches due to scope isolation.

You need to construct a complex search query using the Mem0 API that successfully retrieves memories belonging to either a specific user (`user_id="bob_99"`) OR a specific agent (`agent_id="support_bot"`). 

**Constraints:**
- Must use a compound logical `OR` filter in the search request.
- Do NOT use an `AND` operator for the entity IDs.
- The output must print the aggregated list of retrieved memory IDs.