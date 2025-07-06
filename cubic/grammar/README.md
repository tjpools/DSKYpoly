# DSKYpoly Grammar Notes

This directory contains the formal grammar for the cubic solver's symbolic instruction set.

## 📘 What This Grammar Captures

- The symbolic structure of x86-64 floating-point computation
- The internal logic of the solver as a transformation system
- The constraints and flow of computation through mnemonics
- A parallel to Galois theory: automorphisms of a symbolic field

## 🧠 Design Philosophy

This grammar treats the instruction set as a symbolic language. Each valid sequence of instructions is an automorphism—preserving the internal logic of the computational field.

The `.bnf` file is not just a syntax spec—it is a mirror of the machine’s symbolic soul.