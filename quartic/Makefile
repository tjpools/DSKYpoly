# === Makefile for DSKYpoly-4 (Quartic Solver) ===
# Ferrari's Method for Quartic Polynomial Root Finding

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
CUBIC   = ../cubic

# Source files
C_SRC   = $(SRC)/main.c
ASM_SRC_REF = $(SRC)/solve_poly_4_reference.asm
ASM_SRC_PROD = $(SRC)/solve_poly_4_production.asm

# Object and Binary output
OBJ     = $(BUILD)/main.o $(BUILD)/solve_poly_4_reference.o $(BUILD)/solve_poly_4_production.o
EXE     = $(BUILD)/dskypoly4

# Targets we can invoke from terminal
.PHONY: all clean run test log_structure debug check version doctor lattice tag grammar automorphism_detailed reflect ferrari_info

# === Core Build Rules ===
all: $(EXE) log_structure debug check

# === Ensure build directory exists ===
build:
	@mkdir -p $(BUILD)

# === Linking: final binary from object files ===
$(EXE): $(OBJ) | build
	@echo "🖇️ Linking quartic solver..."
	$(CC) $(OBJ) -o $@ $(LDFLAGS)

# === Compile C source ===
$(BUILD)/main.o: $(C_SRC) | build
	@echo "📐 Compiling C interface..."
	$(CC) $(CFLAGS) -c $< -o $@

# === Assemble Reference Architecture ===
$(BUILD)/solve_poly_4_reference.o: $(ASM_SRC_REF) | build
	@echo "🔧 Assembling Ferrari's method (reference architecture)..."
	$(AS) $(ASFLAGS) $< -o $@

# === Assemble Production Implementation ===
$(BUILD)/solve_poly_4_production.o: $(ASM_SRC_PROD) | build
	@echo "🔧 Assembling Ferrari's method (production implementation)..."
	$(AS) $(ASFLAGS) $< -o $@

# === Run the program ===
run: $(EXE)
	@echo "🚀 Running DSKYpoly-4 (Ferrari's Method)..."
	./$(EXE)

# === Clean build artifacts ===
clean:
	@echo "♻️  Cleaning quartic build files..."
	rm -rf $(BUILD)/*.o $(EXE) DSKYpoly4.log lattice.png $(BUILD)/automorphism_detailed.png

# === Log project structure ===
log_structure:
	@echo "================================================================"
	@echo "📁 Logging quartic project structure..."
	@echo "=== Quartic Project Structure Snapshot ===" > DSKYpoly4.log
	@date >> DSKYpoly4.log
	@tree -L 3 . >> DSKYpoly4.log
	@echo "" >> DSKYpoly4.log

# === Debug info ===
debug:
	@echo "================================================================"
	@echo "🧠 Quartic Debug Info:"
	@echo " Source Directory:     $(SRC)"
	@echo " Build Directory:      $(BUILD)"
	@echo " C Source File:        $(C_SRC)"
	@echo " ASM Reference:        $(ASM_SRC_REF)"
	@echo " ASM Production:       $(ASM_SRC_PROD)"
	@echo " Object Files:         $(OBJ)"
	@echo " Executable Target:    $(EXE)"
	@echo " Compiler:             $(CC)"
	@echo " Assembler:            $(AS)"
	@echo " Cubic Dependency:     $(CUBIC)"

# === Pre-build checks ===
check:
	@echo "================================================================"
	@echo "🔍 Checking Quartic Project Structure..."
	@test -f $(C_SRC) && echo "✅ Found: $(C_SRC)" || echo "❌ Missing: $(C_SRC)"
	@test -f $(ASM_SRC_REF) && echo "✅ Found: $(ASM_SRC_REF)" || echo "❌ Missing: $(ASM_SRC_REF)"
	@test -f $(ASM_SRC_PROD) && echo "✅ Found: $(ASM_SRC_PROD)" || echo "❌ Missing: $(ASM_SRC_PROD)"
	@test -f Makefile && echo "✅ Found: Makefile" || echo "❌ Missing: Makefile"
	@test -d $(BUILD) && echo "✅ Found: $(BUILD)/" || echo "❌ Missing: $(BUILD)/"
	@test -d $(CUBIC) && echo "✅ Found: $(CUBIC)/ (for resolvent cubic)" || echo "❌ Missing: $(CUBIC)/"
	@echo "📝 Logging structure to DSKYpoly4.log..."
	@echo "=== Pre-Build Check ===" >> DSKYpoly4.log
	@date >> DSKYpoly4.log
	@tree -L 3 . >> DSKYpoly4.log
	@echo "" >> DSKYpoly4.log

# === Git version info ===
version:
	@echo "================================================================"
	@echo "🌐 Git Version Info:"
	@git log -1 --pretty=format:"Commit: %h%nAuthor: %an%nDate: %ad%nMessage: %s"
	@echo ""
	@echo "📝 Logging to DSKYpoly4.log..."
	@echo "=== Git Version ===" >> DSKYpoly4.log
	@git log -1 --pretty=format:"[%ad] %h - %s" >> DSKYpoly4.log
	@echo "" >> DSKYpoly4.log

# === Makefile hygiene check ===
doctor:
	@echo "================================================================"
	@echo "🩺 Running Makefile diagnostics..."
	@grep -n '^[ ]\+[^#[:space:]]' Makefile && echo "⚠️  Found lines starting with spaces!" || echo "✅ No space-indented commands found."

# === Optional: Generate lattice diagram ===
lattice:
	@echo "🔗 Generating quartic lattice diagram..."
	dot -Tpng lattice.dot -o lattice.png

# === Run a symbolic test case ===
test: run
	@echo "🧪 Testing quartic: x⁴ - 10x² + 9 = 0"
	@echo "Expected: Roots at x = ±1, ±3"
	@echo "This is a biquadratic - perfect for Ferrari method validation"

# === Tag this version in Git ===
tag:
	@git tag -a v1.0-quartic -m "Stable quartic solver with Ferrari's method"
	@git push origin v1.0-quartic

# === Log symbolic grammar ===
grammar:
	@echo "================================================================"
	@echo "📜 Logging quartic grammar..."
	@echo "=== DSKYpoly-4 Grammar ===" >> DSKYpoly4.log
	@date >> DSKYpoly4.log
	@cat grammar/dskypoly.bnf >> DSKYpoly4.log
	@echo "" >> DSKYpoly4.log
	@echo "=== Grammar Commentary ===" >> DSKYpoly4.log
	@cat grammar/README.md >> DSKYpoly4.log
	@echo "" >> DSKYpoly4.log
	@echo "Quartic grammar logged to DSKYpoly4.log"

# === Generate detailed automorphism graph ===
automorphism_detailed: | build
	@echo "================================================================"
	@echo "🧭 Generating quartic automorphism graph..."
	dot -Tpng grammar/automorphism_detailed.dot -o build/automorphism_detailed.png
	@echo "🖼️  Generated: $(PWD)/build/automorphism_detailed.png"
	@echo "📂 Opening image viewer..."
	@eog build/automorphism_detailed.png 2>/dev/null &

# === Ferrari method information ===
ferrari_info:
	@echo "================================================================"
	@echo "🎯 Ferrari's Method for Quartic Equations"
	@echo "🏛️  Historical: Ludovico Ferrari (1522-1565), student of Cardano"
	@echo "📐 Algorithm:"
	@echo "   1. Depress quartic: ax⁴ + bx³ + cx² + dx + e → y⁴ + py² + qy + r"
	@echo "   2. Resolvent cubic: 8t³ + 8pt² + (2p² - 8r)t - q² = 0"
	@echo "   3. Solve cubic using Cardano's method"
	@echo "   4. Extract quartic roots from cubic solution"
	@echo "🔗 Dependency: Uses cubic solver for resolvent cubic"
	@echo "📝 Logging Ferrari info to DSKYpoly4.log..."
	@echo "=== Ferrari Method Info ===" >> DSKYpoly4.log
	@date >> DSKYpoly4.log
	@echo "Ferrari's method transforms quartic → cubic → solution" >> DSKYpoly4.log
	@echo "Resolvent cubic: 8t³ + 8pt² + (2p² - 8r)t - q² = 0" >> DSKYpoly4.log
	@echo "" >> DSKYpoly4.log

# === Reflective snapshot of the quartic system ===
reflect: grammar automorphism_detailed version ferrari_info
	@echo "================================================================"
	@echo "🪞 Quartic reflective snapshot complete."
	@echo "📘 Includes: Grammar, Commentary, Automorphism Graph, Git Version, Ferrari Info"
	@echo "📝 See: DSKYpoly4.log and build/automorphism_detailed.png"
	@echo "" >> DSKYpoly4.log
	@echo "=== Quartic System Symbolic Verbs (.PHONY Targets) ===" >> DSKYpoly4.log
	@date >> DSKYpoly4.log
	@echo "Available symbolic operations in the quartic system:" >> DSKYpoly4.log
	@grep "^\.PHONY:" Makefile | sed 's/\.PHONY: //' | tr ' ' '\n' | sort | sed 's/^/  - /' >> DSKYpoly4.log
	@echo "" >> DSKYpoly4.log
	@echo "These targets represent the symbolic verbs for interacting with" >> DSKYpoly4.log
	@echo "the DSKYpoly quartic solver using Ferrari's method. Each verb" >> DSKYpoly4.log
	@echo "encapsulates a specific transformation, analysis, or reflection" >> DSKYpoly4.log
	@echo "operation on the quartic polynomial solving system." >> DSKYpoly4.log
	@echo "" >> DSKYpoly4.log
	@echo "The quartic solver extends the cubic through Ferrari's elegant" >> DSKYpoly4.log
	@echo "reduction: quartic → resolvent cubic → Cardano's method → roots" >> DSKYpoly4.log
	@echo "" >> DSKYpoly4.log
