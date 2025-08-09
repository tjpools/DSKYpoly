#!/usr/bin/env python3
"""
DSKYpoly Python Analysis Tools
Mathematical exploration and visualization for polynomial solvers

This demonstrates Python 3 usage for DSKYpoly analysis and complements
the assembly language implementations with high-level mathematical tools.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import sympy as sp
from sympy import symbols, solve, expand, Poly
import subprocess
import json
import os

class PolynomialAnalyzer:
    """
    High-level Python interface for analyzing polynomial equations
    and visualizing their solutions alongside the assembly implementations.
    """
    
    def __init__(self):
        self.x = symbols('x')
        self.results_cache = {}
        
    def analyze_quadratic(self, a, b, c):
        """Analyze quadratic polynomial ax² + bx + c = 0"""
        poly = a*self.x**2 + b*self.x + c
        discriminant = b**2 - 4*a*c
        
        # Symbolic solution
        roots = solve(poly, self.x)
        
        # Numerical analysis
        real_roots = []
        complex_roots = []
        
        for root in roots:
            if root.is_real:
                real_roots.append(complex(root))
            else:
                complex_roots.append(complex(root))
        
        return {
            'polynomial': poly,
            'discriminant': discriminant,
            'symbolic_roots': roots,
            'real_roots': real_roots,
            'complex_roots': complex_roots,
            'degree': 2
        }
    
    def analyze_cubic(self, a, b, c, d):
        """Analyze cubic polynomial ax³ + bx² + cx + d = 0"""
        poly = a*self.x**3 + b*self.x**2 + c*self.x + d
        
        # Cardano's discriminant
        p = (3*a*c - b**2) / (3*a**2)
        q = (2*b**3 - 9*a*b*c + 27*a**2*d) / (27*a**3)
        discriminant = -(4*p**3 + 27*q**2)
        
        # Symbolic solution
        roots = solve(poly, self.x)
        
        return {
            'polynomial': poly,
            'discriminant': discriminant,
            'cardano_p': p,
            'cardano_q': q,
            'symbolic_roots': roots,
            'degree': 3
        }
    
    def analyze_quartic(self, a, b, c, d, e):
        """Analyze quartic polynomial ax⁴ + bx³ + cx² + dx + e = 0"""
        poly = a*self.x**4 + b*self.x**3 + c*self.x**2 + d*self.x + e
        
        # Ferrari's method requires resolvent cubic
        # This is a simplified analysis
        roots = solve(poly, self.x)
        
        return {
            'polynomial': poly,
            'symbolic_roots': roots,
            'degree': 4
        }
    
    def analyze_quintic(self, a, b, c, d, e, f):
        """Analyze quintic polynomial ax⁵ + bx⁴ + cx³ + dx² + ex + f = 0"""
        poly = a*self.x**5 + b*self.x**4 + c*self.x**3 + d*self.x**2 + e*self.x + f
        
        # Quintic: generally not solvable by radicals (Abel-Ruffini)
        # Use numerical methods
        try:
            # Try symbolic solution (may fail for general quintic)
            roots = solve(poly, self.x)
            solvable_by_radicals = True
        except:
            # Fall back to numerical methods
            roots = []
            solvable_by_radicals = False
        
        return {
            'polynomial': poly,
            'symbolic_roots': roots,
            'solvable_by_radicals': solvable_by_radicals,
            'degree': 5
        }
    
    def visualize_roots(self, analysis_result, title=None):
        """Visualize polynomial roots in the complex plane"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Extract roots
        roots = analysis_result['symbolic_roots']
        complex_roots = [complex(root) for root in roots]
        
        # Plot 1: Complex plane visualization
        ax1.set_aspect('equal')
        ax1.grid(True, alpha=0.3)
        ax1.axhline(y=0, color='k', linewidth=0.5)
        ax1.axvline(x=0, color='k', linewidth=0.5)
        
        # Plot roots
        for i, root in enumerate(complex_roots):
            ax1.plot(root.real, root.imag, 'ro', markersize=8)
            ax1.annotate(f'r_{i+1}', (root.real, root.imag), 
                        xytext=(5, 5), textcoords='offset points')
        
        # Unit circle for reference
        circle = Circle((0, 0), 1, fill=False, color='blue', alpha=0.3)
        ax1.add_patch(circle)
        
        ax1.set_xlabel('Real Part')
        ax1.set_ylabel('Imaginary Part')
        ax1.set_title(f'Roots in Complex Plane\n(Degree {analysis_result["degree"]})')
        
        # Plot 2: Polynomial function
        if analysis_result['degree'] <= 4:  # Only plot for manageable degrees
            x_vals = np.linspace(-5, 5, 1000)
            poly_func = sp.lambdify(self.x, analysis_result['polynomial'], 'numpy')
            
            try:
                y_vals = poly_func(x_vals)
                ax2.plot(x_vals, y_vals, 'b-', linewidth=2, label='f(x)')
                ax2.axhline(y=0, color='k', linewidth=0.5)
                ax2.axvline(x=0, color='k', linewidth=0.5)
                ax2.grid(True, alpha=0.3)
                
                # Mark real roots
                for root in complex_roots:
                    if abs(root.imag) < 1e-10:  # Real root
                        ax2.plot(root.real, 0, 'ro', markersize=8)
                
                ax2.set_xlabel('x')
                ax2.set_ylabel('f(x)')
                ax2.set_title('Polynomial Function')
                ax2.legend()
                
            except:
                ax2.text(0.5, 0.5, 'Function plot unavailable', 
                        transform=ax2.transAxes, ha='center', va='center')
        
        if title:
            fig.suptitle(title, fontsize=16)
        
        plt.tight_layout()
        return fig
    
    def compare_with_assembly(self, degree, coefficients):
        """Compare Python results with assembly implementation"""
        print(f"\n🧮 Comparing Python vs Assembly (Degree {degree})")
        print("=" * 50)
        
        # Run assembly solver if available
        assembly_result = self.run_assembly_solver(degree, coefficients)
        
        # Run Python analysis
        if degree == 2:
            python_result = self.analyze_quadratic(*coefficients)
        elif degree == 3:
            python_result = self.analyze_cubic(*coefficients)
        elif degree == 4:
            python_result = self.analyze_quartic(*coefficients)
        elif degree == 5:
            python_result = self.analyze_quintic(*coefficients)
        
        print(f"Python 3 Analysis:")
        print(f"  Polynomial: {python_result['polynomial']}")
        print(f"  Roots: {python_result['symbolic_roots']}")
        
        if assembly_result:
            print(f"Assembly Implementation:")
            print(f"  {assembly_result}")
        
        return python_result, assembly_result
    
    def run_assembly_solver(self, degree, coefficients):
        """Attempt to run the corresponding assembly solver"""
        solvers = {
            2: './build/dskypoly',
            3: './cubic/build/dskypoly3',
            4: './quartic/build/dskypoly4',
            5: './quintic/build/dskypoly5'
        }
        
        solver_path = solvers.get(degree)
        if not solver_path or not os.path.exists(solver_path):
            return f"Assembly solver not found: {solver_path}"
        
        try:
            # This would need to be adapted based on each solver's input format
            result = subprocess.run([solver_path], 
                                  input='\n'.join(map(str, coefficients)) + '\n',
                                  capture_output=True, text=True, timeout=30)
            return result.stdout
        except Exception as e:
            return f"Error running assembly solver: {e}"

def demonstrate_polynomial_analysis():
    """Demonstrate the Python 3 analysis capabilities"""
    analyzer = PolynomialAnalyzer()
    
    print("🧮 DSKYpoly Python 3 Analysis Demonstration")
    print("=" * 50)
    
    # Quadratic example
    print("\n1. Quadratic Analysis: x² - 5x + 6 = 0")
    quad_result = analyzer.analyze_quadratic(1, -5, 6)
    print(f"   Discriminant: {quad_result['discriminant']}")
    print(f"   Roots: {quad_result['symbolic_roots']}")
    
    # Cubic example
    print("\n2. Cubic Analysis: x³ - 6x² + 11x - 6 = 0")
    cubic_result = analyzer.analyze_cubic(1, -6, 11, -6)
    print(f"   Cardano p: {cubic_result['cardano_p']}")
    print(f"   Cardano q: {cubic_result['cardano_q']}")
    print(f"   Roots: {cubic_result['symbolic_roots']}")
    
    # Quartic example
    print("\n3. Quartic Analysis: x⁴ - 10x² + 9 = 0")
    quartic_result = analyzer.analyze_quartic(1, 0, -10, 0, 9)
    print(f"   Roots: {quartic_result['symbolic_roots']}")
    
    # Quintic example
    print("\n4. Quintic Analysis: x⁵ - 5x + 1 = 0")
    quintic_result = analyzer.analyze_quintic(1, 0, 0, 0, -5, 1)
    print(f"   Solvable by radicals: {quintic_result['solvable_by_radicals']}")
    if quintic_result['solvable_by_radicals']:
        print(f"   Roots: {quintic_result['symbolic_roots']}")
    else:
        print("   Requires numerical methods (Abel-Ruffini theorem)")
    
    # Visualize the quadratic
    fig = analyzer.visualize_roots(quad_result, "Quadratic: x² - 5x + 6 = 0")
    plt.show()
    
    return analyzer

def galois_theory_demonstration():
    """Demonstrate Galois theory concepts with Python"""
    print("\n🎭 Galois Theory Demonstration")
    print("=" * 40)
    
    x = symbols('x')
    
    # Demonstrate solvability by radicals
    polynomials = [
        (x**2 - 2, "S₂", "2 elements", True),
        (x**3 - 2, "S₃", "6 elements", True),
        (x**4 - 2, "S₄", "24 elements", True),
        (x**5 - 2, "S₅", "120 elements", False)  # Contains A₅
    ]
    
    for poly, group, size, solvable in polynomials:
        print(f"\nPolynomial: {poly}")
        print(f"  Galois Group: {group} ({size})")
        print(f"  Solvable by radicals: {solvable}")
        
        roots = solve(poly, x)
        print(f"  Symbolic roots: {len(roots)} found")
        
        if solvable:
            print(f"  Example root: {roots[0]}")
        else:
            print("  General solution requires numerical methods")

if __name__ == "__main__":
    print("🐍 DSKYpoly Python 3 Environment")
    print("=" * 35)
    print("Python version:", end=" ")
    import sys
    print(sys.version)
    print()
    
    # Run demonstrations
    analyzer = demonstrate_polynomial_analysis()
    galois_theory_demonstration()
    
    print("\n🔗 Integration with Assembly Code")
    print("=" * 35)
    print("This Python environment complements the assembly implementations")
    print("by providing high-level mathematical analysis and visualization.")
    print("\nUse the PolynomialAnalyzer class to explore mathematical concepts")
    print("while the assembly code provides optimized computational performance.")
