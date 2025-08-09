# DSKYpoly Anaconda Integration Guide

This guide helps you set up a complete mathematical computing environment for DSKYpoly using Anaconda Navigator.

## 🚀 **Quick Start**

### **Option 1: Automatic Setup (Recommended)**

**Windows:**
```cmd
# Open Anaconda Prompt and navigate to DSKYpoly directory
cd path\to\DSKYpoly
setup_anaconda.bat
```

**Linux/Mac:**
```bash
# Open terminal and navigate to DSKYpoly directory
cd /path/to/DSKYpoly
./setup_anaconda.sh
```

### **Option 2: Manual Setup**

1. **Create Environment:**
   ```bash
   conda env create -f environment.yml
   conda activate dskypoly
   ```

2. **Launch Jupyter:**
   ```bash
   jupyter lab
   # or
   jupyter notebook
   ```

3. **Open the exploration notebook:**
   Navigate to `notebooks/quintic_exploration.ipynb`

## 📊 **What You Get**

### **Mathematical Computing Stack**
- **Python 3.11** - Modern Python with excellent mathematical libraries
- **NumPy** - Numerical computing foundation
- **SciPy** - Scientific computing algorithms
- **SymPy** - Symbolic mathematics
- **mpmath** - Arbitrary precision arithmetic
- **Matplotlib** - Static plotting and visualization
- **Plotly** - Interactive visualizations
- **Jupyter Lab** - Modern notebook interface

### **Educational Content**
- **Interactive Notebooks** - Explore quintic polynomials step-by-step
- **Visualizations** - Complex plane plots and mathematical insights
- **DSKYpoly Integration** - Connect high-level math to C/Assembly core
- **Mathematical Theory** - Hypergeometric functions and Galois theory

## 🔬 **Exploration Topics**

### **1. Fifth Roots of Unity**
- Compute roots with arbitrary precision
- Visualize the pentagon pattern in complex plane
- Verify mathematical properties interactively

### **2. Hypergeometric Functions**
- Explore the connection to quintic polynomials
- Investigate special cases and parameters
- Interactive function plotting and analysis

### **3. DSKYpoly Integration**
- Test the Python-based quintic solver
- Compare with analytical results
- Bridge high-level math to implementation

### **4. Mathematical Visualization**
- Complex plane plotting
- Root convergence analysis
- Interactive mathematical exploration

## 🎯 **Development Workflow**

### **Recommended Setup**
1. **Anaconda Navigator** - Environment and package management
2. **Jupyter Lab** - Interactive mathematical exploration
3. **VS Code** - Main development with conda environment
4. **DSKYpoly Core** - C/Assembly integration for performance

### **Environment Management**
```bash
# Activate environment
conda activate dskypoly

# Update packages
conda update --all

# Add new packages
conda install package_name

# Export environment
conda env export > environment.yml
```

## 📁 **Directory Structure**

```
DSKYpoly/
├── environment.yml          # Conda environment specification
├── setup_anaconda.bat       # Windows setup script
├── setup_anaconda.sh        # Linux/Mac setup script
├── notebooks/               # Jupyter notebooks
│   └── quintic_exploration.ipynb
├── quintic/                 # Python quintic solver
│   └── quintic_hypergeometric.py
└── visualizations/          # Generated plots and analysis
```

## 🛠️ **Troubleshooting**

### **Common Issues**

**Environment Creation Fails:**
```bash
# Clean conda cache
conda clean --all
# Try creating again
conda env create -f environment.yml
```

**Jupyter Extensions Not Working:**
```bash
conda activate dskypoly
jupyter contrib nbextension install --user
jupyter nbextension enable --py widgetsnbextension
```

**Import Errors:**
```bash
# Verify environment
conda activate dskypoly
python -c "import numpy, scipy, sympy, matplotlib, plotly, mpmath"
```

### **Performance Tips**
- Use **Jupyter Lab** for better performance with large notebooks
- Enable **widget extensions** for interactive plots
- Use **conda-forge** channel for latest package versions
- Consider **environment.yml** updates for reproducibility

## 🎓 **Educational Value**

This Anaconda setup provides:
- **Interactive Learning** - Explore mathematical concepts hands-on
- **Reproducible Research** - Share mathematical discoveries
- **Cross-Platform** - Works on Windows, Mac, and Linux
- **Professional Tools** - Industry-standard mathematical computing

## 🔗 **Integration with DSKYpoly**

The Anaconda environment complements the DSKYpoly project by:
- **High-Level Exploration** - Python for mathematical investigation
- **Performance Core** - C/Assembly for computational efficiency
- **Educational Bridge** - Connect theory to implementation
- **Visualization** - Make abstract mathematics tangible

---

*Ready to explore the mathematical universe of quintic polynomials? Launch Jupyter and dive in!* 🚀
