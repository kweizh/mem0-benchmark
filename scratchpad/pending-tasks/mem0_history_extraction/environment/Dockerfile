FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl ca-certificates git python3 python3-pip python3-pytest bash && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install --break-system-packages mem0ai qdrant-client openai

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Mem0 task environment with pre-existing chat logs."

RUN mkdir -p /home/user/chat_logs && \
    cat > /home/user/chat_logs/session1.json <<'EOF'
[{"role": "user", "content": "Hi, I'm Bob. I work as a software engineer."}]
EOF

RUN cat > /home/user/chat_logs/session2.json <<'EOF'
[{"role": "user", "content": "I love hiking on weekends and I recently picked up photography."}]
EOF

# Container contents:
#   - mem0ai, qdrant-client, openai installed via pip
#   - /home/user/chat_logs/session1.json with initial chat data
#   - /home/user/chat_logs/session2.json with initial chat data

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]