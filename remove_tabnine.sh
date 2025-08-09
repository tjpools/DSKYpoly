#!/bin/bash
# Quick Tabnine Removal Script for Linux
# Removes Tabnine from VS Code, system directories, and running processes

echo "🚫 Removing Tabnine Completely"
echo "==============================="
echo ""

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Stop any running Tabnine processes
echo "🛑 Stopping Tabnine processes..."
pkill -f tabnine 2>/dev/null
pkill -f TabNine 2>/dev/null
echo "✅ Processes stopped"
echo ""

# Remove VS Code extensions
echo "💻 Removing VS Code extensions..."
if command_exists code; then
    # List and remove Tabnine extensions
    tabnine_extensions=$(code --list-extensions | grep -i tabnine)
    if [ -n "$tabnine_extensions" ]; then
        echo "Found Tabnine extensions:"
        echo "$tabnine_extensions"
        echo "$tabnine_extensions" | while read -r ext; do
            code --uninstall-extension "$ext"
            echo "Removed: $ext"
        done
    else
        echo "No Tabnine extensions found in VS Code"
    fi
    
    # Remove extension directories manually
    rm -rf ~/.vscode/extensions/*tabnine* 2>/dev/null
    rm -rf ~/.vscode/extensions/*TabNine* 2>/dev/null
    echo "✅ VS Code cleanup complete"
else
    echo "VS Code not found, skipping..."
fi
echo ""

# Remove Tabnine directories
echo "📁 Removing Tabnine directories..."
directories_to_remove=(
    ~/.tabnine
    ~/.TabNine
    ~/.local/share/tabnine
    ~/.local/share/TabNine
    ~/.config/tabnine
    ~/.config/TabNine
    /opt/tabnine
    /opt/TabNine
)

for dir in "${directories_to_remove[@]}"; do
    if [ -d "$dir" ]; then
        echo "Removing: $dir"
        if [[ "$dir" == /opt/* ]]; then
            sudo rm -rf "$dir"
        else
            rm -rf "$dir"
        fi
    fi
done
echo "✅ Directories cleaned"
echo ""

# Remove systemd services if they exist
echo "⚙️  Checking for systemd services..."
if systemctl list-units --all | grep -q tabnine; then
    echo "Found Tabnine systemd service, removing..."
    sudo systemctl stop tabnine 2>/dev/null
    sudo systemctl disable tabnine 2>/dev/null
    sudo rm -f /etc/systemd/system/tabnine.service
    sudo systemctl daemon-reload
    echo "✅ Systemd service removed"
else
    echo "No systemd services found"
fi
echo ""

# Remove Jupyter extensions if Jupyter is installed
echo "📓 Checking Jupyter extensions..."
if command_exists jupyter; then
    # Check for Jupyter Lab extensions
    if jupyter labextension list 2>/dev/null | grep -q tabnine; then
        echo "Removing Jupyter Lab Tabnine extension..."
        jupyter labextension uninstall @tabnine/jupyterlab-tabnine 2>/dev/null
    fi
    
    # Check for Jupyter Notebook extensions
    if jupyter nbextension list 2>/dev/null | grep -q tabnine; then
        echo "Removing Jupyter Notebook Tabnine extension..."
        jupyter nbextension uninstall tabnine 2>/dev/null
    fi
    echo "✅ Jupyter extensions checked"
else
    echo "Jupyter not found, skipping..."
fi
echo ""

# Remove Python packages
echo "🐍 Checking Python packages..."
if command_exists pip; then
    if pip list | grep -q tabnine; then
        echo "Removing Tabnine Python package..."
        pip uninstall tabnine -y 2>/dev/null
    fi
fi

if command_exists conda; then
    if conda list | grep -q tabnine; then
        echo "Removing Tabnine from conda..."
        conda remove tabnine -y 2>/dev/null
    fi
fi
echo "✅ Python packages checked"
echo ""

# Final verification
echo "🔍 Final verification..."
remaining_processes=$(ps aux | grep -i tabnine | grep -v grep)
if [ -n "$remaining_processes" ]; then
    echo "⚠️  Warning: Some Tabnine processes still running:"
    echo "$remaining_processes"
    echo ""
    echo "Force killing remaining processes..."
    sudo pkill -9 -f tabnine 2>/dev/null
    sudo pkill -9 -f TabNine 2>/dev/null
else
    echo "✅ No Tabnine processes found"
fi

# Check for remaining files
echo ""
echo "🗂️  Checking for remaining files..."
remaining_files=$(find /home /opt /usr -name "*tabnine*" -o -name "*TabNine*" 2>/dev/null | head -10)
if [ -n "$remaining_files" ]; then
    echo "⚠️  Found some remaining files:"
    echo "$remaining_files"
    echo ""
    echo "💡 You may want to manually review and remove these files"
else
    echo "✅ No remaining Tabnine files found"
fi

echo ""
echo "🎉 Tabnine Removal Complete!"
echo "============================="
echo ""
echo "✅ Processes stopped"
echo "✅ VS Code extensions removed"
echo "✅ System directories cleaned"
echo "✅ Services removed"
echo "✅ Python packages cleaned"
echo ""
echo "💡 You may want to restart VS Code and your terminal"
echo "💡 See REMOVE_TABNINE.md for additional cleanup options"
echo ""
echo "🚀 Your development environment is now Tabnine-free!"
