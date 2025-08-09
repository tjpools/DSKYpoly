chmod_flat: hello_flat.bin   # 🗝️ Make flat binary executable
	chmod +x hello_flat.bin
# 🧑‍💻🛠️ Makefile for Hello World Assembly Comparison Project

all: hello_printf hello_native hello_minimal   # 🏗️ Build all

hello_minimal: hello_minimal.asm   # 🪶 Build minimal version
	nasm -f elf64 hello_minimal.asm -o hello_minimal.o
	ld hello_minimal.o -o hello_minimal

run_minimal: hello_minimal   # ▶️ Run minimal version
	./hello_minimal
hello_minelf: hello_minelf.asm   # 🧬 Build minimal ELF64 binary
	nasm -f bin hello_minelf.asm -o hello_minelf
	chmod +x hello_minelf

run_minelf: hello_minelf   # ▶️ Run minimal ELF64 binary
	./hello_minelf

hello_printf: hello_printf.asm   # 🖨️ Build printf version
	nasm -f elf64 hello_printf.asm -o hello_printf.o
	gcc hello_printf.o -o hello_printf

hello_native: hello_native.asm   # 🛠️ Build native syscall version
	nasm -f elf64 hello_native.asm -o hello_native.o
	ld hello_native.o -o hello_native

run_printf: hello_printf   # ▶️ Run printf version
	./hello_printf

run_native: hello_native   # ▶️ Run native syscall version
	./hello_native

hello_flat.bin: hello_flat.asm   # 🦠 Build flat binary (raw, not ELF)
	nasm -f bin hello_flat.asm -o hello_flat.bin

analyze_flat:   # 🔬 Ghidra import instructions for flat binary
	@echo "To analyze hello_flat.bin in Ghidra:"
	@echo "1. File → Import File... → Select hello_flat.bin"
	@echo "2. Set Format: Raw Binary, Language: x86:LE:64:default, Base Address: 0x400000"
	@echo "3. Finish import and manually define entry point at 0x400000 (label as start)"

clean:   # 🧹 Clean build artifacts
	rm -f hello_printf.o hello_native.o hello_printf hello_native hello_minimal.o hello_minimal

# Open Ghidra (edit GHIDRA_PATH if needed)
GHIDRA_PATH ?= /opt/ghidra
ghidra:
	$(GHIDRA_PATH)/ghidraRun $(CURDIR)/hello_printf $(CURDIR)/hello_native &

.PHONY: all clean run_printf run_native run_minimal ghidra