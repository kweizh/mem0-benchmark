FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl ca-certificates git python3 python3-pip python3-pytest bash && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install --break-system-packages mem0ai openai qdrant-client

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Mem0 task environment for deleting user memories."

RUN cat >/home/user/setup_memories.py <<'EOF'
from mem0 import Memory

m = Memory()
m.add("I am allergic to peanuts", user_id="alice")
m.add("I love hiking", user_id="bob")
print("Memories populated.")
EOF

# Container contents:
#   - mem0ai, openai, and qdrant-client installed
#   - /home/user/setup_memories.py to populate initial memories

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
