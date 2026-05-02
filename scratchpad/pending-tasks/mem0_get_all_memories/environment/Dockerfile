FROM python:3.11-slim

RUN useradd -m -s /bin/bash user

# Install required system packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install mem0ai
RUN pip install --no-cache-dir mem0ai

# Set up workspace
RUN mkdir -p /home/user/workspace && chown -R user:user /home/user/workspace

USER user
WORKDIR /home/user/workspace
