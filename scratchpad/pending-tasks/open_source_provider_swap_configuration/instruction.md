Mem0 Open Source allows developers to override default components (like Qdrant) with alternative vector stores and LLM providers via a configuration dictionary. 

You need to initialize a Mem0 OSS `Memory` instance configured to use ChromaDB as the vector storage provider and Ollama (specifically the `llama3.1` model) as the LLM provider. 

**Constraints:**
- Do NOT use the default Qdrant vector store.
- Initialize the system using the `Memory.from_config(config)` method.
- The Python script must successfully instantiate the memory layer without requiring external API keys (simulating a fully local environment).