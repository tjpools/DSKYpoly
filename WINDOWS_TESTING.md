# Windows Anaconda Navigator Setup Guide
*Get DSKYpoly running on Windows with Anaconda Navigator GUI*

## 🎯 **Quick Setup for Windows Testing**

This guide helps you set up DSKYpoly on Windows using Anaconda Navigator's graphical interface - perfect for testing the mathematical components.

## 📋 **Step-by-Step Setup**

### **Step 1: Download Repository**
```powershell
# In PowerShell or Command Prompt
git clone https://github.com/tjpools/DSKYpoly.git
cd DSKYpoly

# Or download ZIP from GitHub and extract
```

### **Step 2: Open Anaconda Navigator**
1. **Launch Anaconda Navigator** from Start Menu
2. Wait for it to load (may take a moment)
3. You should see the Navigator dashboard

### **Step 3: Import DSKYpoly Environment**
1. **Click "Environments"** tab on the left sidebar
2. **Click "Import"** button at the bottom
3. **Browse and select** `environment.yml` from DSKYpoly folder
4. **Name**: Keep as "dskypoly" or rename if desired
5. **Click "Import"** and wait for packages to install (this may take 5-10 minutes)

### **Step 4: Activate Environment**
1. **Select "dskypoly"** environment from the list
2. **Wait for green play button** to appear
3. Environment is now active

### **Step 5: Launch JupyterLab**
1. **Click "Home"** tab
2. **Select "dskypoly"** from environment dropdown
3. **Find JupyterLab** and click **"Launch"**
4. **JupyterLab opens** in your browser

### **Step 6: Navigate to DSKYpoly**
1. **In JupyterLab file browser**, navigate to DSKYpoly folder
2. **Open** `notebooks/quintic_exploration.ipynb`
3. **Start exploring!**

## 🧪 **Testing Targets**

### **1. Quintic Polynomial Solver**
```python
# In Jupyter notebook cell:
import sys
sys.path.append('../quintic')

from quintic_hypergeometric import QuinticHypergeometricSolver

# Test 5th roots of unity
solver = QuinticHypergeometricSolver()
roots = solver.solve_roots_of_unity(5)
print("5th roots of unity:", roots)
```

### **2. Visualization Tests**
```python
# Test complex plane plotting
import matplotlib.pyplot as plt
import numpy as np

# Plot roots in complex plane
fig, ax = plt.subplots(figsize=(8, 8))
for i, root in enumerate(roots):
    ax.plot(root.real, root.imag, 'ro', markersize=10)
    ax.annotate(f'ω^{i}', (root.real, root.imag), 
                xytext=(5, 5), textcoords='offset points')

ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.grid(True)
ax.set_aspect('equal')
plt.title('5th Roots of Unity in Complex Plane')
plt.show()
```

### **3. Mathematical Verification**
```python
# Verify polynomial solutions
def verify_quintic_roots(roots):
    """Verify that roots satisfy x^5 - 1 = 0"""
    for i, root in enumerate(roots):
        result = root**5 - 1
        error = abs(result)
        print(f"Root {i}: {root}")
        print(f"  x^5 - 1 = {result}")
        print(f"  Error: {error:.2e}")
        print(f"  Valid: {'✅' if error < 1e-10 else '❌'}")
        print()

verify_quintic_roots(roots)
```

## 🔧 **Troubleshooting**

### **Environment Creation Issues**
```
Problem: "Solving environment: failed"
Solution: 
1. Try conda-forge channel
2. Use conda command line instead:
   conda env create -f environment.yml
```

### **JupyterLab Won't Launch**
```
Problem: JupyterLab doesn't start
Solution:
1. Check environment is selected
2. Try launching from command line:
   conda activate dskypoly
   jupyter lab
```

### **Import Errors**
```
Problem: Cannot import DSKYpoly modules
Solution:
1. Check you're in correct directory
2. Add to Python path:
   import sys
   sys.path.append('../quintic')
   sys.path.append('../src')
```

### **Missing Packages**
```
Problem: Package not found
Solution:
1. Install manually in environment:
   Click terminal in JupyterLab
   conda install package_name
   # or
   pip install package_name
```

## 📱 **Windows-Specific Features**

### **Anaconda Navigator Benefits**
- ✅ **GUI Environment Management** - Easy visual environment switching
- ✅ **Integrated Package Manager** - Install packages with clicks
- ✅ **Multiple IDE Options** - JupyterLab, Spyder, VS Code
- ✅ **Environment Isolation** - Clean separation of project dependencies
- ✅ **Visual Debugging** - Step through code in Spyder

### **Performance on Windows**
```python
# Test mathematical performance
import time
from quintic.quintic_hypergeometric import QuinticHypergeometricSolver

solver = QuinticHypergeometricSolver()

# Benchmark polynomial solving
start_time = time.time()
roots = solver.solve_roots_of_unity(5)
end_time = time.time()

print(f"Quintic solving time: {end_time - start_time:.4f} seconds")
print(f"Platform: Windows with Anaconda")
print(f"Roots computed: {len(roots)}")
```

## 🎯 **Windows Testing Checklist**

### **Mathematical Functions**
- [ ] **Quintic solver imports** correctly
- [ ] **Roots of unity calculation** works
- [ ] **Complex number arithmetic** functions
- [ ] **Hypergeometric functions** (mpmath) available
- [ ] **Visualization** with matplotlib/plotly

### **Cross-Platform Verification**
- [ ] **Environment setup** matches Linux version
- [ ] **Package versions** are compatible
- [ ] **Mathematical results** match expected values
- [ ] **Performance** is acceptable on Windows
- [ ] **File paths** work correctly (Windows vs Unix)

## 🚀 **Advanced Windows Features**

### **Visual Studio Integration**
If you have Visual Studio installed:
```
1. Copy vs_templates\DSKYpoly.sln to project root
2. Open DSKYpoly.sln in Visual Studio
3. Configure WSL integration
4. Build and test C/Assembly components
```

### **WSL Integration**
For hybrid Windows/Linux development:
```powershell
# In PowerShell
wsl
cd /mnt/c/path/to/DSKYpoly
make clean && make all
./build/dskypoly
```

## 💡 **Pro Tips**

### **Environment Management**
- **Create snapshots** before major changes
- **Export environment** after successful setup: `conda env export > my_environment.yml`
- **Use environment cloning** for testing variations

### **Development Workflow**
1. **Anaconda Navigator** for mathematical exploration
2. **Visual Studio** for C/Assembly development  
3. **WSL** for cross-platform verification
4. **JupyterLab** for interactive analysis

## 🎉 **Success Indicators**

When everything is working correctly, you should see:
✅ **DSKYpoly environment** active in Navigator  
✅ **JupyterLab launches** without errors  
✅ **Quintic solver imports** successfully  
✅ **Mathematical calculations** complete  
✅ **Visualizations render** correctly  
✅ **Cross-platform consistency** maintained  

---

**Happy mathematical exploration on Windows!** 🧮🪟✨

For any issues, check the main documentation:
- `README.md` - General setup
- `ANACONDA.md` - Cross-platform Anaconda guide
- `VISUAL_STUDIO.md` - Professional development setup
