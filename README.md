# DSKYpoly: Polynomial Root Solver Suite
*Where Galois theory meets machine-level precision*

A comprehensive polynomial equation solver implementing classical algebraic methods in x86-64 assembly language. From quadratic fundamentals to Ferrari's quartic method, with quintic numerical approaches on the horizon.

## 🎯 **Project Overview**

DSKYpoly is a low-level symbolic computation engine that bridges pure mathematics and systems programming. Each polynomial degree is implemented with mathematical rigor and architectural precision.

### **Currently Implemented:**
- ✅ **Quadratic Solver** - Classical formula implementation
- ✅ **Cubic Solver** - Cardano's method with discriminant analysis  
- ✅ **Quartic Solver** - Ferrari's method via resolvent cubic
- 🚧 **Quintic Solver** - Numerical methods (Abel-Ruffini compliant)

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
├── quintic/       # [Planned] Numerical approaches
├── include/       # Shared mathematical constants and structures
└── build/         # Compiled executables and test results
```

## 🚀 **Quick Start**

### **Build Requirements:**
- `gcc` (C compiler)
- `nasm` (Netwide Assembler)
- `make` (Build system)
- Linux x86-64 system

### **Build and Test:**
```bash
# Test quartic solver (Ferrari's method)
cd quartic
make clean && make
./build/dskypoly4

# Test cubic solver (Cardano's method)  
cd ../cubic
make clean && make
./build/dskypoly3
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

### **Quintic Solver (In Progress):**
- **Numerical Methods** - Newton-Raphson, Durand-Kerner
- **Special Cases** - Solvable quintic patterns
- **Hybrid Approach** - Algebraic detection + numerical solving

### **Advanced Features:**
- **Complex Root Support** - Full complex number arithmetic
- **Polynomial Operations** - Multiplication, division, GCD
- **Visualization** - Root plotting and convergence analysis

## 📄 **License**

This project honors the mathematical legacy of classical algebraists while advancing modern computational techniques.

---

*"The quartic yields its secrets through cubic wisdom, but the quintic guards its mysteries with algebraic impossibility."* - DSKYpoly Development Notes

**Built with mathematical rigor and systems programming precision** 🧮⚙️