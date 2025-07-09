# Remove Tabnine Completely
*Get rid of Tabnine AI code completion across all environments*

## 🎯 **Quick Removal Guide**

Tabnine can be persistent across multiple editors and environments. Here's how to remove it completely:

## 🔧 **VS Code**

### **Method 1: Extension Manager**
```
1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X)
3. Search for "Tabnine"
4. Click "Uninstall" on Tabnine extension
5. Restart VS Code
```

### **Method 2: Command Line**
```bash
# List installed extensions
code --list-extensions | grep -i tabnine

# Uninstall Tabnine extension
code --uninstall-extension TabNine.tabnine-vscode
```

### **Method 3: Manual Removal**
```bash
# Remove VS Code extension directory
rm -rf ~/.vscode/extensions/tabnine.*
rm -rf ~/.vscode/extensions/TabNine.*

# Windows paths:
# %USERPROFILE%\.vscode\extensions\tabnine.*
# %USERPROFILE%\.vscode\extensions\TabNine.*
```

## 🏗️ **Visual Studio**

### **Remove from Visual Studio**
```
1. Open Visual Studio
2. Go to Extensions → Manage Extensions
3. Search for "Tabnine"
4. Click "Uninstall"
5. Restart Visual Studio
```

### **Manual Removal (Windows)**
```cmd
# Remove Visual Studio extension
del /s /q "%LOCALAPPDATA%\Microsoft\VisualStudio\*\Extensions\*tabnine*"
del /s /q "%LOCALAPPDATA%\Microsoft\VisualStudio\*\Extensions\*TabNine*"
```

## 🐧 **System-Wide Removal (Linux)**

### **Remove Tabnine Service**
```bash
# Stop Tabnine service if running
pkill -f tabnine
pkill -f TabNine

# Remove Tabnine directories
rm -rf ~/.tabnine
rm -rf ~/.TabNine
rm -rf ~/.local/share/tabnine
rm -rf ~/.local/share/TabNine

# Remove from /opt if installed system-wide
sudo rm -rf /opt/tabnine
sudo rm -rf /opt/TabNine

# Remove any systemd services
sudo systemctl stop tabnine 2>/dev/null
sudo systemctl disable tabnine 2>/dev/null
sudo rm -f /etc/systemd/system/tabnine.service
sudo systemctl daemon-reload
```

### **Check for Running Processes**
```bash
# Check if Tabnine is still running
ps aux | grep -i tabnine
netstat -tulpn | grep -i tabnine

# Force kill if found
sudo pkill -9 -f tabnine
sudo pkill -9 -f TabNine
```

## 🪟 **Windows Removal**

### **Uninstall via Control Panel**
```
1. Windows Settings → Apps
2. Search for "Tabnine"
3. Click and select "Uninstall"
```

### **Manual Windows Cleanup**
```cmd
# Remove user directories
rmdir /s /q "%USERPROFILE%\.tabnine"
rmdir /s /q "%USERPROFILE%\.TabNine"
rmdir /s /q "%APPDATA%\tabnine"
rmdir /s /q "%APPDATA%\TabNine"
rmdir /s /q "%LOCALAPPDATA%\tabnine"
rmdir /s /q "%LOCALAPPDATA%\TabNine"

# Remove Program Files installation
rmdir /s /q "%PROGRAMFILES%\TabNine"
rmdir /s /q "%PROGRAMFILES(X86)%\TabNine"
```

### **Registry Cleanup (Advanced)**
```cmd
# Open Registry Editor (regedit) and remove:
# HKEY_CURRENT_USER\Software\TabNine
# HKEY_LOCAL_MACHINE\SOFTWARE\TabNine
# Search for any other "tabnine" entries
```

## 🧪 **Jupyter/Anaconda**

### **Remove Jupyter Extensions**
```bash
# List Jupyter extensions
jupyter labextension list | grep -i tabnine
jupyter nbextension list | grep -i tabnine

# Remove if found
jupyter labextension uninstall @tabnine/jupyterlab-tabnine
jupyter nbextension uninstall tabnine
```

### **Python Package Removal**
```bash
# Remove Python packages
pip uninstall tabnine
conda remove tabnine 2>/dev/null
```

## 🌐 **Browser Extensions**

### **Chrome/Edge**
```
1. Go to chrome://extensions/ or edge://extensions/
2. Search for "Tabnine"
3. Click "Remove"
```

### **Firefox**
```
1. Go to about:addons
2. Search for "Tabnine"
3. Click "Remove"
```

## 🔍 **Verification**

### **Confirm Complete Removal**
```bash
# Search for any remaining Tabnine files
find / -name "*tabnine*" -o -name "*TabNine*" 2>/dev/null

# Check running processes
ps aux | grep -i tabnine

# Check network connections
netstat -tulpn | grep -i tabnine

# Verify VS Code extensions
code --list-extensions | grep -i tabnine
```

## 🚫 **Prevent Reinstallation**

### **Block Tabnine Domains (Optional)**
Add to `/etc/hosts` (Linux) or `C:\Windows\System32\drivers\etc\hosts` (Windows):
```
127.0.0.1 tabnine.com
127.0.0.1 www.tabnine.com
127.0.0.1 api.tabnine.com
127.0.0.1 update.tabnine.com
```

### **Firewall Rules (Advanced)**
```bash
# Linux: Block Tabnine traffic
sudo ufw deny out to tabnine.com
sudo ufw deny out 443 comment 'Block Tabnine HTTPS'

# Windows: Use Windows Firewall to block TabNine.exe
```

## 🎯 **DSKYpoly-Specific Settings**

### **Recommended VS Code Extensions Instead**
```json
{
    "recommendations": [
        "ms-python.python",
        "ms-toolsai.jupyter", 
        "13xforever.language-x86-64-assembly",
        "eamodio.gitlens",
        "ms-vscode-remote.remote-wsl"
    ]
}
```

### **Disable AI Suggestions in Settings**
```json
{
    "editor.suggestSelection": "first",
    "editor.acceptSuggestionOnCommitCharacter": false,
    "editor.acceptSuggestionOnEnter": "off",
    "editor.quickSuggestions": {
        "other": true,
        "comments": false,
        "strings": false
    }
}
```

## 🔧 **Alternative Code Completion**

### **Built-in VS Code IntelliSense**
```json
{
    "editor.quickSuggestions": true,
    "editor.suggestOnTriggerCharacters": true,
    "editor.wordBasedSuggestions": true,
    "editor.parameterHints.enabled": true
}
```

### **Language-Specific Extensions**
- **C/C++**: Microsoft C/C++ extension
- **Python**: Pylance (Microsoft)
- **Assembly**: x86-64 Assembly syntax highlighting

## 🎉 **Success!**

After following these steps:
✅ **Tabnine completely removed** from all environments  
✅ **No background processes** consuming resources  
✅ **Clean development environment** for DSKYpoly  
✅ **Better performance** without AI overhead  
✅ **Privacy restored** - no code sent to external servers  

---

*Enjoy your Tabnine-free development environment!* 🚀
