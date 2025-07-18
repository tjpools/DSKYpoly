# Complete Ubuntu & Windows Setup Guide
*Pull everything from GitHub and set up cross-platform development*

## 🐧 **Ubuntu Setup (Pull Everything)**

### **Step 1: Pull Latest Changes**
```bash
# Navigate to your DSKYpoly directory
cd ~/assembly-projects/DSKYpoly

# Pull all latest changes
git pull origin quintic-hypergeometric

# Verify you have all the files
ls -la *.yml *.md *.sh
```

### **Step 2: Verify Ubuntu Environment**
```bash
# Check if conda is available
conda --version

# Create/update environment
conda env create -f environment.yml
# OR for a simpler environment:
conda env create -f environment_simple.yml

# Activate environment
conda activate dskypoly

# Test quintic solver
cd quintic
python quintic_hypergeometric.py
```

### **Step 3: Test All Components**
```bash
# Test C/Assembly solvers
make clean && make all
./build/dskypoly

# Test cubic solver
cd cubic && make && ./build/dskypoly3

# Test quartic solver  
cd ../quartic && make && ./build/dskypoly4

# Test quintic solver
cd ../quintic && python test_roots_of_unity.py
```

## 🪟 **Windows Setup (Two Environment Options)**

### **Option 1: environment_simple.yml (Recommended for Windows)**
This is a simplified version that works better with Windows Anaconda Navigator:

```yaml
name: dskypoly
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.11
  - numpy
  - scipy  
  - sympy
  - matplotlib
  - plotly
  - jupyter
  - jupyterlab
  - notebook
  - ipywidgets
  - mpmath
  - pandas
  - seaborn
  - pip
  - pip:
    - kaleido
```

### **Option 2: environment.yml (Full Development)**
Complete environment with development tools (Linux-specific packages may not work on Windows).

### **Windows Anaconda Navigator Steps:**
1. **Download DSKYpoly files to Windows:**
   ```cmd
   git clone https://github.com/tjpools/DSKYpoly.git
   cd DSKYpoly
   git checkout quintic-hypergeometric
   ```

2. **Open Anaconda Navigator**
3. **Go to Environments tab**
4. **Click Import**
5. **Select `environment_simple.yml`** (better Windows compatibility)
6. **Wait for installation** (5-10 minutes)
7. **Launch JupyterLab from the environment**

## 🔄 **Cross-Platform Sync Workflow**

### **Use the Enhanced Sync Script:**
```bash
# On Ubuntu/Fedora
./sync_platforms.sh

# Choose options:
# 1. Push current work to remote
# 3. Prepare for Windows/WSL testing  
# 6. Configure git for cross-platform development
# 7. Remove Tabnine completely (if needed)
```

### **Windows Commands:**
```cmd
# Pull latest changes
git pull origin quintic-hypergeometric

# Activate conda environment
conda activate dskypoly

# Launch Jupyter for testing
jupyter lab notebooks/quintic_exploration.ipynb
```

## 🧪 **Testing Checklist**

### **Ubuntu Testing:**
- [ ] **Environment created** successfully
- [ ] **C/Assembly compilation** works (make all)
- [ ] **Python quintic solver** imports and runs
- [ ] **Jupyter notebooks** launch correctly
- [ ] **Visualization** (matplotlib/plotly) works

### **Windows Testing:**
- [ ] **environment_simple.yml imports** in Anaconda Navigator
- [ ] **JupyterLab launches** from Navigator
- [ ] **Quintic solver runs** in Jupyter notebook
- [ ] **Complex plane plots** render correctly
- [ ] **Mathematical verification** passes

## 🎯 **Key Files for Testing**

### **Mathematical Testing:**
```python
# In Jupyter notebook
import sys
sys.path.append('../quintic')
from quintic_hypergeometric import QuinticHypergeometricSolver

# Test quintic solver
solver = QuinticHypergeometricSolver()
roots = solver.solve_roots_of_unity(5)
print("5th roots of unity:", roots)

# Verify solutions
for i, root in enumerate(roots):
    result = root**5 - 1
    print(f"Root {i}: |x^5 - 1| = {abs(result):.2e}")
```

### **Visualization Testing:**
```python
import matplotlib.pyplot as plt
import numpy as np

# Plot roots in complex plane
fig, ax = plt.subplots(figsize=(8, 8))
for i, root in enumerate(roots):
    ax.plot(root.real, root.imag, 'ro', markersize=10)
    ax.annotate(f'ω^{i}', (root.real, root.imag))

ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.grid(True)
plt.title('5th Roots of Unity')
plt.show()
```

## 📚 **Available Documentation**

Now available on both Ubuntu and Windows:
- **README.md** - Main project overview
- **WINDOWS_TESTING.md** - Windows Anaconda Navigator guide
- **VISUAL_STUDIO.md** - Professional Windows development
- **GIT_VSCODE.md** - Cross-platform git configuration
- **REMOVE_TABNINE.md** - Complete Tabnine removal guide
- **MOBILE.md** - iPhone monitoring workflow
- **analysis/** - Reverse engineering tools and analysis

## 🚀 **Success Indicators**

### **Ubuntu:**
✅ All solvers compile and run  
✅ Python environment works correctly  
✅ Jupyter notebooks launch  
✅ Mathematical computations complete  
✅ Visualizations render  

### **Windows:**
✅ Anaconda environment imports successfully  
✅ JupyterLab launches from Navigator  
✅ Quintic solver mathematical operations work  
✅ Complex plane visualizations display  
✅ Cross-platform mathematical consistency  

---

**You now have the complete DSKYpoly development environment on both Ubuntu and Windows!** 🎉

Let me know how the setup goes on both platforms! 🚀
