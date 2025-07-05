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
.PHONY: all clean run test log_structure debug check version doctor lattice tag

# === Core Build Rules ===
all: $(EXE) log_structure debug check

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
	rm -rf $(BUILD)/*.o $(EXE) DSKYpoly3.log lattice.png

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
