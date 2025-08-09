# Windows 11 Anaconda Navigator Setup Guide

*Get DSKYpoly running with Anaconda Navigator GUI*

## 🎯 **Quick Start with Anaconda Navigator**

### **Step 1: Get the Project**
```cmd
# Clone or pull latest changes
git clone https://github.com/tjpools/DSKYpoly.git
# OR
cd DSKYpoly
git pull origin quintic-hypergeometric
```

### **Step 2: Create Environment via Navigator**
1. **Open Anaconda Navigator**
2. **Click "Environments" tab**
3. **Click "Import" button**
4. **Browse to your `DSKYpoly/environment.yml`**
5. **Click "Import"** (wait 5-10 minutes)

### **Step 3: Launch Your App**

**🥇 For Mathematical Exploration (Recommended)**
1. Select `dskypoly` environment from dropdown
2. Click **JupyterLab** → **Launch**
3. Navigate to `DSKYpoly/notebooks/`
4. Open `quintic_exploration.ipynb`
5. Start exploring quintic polynomials! 🎊

**🥈 For Python Development**
1. Select `dskypoly` environment
2. Click **Spyder** → **Launch**  
3. Open `DSKYpoly/quintic/quintic_hypergeometric.py`
4. Start coding and debugging

## 📚 **Anaconda Navigator App Guide**

### **🔬 JupyterLab** - Mathematical Exploration
**Best for:**
- Interactive quintic polynomial analysis
- Mathematical visualization and plotting
- Educational content creation
- Step-by-step algorithm development

**Key Features:**
- Rich LaTeX math rendering
- Interactive Plotly visualizations
- Integrated file browser
- Markdown documentation support

**Getting Started:**
```python
# In JupyterLab notebook
import sys
sys.path.append('..')  # Access DSKYpoly modules

from quintic.quintic_hypergeometric import QuinticHypergeometricSolver
solver = QuinticHypergeometricSolver()

# Explore 5th roots of unity
roots = solver.solve_roots_of_unity(5)
print("Fifth roots of unity:", roots)
```

### **🔧 Spyder** - Python Development
**Best for:**
- Quintic solver development
- Algorithm debugging
- Variable inspection
- MATLAB-like workflow

**Key Features:**
- Integrated debugger
- Variable explorer
- IPython console
- Code completion

**Getting Started:**
1. Open `quintic_hypergeometric.py`
2. Set breakpoints for debugging
3. Run with F5
4. Inspect variables in right panel

### **📓 Jupyter Notebook** - Focused Analysis
**Best for:**
- Single-topic mathematical exploration
- Creating educational content
- Sharing mathematical insights
- Step-by-step documentation

**Key Features:**
- Cell-by-cell execution
- Rich output formatting
- Easy sharing via GitHub
- Mathematical notation support

### **🆚 VS Code** (if installed)
**Best for:**
- Full project development
- Git integration
- Mixed C/Assembly + Python work
- Professional development workflow

**Setup:**
1. Install Python extension in VS Code
2. Select `dskypoly` conda environment
3. Open DSKYpoly project folder
4. Start developing!

## 🎨 **Recommended Workflow**

### **For Mathematical Learning**
1. **JupyterLab** → `quintic_exploration.ipynb`
2. Explore roots of unity interactively
3. Visualize complex plane mathematics
4. Learn hypergeometric functions

### **For Algorithm Development**
1. **Spyder** → `quintic_hypergeometric.py`
2. Develop new quintic solving methods
3. Debug with integrated tools
4. Test with variable explorer

### **For Documentation**
1. **Jupyter Notebook** → Create new notebooks
2. Document mathematical discoveries
3. Create educational content
4. Share insights with others

## 🔧 **Troubleshooting**

### **Environment Import Fails**
- Ensure `environment.yml` is in DSKYpoly folder
- Check internet connection for package downloads
- Try creating environment manually:
  ```cmd
  conda env create -f environment.yml
  ```

### **Apps Won't Launch**
- Verify `dskypoly` environment is selected
- Restart Anaconda Navigator
- Check if apps are installed in environment
- Try launching from command line:
  ```cmd
  conda activate dskypoly
  jupyter lab
  ```

### **Import Errors in Notebooks**
- Ensure you're in the correct directory
- Add DSKYpoly to Python path:
  ```python
  import sys
  sys.path.append('path/to/DSKYpoly')
  ```

### **Git Integration**
- Use JupyterLab terminal for git commands
- Or use external Git GUI (GitHub Desktop)
- Commit and push from Navigator terminal

## 🎯 **Next Steps**

1. **Start with JupyterLab** and the quintic exploration notebook
2. **Experiment** with hypergeometric functions
3. **Visualize** complex plane mathematics
4. **Develop** new quintic solving approaches
5. **Document** your mathematical discoveries

## 🌟 **Pro Tips**

- **Pin Anaconda Navigator** to taskbar for quick access
- **Bookmark** the DSKYpoly project folder in JupyterLab
- **Use split view** in JupyterLab for code + documentation
- **Enable Jupyter extensions** for enhanced functionality
- **Create shortcuts** for frequently used environments

---

*Ready to explore the mathematical universe with Anaconda Navigator!* 🚀🔬📱
