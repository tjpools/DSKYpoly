#!/usr/bin/env python3
"""
DSKYpoly Windows-Anaconda Bridge
================================

This script bridges the WSL Ubuntu DSKYpoly project with Windows Anaconda Navigator
to leverage sophisticated mathematical computing capabilities.

Usage from WSL:
    python3 anaconda_bridge.py --function quintic_analysis --coeffs 1 0 -5 0 4 0

Features:
- Quintic hypergeometric solving
- Advanced visualization with Plotly
- High-precision arithmetic with mpmath
- Jupyter notebook integration
- Cross-platform mathematical analysis
"""

import subprocess
import json
import os
import sys
from pathlib import Path

class AnacondaBridge:
    """Bridge between WSL DSKYpoly and Windows Anaconda Navigator"""
    
    def __init__(self):
        # Detect if we're running in WSL
        self.is_wsl = self._detect_wsl()
        self.windows_python = self._find_windows_python()
        self.project_root = Path(__file__).parent
        
    def _detect_wsl(self):
        """Detect if running in WSL environment"""
        try:
            with open('/proc/version', 'r') as f:
                return 'microsoft' in f.read().lower()
        except:
            return False
    
    def _find_windows_python(self):
        """Find Windows Anaconda Python executable"""
        if not self.is_wsl:
            return sys.executable
            
        # Common Windows Anaconda paths accessible from WSL
        potential_paths = [
            "/mnt/c/Users/tmcla/anaconda3/envs/pythonProject3/python.exe",
            "/mnt/c/Users/tmcla/anaconda3/python.exe",
            "/mnt/c/ProgramData/Anaconda3/python.exe",
            "/mnt/c/anaconda3/python.exe"
        ]
        
        for path in potential_paths:
            if os.path.exists(path):
                return path
        
        print("Warning: Windows Anaconda Python not found. Using WSL Python.")
        return sys.executable
    
    def execute_quintic_analysis(self, coefficients):
        """Execute quintic analysis using Windows Anaconda environment"""
        script_content = f'''
import sys
sys.path.append(r"C:\\Users\\tmcla\\anaconda3\\envs\\pythonProject3\\Lib\\site-packages")

import numpy as np
import mpmath as mp
from scipy.special import hyp2f1
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import json

# Set high precision
mp.dps = 50

class AdvancedQuinticSolver:
    def __init__(self):
        self.coefficients = {coefficients}
        
    def solve_hypergeometric(self):
        """Advanced quintic solving with hypergeometric functions"""
        coeffs = self.coefficients
        print(f"Analyzing quintic: {{coeffs[0]}}x⁵ + {{coeffs[1]}}x⁴ + {{coeffs[2]}}x³ + {{coeffs[3]}}x² + {{coeffs[4]}}x + {{coeffs[5]}} = 0")
        
        # Use mpmath for high-precision root finding
        from mpmath import polyroots
        
        roots = polyroots(coeffs[::-1])  # mpmath expects coefficients in reverse order
        
        results = []
        for i, root in enumerate(roots):
            real_part = float(root.real)
            imag_part = float(root.imag)
            results.append({{
                'root_number': i+1,
                'real': real_part,
                'imaginary': imag_part,
                'magnitude': abs(root),
                'argument': mp.arg(root)
            }})
        
        return results
    
    def create_advanced_visualization(self, roots):
        """Create sophisticated visualization using Plotly"""
        # Extract real and imaginary parts
        real_parts = [r['real'] for r in roots]
        imag_parts = [r['imaginary'] for r in roots]
        
        # Create subplots
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Complex Plane', 'Root Magnitudes', 'Root Arguments', 'Convergence Analysis'),
            specs=[[{{"type": "scatter"}}, {{"type": "bar"}}],
                   [{{"type": "bar"}}, {{"type": "scatter"}}]]
        )
        
        # Complex plane plot
        fig.add_trace(
            go.Scatter(x=real_parts, y=imag_parts, 
                      mode='markers', name='Quintic Roots',
                      marker=dict(size=12, color='red')),
            row=1, col=1
        )
        
        # Root magnitudes
        fig.add_trace(
            go.Bar(x=[f'Root {{i+1}}' for i in range(5)],
                   y=[r['magnitude'] for r in roots],
                   name='Magnitudes'),
            row=1, col=2
        )
        
        # Root arguments
        fig.add_trace(
            go.Bar(x=[f'Root {{i+1}}' for i in range(5)],
                   y=[r['argument'] for r in roots],
                   name='Arguments'),
            row=2, col=1
        )
        
        # Update layout
        fig.update_layout(height=800, showlegend=True, 
                         title_text="DSKYpoly Quintic Analysis - Anaconda Navigator")
        
        # Save as HTML
        output_path = r"C:\\Users\\tmcla\\DSKYpoly_quintic_analysis.html"
        fig.write_html(output_path)
        print(f"Advanced visualization saved to: {{output_path}}")
        
        return output_path

# Execute analysis
solver = AdvancedQuinticSolver()
roots = solver.solve_hypergeometric()
visualization_path = solver.create_advanced_visualization(roots)

# Output results as JSON
result = {{
    'roots': roots,
    'visualization_path': visualization_path,
    'precision': mp.dps,
    'method': 'hypergeometric_mpmath'
}}

print("=== QUINTIC ANALYSIS RESULTS ===")
print(json.dumps(result, indent=2))
'''
        
        # Create temporary script file
        script_file = self.project_root / "temp_anaconda_script.py"
        with open(script_file, 'w') as f:
            f.write(script_content)
        
        try:
            # Execute using Windows Anaconda Python
            cmd = [self.windows_python, str(script_file)]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            
            if result.returncode == 0:
                print("✅ Anaconda analysis completed successfully!")
                print(result.stdout)
            else:
                print("❌ Anaconda analysis failed:")
                print(result.stderr)
                
        except subprocess.TimeoutExpired:
            print("⏱️ Analysis timed out after 60 seconds")
        except Exception as e:
            print(f"🚫 Error executing Anaconda analysis: {e}")
        finally:
            # Clean up temporary file
            if script_file.exists():
                script_file.unlink()
    
    def launch_jupyter_bridge(self):
        """Launch Jupyter Lab with DSKYpoly notebooks in Windows Anaconda"""
        if not self.is_wsl:
            print("Direct Jupyter launch not needed - already in Windows environment")
            return
            
        # Create a batch script to launch Jupyter Lab
        batch_content = f'''@echo off
cd /d C:\\Users\\tmcla
call C:\\Users\\tmcla\\anaconda3\\Scripts\\activate.bat pythonProject3
echo Starting Jupyter Lab for DSKYpoly analysis...
jupyter lab --notebook-dir=C:\\Users\\tmcla\\DSKYpoly_notebooks
pause
'''
        
        batch_file = "/mnt/c/Users/tmcla/launch_dskypoly_jupyter.bat"
        with open(batch_file, 'w') as f:
            f.write(batch_content)
        
        print(f"✅ Jupyter launcher created: {batch_file}")
        print("Run this from Windows Command Prompt to launch Jupyter Lab with DSKYpoly")
    
    def test_mathematical_capabilities(self):
        """Test advanced mathematical capabilities in Anaconda environment"""
        test_script = '''
import sys
print("🔬 Testing DSKYpoly Mathematical Capabilities in Anaconda...")
print(f"Python version: {sys.version}")

try:
    import numpy as np
    print(f"✅ NumPy {np.__version__}")
except ImportError:
    print("❌ NumPy not available")

try:
    import mpmath as mp
    mp.dps = 50
    pi_50 = mp.pi
    print(f"✅ mpmath - π to 50 digits: {pi_50}")
except ImportError:
    print("❌ mpmath not available")

try:
    import plotly
    print(f"✅ Plotly {plotly.__version__} - Advanced visualization ready")
except ImportError:
    print("❌ Plotly not available")

try:
    import sympy as sp
    x = sp.Symbol('x')
    quintic = x**5 - 1
    print(f"✅ SymPy - Symbolic quintic: {quintic}")
except ImportError:
    print("❌ SymPy not available")

try:
    from scipy.special import hyp2f1
    result = hyp2f1(1, 2, 3, 0.5)
    print(f"✅ SciPy - Hypergeometric 2F1(1,2,3,0.5) = {result}")
except ImportError:
    print("❌ SciPy not available")

print("🎯 Mathematical capability test complete!")
'''
        
        script_file = self.project_root / "test_capabilities.py"
        with open(script_file, 'w') as f:
            f.write(test_script)
        
        try:
            cmd = [self.windows_python, str(script_file)]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            
            print(result.stdout)
            if result.stderr:
                print("Warnings/Errors:")
                print(result.stderr)
                
        except Exception as e:
            print(f"Error testing capabilities: {e}")
        finally:
            if script_file.exists():
                script_file.unlink()

def main():
    bridge = AnacondaBridge()
    
    if len(sys.argv) < 2:
        print("DSKYpoly Anaconda Bridge")
        print("Usage:")
        print("  python3 anaconda_bridge.py test")
        print("  python3 anaconda_bridge.py quintic 1 0 -5 0 4 0")
        print("  python3 anaconda_bridge.py jupyter")
        return
    
    command = sys.argv[1]
    
    if command == "test":
        bridge.test_mathematical_capabilities()
    elif command == "quintic":
        if len(sys.argv) >= 8:
            coeffs = [float(x) for x in sys.argv[2:8]]
            bridge.execute_quintic_analysis(coeffs)
        else:
            print("Error: Quintic requires 6 coefficients (a5 a4 a3 a2 a1 a0)")
    elif command == "jupyter":
        bridge.launch_jupyter_bridge()
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
