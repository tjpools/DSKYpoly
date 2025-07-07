# DSKYpoly-4: Quartic Polynomial Solver (Ferrari's Method)

<!-- Test comment added for git commit demonstration -->

## Overview
Implementation of Ludovico Ferrari's method for solving quartic polynomial equations in x86-64 assembly language.

**Equation Form:** `ax⁴ + bx³ + cx² + dx + e = 0`

## Architecture & Pipeline

### Two-Implementation Strategy

This project maintains **two distinct implementations** that serve different purposes in our development pipeline:

#### 1. **Reference Architecture** (`solve_poly_4_reference.asm`)
- **Purpose:** Proven, stable architectural foundation
- **Status:** ✅ Guaranteed non-crashing, proper stack alignment
- **Features:**
  - 16-byte aligned stack layout
  - Proper x86-64 ABI compliance  
  - Systematic register initialization
  - Uses placeholder values for mathematical safety
- **Use Case:** Template for quintic and higher-degree implementations
- **Key Value:** When extending to quintic gets complex, we can fall back to this proven structure

#### 2. **Production Implementation** (`solve_poly_4_production.asm`)
- **Purpose:** Full mathematical Ferrari method implementation
- **Status:** ✅ Real Ferrari calculations, some numerical edge cases
- **Features:**
  - Complete depressed quartic transformation
  - Actual resolvent cubic setup
  - Real mathematical discriminant calculation
  - Proper coefficient calculations
- **Use Case:** Foundation for actual mathematical work and quintic mathematical patterns
- **Key Value:** Shows the mathematical flow needed for advanced polynomial solving

### Stack Layout (Standardized for Scalability)

Both implementations follow this **16-byte aligned pattern** that scales to quintic:

```assembly
; Input coefficients (degree n: 0 to 16*n)
[rsp+0]   : a (x^4 coefficient)  
[rsp+16]  : b (x^3 coefficient)  
[rsp+32]  : c (x^2 coefficient)  
[rsp+48]  : d (x^1 coefficient)  
[rsp+64]  : e (constant term)    

; For quintic: [rsp+80] : f (additional coefficient)

; Working space (starts at 16*(n+2))
[rsp+96+] : Intermediate calculations
[rsp+112+]: Transformed coefficients  
[rsp+128+]: Algorithm-specific values
```

## Ferrari's Method Implementation

### Mathematical Flow
1. **Input Processing:** Validate and store coefficients
2. **Depress Quartic:** Remove cubic term via substitution `y = x + b/(4a)`
3. **Resolvent Cubic:** Transform to `8t³ + 8pt² + (2p² - 8r)t - q² = 0`
4. **Solve Cubic:** Apply Cardano's method (simplified in current version)
5. **Extract Roots:** Back-substitute to get quartic roots

### Key Lessons for Quintic Development

#### ✅ **Architectural Patterns Established:**
- **Stack Discipline:** Every memory location explicitly initialized
- **Register Management:** Systematic preservation across function calls
- **Error Handling:** Proper validation and graceful degradation
- **Debugging Strategy:** Incremental testing with fallback implementations

#### 🎯 **Quintic Readiness:**
- **No General Algebraic Solution:** Abel-Ruffini theorem means numerical methods
- **Structure Scaling:** Our 16-byte pattern extends directly to quintic
- **Mathematical Foundation:** Ferrari patterns inform quintic special cases
- **Debugging Framework:** Two-implementation strategy proven effective

## Build System

### Files Structure
```
src/
├── main.c                          # C interface and test cases
├── solve_poly_4_reference.asm      # Reference architecture 
└── solve_poly_4_production.asm     # Production Ferrari implementation

Makefile                            # Builds both implementations
```

### Build Commands
```bash
make clean && make                  # Build both implementations  
./build/dskypoly4                   # Run test suite (both versions)
make run                           # Quick test
```

## Test Results

### Current Status
- **Reference:** ✅ Stable, placeholder mathematics
- **Production:** ✅ Real Ferrari math, some numerical issues (-nan in edge cases)

### Test Cases
1. **Biquadratic:** `x⁴ - 10x² + 9 = 0` → Expected: `x = ±1, ±3`
2. **Depressed:** `x⁴ - 5x² + 6 = 0` → Expected: `x = ±1, ±√6`  
3. **General:** `x⁴ - 4x³ + 6x² - 4x + 1 = 0` → Expected: `x = 1` (multiplicity 4)
4. **Complex:** `x⁴ + x² + 1 = 0` → Expected: `x = ±i, ±1/i`
5. **Ferrari Example:** Mixed real/complex roots

## Next Steps: Quintic Development

### Planned Architecture
```
DSKYpoly-5/
├── solve_poly_5_reference.asm      # Copy reference stack patterns
├── solve_poly_5_numerical.asm      # Numerical methods (Newton-Raphson, etc.)
├── solve_poly_5_special.asm       # Special cases (depressed quintic, etc.)
└── solve_poly_5_hybrid.asm        # Combined algebraic/numerical approach
```

### Key Insights Applied
1. **Start with proven stack structure** from reference implementation
2. **Apply mathematical patterns** from production implementation  
3. **Maintain two-track development** for stability and innovation
4. **Scale the 16-byte alignment pattern** to 6 coefficients
5. **Implement numerical methods** due to Abel-Ruffini limitations

## Historical Context

**Ludovico Ferrari (1522-1565)**
- Student of Gerolamo Cardano
- Discovered general solution to quartic equations  
- Method: Reduce quartic to resolvent cubic
- Revolutionary: First general algebraic solution beyond cubic
- Foundation: Our implementation honors his mathematical legacy

---

*"The quartic yields its secrets through cubic wisdom, but the quintic guards its mysteries with algebraic impossibility."*

## Development Notes

### Debugging Session Results
- **Critical Issue:** Uninitialized registers causing segfaults
- **Solution:** Systematic stack offset management
- **Key Learning:** Consistent memory layout prevents architectural bugs
- **Impact:** Methodology ready for quintic complexity

### Architecture Validation
- ✅ Stack alignment (16-byte boundaries)
- ✅ Register initialization discipline  
- ✅ x86-64 ABI compliance
- ✅ Scalable coefficient storage pattern
- ✅ Error handling and validation
