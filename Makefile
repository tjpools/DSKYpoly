# === Makefile for DSKYpoly ===

# Compiler and Assembler
CC = gcc
AS = nasm

# Flags
CFLAGS = -Wall -g -no-pie
ASFLAGS = -f elf64
LDFLAGS = -no-pie

# Folder Structure
BUILD = build
SRC = src
INCLUDE = include

# Source files
C_SRC = $(SRC)/main.c
ASM_SRC = $(SRC)/solve_poly_2.asm

# Object and Binary output
OBJ = $(BUILD)/main.o $(BUILD)/solve_poly_2.o
EXE = $(BUILD)/dskypoly

# Targets we can invoke from terminal
.PHONY: all clean run

# === Core Build Rules ===
all: $(EXE) log_structure debug check

# === Linking: final binary from object files ===
$(EXE): $(OBJ)
	@echo "🖇️ Linking object files..."
	$(CC) $(LDFLAGS) $(OBJ) -o $@

# === Compile C source ===
$(BUILD)/main.o: $(C_SRC)
	@echo "📐 Compiling C source..."
	$(CC) $(CFLAGS) -c $< -o $@

# === Assemble NASM source ===
$(BUILD)/solve_poly_2.o: $(ASM_SRC)
	@echo "🔧 Assembling NASM source..."
	$(AS) $(ASFLAGS) $< -o $@

# === Run the program ===
run: $(EXE)
	@echo "🚀 Running DSKYpoly..."
	./$(EXE)

# === Clean build artifacts ===
clean:
	@echo "♻️ Cleaning build files..."
	rm -rf $(BUILD)/*.o $(EXE)

log_structure:
	@echo "================================================================"
	@echo "Logging project structure ..."
	@echo "=== Project Structure Snapshot ===" > DSKYpoly.log
	@date >> DSKYpoly.log
	@tree -L 2 . >> DSKYpoly.log
	@echo "" >> DSKYpoly.log

debug:
	@echo "================================================================"
	@echo "Debug Info:"
	@echo "Source Directory: $(SRC)"
	@echo "Build Directory: $(BUILD)"
	@echo "C Source File: $(C_SRC)"
	@echo "ASM Source File: $(ASM_SRC)"
	@echo "Object Files: $(OBJ)"
	@echo "Executable Target: $(EXE)"
	@echo "Compiler: $(CC)"
	@echo "Assembler: $(AS)"
	@echo "CFLAGS: $(CFLAGS)"
	@echo "ASFLAGS: $(ASFLAGS)"
	@echo "LDFLAGS: $(LDFLAGS)"

check:
	@echo "================================================================"
	@echo "🔧 Current directory: $(shell pwd)"
	@echo "💻🔗💾 Checking Project Structure..."
	@test -f $(C_SRC) && echo "✅ Found: $(C_SRC)" || echo "❌ Missing: $(C_SRC)"
	@test -f $(ASM_SRC) && echo "✅ Found: $(ASM_SRC)" || echo "❌ Missing: $(ASM_SRC)"
	@test -f Makefile && echo "✅ Found: Makefile" || echo "❌ Missing: Makefile"
	@test -d $(BUILD) && echo "✅ Found: $(BUILD)/" || echo "❌ Missing: $(BUILD)/"
	@echo "📝 Logging structure to DSKYpoly.log..."
	@echo "=== Pre-Build Check ===" >> DSKYpoly.log
	@date >> DSKYpoly.log
	@tree -L 2 . >> DSKYpoly.log
	@echo "" >> DSKYpoly.log

version:
	@echo "================================================================"
	@echo "🌐 Git Version Info:"
	@git log -1 --pretty=format:"Commit: %h%nAuthor: %an%nDate: %ad%nMessage: %s"
	@echo ""
	@echo "Logging to DSKYpoly.log..."
	@echo "=== Git Version ===" >> DSKYpoly.log
	@git log -1 --pretty=format:"[%ad] %h - %s" >> DSKYpoly.log
	@echo "" >> DSKYpoly.log

doctor:
	@echo "================================================================="
	@echo "🕵️ Running Makefile diagnostics..."
	@grep -n '^[ ]\+[^#[:space:]]' Makefile && echo "⚠️ Found lines starting with spaces!" || echo "👌 No space-indented commands found."

lattice:
	dot -Tpng lattice.dot -o lattice.png

runpy:
	@./src/dskypoly.py 1 -3 2

runpy-symbolic:
	@./src/dskypoly.py "x² - 3x + 2"
