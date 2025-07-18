#!/usr/bin/env python3
"""
Test DSKYpoly Quintic Solver with Roots of Unity
===============================================

This script tests the quintic hypergeometric solver using x^5 - 1 = 0,
which has the beautiful property of having roots that are the 5th roots of unity:
1, ω, ω², ω³, ω⁴ where ω = e^(2πi/5)

These roots form a perfect pentagon on the unit circle in the complex plane.
"""

import numpy as np
import matplotlib.pyplot as plt
import cmath
import sys
import os

# Add quintic directory to path
sys.path.append('/home/tjpools/assembly-projects/DSKYpoly/quintic')

try:
    from quintic_hypergeometric import QuinticHypergeometricSolver
except ImportError as e:
    print(f"Import error: {e}")
    print("Creating simplified roots of unity solver...")

def analytical_5th_roots_of_unity():
    """
    Compute the exact 5th roots of unity analytically.
    These are: 1, ω, ω², ω³, ω⁴ where ω = e^(2πi/5)
    """
    roots = []
    for k in range(5):
        # ω^k = e^(2πik/5)
        angle = 2 * np.pi * k / 5
        root = cmath.exp(1j * angle)
        roots.append(root)
    return roots

def simple_quintic_roots_of_unity():
    """
    Simple implementation for x^5 - 1 = 0
    """
    # For x^5 - 1 = 0, we can factor as:
    # x^5 - 1 = (x - 1)(x^4 + x^3 + x^2 + x + 1) = 0
    
    # Root 1: x = 1
    root1 = complex(1, 0)
    
    # Roots 2-5: Solutions to x^4 + x^3 + x^2 + x + 1 = 0
    # These are the primitive 5th roots of unity
    roots = [root1]
    
    for k in range(1, 5):
        angle = 2 * np.pi * k / 5
        root = cmath.exp(1j * angle)
        roots.append(root)
    
    return roots

def visualize_5th_roots_of_unity(roots, title="5th Roots of Unity"):
    """
    Create a beautiful visualization of the 5th roots of unity.
    """
    plt.figure(figsize=(12, 10))
    
    # Extract real and imaginary parts
    real_parts = [r.real for r in roots]
    imag_parts = [r.imag for r in roots]
    
    # Plot the roots
    colors = ['red', 'blue', 'green', 'orange', 'purple']
    for i, (real, imag) in enumerate(zip(real_parts, imag_parts)):
        plt.scatter(real, imag, s=200, c=colors[i], marker='o', 
                   label=f'Root {i+1}: {roots[i]:.4f}', alpha=0.8, edgecolors='black', linewidth=2)
    
    # Draw the unit circle
    theta = np.linspace(0, 2*np.pi, 1000)
    plt.plot(np.cos(theta), np.sin(theta), 'k--', alpha=0.5, linewidth=2, label='Unit Circle')
    
    # Draw lines connecting roots to origin
    for real, imag in zip(real_parts, imag_parts):
        plt.plot([0, real], [0, imag], 'gray', alpha=0.3, linewidth=1)
    
    # Draw the pentagon connecting the roots
    # Sort roots by angle for proper pentagon drawing
    sorted_roots = sorted(roots, key=lambda z: cmath.phase(z))
    pentagon_real = [r.real for r in sorted_roots] + [sorted_roots[0].real]
    pentagon_imag = [r.imag for r in sorted_roots] + [sorted_roots[0].imag]
    plt.plot(pentagon_real, pentagon_imag, 'g-', alpha=0.6, linewidth=2, label='Regular Pentagon')
    
    # Coordinate axes
    plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    
    # Formatting
    plt.xlabel('Real Part', fontsize=12)
    plt.ylabel('Imaginary Part', fontsize=12)
    plt.title(f'{title}\nPolynomial: x⁵ - 1 = 0', fontsize=14, fontweight='bold')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    
    # Set reasonable limits
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    
    plt.tight_layout()
    return plt.gcf()

def verify_roots(roots, coeffs):
    """
    Verify that the computed roots actually satisfy the polynomial.
    """
    print("\n" + "="*60)
    print("ROOT VERIFICATION")
    print("="*60)
    
    def evaluate_polynomial(x, coeffs):
        """Evaluate polynomial at x using coefficients [a5, a4, a3, a2, a1, a0]"""
        result = 0
        for i, coeff in enumerate(coeffs):
            power = len(coeffs) - 1 - i
            result += coeff * (x ** power)
        return result
    
    max_error = 0
    for i, root in enumerate(roots):
        value = evaluate_polynomial(root, coeffs)
        error = abs(value)
        max_error = max(max_error, error)
        
        print(f"Root {i+1}: {root:>12.6f}")
        print(f"  P(root) = {value:>12.6e}")
        print(f"  |Error| = {error:>12.6e}")
        print()
    
    print(f"Maximum error: {max_error:.6e}")
    
    if max_error < 1e-10:
        print("✅ All roots verified successfully!")
    elif max_error < 1e-6:
        print("⚠️  Roots verified with acceptable precision")
    else:
        print("❌ Root verification failed - large errors detected")
    
    return max_error

def main():
    print("🌟 DSKYpoly Quintic Test: 5th Roots of Unity")
    print("=" * 50)
    print("Testing polynomial: x⁵ - 1 = 0")
    print("Expected roots: 5th roots of unity forming a regular pentagon\n")
    
    # Coefficients for x^5 - 1 = 0: [1, 0, 0, 0, 0, -1]
    coeffs = [1.0, 0.0, 0.0, 0.0, 0.0, -1.0]
    
    # Method 1: Analytical solution
    print("Method 1: Analytical 5th Roots of Unity")
    print("-" * 40)
    analytical_roots = analytical_5th_roots_of_unity()
    
    for i, root in enumerate(analytical_roots):
        angle_deg = cmath.phase(root) * 180 / np.pi
        print(f"Root {i+1}: {root:>12.6f} (angle: {angle_deg:>6.1f}°)")
    
    # Verify analytical roots
    verify_roots(analytical_roots, coeffs)
    
    # Method 2: Simple implementation
    print("\nMethod 2: Simple Quintic Implementation")
    print("-" * 40)
    simple_roots = simple_quintic_roots_of_unity()
    
    for i, root in enumerate(simple_roots):
        angle_deg = cmath.phase(root) * 180 / np.pi
        print(f"Root {i+1}: {root:>12.6f} (angle: {angle_deg:>6.1f}°)")
    
    # Method 3: Try hypergeometric solver (if available)
    try:
        print("\nMethod 3: Hypergeometric Solver")
        print("-" * 40)
        solver = QuinticHypergeometricSolver()
        hyp_roots = solver.solve_quintic(coeffs)
        
        for i, root in enumerate(hyp_roots):
            angle_deg = cmath.phase(root) * 180 / np.pi
            print(f"Root {i+1}: {root:>12.6f} (angle: {angle_deg:>6.1f}°)")
        
        verify_roots(hyp_roots, coeffs)
        
    except Exception as e:
        print(f"Hypergeometric solver not available: {e}")
        print("Using analytical solution for visualization...")
        hyp_roots = analytical_roots
    
    # Create visualization
    print("\n🎨 Creating visualization...")
    fig = visualize_5th_roots_of_unity(analytical_roots, "5th Roots of Unity (Analytical)")
    
    # Save the plot
    output_path = "/home/tjpools/assembly-projects/DSKYpoly/visualizations/quintic_roots_of_unity.png"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    fig.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"📊 Visualization saved to: {output_path}")
    
    # Display the plot
    plt.show()
    
    # Mathematical insights
    print("\n🔬 Mathematical Insights:")
    print("-" * 30)
    print("• The 5th roots of unity form a regular pentagon on the unit circle")
    print("• Root angles: 0°, 72°, 144°, 216°, 288° (multiples of 72°)")
    print("• These roots are: 1, ω, ω², ω³, ω⁴ where ω = e^(2πi/5)")
    print("• The polynomial factors as: x⁵ - 1 = (x - 1)(x⁴ + x³ + x² + x + 1)")
    print("• This demonstrates the beautiful connection between:")
    print("  - Algebra (polynomial roots)")
    print("  - Geometry (regular pentagon)")
    print("  - Complex analysis (unit circle)")
    print("  - Group theory (cyclic group C₅)")

if __name__ == "__main__":
    main()
