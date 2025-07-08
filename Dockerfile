# DSKYpoly: Containerized Mathematical Computation Environment
# A Docker image for exploring polynomial solvers across platforms

FROM ubuntu:22.04

# Set up environment
ENV DEBIAN_FRONTEND=noninteractive
ENV TERM=xterm-256color

# Install system dependencies
RUN apt-get update && apt-get install -y \
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
CMD ["/bin/bash"]
