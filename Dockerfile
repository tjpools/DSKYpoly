# DSKYpoly: Containerized Mathematical Computation Environment
# A Docker image for exploring polynomial solvers across platforms

FROM ubuntu:22.04

# Avoid interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive
ENV TERM=xterm-256color
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

# Set working directory
WORKDIR /workspace


# Install system dependencies (with --no-install-recommends) and create non-root user
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    nasm \
    make \
    git \
    vim \
    nano \
    tree \
    graphviz \
    python3 \
    python3-pip \
    python3-venv \
    curl \
    wget \
    less \
    man-db \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/* \
    && useradd -ms /bin/bash dskypolyuser \
    && chown -R dskypolyuser:dskypolyuser /workspace


# Install Python packages for analysis and visualization
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install --upgrade pip && \
    pip3 install -r /tmp/requirements.txt


# Copy the rest of the project
COPY . /workspace/


# Set executable permissions for test programs and scripts
RUN find /workspace -name "test_*" -type f -exec chmod +x {} \; || true && \
    chmod +x /workspace/src/dskypoly.py 2>/dev/null || true


# Build all components and generate visualization files (ignore errors if Makefile or dirs are missing)
RUN cd /workspace && make -f Makefile clean || true && \
    cd /workspace && make -f Makefile all || true && \
    cd /workspace/cubic && make clean || true && \
    cd /workspace/cubic && make all || true && \
    cd /workspace/quartic && make clean || true && \
    cd /workspace/quartic && make all || true && \
    cd /workspace/quintic && make clean || true && \
    cd /workspace/quintic && make all || true && \
    cd /workspace/quartic/grammar && dot -Tpng automorphism_detailed.dot -o automorphism_detailed.png || true


# Create a startup script
RUN echo '#!/bin/bash' > /workspace/container_welcome.sh && \
    echo 'echo "🧮 Welcome to DSKYpoly - Containerized Mathematical Computation"' >> /workspace/container_welcome.sh && \
    echo 'echo "=================================================="' >> /workspace/container_welcome.sh && \
    echo 'echo "Available polynomial solvers:"' >> /workspace/container_welcome.sh && \
    echo 'echo "  • Quadratic: ./build/dskypoly"' >> /workspace/container_welcome.sh && \
    echo 'echo "  • Cubic: ./cubic/build/dskypoly3"' >> /workspace/container_welcome.sh && \
    echo 'echo "  • Quartic: ./quartic/build/dskypoly4"' >> /workspace/container_welcome.sh && \
    echo 'echo "  • Quintic: ./quintic/build/dskypoly5"' >> /workspace/container_welcome.sh && \
    echo 'echo ""' >> /workspace/container_welcome.sh && \
    echo 'echo "Documentation:"' >> /workspace/container_welcome.sh && \
    echo 'echo "  • README.md - Project overview"' >> /workspace/container_welcome.sh && \
    echo 'echo "  • MINIMAL_TAKEAWAY.md - Quick summary"' >> /workspace/container_welcome.sh && \
    echo 'echo "  • PHILOSOPHICAL_OVERVIEW.md - Deep dive"' >> /workspace/container_welcome.sh && \
    echo 'echo ""' >> /workspace/container_welcome.sh && \
    echo 'echo "Try: tree -L 2 to explore the project structure"' >> /workspace/container_welcome.sh && \
    echo 'echo "=================================================="' >> /workspace/container_welcome.sh && \
    chmod +x /workspace/container_welcome.sh


# Switch to non-root user
USER dskypolyuser

# Set up container entrypoint
ENTRYPOINT ["/workspace/container_welcome.sh"]
