# DSKYpoly Docker Environment Guide

## 🐳 **Docker Desktop Windows 11 Integration**

This guide shows how to run DSKYpoly in a containerized environment on Windows 11 using Docker Desktop, creating a consistent cross-platform development experience.

### **Prerequisites**

1. **Docker Desktop for Windows 11** installed and running
2. **WSL 2** enabled (recommended for best performance)
3. **Git for Windows** (to clone the repository)

### **Quick Start**

```bash
# Clone the repository
git clone https://github.com/tjpools/DSKYpoly.git
cd DSKYpoly

# Build and run the development environment
docker-compose up --build dskypoly-dev

# Or run just the main container
docker build -t dskypoly:latest .
docker run -it --rm -v ${PWD}:/workspace dskypoly:latest
```

### **Container Environments**

#### **1. Development Environment (`dskypoly-dev`)**
- **Purpose**: Interactive development and testing
- **Includes**: All solvers, build tools, editors
- **Access**: `docker-compose up dskypoly-dev`

#### **2. Analytics Environment (`dskypoly-analytics`)**
- **Purpose**: Jupyter notebooks for mathematical analysis
- **Includes**: JupyterLab, scientific Python stack
- **Access**: `docker-compose up dskypoly-analytics`
- **URL**: http://localhost:8888

### **Container Commands**

#### **Building the Environment**
```bash
# Build all containers
docker-compose build

# Build specific container
docker build -t dskypoly:latest .
docker build -t dskypoly:analytics -f Dockerfile.analytics .
```

#### **Running Containers**
```bash
# Interactive development
docker-compose run --rm dskypoly-dev /bin/bash

# Start Jupyter analytics
docker-compose up dskypoly-analytics

# Run a specific solver
docker run --rm dskypoly:latest ./build/dskypoly

# Mount local directory for development
docker run -it --rm -v ${PWD}:/workspace dskypoly:latest /bin/bash
```

#### **Container Management**
```bash
# View running containers
docker-compose ps

# Stop all containers
docker-compose down

# Remove containers and volumes
docker-compose down -v

# Clean up images
docker image prune -f
```

### **Windows 11 Specific Features**

#### **WSL 2 Integration**
- **Performance**: Native Linux performance on Windows
- **File System**: Seamless file sharing between Windows and container
- **Networking**: Direct access to container ports from Windows

#### **Docker Desktop Dashboard**
- **Container Status**: Visual monitoring of running containers
- **Resource Usage**: CPU, memory, disk usage statistics
- **Port Mapping**: Easy access to exposed services
- **Volume Management**: Persistent data storage

#### **PowerShell Integration**
```powershell
# PowerShell commands for Windows 11
# Build and run in PowerShell
docker-compose up --build

# Open container in Windows Terminal
docker exec -it dskypoly-mathematical-workspace /bin/bash

# Copy files between Windows and container
docker cp dskypoly-mathematical-workspace:/workspace/output.txt ./
```

### **Development Workflow**

#### **1. Code Development**
```bash
# Start development container
docker-compose up -d dskypoly-dev

# Enter interactive shell
docker exec -it dskypoly-mathematical-workspace /bin/bash

# Edit code using container tools
vim src/main.c
nano solve_poly_2.asm

# Build and test
make clean && make all
./build/dskypoly
```

#### **2. Mathematical Analysis**
```bash
# Start analytics environment
docker-compose up -d dskypoly-analytics

# Open Jupyter in browser
# Navigate to http://localhost:8888

# Create new notebook for analysis
# Import DSKYpoly results and visualize
```

#### **3. Cross-Platform Testing**
```bash
# Test on different architectures
docker buildx build --platform linux/amd64,linux/arm64 -t dskypoly:multiarch .

# Run performance benchmarks
docker run --rm dskypoly:latest ./quintic/test_simple
```

### **Statistical Analysis Features**

#### **Built-in Tools**
- **Performance Profiling**: Time and memory usage analysis
- **Mathematical Visualization**: Polynomial plots and root diagrams
- **Galois Group Analysis**: Symmetry and solvability insights
- **Assembly Code Metrics**: Instruction count and complexity

#### **Jupyter Notebooks**
- **Interactive Analysis**: Real-time mathematical exploration
- **Visualization**: Plot polynomial functions and roots
- **Documentation**: Combine code, math, and narrative
- **Reproducibility**: Consistent results across environments

### **File Structure in Container**

```
/workspace/
├── src/                    # Source code
├── build/                  # Compiled binaries
├── cubic/                  # Cubic solver
├── quartic/                # Quartic solver
├── quintic/                # Quintic solver
├── notebooks/              # Jupyter notebooks
├── documentation/          # README files
└── docker-output/          # Container-specific outputs
```

### **Environment Variables**

```bash
# Set in docker-compose.yml or command line
DISPLAY=host.docker.internal:0.0  # For GUI apps
TERM=xterm-256color               # Terminal colors
JUPYTER_ENABLE_LAB=yes            # Enable JupyterLab
```

### **Port Mappings**

- **8080**: Development web interface (if implemented)
- **8888**: Jupyter notebook/lab
- **Custom ports**: Can be added for additional services

### **Volume Management**

```bash
# Named volumes for persistent data
docker volume create dskypoly-data
docker volume ls
docker volume inspect dskypoly-data

# Backup volume data
docker run --rm -v dskypoly-data:/data -v ${PWD}:/backup alpine tar czf /backup/dskypoly-backup.tar.gz -C /data .
```

### **Performance Optimization**

#### **Windows 11 Specific**
- **WSL 2 Backend**: Use WSL 2 for better performance
- **Memory Allocation**: Adjust Docker Desktop memory limits
- **File System**: Use bind mounts for active development
- **Resource Limits**: Set appropriate CPU and memory limits

#### **Container Optimization**
- **Multi-stage Builds**: Reduce final image size
- **Layer Caching**: Optimize Dockerfile for build speed
- **Resource Constraints**: Set memory and CPU limits

### **Troubleshooting**

#### **Common Issues**
```bash
# Container won't start
docker-compose logs dskypoly-dev

# Build failures
docker-compose build --no-cache

# Permission issues
docker run --user $(id -u):$(id -g) ...

# Port conflicts
docker-compose down
netstat -an | findstr :8888
```

#### **Windows 11 Specific**
- **WSL 2 Issues**: Restart WSL with `wsl --shutdown`
- **Docker Desktop**: Restart Docker Desktop service
- **Firewall**: Configure Windows Firewall for Docker ports
- **Antivirus**: Exclude Docker directories from scans

### **Integration with Development Tools**

#### **Visual Studio Code**
- **Remote Containers Extension**: Develop directly in container
- **Docker Extension**: Manage containers from VS Code
- **Integrated Terminal**: Access container shell from editor

#### **JetBrains IDEs**
- **Docker Plugin**: Container management and debugging
- **Remote Development**: Connect to container environments
- **Code Navigation**: Browse container file system

### **Security Considerations**

```bash
# Run as non-root user
docker run --user 1000:1000 dskypoly:latest

# Read-only file system
docker run --read-only --tmpfs /tmp dskypoly:latest

# Network isolation
docker network create --internal dskypoly-internal
```

### **Extending the Environment**

#### **Adding New Tools**
```dockerfile
# Add to Dockerfile
RUN apt-get install -y your-tool
RUN pip3 install your-python-package
```

#### **Custom Services**
```yaml
# Add to docker-compose.yml
services:
  your-service:
    image: your-image
    depends_on:
      - dskypoly-dev
```

This containerized environment brings DSKYpoly's philosophical themes full circle - demonstrating how mathematical abstractions can be made **universally accessible** through containerization, regardless of the underlying operating system or hardware architecture.

The Docker environment becomes another **strange loop** in the project: the same mathematical insights that work in assembly language on bare metal also work in virtualized containers on Windows 11, showcasing the **universal nature of mathematical truth** across computational platforms.
