# DSKYpoly Development Environment
# Base Ubuntu image for C/Assembly development with mathematical computation tools

FROM ubuntu:22.04

# Avoid interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Set working directory
WORKDIR /workspace

# Install system dependencies, create Python virtual environment, and install Python packages
RUN apt-get update && apt-get install -y --no-install-recommends \
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
    sudo \
    && rm -rf /var/lib/apt/lists/* \
    && python3 -m venv /opt/venv \
    && /opt/venv/bin/pip install --upgrade pip \
    && /opt/venv/bin/pip install --no-cache-dir \
        matplotlib \
        numpy \
        scipy \
        sympy \
        jupyter \
        ipython \
    && mkdir -p /workspace/build /workspace/src /workspace/include /data

# Set environment variables
ENV PATH="/opt/venv/bin:$PATH"
ENV TERM=xterm-256color
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

# Create non-root user
RUN useradd -m -s /bin/bash dskypoly && \
    usermod -aG sudo dskypoly && \
    echo "dskypoly ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \
    chown -R dskypoly:dskypoly /workspace /opt/venv /data

# First copy requirements/dependencies files for better caching
COPY requirements.txt* pyproject.toml* setup.py* ./

# Copy project files
COPY . /workspace/

# Set permissions and switch to non-root user
RUN chmod +x /workspace/src/dskypoly.py 2>/dev/null || true && \
    chown -R dskypoly:dskypoly /workspace

USER dskypoly

# Default command
CMD ["/bin/bash"]
