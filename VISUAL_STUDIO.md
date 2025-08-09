# Visual Studio Setup for DSKYpoly
*Optimize development workflow with Visual Studio on Windows and WSL Ubuntu*

## 🎯 **Overview**
This guide configures Visual Studio (VS) + WSL Ubuntu for optimal DSKYpoly development, focusing on:
- C/Assembly core development with Visual Studio
- Python mathematical exploration with integrated tools
- Seamless git workflow across Windows/WSL
- Cross-platform build verification

## 🔧 **Visual Studio Configuration**

### **1. Install Required Extensions**
```
Recommended Visual Studio Extensions:
- Linux development with C++
- WSL Extension
- Git Tools for Visual Studio  
- GitHub Extension for Visual Studio
- Intel C++ Compiler (optional for assembly optimization)
```

### **2. WSL Integration**
Visual Studio automatically detects WSL if properly configured:
```powershell
# In Windows PowerShell/Command Prompt
wsl --list --verbose
wsl --set-default Ubuntu

# Verify gcc/nasm in WSL
wsl gcc --version
wsl nasm --version
```

### **3. Project Configuration**
```cpp
// For DSKYpoly C components
#ifdef _WIN32
    // Windows-specific includes
    #include <windows.h>
#else
    // Linux/WSL includes  
    #include <unistd.h>
#endif
```

## 🐍 **Python Integration**

### **Visual Studio Python Workload**
Install "Python development" workload in Visual Studio installer:
- Python language support
- IntelliSense for Python
- Mixed-mode debugging (Python/C++)
- Jupyter notebook support

### **DSKYpoly Python Environment**
```powershell
# In Visual Studio Developer PowerShell
cd path\to\DSKYpoly
conda env create -f environment.yml
conda activate dskypoly

# Test quintic solver
python quintic/quintic_hypergeometric.py
```

## 🔄 **Git Integration**

### **Configure Git for Visual Studio**
```cmd
# Set Visual Studio as git editor (better than vim!)
git config --global core.editor "devenv /edit"

# Alternative: Use VS Code from Visual Studio
git config --global core.editor "code --wait"

# Configure merge/diff tools
git config --global merge.tool vsdiffmerge
git config --global mergetool.vsdiffmerge.cmd "\"C:\Program Files\Microsoft Visual Studio\2022\Professional\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\vsdiffmerge.exe\" \"$REMOTE\" \"$LOCAL\" \"$BASE\" \"$MERGED\" //m"

# Set diff tool
git config --global diff.tool vsdiffmerge
git config --global difftool.vsdiffmerge.cmd "\"C:\Program Files\Microsoft Visual Studio\2022\Professional\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\vsdiffmerge.exe\" \"$LOCAL\" \"$REMOTE\" //t"
```

### **WSL Git Configuration**
```bash
# In WSL Ubuntu terminal
# Use Visual Studio Code for git operations
git config --global core.editor "code --wait"

# Or use nano instead of vim
git config --global core.editor "nano"

# Cross-platform line endings
git config --global core.autocrlf input
```

## 🏗️ **Build Configuration**

### **Visual Studio Solution Setup**
```
DSKYpoly.sln
├── DSKYpoly.Core (C/Assembly)
│   ├── main.c
│   ├── solve_poly_2.asm
│   └── headers/
├── DSKYpoly.Python (Python integration)
│   ├── quintic_hypergeometric.py
│   └── test_roots_of_unity.py
└── DSKYpoly.Tests
    ├── unit_tests.cpp
    └── integration_tests.py
```

### **MSBuild Configuration**
```xml
<!-- DSKYpoly.Core.vcxproj -->
<PropertyGroup>
  <TargetSubsystem>Console</TargetSubsystem>
  <PlatformToolset>v143</PlatformToolset>
  <WindowsTargetPlatformVersion>10.0</WindowsTargetPlatformVersion>
</PropertyGroup>

<ItemGroup>
  <ClCompile Include="src\main.c" />
  <MASM Include="src\solve_poly_2.asm" />
</ItemGroup>
```

### **WSL Build Verification**
```bash
# Build in WSL using existing Makefile
make clean
make all

# Test binaries
./build/dskypoly
./quintic/build/dskypoly5
```

## 🧪 **Testing Strategy**

### **Visual Studio Unit Tests**
```cpp
// test_polynomial_solver.cpp
#include "CppUnitTest.h"
extern "C" {
    #include "../src/main.h"
}

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace DSKYpolyTests {
    TEST_CLASS(PolynomialSolverTests) {
    public:
        TEST_METHOD(TestQuadraticSolver) {
            // Test quadratic polynomial solving
            // Compare with known analytical solutions
        }
        
        TEST_METHOD(TestCubicSolver) {
            // Test cubic polynomial solving
        }
    };
}
```

### **Python Test Integration**
```python
# In Visual Studio Python project
import subprocess
import unittest

class CrossPlatformTests(unittest.TestCase):
    def test_c_assembly_integration(self):
        """Test C/Assembly components from Python"""
        result = subprocess.run(['./build/dskypoly'], 
                               capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        
    def test_quintic_solver(self):
        """Test Python quintic solver"""
        from quintic.quintic_hypergeometric import solve_quintic
        # Test with known quintic equations
```

## 🔄 **Workflow Integration**

### **Development Cycle**
```
1. Windows Visual Studio:
   - Edit C/Assembly core
   - Run unit tests
   - Debug with VS debugger

2. WSL Ubuntu:
   - Build with Makefile
   - Verify cross-platform compatibility
   - Run integration tests

3. Python Development:
   - Use Visual Studio Python tools
   - Jupyter integration for math exploration
   - Anaconda environment management
```

### **Git Workflow**
```cmd
# In Visual Studio Developer Command Prompt
git checkout quintic-hypergeometric
git pull origin quintic-hypergeometric

# Make changes in Visual Studio
# Use Team Explorer for git operations

# Push from command line or Team Explorer
git add .
git commit -m "VS: Enhanced polynomial solver"
git push origin quintic-hypergeometric
```

## 🚀 **Advanced Features**

### **Mixed-Mode Debugging**
Debug C/Assembly code with Python integration:
```
1. Set breakpoints in C code
2. Attach Python debugger
3. Step through C ↔ Python transitions
4. Inspect variables in both contexts
```

### **Performance Profiling**
```cpp
// Use Visual Studio Diagnostic Tools
#include <chrono>

auto start = std::chrono::high_resolution_clock::now();
// Polynomial solving code
auto end = std::chrono::high_resolution_clock::now();
auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
```

### **IntelliSense for Assembly**
Configure Visual Studio for NASM assembly:
```
Tools → Options → Text Editor → File Extension
- Add "asm" extension
- Associate with "Microsoft Macro Assembler"
```

## 📱 **Cross-Platform Sync**

### **Use Existing sync_platforms.sh**
```bash
# From WSL terminal in DSKYpoly directory
./sync_platforms.sh

# Choose option 6 to configure git for VS Code
# This prevents vim editor issues
```

### **Mobile Monitoring**
Check MOBILE.md for iPhone-friendly project monitoring while developing in Visual Studio.

## 🎯 **Benefits of This Setup**

✅ **Full IDE power** for C/Assembly development  
✅ **Integrated Python** mathematical exploration  
✅ **Cross-platform verification** via WSL  
✅ **Professional debugging** tools  
✅ **Git integration** without vim issues  
✅ **Anaconda integration** for data science  
✅ **Mixed-mode debugging** C ↔ Python  

## 🔗 **Related Documentation**

- `GIT_VSCODE.md` - VS Code git configuration (also works for Visual Studio)
- `ANACONDA.md` - Python environment setup
- `WINDOWS_ANACONDA.md` - Windows-specific Anaconda workflow
- `sync_platforms.sh` - Cross-platform sync tool
- `MOBILE.md` - iPhone monitoring setup

---

*Visual Studio + WSL + Python = Powerful DSKYpoly development environment!* 🚀
