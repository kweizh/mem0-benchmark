In the transition to Mem0 OSS v3, external graph stores (like Neo4j) were deprecated in favor of internal "Entity Linking" within the base vector store. Legacy configurations containing graph flags will now cause errors.

You need to refactor a provided legacy v2 Python script (which instantiates Mem0 with `enable_graph: True` and Neo4j credentials) to comply with the v3 architecture. 

**Constraints:**
- Remove all references to Neo4j, graph config dictionaries, and the `enable_graph` flag.
- Do NOT alter the existing LLM and embedding provider configurations in the file.
- The script must successfully initialize the `Memory` object using the updated v3 standard.