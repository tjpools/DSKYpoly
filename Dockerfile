<<<<<<< HEAD
# DSKYpoly: Containerized Mathematical Computation Environment
# A Docker image for exploring polynomial solvers across platforms

FROM ubuntu:22.04

# Set up environment
ENV DEBIAN_FRONTEND=noninteractive
ENV TERM=xterm-256color
=======
# DSKYpoly Development Environment
# Base Ubuntu image for C/Assembly development with mathematical computation tools

FROM ubuntu:22.04

# Avoid interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Set working directory
WORKDIR /workspace
>>>>>>> main

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    nasm \
    make \
    git \
<<<<<<< HEAD
    vim \
    nano \
    tree \
    graphviz \
    python3 \
    python3-pip \
    curl \
    wget \
    less \
    man-db \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages for analysis and visualization
RUN pip3 install --upgrade pip && \
    pip3 install numpy matplotlib scipy sympy jupyter notebook pandas

# Create working directory
WORKDIR /workspace

# Copy the entire project
COPY . /workspace/

# Set executable permissions for test programs
RUN find /workspace -name "test_*" -type f -exec chmod +x {} \; || true

# Build all components
RUN cd /workspace && make -f Makefile clean || true
RUN cd /workspace && make -f Makefile all || true

# Build cubic solver
RUN cd /workspace/cubic && make clean || true
RUN cd /workspace/cubic && make all || true

# Build quartic solver
RUN cd /workspace/quartic && make clean || true
RUN cd /workspace/quartic && make all || true

# Build quintic solver
RUN cd /workspace/quintic && make clean || true
RUN cd /workspace/quintic && make all || true

# Generate visualization files
RUN cd /workspace/quartic/grammar && dot -Tpng automorphism_detailed.dot -o automorphism_detailed.png || true

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

# Set up container entrypoint
ENTRYPOINT ["/workspace/container_welcome.sh"]
=======
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
>>>>>>> main
CMD ["/bin/bash"]
