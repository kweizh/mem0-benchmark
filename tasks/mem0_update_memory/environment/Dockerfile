FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl ca-certificates git python3 python3-pip python3-pytest bash && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install --break-system-packages mem0ai qdrant-client openai

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Mem0 project with qdrant vector store configuration."

RUN mkdir -p /home/user/mem0_project/qdrant_db && \
    cd /home/user/mem0_project && \
    cat >config.py <<'EOF'
import os

MEM0_CONFIG = {
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "path": "/home/user/mem0_project/qdrant_db"
        }
    }
}
EOF

# Container contents:
#   - mem0ai, qdrant-client, openai installed.
#   - /home/user/mem0_project  — mem0 project with config.py
#   - config.py with MEM0_CONFIG

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
