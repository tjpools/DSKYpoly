# === Makefile for DSKYpoly-5 (Quintic Solver) ===
# Beyond Radical Solvability: Numerical Methods for General Quintics

# Compiler and Assembler
CC      = gcc
AS      = nasm

# Flags
CFLAGS  = -Wall -g -O2
ASFLAGS = -f elf64
LDFLAGS = -no-pie -lm

# Folder Structure
BUILD   = build
SRC     = src
INCLUDE = include
QUARTIC = ../quartic

# Source files
C_SRC   = $(SRC)/main.c
ASM_SRC_REF = $(SRC)/solve_poly_5_reference.asm
ASM_SRC_SPECIAL = $(SRC)/solve_poly_5_special.asm
ASM_SRC_NUMERICAL = $(SRC)/solve_poly_5_numerical.asm
ASM_SRC_HYBRID = $(SRC)/solve_poly_5_hybrid.asm

# Object and Binary output
OBJ     = $(BUILD)/main.o $(BUILD)/solve_poly_5_reference.o $(BUILD)/solve_poly_5_special.o
EXE     = $(BUILD)/dskypoly5

# Targets we can invoke from terminal
.PHONY: all clean run test log_structure debug check version doctor quintic_info galois_theory abel_ruffini

# === Core Build Rules ===
all: $(EXE) log_structure debug check

# === Ensure build directory exists ===
build:
	@mkdir -p $(BUILD)

# === Linking: final binary from object files ===
$(EXE): $(OBJ) | build
	@echo "🖇️ Linking quintic solver..."
	$(CC) $(OBJ) -o $@ $(LDFLAGS)

# === Compile C source ===
$(BUILD)/main.o: $(C_SRC) | build
	@echo "📐 Compiling C interface..."
	$(CC) $(CFLAGS) -c $< -o $@

# === Assemble Reference Architecture ===
$(BUILD)/solve_poly_5_reference.o: $(ASM_SRC_REF) | build
	@echo "🔧 Assembling quintic solver (reference architecture)..."
	$(AS) $(ASFLAGS) $< -o $@

# === Future assembly targets ===
$(BUILD)/solve_poly_5_special.o: $(ASM_SRC_SPECIAL) | build
	@echo "🔧 Assembling solvable quintic cases..."
	$(AS) $(ASFLAGS) $< -o $@

$(BUILD)/solve_poly_5_numerical.o: $(ASM_SRC_NUMERICAL) | build
	@echo "🔧 Assembling numerical methods..."
	$(AS) $(ASFLAGS) $< -o $@

$(BUILD)/solve_poly_5_hybrid.o: $(ASM_SRC_HYBRID) | build
	@echo "🔧 Assembling hybrid solver..."
	$(AS) $(ASFLAGS) $< -o $@

# === Run the program ===
run: $(EXE)
	@echo "🚀 Running DSKYpoly-5 (Quintic Solver)..."
	./$(EXE)

# === Clean build artifacts ===
clean:
	@echo "♻️  Cleaning quintic build files..."
	rm -rf $(BUILD)/*.o $(EXE) DSKYpoly5.log

# === Log project structure ===
log_structure:
	@echo "================================================================"
	@echo "📁 Logging quintic project structure..."
	@echo "=== Quintic Project Structure Snapshot ===" > DSKYpoly5.log
	@date >> DSKYpoly5.log
	@tree -L 3 . >> DSKYpoly5.log
	@echo "" >> DSKYpoly5.log

# === Debug info ===
debug:
	@echo "================================================================"
	@echo "🧠 Quintic Debug Info:"
	@echo " Source Directory:     $(SRC)"
	@echo " Build Directory:      $(BUILD)"
	@echo " C Source File:        $(C_SRC)"
	@echo " ASM Reference:        $(ASM_SRC_REF)"
	@echo " Object Files:         $(OBJ)"
	@echo " Executable Target:    $(EXE)"
	@echo " Compiler:             $(CC)"
	@echo " Assembler:            $(AS)"
	@echo " Quartic Dependency:   $(QUARTIC)"
	@echo "================================================================"

# === Check project structure ===
check:
	@echo "🔍 Checking Quintic Project Structure..."
	@test -f $(C_SRC) && echo "✅ Found: $(C_SRC)" || echo "❌ Missing: $(C_SRC)"
	@test -f $(ASM_SRC_REF) && echo "✅ Found: $(ASM_SRC_REF)" || echo "⏳ Pending: $(ASM_SRC_REF)"
	@test -f Makefile && echo "✅ Found: Makefile" || echo "❌ Missing: Makefile"
	@test -d $(BUILD) && echo "✅ Found: $(BUILD)/" || echo "⏳ Will create: $(BUILD)/"
	@test -d $(QUARTIC) && echo "✅ Found: $(QUARTIC)/ (for reference patterns)" || echo "⚠️  Missing: $(QUARTIC)/"
	@echo "📝 Logging structure to DSKYpoly5.log..."

# === Quintic mathematical info ===
quintic_info:
	@echo "================================================================"
	@echo "🎓 Quintic Mathematical Context:"
	@echo "================================================================"
	@echo "📐 Abel-Ruffini Theorem (1824-1826):"
	@echo "   • No general quintic solvable by radicals"
	@echo "   • Proved by Niels Henrik Abel and Paolo Ruffini"
	@echo ""
	@echo "🧮 Galois Theory Insights:"
	@echo "   • Symmetric group S₅ has 120 permutations"
	@echo "   • Alternating group A₅ ⊂ S₅ (60 even permutations)"
	@echo "   • A₅ is simple and non-solvable"
	@echo "   • Only solvable subgroups allow radical solutions"
	@echo ""
	@echo "⚡ Solvable Special Cases:"
	@echo "   • Monomial: x⁵ - a = 0"
	@echo "   • Certain binomial forms"
	@echo "   • Factorizable polynomials"
	@echo ""
	@echo "🔬 Numerical Methods Required:"
	@echo "   • Newton-Raphson iteration"
	@echo "   • Durand-Kerner method"
	@echo "   • Complex root approximation"
	@echo "================================================================"

# === Galois theory educational target ===
galois_theory:
	@echo "🏛️ Galois Theory and Quintic Solvability:"
	@echo "================================================================"
	@echo "Group S₅ (Symmetric group on 5 elements):"
	@echo "  • Order: 120 elements"
	@echo "  • Generators: (1 2) and (1 2 3 4 5)"
	@echo "  • Contains A₅ as normal subgroup"
	@echo ""
	@echo "Group A₅ (Alternating group on 5 elements):"
	@echo "  • Order: 60 elements (even permutations)"
	@echo "  • Simple group (no non-trivial normal subgroups)"
	@echo "  • NOT solvable → quintic not solvable by radicals"
	@echo ""
	@echo "Solvable quintics correspond to polynomials whose"
	@echo "Galois group is a solvable subgroup of S₅, avoiding A₅."
	@echo "================================================================"

# === Abel-Ruffini theorem context ===
abel_ruffini:
	@echo "📚 Abel-Ruffini Theorem Historical Context:"
	@echo "================================================================"
	@echo "Paolo Ruffini (1765-1822):"
	@echo "  • 1799: First proof attempt (incomplete)"
	@echo "  • Showed general quintic unsolvable by radicals"
	@echo ""
	@echo "Niels Henrik Abel (1802-1829):"
	@echo "  • 1824: Complete rigorous proof"
	@echo "  • Established fundamental limitations of algebra"
	@echo "  • Opened path to Galois theory"
	@echo ""
	@echo "Impact:"
	@echo "  • End of 300-year quest for quintic formula"
	@echo "  • Birth of abstract algebra"
	@echo "  • Foundation for modern group theory"
	@echo "================================================================"

# === Version information ===
version:
	@echo "DSKYpoly-5 Quintic Solver"
	@echo "Mathematical Foundation: Abel-Ruffini Theorem + Galois Theory"
	@echo "Implementation: x86-64 Assembly + Numerical Methods"
	@echo "Status: Reference Architecture Development"
