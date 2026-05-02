FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl ca-certificates git python3 python3-pip python3-pytest bash && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install --break-system-packages mem0ai openai qdrant-client

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Mem0 environment for testing update of nonexistent memory."

# Container contents:
#   - python3, pip, pytest
#   - mem0ai, openai, qdrant-client installed
#   - /home/user directory

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]