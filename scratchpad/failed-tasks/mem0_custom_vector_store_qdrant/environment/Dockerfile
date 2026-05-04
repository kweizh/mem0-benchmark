FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl ca-certificates git python3 python3-pip python3-pytest bash && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install --break-system-packages mem0ai qdrant-client openai

RUN curl -fsSL https://github.com/qdrant/qdrant/releases/download/v1.12.0/qdrant-x86_64-unknown-linux-gnu.tar.gz | tar -xz -C /usr/local/bin && \
    chmod +x /usr/local/bin/qdrant

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Mem0 environment with local Qdrant vector store."

# Container contents:
#   - mem0ai, qdrant-client, openai installed.
#   - Qdrant binary installed in /usr/local/bin/qdrant.
#   - /home/user directory ready for the task.

CMD ["/bin/bash", "-c", "qdrant & trap : TERM INT; sleep infinity & wait"]
