# === Makefile for DSKYpoly-3 (Cubic Solver) ===

# Compiler and Assembler
CC      = gcc
AS      = nasm

# Flags
CFLAGS  = -Wall -g
ASFLAGS = -f elf64
LDFLAGS = -no-pie -lm

# Folder Structure
BUILD   = build
SRC     = src
INCLUDE = include

# Source files
C_SRC   = $(SRC)/main.c
ASM_SRC = $(SRC)/solve_poly_3.asm

# Object and Binary output
OBJ     = $(BUILD)/main.o $(BUILD)/solve_poly_3.o
EXE     = $(BUILD)/dskypoly3

# Targets we can invoke from terminal
.PHONY: all clean run test log_structure debug check version doctor lattice tag grammar automorphism_detailed reflect

# === Core Build Rules ===
all: $(EXE) log_structure debug check

# === Ensure build directory exists ===
build:
	@mkdir -p $(BUILD)

# === Linking: final binary from object files ===
$(EXE): $(OBJ)
	@echo "🖇️ Linking object files..."
	$(CC) $(LDFLAGS) $(OBJ) -o $@

# === Compile C source ===
$(BUILD)/main.o: $(C_SRC)
	@echo "📐 Compiling C source..."
	@mkdir -p $(BUILD)
	$(CC) $(CFLAGS) -c $< -o $@

# === Assemble NASM source ===
$(BUILD)/solve_poly_3.o: $(ASM_SRC)
	@echo "🔧 Assembling NASM source..."
	@mkdir -p $(BUILD)
	$(AS) $(ASFLAGS) $< -o $@

# === Run the program ===
run: $(EXE)
	@echo "🚀 Running DSKYpoly-3..."
	./$(EXE)

# === Clean build artifacts ===
clean:
	@echo "♻️  Cleaning build files..."
	rm -rf $(BUILD)/*.o $(EXE) DSKYpoly3.log lattice.png $(BUILD)/automorphism_detailed.png

# === Log project structure ===
log_structure:
	@echo "================================================================"
	@echo "📁 Logging project structure..."
	@echo "=== Project Structure Snapshot ===" > DSKYpoly3.log
	@date >> DSKYpoly3.log
	@tree -L 2 . >> DSKYpoly3.log
	@echo "" >> DSKYpoly3.log

# === Debug info ===
debug:
	@echo "================================================================"
	@echo "🧠 Debug Info:"
	@echo " Source Directory:     $(SRC)"
	@echo " Build Directory:      $(BUILD)"
	@echo " C Source File:        $(C_SRC)"
	@echo " ASM Source File:      $(ASM_SRC)"
	@echo " Object Files:         $(OBJ)"
	@echo " Executable Target:    $(EXE)"
	@echo " Compiler:             $(CC)"
	@echo " Assembler:            $(AS)"

# === Pre-build checks ===
check:
	@echo "================================================================"
	@echo "🔍 Checking Project Structure..."
	@test -f $(C_SRC) && echo "✅ Found: $(C_SRC)" || echo "❌ Missing: $(C_SRC)"
	@test -f $(ASM_SRC) && echo "✅ Found: $(ASM_SRC)" || echo "❌ Missing: $(ASM_SRC)"
	@test -f Makefile && echo "✅ Found: Makefile" || echo "❌ Missing: Makefile"
	@test -d $(BUILD) && echo "✅ Found: $(BUILD)/" || echo "❌ Missing: $(BUILD)/"
	@echo "📝 Logging structure to DSKYpoly3.log..."
	@echo "=== Pre-Build Check ===" >> DSKYpoly3.log
	@date >> DSKYpoly3.log
	@tree -L 2 . >> DSKYpoly3.log
	@echo "" >> DSKYpoly3.log

# === Git version info ===
version:
	@echo "================================================================"
	@echo "🌐 Git Version Info:"
	@git log -1 --pretty=format:"Commit: %h%nAuthor: %an%nDate: %ad%nMessage: %s"
	@echo ""
	@echo "📝 Logging to DSKYpoly3.log..."
	@echo "=== Git Version ===" >> DSKYpoly3.log
	@git log -1 --pretty=format:"[%ad] %h - %s" >> DSKYpoly3.log
	@echo "" >> DSKYpoly3.log

# === Makefile hygiene check ===
doctor:
	@echo "================================================================"
	@echo "🩺 Running Makefile diagnostics..."
	@grep -n '^[ ]\+[^#[:space:]]' Makefile && echo "⚠️  Found lines starting with spaces!" || echo "✅ No space-indented commands found."

# === Optional: Generate lattice diagram ===
lattice:
	dot -Tpng lattice.dot -o lattice.png

# === Run a symbolic test case ===
test: run
	@echo "🧪 Testing cubic: x³ - 6x² + 11x - 6 = 0"
	@echo "Expected: Roots at x = 1, 2, 3"

# === Tag this version in Git ===
tag:
	@git tag -a v1.0-cubic -m "Stable cubic solver with real/complex root support"
	@git push origin v1.0-cubic

# === Log symbolic grammar ===
grammar:
	@echo "================================================================"
	@echo "📜 Logging symbolic grammar..."
	@echo "=== DSKYpoly Grammar ===" >> DSKYpoly3.log
	@date >> DSKYpoly3.log
	@cat grammar/dskypoly.bnf >> DSKYpoly3.log
	@echo "" >> DSKYpoly3.log
	@echo "=== Grammar Commentary ===" >> DSKYpoly3.log
	@cat grammar/README.md >> DSKYpoly3.log
	@echo "" >> DSKYpoly3.log
	@echo "Grammar logged to DSKYpoly3.log"

# === Generate detailed automorphism graph ===
automorphism_detailed: | build
	@echo "================================================================"
	@echo "🧭 Generating detailed automorphism graph..."
	dot -Tpng grammar/automorphism_detailed.dot -o build/automorphism_detailed.png
	@echo "🖼️  Generated: $(PWD)/build/automorphism_detailed.png"
	@echo "📂 Opening image viewer..."
	@eog build/automorphism_detailed.png 2>/dev/null &

# === Reflective snapshot of the system ===
reflect: grammar automorphism_detailed version
	@echo "================================================================"
	@echo "🪞 Reflective snapshot complete."
	@echo "📘 Includes: Grammar, Commentary, Automorphism Graph, Git Version"
	@echo "📝 See: DSKYpoly3.log and build/automorphism_detailed.png"
	@echo "" >> DSKYpoly3.log
	@echo "=== System Symbolic Verbs (.PHONY Targets) ===" >> DSKYpoly3.log
	@date >> DSKYpoly3.log
	@echo "Available symbolic operations in this system:" >> DSKYpoly3.log
	@grep "^\.PHONY:" Makefile | sed 's/\.PHONY: //' | tr ' ' '\n' | sort | sed 's/^/  - /' >> DSKYpoly3.log
	@echo "" >> DSKYpoly3.log
	@echo "These targets represent the symbolic verbs available to interact" >> DSKYpoly3.log
	@echo "with the DSKYpoly cubic solver system. Each verb encapsulates" >> DSKYpoly3.log
	@echo "a specific transformation or introspection operation." >> DSKYpoly3.log
	@echo "" >> DSKYpoly3.log