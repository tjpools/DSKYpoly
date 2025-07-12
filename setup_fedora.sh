#!/bin/bash

echo "🔍 DSKYpoly Reverse Engineering Toolkit - Fedora Setup"
echo "========================================================"

# Update system
echo "📦 Updating package list..."
sudo dnf update -y

# Install core development tools
echo "🛠️  Installing core development tools..."
sudo dnf groupinstall -y "Development Tools" "Development Libraries"

# Install specific tools for reverse engineering
echo "🔧 Installing reverse engineering tools..."
sudo dnf install -y \
    binutils \
    gdb \
    strace \
    ltrace \
    file \
    strings \
    objdump \
    nm \
    readelf \
    hexdump \
    python3 \
    python3-pip \
    python3-devel \
    gcc \
    make \
    nasm \
    yasm

# Install Python packages for analysis and visualization
echo "🐍 Installing Python dependencies..."
pip3 install --user matplotlib plotly numpy pandas scipy

# Optional: Install Ghidra if available in repositories
echo "🕵️  Checking for Ghidra availability..."
if sudo dnf list available | grep -q ghidra; then
    echo "📥 Installing Ghidra from repositories..."
    sudo dnf install -y ghidra
else
    echo "ℹ️  Ghidra not available in repositories. You can install via:"
    echo "   • Flatpak: flatpak install flathub org.ghidra_sre.Ghidra"
    echo "   • Manual: Download from https://ghidra-sre.org/"
fi

# Check if Flatpak Ghidra is available
echo "🔍 Checking for Flatpak Ghidra..."
if command -v flatpak >/dev/null 2>&1; then
    if flatpak list --app | grep -q "org.ghidra_sre.Ghidra"; then
        echo "✅ Found Ghidra Flatpak installation"
    else
        echo "💡 To install Ghidra via Flatpak:"
        echo "   flatpak install flathub org.ghidra_sre.Ghidra"
    fi
else
    echo "ℹ️  Flatpak not available"
fi

# Verify installations
echo ""
echo "🔍 Verifying installations..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

commands=(
    "gcc --version | head -1"
    "python3 --version"
    "objdump --version | head -1"
    "nm --version | head -1"
    "gdb --version | head -1"
)

for cmd in "${commands[@]}"; do
    echo -n "Checking $(echo $cmd | cut -d' ' -f1)... "
    if eval $cmd >/dev/null 2>&1; then
        echo "✅"
    else
        echo "❌"
    fi
done

# Check Python packages
echo -n "Checking matplotlib... "
if python3 -c "import matplotlib" 2>/dev/null; then
    echo "✅"
else
    echo "❌"
fi

echo -n "Checking plotly... "
if python3 -c "import plotly" 2>/dev/null; then
    echo "✅"
else
    echo "❌"
fi

echo -n "Checking numpy... "
if python3 -c "import numpy" 2>/dev/null; then
    echo "✅"
else
    echo "❌"
fi

echo ""
echo "🎉 Fedora setup complete!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📁 Current directory: $(pwd)"
echo "🔧 Next steps:"
echo "   1. Build DSKYpoly binaries: make"
echo "   2. Test reverse engineering: python3 reverse_engineering/simple_demo.py"
echo "   3. Run full analysis: python3 reverse_engineering/ghidra_analyzer.py"
echo ""
