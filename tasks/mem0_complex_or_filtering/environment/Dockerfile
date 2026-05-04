FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl ca-certificates git python3 python3-pip python3-pytest bash && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install --break-system-packages mem0ai openai

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Mem0 task environment with python3 and mem0ai installed."

# Container contents:
#   - python3, pip, pytest
#   - mem0ai and openai python packages
#   - /home/user directory for the project

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]