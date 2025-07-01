# === Makefile for DSKYpoly ===

# Compiler and Assembler
CC	= gcc					# The C compiler
AS	= nasm					# The assembler for x86-64 NASM

# Flags						
CFLAGS  = -Wall -g				# Warn about all issues and include debug symbols
ASFLAGS = -f elf64				# Output format compatible with Linux x86-64
LDFLAGS = 					# Optional: linker flags (empty for now)

# Folder Structure
BUILD   = build
SRC     = src
INCLUDE = include

# Source files
C_SRC   = $(SRC)/main.c
ASM_SRC = $(SRC)/solve_poly_2.asm

# Object and Binary output
OBJ     = $(BUILD)/main.o $(BUILD)/solve_poly_2.o
EXE     = $(BUILD)/dskypoly

# Targets we can invoke from terminal
.PHONY: all clean run

# === Core Build Rules ===
all: $(EXE) log_structure debug check

# ===  Linking: final binary from object files ===
$(EXE): $(OBJ)
	@echo "🖇️ Linking object files..."
	$(CC) $(OBJ) -o $@

# === Compile C source ===
$(BUILD)/main.o: $(C_SRC)
	@echo "📐 Compiling C source..."
	$(CC) $(CFLAGS) -c $< -o $@

# === Assemble NASM source ===
$(BUILD)/solve_poly_2.o: $(ASM_SRC)
	@echo " Assembling Nasm source..."
	$(AS) $(ASFLAGS) $< -o $@

# === Run the program ===
run: $(EXE)
	@echo " 🚀 Running DSKYpoly..."
	./$(EXE)

# === Clean build artifacts
clean:
	@echo " ♻️  Cleaning build files..."
	rm -rf $(BUILD)/*.0 $(EXE)

log_structure:
	# your logging command here
	@echo "======================================================"
	@echo " Logging project structure ..."
	@echo "=== Project Stucture Snapshot ===" > DSKYpoly.log
	@date >> DSKYpoly.log
	@tree -L 2 . >> DSKYpoly.log
	@echo "" >> DSKYpoly.log

debug:
	# your debug variable prints here
	@echo "======================================================"
	@echo " Debug Info:"
	@echo " Source Directory:	$(SRC)"
	@echo " Build Directory:	$(BUILD)"	
	@echo " C Source File:		$(C_SRC)"
	@echo " ASM Source File:	$(ASM_SRC)"
	@echo " Object Files:		$(OBJ)"
	@echo " Executable Target:	$(EXE)"
	@echo " Compiler:		$(CC)"
	@echo " Assembler: 		$(AS)"

check:
	# your file presence checks here
	@echo "======================================================"
	@echo "🔧 Current directory: $(shell pwd)"
	@echo "💻🔗💾 Checking Project Structure..."
	@test -f $(C_SRC) && echo "😎💻⚡️Found: $(C_SRC)" || echo "🛠️Missing: $(C_SRC)"
	@test -f $(ASM_SRC) && echo " Found: $(ASM_SRC)" || echo "Missing: $(ASM_SRC)"
	@test -f MakeFile && echo " Found: Makefile" || echo "Missing: Makefile"
	@test -d $(BUILD) && echo " Found: $(BUILD)/" || echo "Missing: $(BUILD)/"
	@echo "📝 Logging structure to DSKYpoly.log..."
	@echo "=== Pre-Build Check ===" >> DSKYpoly.log
	@date >> DSKYpoly.log
	@tree -L 2 . >> DSKYpoly.log
	@echo "" >> DSKYpoly.log
