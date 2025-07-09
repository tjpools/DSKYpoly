# DSKYpoly: Polynomial Root Solver Suite
*Where Galois theory meets machine-level precision*

A comprehensive polynomial equation solver implementing classical algebraic methods in x86-64 assembly language. From quadratic fundamentals to Ferrari's quartic method, with quintic numerical approaches on the horizon.

> **🎭 For the deeper philosophical context:** See [`PHILOSOPHICAL_OVERVIEW.md`](PHILOSOPHICAL_OVERVIEW.md) for how this project connects to Gödel, Escher, Bach and group theory as a meditation on mathematical consciousness and computational self-reference.

> **⚡ For the minimal takeaway:** See [`MINIMAL_TAKEAWAY.md`](MINIMAL_TAKEAWAY.md) for the essential insight in under 2 minutes.

## 🎯 **Project Overview**

DSKYpoly is a low-level symbolic computation engine that bridges pure mathematics and systems programming. Each polynomial degree is implemented with mathematical rigor and architectural precision.

### **Currently Implemented:**
- ✅ **Quadratic Solver** - Classical formula implementation
- ✅ **Cubic Solver** - Cardano's method with discriminant analysis  
- ✅ **Quartic Solver** - Ferrari's method via resolvent cubic
- ✅ **Quintic Solver** - Hypergeometric approach with Python/mpmath
- 🚧 **Quintic Solver** - Extended numerical methods (ongoing)

## 🏛️ **Mathematical Heritage**

### **Classical Methods Implemented:**
- **Gerolamo Cardano (1501-1576)** - Cubic equation solutions
- **Ludovico Ferrari (1522-1565)** - Quartic reduction to resolvent cubic
- **Évariste Galois (1811-1832)** - Theoretical foundation for quintic impossibility

### **Modern Implementation:**
- **x86-64 Assembly** - Direct hardware floating-point operations
- **SSE Instructions** - Vectorized mathematical computations
- **Stack Discipline** - 16-byte alignment for scalability
- **Two-Track Development** - Reference architecture + production mathematics

## 📁 **Repository Structure**

```
DSKYpoly/
├── src/           # Core polynomial solver (quadratic foundation)
├── cubic/         # Cardano's method implementation
├── quartic/       # Ferrari's method (dual implementation strategy)
├── quintic/       # Hypergeometric & numerical approaches
├── include/       # Shared mathematical constants and structures
├── visualizations/ # Mathematical plots and analysis
└── build/         # Compiled executables and test results
```

## 🚀 **Quick Start**

### **Option 1: Docker (Recommended for Windows/Cross-Platform)**

#### **Prerequisites**
- **Docker Desktop** (Windows 11, macOS, or Linux)
- **Git** (to clone the repository)

#### **Quick Start with Docker**
```bash
# Clone the repository
git clone https://github.com/tjpools/DSKYpoly.git
cd DSKYpoly

# Build and run development environment
docker-compose up --build dskypoly-dev

# Or run analytics environment with Jupyter
docker-compose up --build dskypoly-analytics
# Then open http://localhost:8888 in your browser
```

#### **Docker Features**
- **Cross-Platform**: Works on Windows 11, macOS, and Linux
- **Isolated Environment**: No need to install NASM, GCC locally
- **Analytics Support**: Jupyter notebooks for mathematical analysis
- **Python Mathematics**: Pre-installed mpmath, scipy, sympy, matplotlib, plotly
- **Pre-built Tools**: All dependencies included

See [`DOCKER.md`](DOCKER.md) for comprehensive Docker setup and usage.

### **Option 3: Anaconda Navigator (Recommended for Mathematical Exploration)**

For advanced mathematical computing and interactive exploration:

```bash
# Create conda environment
conda env create -f environment.yml
conda activate dskypoly

# Launch Jupyter Lab
jupyter lab

# Open notebooks/quintic_exploration.ipynb
```

#### **Anaconda Features**
- **Interactive Notebooks**: Jupyter Lab for mathematical exploration
- **Arbitrary Precision**: mpmath for exact hypergeometric calculations
- **Advanced Visualization**: Plotly for interactive complex plane plots
- **Educational Content**: Step-by-step quintic polynomial analysis
- **Cross-Platform**: Works with Windows 11 Anaconda Navigator

See [`ANACONDA.md`](ANACONDA.md) for comprehensive Anaconda setup and mathematical exploration.

### **Option 2: Native Linux Installation**

#### **Prerequisites**
- **x86-64 Linux system** (tested on Ubuntu/Debian)  
- **NASM assembler** (`sudo apt install nasm`)
- **GCC compiler** (`sudo apt install build-essential`)
- **Make** (usually included with build-essential)

#### **Build and Test**
```bash
# Test quartic solver (Ferrari's method)
cd quartic
make clean && make
./build/dskypoly4

# Test cubic solver (Cardano's method)  
cd ../cubic
make clean && make
./build/dskypoly3

# Test quintic solver (Hypergeometric approach)
cd ../quintic
make test-roots-of-unity  # Comprehensive test with visualization
```

## 🧮 **Example: Quartic Polynomial**

**Input:** `x⁴ - 10x² + 9 = 0`

**Ferrari's Method:**
1. Already depressed (no cubic term)
2. Resolvent cubic: `8t³ - 80t² + 128t = 0`  
3. Solve cubic for auxiliary parameter
4. Extract quartic roots: `x = ±1, ±3`

**Assembly Implementation:**
```assembly
; 16-byte aligned coefficient storage
[rsp+0]   : 1.0    ; x⁴ coefficient
[rsp+16]  : 0.0    ; x³ coefficient  
[rsp+32]  : -10.0  ; x² coefficient
[rsp+48]  : 0.0    ; x¹ coefficient
[rsp+64]  : 9.0    ; constant term
```

## 🔬 **Example: Quintic Polynomial (5th Roots of Unity)**

**Input:** `x⁵ - 1 = 0`

**Hypergeometric Approach:**
1. Recognize as roots of unity: `exp(2πik/5)` for k = 0,1,2,3,4
2. Use hypergeometric functions to compute exact algebraic expressions
3. Extract numerical values with arbitrary precision
4. Visualize roots in complex plane

**Python Implementation:**
```python
solver = QuinticHypergeometricSolver()
roots = solver.solve_roots_of_unity(5)
# Returns: [1+0j, 0.309+0.951j, -0.809+0.588j, -0.809-0.588j, 0.309-0.951j]
```

**Key Features:**
- **Arbitrary Precision**: Uses mpmath for exact computations
- **Visualization**: Complex plane plotting with matplotlib/plotly
- **Root Verification**: Automatic validation of solutions
- **Educational Output**: Step-by-step mathematical analysis

## 🔬 **Technical Highlights**

### **Architectural Patterns:**
- **Stack-Based Computation** - Systematic memory layout
- **Reference + Production** - Dual implementation strategy
- **Error Resilience** - Graceful handling of edge cases
- **Scalable Design** - Patterns extend to higher degrees

### **Mathematical Precision:**
- **IEEE 754 Compliance** - Standard floating-point operations
- **Discriminant Analysis** - Root classification and validation
- **Numerical Stability** - Careful handling of ill-conditioned cases

## 🌉 **The Abstraction Journey: From Silicon to Symmetry**

DSKYpoly represents more than just a polynomial solver—it's a meditation on the layers of abstraction that separate raw computation from mathematical truth. This project deliberately bridges multiple levels of the computational hierarchy:

### **Layer 1: Bare Metal Assembly**
At the foundation, we manipulate floating-point registers directly, crafting machine code that speaks to the silicon itself. Every coefficient placement, every stack alignment, every SSE instruction is a conscious choice about how mathematical concepts map to physical circuits.

### **Layer 2: Classical Algorithms**
Ferrari's quartic method and Cardano's cubic solutions encode centuries of mathematical insight into precise computational steps. These aren't mere calculations—they're executable proofs of algebraic theorems.

### **Layer 3: Modern Numerical Methods**
The quintic solver introduces a hybrid approach, combining exact algebraic detection with numerical approximation. Here, we acknowledge both the power and limitations of symbolic computation.

### **Layer 4: High-Level Mathematical Abstraction**
The Python-based hypergeometric quintic solver operates in the realm of pure mathematical concepts—complex analysis, special functions, and symmetry groups. At this level, we're not just solving equations; we're exploring the deep structures that govern polynomial behavior.

### **The Philosophical Synthesis**
This multi-layered approach reveals something profound: **mathematical truth exists independently of its implementation**, yet the method of implementation shapes our understanding. The assembly code teaches us about computational constraints, while the high-level algorithms reveal mathematical patterns invisible at the machine level.

The project demonstrates that abstraction isn't about hiding complexity—it's about revealing different aspects of mathematical reality. Each layer offers unique insights:
- Assembly reveals the **computational cost** of mathematical operations
- Classical algorithms show the **historical development** of mathematical thought  
- Numerical methods expose the **practical limits** of exact computation
- High-level abstractions illuminate the **underlying mathematical structures**

This is why DSKYpoly maintains implementations at multiple levels: not for redundancy, but for **mathematical completeness**. Each layer is a different lens through which to view the same fundamental truths about polynomial equations.

## 📖 **Documentation**

Each solver includes comprehensive documentation:
- **Mathematical Theory** - Classical algebraic methods
- **Implementation Details** - Assembly code structure
- **Test Cases** - Verification with known polynomials
- **Build Instructions** - Platform-specific compilation

## 🎓 **Educational Value**

DSKYpoly demonstrates:
- **Computer Algebra** - Symbolic computation at machine level
- **Assembly Programming** - Advanced x86-64 techniques
- **Mathematical Software** - Bridging theory and implementation
- **Software Architecture** - Scalable design patterns

## 🚧 **Future Development**

### **Quintic Solver (Ongoing):**
- ✅ **Hypergeometric Methods** - Special function approaches via mpmath
- ✅ **Visualization Framework** - Root plotting and mathematical analysis
- 🚧 **General Quintic Cases** - Extended hypergeometric transformations
- 🚧 **Numerical Methods** - Newton-Raphson, Durand-Kerner integration
- 🚧 **Interactive Analysis** - Jupyter notebooks for quintic exploration

### **Advanced Features:**
- **Complex Root Support** - Full complex number arithmetic
- **Polynomial Operations** - Multiplication, division, GCD
- **Performance Analysis** - Computational complexity studies
- **Educational Notebooks** - Interactive mathematical exploration

## 📄 **License**

This project honors the mathematical legacy of classical algebraists while advancing modern computational techniques.

---

*"The quartic yields its secrets through cubic wisdom, but the quintic guards its mysteries with algebraic impossibility."* - DSKYpoly Development Notes

**Built with mathematical rigor and systems programming precision** 🧮⚙️