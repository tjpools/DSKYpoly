# DSKYpoly Development Environment
# Base Ubuntu image for C/Assembly development with mathematical computation tools

FROM ubuntu:22.04

# Avoid interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Set working directory
WORKDIR /workspace

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    nasm \
    make \
    git \
    tree \
    vim \
    nano \
    curl \
    wget \
    graphviz \
    python3 \
    python3-pip \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

# Create Python virtual environment
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install Python dependencies for mathematical computation
RUN pip install --no-cache-dir \
    matplotlib \
    numpy \
    scipy \
    sympy \
    jupyter \
    ipython

# Set environment variables
ENV TERM=xterm-256color
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

# Create necessary directories
RUN mkdir -p /workspace/build /workspace/src /workspace/include /data

# Copy project files
COPY . /workspace/

# Set permissions for executables
RUN chmod +x /workspace/src/dskypoly.py 2>/dev/null || true

# Default command
CMD ["/bin/bash"]
