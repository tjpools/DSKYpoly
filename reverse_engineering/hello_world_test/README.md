# 🧑‍💻 Hello World Assembly Comparison: NASM x86-64

## � Quick Access

Scan the QR code below to visit the project repository:

![QR Code for GitHub](qr_github.png)

## �📄 Project Overview

This mini-project demonstrates and compares three simple "Hello, world!" programs written in NASM assembly for x86-64 Linux:


- 🖨️ `hello_printf.asm`: Uses the C library `printf` for output.
- 🛠️ `hello_native.asm`: Uses native Linux syscalls for output (no libc).
- 🪶 `hello_minimal.asm`: Uses the absolute minimal code and direct syscalls (no libc, no extra sections).

The goal is to build both binaries and analyze their differences using a reverse engineering tool such as Ghidra.

---

## 🏗️ Build Instructions

```sh
# Assemble and link printf version
nasm -f elf64 hello_printf.asm -o hello_printf.o
gcc hello_printf.o -o hello_printf

 # Assemble and link native syscall version
nasm -f elf64 hello_native.asm -o hello_native.o
ld hello_native.o -o hello_native

# Assemble and link minimal version
nasm -f elf64 hello_minimal.asm -o hello_minimal.o
ld hello_minimal.o -o hello_minimal
```

---

## 🚀 Run Instructions

```sh
./hello_printf    # Output using printf (libc)
./hello_native    # Output using native syscalls
./hello_minimal   # Output using minimal direct syscalls
```

---

## 🔍 Reverse Engineering Exercise

1. Open all three binaries (`hello_printf`, `hello_native`, and `hello_minimal`) in Ghidra or your favorite disassembler.
2. Compare:
   - Function calls and library dependencies
   - Program entry points and structure
   - System call usage vs. libc abstraction
   - Binary size and complexity
   - How much code is truly required for "Hello, world!"
3. Observe how high-level output ("Hello, world!") is implemented differently at the machine level.

---

## 🧩 Symbolic Glyphs

- 🖨️ = printf (libc abstraction)
- 🛠️ = native syscall (direct kernel interface)
- 🪶 = minimal syscall (ultra-minimal, no extras)
- 🔍 = reverse engineering/analysis
- 🧑‍💻 = assembly programming

---

## 📚 Purpose

This project is a simple, hands-on demonstration for learning and teaching:
- The difference between library-based and native system call programming
- How reverse engineering tools reveal program structure
- The basics of x86-64 assembly and Linux binary formats
