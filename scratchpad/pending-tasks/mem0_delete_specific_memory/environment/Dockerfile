FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl ca-certificates git python3 python3-pip python3-pytest bash && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install --break-system-packages mem0ai openai qdrant-client

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Mem0 OSS environment with a setup script to initialize memories."

RUN mkdir -p /home/user/project && \
    cd /home/user/project && \
    cat >setup.py <<'EOF'
import os
from mem0 import Memory

config = {
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "path": "/home/user/project/qdrant_db"
        }
    }
}

def main():
    m = Memory.from_config(config)
    m.add("Charlie loves playing tennis", user_id="charlie")
    m.add("Charlie is allergic to strawberries", user_id="charlie")
    m.add("Charlie works as a software engineer", user_id="charlie")
    print("Memories added successfully.")

if __name__ == "__main__":
    main()
EOF

# Container contents:
#   - mem0ai, openai, qdrant-client installed.
#   - /home/user/project with setup.py
#   - setup.py initializes Mem0 with a local Qdrant path for persistence.

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
