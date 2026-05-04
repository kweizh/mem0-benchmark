# Mem0 Search Score Threshold

## Background
You have a Python script `setup_memories.py` at `/home/user/project` that initializes a `Memory` instance using Mem0 Open Source and adds several memories for `user_id="bob"`. Your task is to write a script `search_mem0.py` that retrieves relevant memories and filters them based on a score threshold.

## Requirements
- Create a script `/home/user/project/search_mem0.py`.
- Initialize `Memory` from `mem0` using the default configuration (which uses Qdrant and OpenAI).
- Search for the query "What are my dietary restrictions?" for `user_id="bob"`.
- Filter the search results, keeping only memories with a `score` strictly greater than `0.6`.
- Write the `memory` text of the matched results to `/home/user/project/high_score_memories.txt`, one per line.

## Constraints
- Project path: `/home/user/project`
- You must use `mem0ai`.

## Integrations
- OpenAI