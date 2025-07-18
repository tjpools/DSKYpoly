#!/bin/bash
# DSKYpoly Reverse Engineering Analysis Toolkit
# Comprehensive analysis of mathematical software binaries

echo "🔍 DSKYpoly Reverse Engineering Analysis Toolkit"
echo "================================================="
echo ""

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

ANALYSIS_DIR="analysis"
DISASM_DIR="$ANALYSIS_DIR/disassembly"
REPORTS_DIR="$ANALYSIS_DIR/reports"

# Create output directories
mkdir -p "$DISASM_DIR" "$REPORTS_DIR"

echo -e "${BLUE}Phase 1: Static Binary Analysis${NC}"
echo "================================="

# Function to analyze a binary
analyze_binary() {
    local binary_path="$1"
    local binary_name=$(basename "$binary_path")
    local output_base="$DISASM_DIR/${binary_name}"
    
    if [ ! -f "$binary_path" ]; then
        echo -e "${RED}❌ Binary not found: $binary_path${NC}"
        return 1
    fi
    
    echo -e "${GREEN}🔍 Analyzing: $binary_name${NC}"
    
    # Basic file information
    echo "📊 File Information:" > "${output_base}_info.txt"
    file "$binary_path" >> "${output_base}_info.txt"
    size "$binary_path" >> "${output_base}_info.txt"
    
    # Disassembly with objdump
    echo "🔧 Generating disassembly..."
    objdump -d "$binary_path" > "${output_base}_disasm.txt"
    objdump -t "$binary_path" > "${output_base}_symbols.txt"
    objdump -h "$binary_path" > "${output_base}_headers.txt"
    
    # String analysis
    echo "🔤 Extracting strings..."
    strings "$binary_path" > "${output_base}_strings.txt"
    
    # Function analysis
    echo "🎯 Analyzing functions..."
    objdump -t "$binary_path" | grep -E "(solve|poly|root|quartic|cubic)" > "${output_base}_math_functions.txt"
    
    # Create analysis summary
    echo "📋 Creating analysis summary..."
    {
        echo "# $binary_name Analysis Summary"
        echo "Generated: $(date)"
        echo ""
        echo "## File Information"
        cat "${output_base}_info.txt"
        echo ""
        echo "## Mathematical Functions Found"
        cat "${output_base}_math_functions.txt"
        echo ""
        echo "## Key Strings"
        head -20 "${output_base}_strings.txt"
    } > "${output_base}_summary.md"
    
    echo -e "${GREEN}✅ Analysis complete for $binary_name${NC}"
    echo ""
}

# Analyze all DSKYpoly binaries
echo "🎯 Analyzing DSKYpoly Binaries"
echo "==============================="

# Main quadratic solver
if [ -f "build/dskypoly" ]; then
    analyze_binary "build/dskypoly"
fi

# Cubic solver
if [ -f "cubic/build/dskypoly3" ]; then
    analyze_binary "cubic/build/dskypoly3"
fi

# Quartic solver
if [ -f "quartic/build/dskypoly4" ]; then
    analyze_binary "quartic/build/dskypoly4"
fi

# Quintic solver (if compiled)
if [ -f "quintic/build/dskypoly5" ]; then
    analyze_binary "quintic/build/dskypoly5"
fi

echo -e "${BLUE}Phase 2: Comparative Analysis${NC}"
echo "==============================="

# Create comparative analysis report
{
    echo "# DSKYpoly Comparative Binary Analysis"
    echo "Generated: $(date)"
    echo ""
    echo "## Overview"
    echo "This report compares the compiled binaries of different polynomial solvers"
    echo "to understand how mathematical algorithms translate to machine code."
    echo ""
    echo "## Binary Sizes"
    for binary in build/dskypoly cubic/build/dskypoly3 quartic/build/dskypoly4; do
        if [ -f "$binary" ]; then
            echo "- $(basename $binary): $(wc -c < "$binary") bytes"
        fi
    done
    echo ""
    echo "## Function Count Analysis"
    for disasm_file in $DISASM_DIR/*_symbols.txt; do
        if [ -f "$disasm_file" ]; then
            binary_name=$(basename "$disasm_file" _symbols.txt)
            func_count=$(grep -c "F \.text" "$disasm_file" 2>/dev/null || echo "0")
            echo "- $binary_name: $func_count functions"
        fi
    done
    echo ""
    echo "## Next Steps"
    echo "1. Manual analysis with Ghidra"
    echo "2. Dynamic analysis with GDB"
    echo "3. Performance profiling"
    echo "4. Optimization opportunity identification"
} > "$REPORTS_DIR/comparative_analysis.md"

echo -e "${GREEN}🎉 Analysis Complete!${NC}"
echo "======================="
echo ""
echo "📂 Results saved in:"
echo "  - Disassembly: $DISASM_DIR/"
echo "  - Reports: $REPORTS_DIR/"
echo ""
echo "🔍 Next steps:"
echo "  1. Review generated reports"
echo "  2. Import binaries into Ghidra"
echo "  3. Perform dynamic analysis with GDB"
echo "  4. Create educational content from findings"
echo ""
