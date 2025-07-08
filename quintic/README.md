# DSKYpoly-5: Quintic Polynomial Solver
*Where radical solvability meets algebraic impossibility*

## Overview
Implementation of quintic polynomial equation solving in x86-64 assembly language, respecting the profound mathematical limits established by Abel-Ruffini theorem and Galois theory.

**Equation Form:** `ax⁵ + bx⁴ + cx³ + dx² + ex + f = 0`

## 🏛️ **Mathematical Foundation**

### **The Quintic Challenge:**
The quintic represents a fundamental boundary in algebra:
- **Abel-Ruffini Theorem (1824-1826)** - No general solution using radicals
- **Galois Theory** - Symmetric group S₅ contains non-solvable alternating group A₅ 
- **Permutation Groups** - Only even permutations expressible via radicals, but A₅ ≠ solvable

### **Historical Context:**
- **Niels Henrik Abel (1802-1829)** - Proved impossibility of general radical solutions
- **Paolo Ruffini (1765-1822)** - Early impossibility work
- **Évariste Galois (1811-1832)** - Group theory framework explaining the impossibility
- **Charles Hermite (1822-1901)** - First to solve general quintic using elliptic functions

## 🎯 **Implementation Strategy**

### **Multi-Track Approach:**

#### 1. **Reference Architecture** (`solve_poly_5_reference.asm`)
- **Purpose:** Proven, stable computational foundation
- **Features:** 
  - Extended 16-byte aligned stack layout (6 coefficients)
  - Systematic register management for degree-5 complexity
  - Placeholder mathematical framework
- **Use Case:** Architectural validation and debugging base

#### 2. **Solvable Case Detector** (`solve_poly_5_special.asm`)
- **Purpose:** Identify quintics that ARE solvable by radicals
- **Special Cases:**
  - **Monomial:** `x⁵ - a = 0` → `x = ⁿ√a · ωᵏ` (5th roots of unity)
  - **Binomial:** `x⁵ + px + q = 0` (Bring-Jerrard form)
  - **De Moivre Type:** Special symmetry patterns
  - **Factorizable:** Cases reducible to lower degrees

#### 3. **Numerical Solver** (`solve_poly_5_numerical.asm`)
- **Purpose:** General quintic solving via numerical methods
- **Methods:**
  - **Newton-Raphson:** Iterative root refinement
  - **Durand-Kerner:** Simultaneous approximation of all roots
  - **Aberth Method:** Enhanced parallel root finding
  - **Deflation:** Sequential root extraction

#### 4. **Hybrid Implementation** (`solve_poly_5_hybrid.asm`)
- **Purpose:** Combine algebraic detection with numerical solving
- **Flow:**
  1. **Discriminant Analysis** - Classify root structure
  2. **Solvability Test** - Check for special cases
  3. **Method Selection** - Algebraic vs. numerical approach
  4. **Root Extraction** - Apply appropriate solver

## 📐 **Stack Layout (Quintic Extension)**

Extended from quartic 16-byte alignment pattern:

```assembly
; Input coefficients (degree 5: 0 to 80)
[rsp+0]   : a (x⁵ coefficient)  
[rsp+16]  : b (x⁴ coefficient)  
[rsp+32]  : c (x³ coefficient)  
[rsp+48]  : d (x² coefficient)  
[rsp+64]  : e (x¹ coefficient)  
[rsp+80]  : f (constant term)   

; Working space (starts at 96)
[rsp+96]  : Discriminant calculations
[rsp+112] : Newton-Raphson iterates
[rsp+128] : Root approximations (real parts)
[rsp+144] : Root approximations (imaginary parts)
[rsp+160] : Convergence tolerances
[rsp+176] : Special case flags
```

## 🔬 **Galois Theory Implementation**

### **Solvability Detection:**
```assembly
; Pseudo-code for solvability check
check_solvable_quintic:
    ; 1. Compute quintic discriminant
    ; 2. Check for monomial form (4 zero coefficients)
    ; 3. Test binomial patterns
    ; 4. Analyze coefficient relationships
    ; 5. Return solvability flag
```

### **Group Theory Insights:**
- **S₅ Structure:** 120 permutations, non-abelian
- **A₅ Subgroup:** 60 even permutations, simple group
- **Solvable Subgroups:** Only those avoiding A₅ patterns
- **Radical Extensions:** Limited to specific coefficient relationships

## 🧮 **Test Cases**

### **Solvable Cases:**
1. **Monomial:** `x⁵ - 32 = 0` → `x = 2ω^k` where ω = e^(2πi/5)
2. **Binomial:** `x⁵ + 5x - 12 = 0` (special Bring-Jerrard case)
3. **Factorizable:** `(x² + 1)(x³ - 8) = 0` → known roots

### **General Cases (Numerical):**
1. **Wilkinson:** `x⁵ - 15x⁴ + 85x³ - 225x² + 274x - 120 = 0`
2. **Oscillatory:** `x⁵ - x⁴ - 4x³ + 4x² + x - 1 = 0`
3. **Complex Dominant:** `x⁵ + x³ + x + 1 = 0`

## 🎓 **Educational Value**

### **Mathematical Concepts Demonstrated:**
- **Abstract Algebra:** Galois theory in computational practice
- **Group Theory:** Permutation groups and solvability
- **Numerical Analysis:** Iterative methods and convergence
- **Computer Algebra:** Bridging symbolic and numeric computation

### **Historical Significance:**
This implementation honors the profound mathematical insights that established the limits of algebraic solvability while demonstrating how numerical methods transcend those classical boundaries.

## 🚧 **Development Phases**

### **Phase 1: Foundation (Current)**
- ✅ Directory structure and documentation
- 🚧 Reference architecture implementation
- 🚧 Stack layout validation

### **Phase 2: Special Cases**
- 🔲 Monomial quintic solver
- 🔲 Binomial form detection
- 🔲 Factorization attempts

### **Phase 3: Numerical Methods**
- 🔲 Newton-Raphson implementation
- 🔲 Durand-Kerner method
- 🔲 Convergence and stability analysis

### **Phase 4: Integration**
- 🔲 Hybrid solver coordination
- 🔲 Error handling and edge cases
- 🔲 Performance optimization

## 🎯 **Quintic Discriminant**

The quintic discriminant is a polynomial of degree 59,049 in the coefficients - computationally intense but theoretically crucial for root classification.

**Simplified Approach:** Focus on practical discriminant approximations for:
- **Real vs. Complex root distribution**
- **Multiple root detection**
- **Numerical conditioning assessment**

---

*"The quintic stands as algebra's Everest - not conquerable by classical means, yet yielding to the persistence of numerical approximation guided by theoretical wisdom."*

**Next Steps:** Implement the reference architecture with our proven 16-byte stack patterns, then build toward the mathematical frontier where algebra meets analysis. 🧮🚀
