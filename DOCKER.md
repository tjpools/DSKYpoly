# DSKYpoly Docker Integration

*Containerized mathematical computation environment for cross-platform development*

## 🐳 **Docker Desktop Integration**

DSKYpoly provides a complete Docker environment optimized for **Windows 11 Docker Desktop**, with full compatibility across all platforms. This containerized approach embodies the project's philosophy of making mathematical computation accessible across different systems.

### **Why Docker for DSKYpoly?**

Docker integration serves multiple philosophical and practical purposes:

- **🌐 Universal Access**: Mathematical truth should be platform-independent
- **🔄 Reproducible Environment**: Consistent computation across all systems
- **📦 Isolation**: Clean mathematical workspace without system dependencies
- **🤝 Collaboration**: Easy sharing of complete mathematical environments
- **🚀 Quick Start**: From concept to computation in minutes

## 📋 **Prerequisites**

### **Windows 11 Setup**
1. **Docker Desktop**: Download from [docker.com](https://www.docker.com/products/docker-desktop)
2. **WSL 2**: Enable Windows Subsystem for Linux (required for Docker Desktop)
3. **Git**: For cloning the repository
4. **Terminal**: Windows Terminal recommended for best experience

### **Other Platforms**
- **macOS**: Docker Desktop for Mac
- **Linux**: Docker Engine + Docker Compose

## 🚀 **Quick Start Guide**

### **1. Clone the Repository**
```bash
git clone https://github.com/tjpools/DSKYpoly.git
cd DSKYpoly
```

### **2. Build the Environment**
```bash
# Linux/macOS
./docker-manage.sh build

# Windows 11
docker-manage.bat build
```

### **3. Start Development Environment**
```bash
# Linux/macOS
./docker-manage.sh run

# Windows 11
docker-manage.bat run
```

### **4. Access the Mathematical Workspace**
```bash
# Get a shell in the container
docker exec -it dskypoly-mathematical-workspace /bin/bash

# Or use the management script
./docker-manage.sh shell  # Linux/macOS
docker-manage.bat shell   # Windows
```

## 🧮 **Container Services**

### **Main Development Container (`dskypoly-dev`)**
- **Complete build environment** with GCC, NASM, Make
- **All polynomial solvers** pre-built and ready to run
- **Python 3 mathematical stack** (NumPy, SciPy, SymPy, Matplotlib)
- **Documentation tools** (Graphviz for visualizations)
- **Interactive shell** for mathematical exploration

### **Analytics Container (`dskypoly-analytics`)**
- **Jupyter Lab environment** for interactive analysis
- **Enhanced Python libraries** (Pandas, Seaborn, Plotly)
- **LaTeX support** for mathematical typesetting
- **Automatic port forwarding** to localhost:8888

## 🌟 **Available Commands**

### **Core Operations**
```bash
# Build the Docker images
./docker-manage.sh build

# Start the development environment
./docker-manage.sh run

# Launch Jupyter analytics environment
./docker-manage.sh jupyter

# Get interactive shell
./docker-manage.sh shell

# View container status
./docker-manage.sh status

# Stop all containers
./docker-manage.sh stop

# Clean up everything
./docker-manage.sh clean
```

### **Mathematical Solvers in Container**
Once inside the container, all polynomial solvers are available:

```bash
# Quadratic solver (DSKY interface)
./build/dskypoly

# Cubic solver (Cardano method)
./cubic/build/dskypoly3

# Quartic solver (Ferrari method)
./quartic/build/dskypoly4

# Quintic solver (Galois theory)
./quintic/build/dskypoly5
```

## 🔧 **Windows 11 Docker Desktop Integration**

### **Visual Management**
- **Container Overview**: View all DSKYpoly containers in Docker Desktop GUI
- **Resource Monitoring**: Real-time CPU, memory, and network usage
- **Log Viewing**: Integrated log viewer for debugging
- **Volume Management**: Persistent data storage across container restarts

### **Port Forwarding**
- **Port 8888**: Jupyter Lab interface
- **Port 8080**: Reserved for future web interfaces
- **Automatic Detection**: Docker Desktop automatically detects and displays accessible ports

### **Windows-Specific Features**
```batch
REM Windows batch script automatically opens Jupyter in browser
docker-manage.bat jupyter

REM Integration with Windows Terminal
docker-manage.bat shell
```

## 📊 **Development Workflow**

### **1. Mathematical Exploration**
```bash
# Start the development container
./docker-manage.sh run

# Enter the mathematical workspace
./docker-manage.sh shell

# Explore polynomial hierarchies
./build/dskypoly
./cubic/build/dskypoly3
./quartic/build/dskypoly4
./quintic/build/dskypoly5
```

### **2. Interactive Analysis**
```bash
# Launch Jupyter environment
./docker-manage.sh jupyter

# Access at: http://localhost:8888
# Create notebooks for mathematical visualization
# Explore group theory concepts interactively
```

### **3. Code Development**
```bash
# Container has full development environment
# Edit files with vim/nano inside container
# Or use bind mounts to edit externally

# Rebuild and test changes
make clean && make all
```

## 🔍 **Troubleshooting**

### **Common Issues**

**Container won't start:**
```bash
# Check Docker Desktop is running
docker version

# Verify system requirements
docker system info

# Clean and rebuild
./docker-manage.sh clean
./docker-manage.sh build
```

**Port conflicts:**
```bash
# Check what's using port 8888
netstat -an | grep 8888

# Or use alternative port
docker run -p 8889:8888 dskypoly:latest
```

**Permission issues (Linux):**
```bash
# Ensure Docker daemon is running
sudo systemctl start docker

# Add user to docker group
sudo usermod -aG docker $USER
```

## 📱 **Cross-Platform Compatibility**

### **Tested Environments**
- ✅ **Windows 11** with Docker Desktop
- ✅ **macOS** with Docker Desktop
- ✅ **Ubuntu 20.04/22.04** with Docker Engine
- ✅ **WSL 2** integration on Windows

### **Platform-Specific Notes**

**Windows 11:**
- Use `docker-manage.bat` for native Windows experience
- Jupyter automatically opens in default browser
- Full integration with Windows Terminal

**macOS:**
- Use `docker-manage.sh` with Terminal.app or iTerm2
- Full native performance with Docker Desktop

**Linux:**
- Direct Docker Engine integration
- Optimal performance for mathematical computation

## 🎯 **Educational Use Cases**

### **Classroom Deployment**
```bash
# Students can quickly set up identical environments
git clone https://github.com/tjpools/DSKYpoly.git
cd DSKYpoly
./docker-manage.sh build
./docker-manage.sh run
```

### **Research Collaboration**
```bash
# Share exact computational environment
docker save dskypoly:latest > dskypoly-environment.tar
# Transfer to collaborators
docker load < dskypoly-environment.tar
```

### **Mathematical Workshops**
```bash
# Pre-built environment for immediate exploration
./docker-manage.sh jupyter
# Participants can immediately start with polynomial solving
```

## 🔮 **Future Enhancements**

### **Planned Features**
- **Web Interface**: Browser-based polynomial solver
- **Cloud Integration**: Docker Hub automated builds
- **GPU Support**: CUDA containers for advanced computation
- **Multi-Architecture**: ARM64 support for Apple Silicon

### **Community Contributions**
- **Custom Dockerfiles**: Specialized mathematical environments
- **Orchestration**: Kubernetes manifests for cluster deployment
- **CI/CD Integration**: Automated testing in containerized environments

## 📝 **Docker Philosophy**

The Docker integration embodies DSKYpoly's core philosophy:

> **"Mathematical truth should be accessible regardless of the underlying computational substrate. Just as polynomial equations transcend their specific implementations, mathematical insight should transcend platform boundaries."**

Docker becomes the **universal translator** between mathematical concepts and diverse computing environments, much like how formal grammars translate between philosophical contemplation and machine instructions.

---

*The containerized DSKYpoly environment: where mathematical universality meets computational portability.*
