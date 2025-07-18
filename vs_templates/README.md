# Visual Studio Project Setup

This directory contains templates for setting up DSKYpoly in Visual Studio.

## 🚀 Quick Setup

1. **Copy template files to Windows:**
   ```cmd
   # In Windows Command Prompt or PowerShell
   copy vs_templates\DSKYpoly.sln .
   copy vs_templates\DSKYpoly.Core.vcxproj src\
   copy vs_templates\DSKYpoly.Python.pyproj quintic\
   ```

2. **Open in Visual Studio:**
   ```cmd
   devenv DSKYpoly.sln
   ```

3. **Configure WSL integration:**
   - Tools → Options → Cross Platform → Linux
   - Add your WSL Ubuntu connection
   - Set build output to WSL directory

## 📁 Template Files

- `DSKYpoly.sln` - Main solution file
- `DSKYpoly.Core.vcxproj` - C/Assembly project
- `DSKYpoly.Python.pyproj` - Python project
- `DSKYpoly.Tests.vcxproj` - Unit test project

## 🔧 Build Configuration

The solution includes configurations for:
- **Debug/Release** - Standard builds
- **WSL Debug/Release** - Cross-platform verification
- **Python Integration** - Mixed C/Python debugging

## 📖 Documentation

See `../VISUAL_STUDIO.md` for complete setup instructions.
