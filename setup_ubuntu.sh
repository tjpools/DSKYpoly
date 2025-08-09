#!/bin/bash
# DSKYpoly Ubuntu Setup Script
# Prepares Ubuntu for reverse engineering toolkit

echo "🔍 DSKYpoly Reverse Engineering Toolkit - Ubuntu Setup"
echo "======================================================="

# Update package list
echo "📦 Updating package list..."
sudo apt update

# Install core development tools
echo "🛠️  Installing core tools..."
sudo apt install -y \
    build-essential \
    binutils \
    gdb \
    make \
    gcc \
    python3 \
    python3-pip \
    git

# Install Python dependencies
echo "🐍 Installing Python dependencies..."
pip3 install --user matplotlib plotly numpy

# Check if everything is installed
echo ""
echo "✅ Verification:"
echo "=================="

# Check tools
for tool in objdump nm strings file make gcc python3; do
    if command -v $tool &> /dev/null; then
        echo "✅ $tool: Available"
    else
        echo "❌ $tool: Missing"
    fi
done

# Check Python packages
python3 -c "
import sys
packages = ['matplotlib', 'plotly', 'numpy']
for pkg in packages:
    try:
        __import__(pkg)
        print(f'✅ {pkg}: Available')
    except ImportError:
        print(f'❌ {pkg}: Missing')
"

echo ""
echo "🎯 Optional: Install Ghidra for advanced analysis"
echo "=================================================="
echo "Option 1 (Snap): sudo snap install ghidra"
echo "Option 2 (Flatpak): flatpak install flathub org.ghidra_sre.Ghidra"
echo "Option 3 (Manual): Download from https://ghidra-sre.org/"

echo ""
echo "🚀 Next Steps:"
echo "=============="
echo "1. cd DSKYpoly"
echo "2. make                    # Build binaries"
echo "3. python3 reverse_engineering/simple_demo.py  # Test toolkit"

echo ""
echo "✨ Setup complete! Your Ubuntu system is ready for reverse engineering! ✨"
