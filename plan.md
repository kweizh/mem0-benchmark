# Evaluation Dataset Research: Mem0
Mem0 is a memory layer for AI agents that provides persistent, self-improving context across sessions. It offers two distinct paths: **Mem0 Platform** (managed, low-latency) and **Mem0 Open Source** (self-hosted, infra-controlled).
### 1. Library Overview
*   **Description**: Mem0 (formerly Embedchain's memory component) manages long-term memory for LLMs. It extracts facts from conversations, stores them in a hybrid vector/graph-like structure, and retrieves relevant context for future interactions.
*   **Ecosystem Role**: Sits between the application logic and the LLM. It replaces simple "chat history" buffers with a structured memory layer that scales beyond context window limits.
*   **Project Setup**:
    *   **Platform**: `pip install mem0ai` and initialize with `MemoryClient(api_key="...")`.
    *   **Open Source**: `pip install mem0ai` plus providers (e.g., `qdrant-client`, `openai`). Requires a vector store (default Qdrant) and an LLM/Embedder.
    *   **CLI**: `mem0 configure` to set up default providers.
### 2. Core Primitives & APIs
*   **`add(messages, user_id, ...)`**: Extracts facts from a list of messages and stores them.
*   **`search(query, user_id, ...)`**: Retrieves the most relevant memories for a given query.
*   **`get_all(user_id, ...)`**: Lists all memories for a specific scope.
*   **`update(memory_id, data)`**: Manually updates a memory entry.
*   **`delete(memory_id)`** / **`delete_all(user_id)`**: Removes memories.
**Code Snippet (Platform - Python):**
```python
from mem0 import MemoryClient
client = MemoryClient(api_key="your-api-key")
# Store facts
client.add([{"role": "user", "content": "I am allergic to peanuts"}], user_id="alice")
# Search relevant context
memories = client.search("What should I avoid eating?", user_id="alice")
# Output: [{'id': '...', 'memory': 'Alice is allergic to peanuts', 'score': 0.92}]
```
**Code Snippet (OSS - Python):**
```python
from mem0 import Memory
config = {
    "vector_store": {"provider": "qdrant", "config": {"host": "localhost", "port": 6333}},
    "llm": {"provider": "ollama", "config": {"model": "llama3.1"}}
}
memory = Memory.from_config(config)
memory.add("I love hiking", user_id="bob")
```
*   **Documentation**: [Core Operations](https://docs.mem0.ai/core-concepts/memory-operations/add), [Platform Quickstart](https://docs.mem0.ai/platform/quickstart), [OSS Configuration](https://docs.mem0.ai/open-source/configuration).
### 3. Real-World Use Cases & Templates
*   **AI Companions**: Personal assistants that remember user preferences, injuries (fitness), or learning progress (tutor). [Cookbook](https://docs.mem0.ai/cookbooks/essentials/building-ai-companion).
*   **Multi-Agent Systems**: Agents that share user context but maintain separate "Agent Memories" (personality/instructions). [Multi-Agent Cookbook](https://docs.mem0.ai/cookbooks/frameworks/llamaindex-multiagent).
*   **Customer Support**: Bots that recall past tickets and user history across different sessions. [Support Inbox Cookbook](https://docs.mem0.ai/cookbooks/operations/support-inbox).
### 4. Developer Friction Points
*   **OSS v3 Architectural Shift**: In v3, Mem0 OSS removed external graph store support (Neo4j, etc.) in favor of internal "Entity Linking" within the vector store. Many community tutorials still reference `enable_graph: True`, which now causes errors or is ignored. [Migration Guide](https://docs.mem0.ai/migration/oss-v2-to-v3).*   **Entity Scope Isolation**: Memories are partitioned by `user_id`, `agent_id`, `app_id`, and `run_id`. A common mistake is using `AND` logic in filters for multiple IDs (e.g., `user_id` AND `agent_id`), which returns nothing because records are stored per-entity. Users must use `OR` to retrieve both. [Filter Docs](https://docs.mem0.ai/platform/features/v2-memory-filters#troubleshooting).
*   **API Inconsistencies**: The TypeScript SDK uses camelCase (e.g., `userId`) in some OSS paths but the Platform API expects snake_case (`user_id`).
### 5. Evaluation Ideas
*   **Basic Personalization**: Implement a chat loop that remembers a user's favorite coffee and recalls it in a new session.
*   **Multi-Agent Coordination**: Set up two agents (e.g., a "Coach" and a "NutriBot") that share a `user_id` but have distinct `agent_id` memories for their respective styles.
*   **Complex Filtering**: Retrieve all "fitness" related memories for a user created within the last 30 days using compound logical filters.
*   **OSS Provider Swap**: Configure Mem0 OSS to use Ollama for LLM and ChromaDB for vector storage instead of the defaults.
*   **Migration Task**: Refactor a legacy Mem0 v2 configuration (using Neo4j) to the new v3 "Entity Linking" approach.
*   **Temporal Cleanup**: Implement a script that uses metadata timestamps to find and delete "expired" memories (e.g., a temporary injury that has healed).
*   **Conflict Resolution**: Add a memory that contradicts an existing one (e.g., "I moved from NY to SF") and verify how the system handles the update/search.
### 6. Sources
1. [Mem0 Official Documentation](https://docs.mem0.ai/) - Primary source for API and features.
2. [Mem0 llms.txt](https://docs.mem0.ai/llms.txt) - Structured overview of the entire documentation.
3. [OSS v2 to v3 Migration Guide](https://docs.mem0.ai/migration/oss-v2-to-v3) - Details on the removal of external graph stores.
4. [Mem0 GitHub Repository](https://github.com/mem0ai/mem0) - Source code and integration examples.
5. [Mem0 Cookbooks](https://docs.mem0.ai/cookbooks/overview) - Real-world implementation patterns.
6. [Platform Memory Filters](https://docs.mem0.ai/platform/features/v2-memory-filters) - Documentation on advanced retrieval logic.