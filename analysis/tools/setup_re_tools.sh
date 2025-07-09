#!/bin/bash
# DSKYpoly Modern Reverse Engineering Tools Setup
# Install and configure cutting-edge RE tools for mathematical software analysis

echo "🔧 Setting up Modern Reverse Engineering Toolkit"
echo "================================================"
echo ""

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to install tool if not present
install_tool() {
    local tool_name="$1"
    local install_cmd="$2"
    local check_cmd="$3"
    
    if command_exists "$check_cmd"; then
        echo "✅ $tool_name already installed"
    else
        echo "📦 Installing $tool_name..."
        eval "$install_cmd"
        if command_exists "$check_cmd"; then
            echo "✅ $tool_name installed successfully"
        else
            echo "❌ Failed to install $tool_name"
        fi
    fi
}

echo "🎯 Installing Core Reverse Engineering Tools"
echo "============================================"

# Ghidra (if not already installed)
if [ ! -d "/opt/ghidra" ] && [ ! -d "$HOME/ghidra" ]; then
    echo "📥 Ghidra installation required"
    echo "Please download Ghidra from: https://ghidra-sre.org/"
    echo "Extract to /opt/ghidra or ~/ghidra"
else
    echo "✅ Ghidra found"
fi

# Radare2
install_tool "Radare2" "git clone https://github.com/radareorg/radare2 && cd radare2 && ./sys/install.sh" "r2"

# Binary Ninja (Community Edition) - requires manual download
if [ ! -f "$HOME/binaryninja/binaryninja" ]; then
    echo "📥 Binary Ninja Community Edition available at:"
    echo "https://binary.ninja/free/"
fi

# Rizin (modern fork of radare2)
install_tool "Rizin" "git clone https://github.com/rizinorg/rizin && cd rizin && meson setup build && ninja -C build && sudo ninja -C build install" "rizin"

# Additional analysis tools
install_tool "Checksec" "sudo apt-get update && sudo apt-get install -y checksec" "checksec"
install_tool "Ltrace" "sudo apt-get install -y ltrace" "ltrace"
install_tool "Strace" "sudo apt-get install -y strace" "strace"
install_tool "Valgrind" "sudo apt-get install -y valgrind" "valgrind"

echo ""
echo "🐍 Setting up Python RE Tools"
echo "============================="

# Python-based tools
python3 -m pip install --user \
    capstone \
    pwntools \
    angr \
    z3-solver \
    keystone-engine \
    unicorn \
    ropper \
    pefile

echo ""
echo "🔍 Creating Analysis Scripts"
echo "============================"

# Create Ghidra analysis script
cat > "analysis/tools/ghidra_analysis.py" << 'EOF'
#!/usr/bin/env python3
"""
Ghidra automation script for DSKYpoly analysis
Requires Ghidra headless mode
"""

import subprocess
import sys
import os

def analyze_with_ghidra(binary_path, project_name="DSKYpoly_Analysis"):
    """Analyze binary with Ghidra headless mode"""
    
    ghidra_path = os.environ.get('GHIDRA_HOME', '/opt/ghidra')
    if not os.path.exists(ghidra_path):
        ghidra_path = os.path.expanduser('~/ghidra')
    
    if not os.path.exists(ghidra_path):
        print("❌ Ghidra not found. Please set GHIDRA_HOME environment variable.")
        return False
    
    analyzer_script = f"{ghidra_path}/support/analyzeHeadless"
    
    if not os.path.exists(analyzer_script):
        print("❌ Ghidra headless analyzer not found.")
        return False
    
    # Create analysis project
    project_dir = "analysis/ghidra_projects"
    os.makedirs(project_dir, exist_ok=True)
    
    # Run headless analysis
    cmd = [
        analyzer_script,
        project_dir,
        project_name,
        "-import", binary_path,
        "-postScript", "CreateStructuresByAlignment.java",
        "-postScript", "DecompileAllFunctions.java"
    ]
    
    print(f"🔍 Analyzing {binary_path} with Ghidra...")
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Ghidra analysis complete")
            return True
        else:
            print(f"❌ Ghidra analysis failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Error running Ghidra: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 ghidra_analysis.py <binary_path>")
        sys.exit(1)
    
    binary_path = sys.argv[1]
    analyze_with_ghidra(binary_path)
EOF

chmod +x "analysis/tools/ghidra_analysis.py"

# Create dynamic analysis script
cat > "analysis/tools/dynamic_analysis.sh" << 'EOF'
#!/bin/bash
# Dynamic analysis toolkit for DSKYpoly

echo "🎯 DSKYpoly Dynamic Analysis"
echo "============================"

BINARY="$1"
if [ -z "$BINARY" ]; then
    echo "Usage: $0 <binary_path>"
    exit 1
fi

if [ ! -f "$BINARY" ]; then
    echo "❌ Binary not found: $BINARY"
    exit 1
fi

OUTPUT_DIR="analysis/dynamic/$(basename $BINARY)"
mkdir -p "$OUTPUT_DIR"

echo "📊 Security Analysis"
echo "==================="
checksec --file="$BINARY" > "$OUTPUT_DIR/security_analysis.txt"

echo "🔍 System Call Tracing"
echo "======================"
echo "Running strace analysis..."
timeout 30s strace -o "$OUTPUT_DIR/syscalls.txt" "$BINARY" 2>/dev/null || true

echo "📚 Library Call Tracing"
echo "======================="
echo "Running ltrace analysis..."
timeout 30s ltrace -o "$OUTPUT_DIR/libcalls.txt" "$BINARY" 2>/dev/null || true

echo "🧠 Memory Analysis"
echo "=================="
echo "Running Valgrind analysis..."
valgrind --tool=memcheck \
         --leak-check=full \
         --show-leak-kinds=all \
         --track-origins=yes \
         --log-file="$OUTPUT_DIR/valgrind.txt" \
         "$BINARY" 2>/dev/null || true

echo "✅ Dynamic analysis complete"
echo "Results saved in: $OUTPUT_DIR"
EOF

chmod +x "analysis/tools/dynamic_analysis.sh"

echo ""
echo "✅ Modern RE Toolkit Setup Complete!"
echo "===================================="
echo ""
echo "🔧 Available Tools:"
echo "  - Static Analysis: objdump, readelf, strings"
echo "  - Disassemblers: Ghidra, Radare2/Rizin"
echo "  - Dynamic Analysis: GDB, Valgrind, strace, ltrace"
echo "  - Python Tools: Capstone, Angr, pwntools"
echo ""
echo "🚀 Next Steps:"
echo "  1. Build your DSKYpoly binaries"
echo "  2. Run ./analysis/tools/analyze_binaries.sh"
echo "  3. Use Ghidra for detailed analysis"
echo "  4. Perform dynamic analysis with GDB"
echo ""
