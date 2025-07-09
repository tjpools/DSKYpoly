# Grammar for DSKYpoly-4: Ferrari's Method

## Overview
This directory contains formal grammars and structural definitions for the quartic polynomial solver implementations.

## Grammar Components

### 1. Mathematical Grammar (`dskypoly.bnf`)
Defines the mathematical structure and transformations in Ferrari's method.

### 2. Architectural Grammar (`automorphism_detailed.dot`)
Describes the computational flow and register transformations.

### 3. Implementation Grammar
Documents the two-track implementation strategy.

## Usage
```bash
make grammar          # Generate grammar visualizations
make automorphism     # Generate detailed flow diagrams
```

## Purpose
- Document mathematical transformations for quintic scaling
- Validate computational correctness
- Provide formal specification for algorithm verification
