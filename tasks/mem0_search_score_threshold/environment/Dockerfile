FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl ca-certificates git python3 python3-pip python3-pytest bash && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install --break-system-packages mem0ai openai qdrant-client

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Mem0 environment with setup script for adding memories."

RUN mkdir -p /home/user/project && \
    cd /home/user/project && \
    cat >setup_memories.py <<'EOF'
import os
from mem0 import Memory

def main():
    memory = Memory()
    memory.add("I am allergic to peanuts", user_id="bob")
    memory.add("I love hiking", user_id="bob")
    memory.add("My favorite color is blue", user_id="bob")

if __name__ == "__main__":
    main()
EOF

# Container contents:
#   - mem0ai, openai, qdrant-client installed
#   - /home/user/project  — project directory
#   - /home/user/project/setup_memories.py — script to add initial memories

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
