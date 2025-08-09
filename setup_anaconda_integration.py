#!/usr/bin/env python3
"""
DSKYpoly Windows Integration Guide
==================================

This guide helps you leverage your Windows Anaconda Navigator environment 
for sophisticated DSKYpoly mathematical analysis.
"""

import subprocess
import os
import sys

def create_windows_batch_launcher():
    """Create a Windows batch file to launch Anaconda with DSKYpoly"""
    
    batch_content = '''@echo off
echo ================================================
echo DSKYpoly Advanced Mathematical Analysis
echo Leveraging Windows Anaconda Navigator
echo ================================================

REM Activate your Anaconda environment
call C:\\Users\\tmcla\\anaconda3\\Scripts\\activate.bat pythonProject3

echo Testing mathematical capabilities...
python -c "import numpy as np; print('NumPy:', np.__version__)"
python -c "import matplotlib.pyplot as plt; print('Matplotlib: Available')"
python -c "import plotly; print('Plotly: Available')"
python -c "import mpmath; print('mpmath: Available')"
python -c "import sympy; print('SymPy: Available')"

echo.
echo Starting Jupyter Lab for DSKYpoly analysis...
echo Navigate to: http://localhost:8888
echo.

REM Start Jupyter Lab
jupyter lab --no-browser --port=8888

pause
'''
    
    batch_path = "/mnt/c/Users/tmcla/DSKYpoly_Anaconda_Launcher.bat"
    try:
        with open(batch_path, 'w', encoding='utf-8') as f:
            f.write(batch_content)
        print(f"✅ Windows launcher created: {batch_path}")
        print("📝 To use: Double-click this file from Windows Explorer")
    except Exception as e:
        print(f"❌ Could not create launcher: {e}")

def create_anaconda_environment_file():
    """Create an enhanced environment.yml for sophisticated analysis"""
    
    enhanced_env = '''name: dskypoly-advanced
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.11
  # Core mathematical computing
  - numpy>=1.24
  - scipy>=1.10
  - sympy>=1.12
  - mpmath>=1.3
  
  # Advanced visualization
  - matplotlib>=3.7
  - plotly>=5.15
  - bokeh>=3.0
  - seaborn>=0.12
  
  # Interactive computing
  - jupyter
  - jupyterlab>=4.0
  - notebook
  - ipywidgets>=8.0
  - ipympl  # Interactive matplotlib
  
  # Data science
  - pandas>=2.0
  - networkx  # For graph theory visualizations
  
  # Development tools
  - black  # Code formatting
  - pytest  # Testing
  
  # Specialized packages via pip
  - pip
  - pip:
    - kaleido  # Plotly static export
    - jupyter_contrib_nbextensions
    - rise  # Jupyter presentations
    - watermark  # Documentation
'''
    
    env_path = "/home/tjpools/DSKYpoly/environment_enhanced.yml"
    with open(env_path, 'w') as f:
        f.write(enhanced_env)
    
    print(f"✅ Enhanced environment file created: {env_path}")
    print("📋 To create this environment on Windows:")
    print("   1. Open Anaconda Prompt")
    print("   2. Navigate to your DSKYpoly folder")
    print("   3. Run: conda env create -f environment_enhanced.yml")
    print("   4. Run: conda activate dskypoly-advanced")

def create_quintic_demo_script():
    """Create a demonstration script for quintic analysis"""
    
    demo_script = '''#!/usr/bin/env python3
"""
DSKYpoly Quintic Demonstration
Advanced mathematical analysis using Anaconda Navigator
"""

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import mpmath as mp
import sympy as sp

# Set high precision
mp.dps = 50

def demonstrate_quintic_analysis():
    """Demonstrate sophisticated quintic polynomial analysis"""
    print("DSKYpoly Quintic Analysis Demonstration")
    print("=" * 50)
    
    # Define quintic: x^5 - 5x^3 + 4x = 0
    coeffs = [1, 0, -5, 0, 4, 0]  # [a5, a4, a3, a2, a1, a0]
    
    print(f"Analyzing: {coeffs[0]}x^5 + {coeffs[1]}x^4 + {coeffs[2]}x^3 + {coeffs[3]}x^2 + {coeffs[4]}x + {coeffs[5]} = 0")
    
    # High-precision root finding
    roots = mp.polyroots(coeffs[::-1])  # mpmath expects reverse order
    
    print("\\nHigh-precision roots (50 decimal places):")
    for i, root in enumerate(roots):
        print(f"Root {i+1}: {root}")
        print(f"  |z| = {abs(root)}")
        print(f"  arg(z) = {mp.arg(root)} radians")
        print()
    
    # Create visualization
    real_parts = [float(root.real) for root in roots]
    imag_parts = [float(root.imag) for root in roots]
    
    # Interactive plot with Plotly
    fig = go.Figure()
    
    # Add unit circle for reference
    theta = np.linspace(0, 2*np.pi, 100)
    fig.add_trace(go.Scatter(
        x=np.cos(theta), y=np.sin(theta),
        mode='lines', name='Unit Circle',
        line=dict(color='lightgray', dash='dash')
    ))
    
    # Add roots
    fig.add_trace(go.Scatter(
        x=real_parts, y=imag_parts,
        mode='markers+text',
        marker=dict(size=15, color='red', symbol='diamond'),
        text=[f'Root {i+1}' for i in range(5)],
        textposition='top center',
        name='Quintic Roots'
    ))
    
    fig.update_layout(
        title='DSKYpoly: Quintic Polynomial Roots (x^5 - 5x^3 + 4x = 0)',
        xaxis_title='Real Part',
        yaxis_title='Imaginary Part',
        showlegend=True,
        width=800, height=800,
        xaxis=dict(zeroline=True),
        yaxis=dict(zeroline=True)
    )
    
    # Save the plot
    output_path = 'DSKYpoly_Quintic_Analysis.html'
    fig.write_html(output_path)
    print(f"Interactive visualization saved to: {output_path}")
    
    # Also create a matplotlib version
    plt.figure(figsize=(10, 10))
    
    # Plot unit circle
    theta = np.linspace(0, 2*np.pi, 100)
    plt.plot(np.cos(theta), np.sin(theta), 'k--', alpha=0.3, label='Unit Circle')
    
    # Plot roots
    plt.scatter(real_parts, imag_parts, c='red', s=200, marker='D', 
               label='Quintic Roots', edgecolors='black', linewidths=2)
    
    # Annotate roots
    for i, (x, y) in enumerate(zip(real_parts, imag_parts)):
        plt.annotate(f'Root {i+1}', (x, y), xytext=(10, 10), 
                    textcoords='offset points', fontsize=12, 
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7))
    
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    plt.xlabel('Real Part', fontsize=14)
    plt.ylabel('Imaginary Part', fontsize=14)
    plt.title('DSKYpoly: Quintic Polynomial Roots\\n(x^5 - 5x^3 + 4x = 0)', fontsize=16)
    plt.legend(fontsize=12)
    
    # Save matplotlib version
    plt.savefig('DSKYpoly_Quintic_Matplotlib.png', dpi=300, bbox_inches='tight')
    print("Static visualization saved to: DSKYpoly_Quintic_Matplotlib.png")
    
    plt.show()
    
    return roots

def demonstrate_symbolic_analysis():
    """Demonstrate symbolic mathematics capabilities"""
    print("\\nSymbolic Analysis with SymPy")
    print("=" * 30)
    
    x = sp.Symbol('x')
    
    # Define polynomials
    polynomials = {
        'Quadratic': x**2 - 3*x + 2,
        'Cubic': x**3 - 6*x**2 + 11*x - 6,
        'Quartic': x**4 - 10*x**2 + 9,
        'Quintic': x**5 - 1
    }
    
    for name, poly in polynomials.items():
        print(f"\\n{name}: {poly}")
        try:
            factored = sp.factor(poly)
            print(f"Factored: {factored}")
            
            roots = sp.solve(poly, x)
            print(f"Symbolic roots: {roots}")
        except Exception as e:
            print(f"Complex factorization: {e}")

if __name__ == "__main__":
    print("Starting DSKYpoly Advanced Mathematical Analysis...")
    print("Leveraging Windows Anaconda Navigator capabilities\\n")
    
    roots = demonstrate_quintic_analysis()
    demonstrate_symbolic_analysis()
    
    print("\\nAnalysis complete!")
    print("Check the generated files:")
    print("- DSKYpoly_Quintic_Analysis.html (interactive)")
    print("- DSKYpoly_Quintic_Matplotlib.png (static)")
'''
    
    script_path = "/home/tjpools/DSKYpoly/quintic_demo_anaconda.py"
    with open(script_path, 'w') as f:
        f.write(demo_script)
    
    # Make executable
    os.chmod(script_path, 0o755)
    
    print(f"✅ Quintic demo script created: {script_path}")
    print("🚀 This script showcases sophisticated mathematical analysis")

def main():
    print("🔧 Setting up DSKYpoly Windows Anaconda Navigator Integration")
    print("=" * 65)
    
    create_windows_batch_launcher()
    print()
    
    create_anaconda_environment_file()
    print()
    
    create_quintic_demo_script()
    print()
    
    print("🎯 Next Steps:")
    print("1. Copy DSKYpoly_Anaconda_Showcase.ipynb to your Windows machine")
    print("2. Run DSKYpoly_Anaconda_Launcher.bat from Windows")
    print("3. Open the notebook in Jupyter Lab")
    print("4. Explore the sophisticated mathematical capabilities!")
    print()
    print("💡 Your Windows Anaconda environment provides:")
    print("   - 50-digit precision arithmetic (mpmath)")
    print("   - Interactive visualizations (Plotly)")
    print("   - Symbolic mathematics (SymPy)")
    print("   - Advanced numerical methods (SciPy)")
    print("   - Professional data analysis (Pandas)")

if __name__ == "__main__":
    main()
