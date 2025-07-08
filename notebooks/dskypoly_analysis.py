# DSKYpoly Analysis and Statistics Notebook
# Mathematical insights through computational analysis

import numpy as np
import matplotlib.pyplot as plt
import subprocess
import os
import time
from pathlib import Path

class DSKYpolyAnalyzer:
    """Analysis tools for DSKYpoly polynomial solvers"""
    
    def __init__(self, workspace_path="/workspace"):
        self.workspace = Path(workspace_path)
        self.solvers = {
            "quadratic": self.workspace / "build" / "dskypoly",
            "cubic": self.workspace / "cubic" / "build" / "dskypoly3", 
            "quartic": self.workspace / "quartic" / "build" / "dskypoly4",
            "quintic": self.workspace / "quintic" / "build" / "dskypoly5"
        }
    
    def performance_analysis(self):
        """Analyze performance characteristics of each solver"""
        results = {}
        
        for name, solver_path in self.solvers.items():
            if solver_path.exists():
                print(f"🔬 Analyzing {name} solver...")
                
                # Time execution
                start_time = time.time()
                try:
                    result = subprocess.run([str(solver_path)], 
                                          capture_output=True, 
                                          text=True, 
                                          timeout=30,
                                          input="1\n2\n1\n" if name == "cubic" else "")
                    end_time = time.time()
                    
                    results[name] = {
                        "execution_time": end_time - start_time,
                        "exit_code": result.returncode,
                        "output_length": len(result.stdout),
                        "binary_size": solver_path.stat().st_size if solver_path.exists() else 0
                    }
                except subprocess.TimeoutExpired:
                    results[name] = {"error": "timeout"}
                except Exception as e:
                    results[name] = {"error": str(e)}
        
        return results
    
    def complexity_visualization(self):
        """Visualize the complexity growth from S2 to S5"""
        degrees = [2, 3, 4, 5]
        galois_sizes = [2, 6, 24, 120]  # |S_n|
        interface_complexity = [1, 2, 4, 8]  # Relative complexity score
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # Galois group size growth
        ax1.semilogy(degrees, galois_sizes, 'bo-', linewidth=2, markersize=8)
        ax1.set_xlabel('Polynomial Degree')
        ax1.set_ylabel('Galois Group Size |Sₙ|')
        ax1.set_title('Factorial Explosion: Galois Group Growth')
        ax1.grid(True, alpha=0.3)
        ax1.set_xticks(degrees)
        
        # Interface complexity
        ax2.bar(degrees, interface_complexity, color=['green', 'blue', 'orange', 'red'])
        ax2.set_xlabel('Polynomial Degree')
        ax2.set_ylabel('Interface Complexity Score')
        ax2.set_title('Interface Evolution Response')
        ax2.set_xticks(degrees)
        ax2.set_xticklabels(['S₂\n(DSKY)', 'S₃\n(Direct)', 'S₄\n(Framework)', 'S₅\n(Theater)'])
        
        plt.tight_layout()
        plt.savefig('/workspace/notebooks/complexity_analysis.png', dpi=150, bbox_inches='tight')
        plt.show()
    
    def polynomial_visualization(self):
        """Visualize polynomial functions and their roots"""
        x = np.linspace(-3, 3, 1000)
        
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        
        # Quadratic: x² - 1
        ax = axes[0, 0]
        y = x**2 - 1
        ax.plot(x, y, 'b-', linewidth=2, label='x² - 1')
        ax.axhline(y=0, color='k', linestyle='--', alpha=0.3)
        ax.axvline(x=0, color='k', linestyle='--', alpha=0.3)
        ax.plot([-1, 1], [0, 0], 'ro', markersize=8, label='Roots: ±1')
        ax.set_title('Quadratic (S₂): 2 elements')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # Cubic: x³ - x
        ax = axes[0, 1]
        y = x**3 - x
        ax.plot(x, y, 'g-', linewidth=2, label='x³ - x')
        ax.axhline(y=0, color='k', linestyle='--', alpha=0.3)
        ax.axvline(x=0, color='k', linestyle='--', alpha=0.3)
        ax.plot([-1, 0, 1], [0, 0, 0], 'ro', markersize=8, label='Roots: -1, 0, 1')
        ax.set_title('Cubic (S₃): 6 elements')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # Quartic: x⁴ - 10x² + 9
        ax = axes[1, 0]
        y = x**4 - 10*x**2 + 9
        ax.plot(x, y, 'orange', linewidth=2, label='x⁴ - 10x² + 9')
        ax.axhline(y=0, color='k', linestyle='--', alpha=0.3)
        ax.axvline(x=0, color='k', linestyle='--', alpha=0.3)
        ax.plot([-3, -1, 1, 3], [0, 0, 0, 0], 'ro', markersize=8, label='Roots: ±1, ±3')
        ax.set_title('Quartic (S₄): 24 elements')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # Quintic: x⁵ - x (simplified)
        ax = axes[1, 1]
        y = x**5 - x
        ax.plot(x, y, 'r-', linewidth=2, label='x⁵ - x')
        ax.axhline(y=0, color='k', linestyle='--', alpha=0.3)
        ax.axvline(x=0, color='k', linestyle='--', alpha=0.3)
        ax.plot([-1, 0, 1], [0, 0, 0], 'ro', markersize=8, label='Some roots')
        ax.set_title('Quintic (S₅): 120 elements - Unsolvable!')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('/workspace/notebooks/polynomial_visualization.png', dpi=150, bbox_inches='tight')
        plt.show()
    
    def galois_theory_diagram(self):
        """Create a diagram showing the Galois theory connections"""
        import matplotlib.patches as patches
        
        fig, ax = plt.subplots(1, 1, figsize=(10, 8))
        
        # Define positions for groups
        positions = {
            'S₂': (2, 6),
            'S₃': (2, 4.5),
            'S₄': (2, 3),
            'S₅': (2, 1.5),
            'A₅': (4, 1.5),
            'Rubik': (6, 3),
            'Monster': (8, 1.5)
        }
        
        # Group properties
        groups = {
            'S₂': {'size': 2, 'solvable': True, 'color': 'lightgreen'},
            'S₃': {'size': 6, 'solvable': True, 'color': 'lightgreen'},
            'S₄': {'size': 24, 'solvable': True, 'color': 'lightgreen'},
            'S₅': {'size': 120, 'solvable': False, 'color': 'lightcoral'},
            'A₅': {'size': 60, 'solvable': False, 'color': 'lightcoral'},
            'Rubik': {'size': '4.3×10¹⁹', 'solvable': True, 'color': 'lightyellow'},
            'Monster': {'size': '8×10⁵³', 'solvable': True, 'color': 'lightblue'}
        }
        
        # Draw groups
        for name, pos in positions.items():
            props = groups[name]
            circle = patches.Circle(pos, 0.3, facecolor=props['color'], 
                                  edgecolor='black', linewidth=2)
            ax.add_patch(circle)
            ax.text(pos[0], pos[1], name, ha='center', va='center', 
                   fontweight='bold', fontsize=10)
            ax.text(pos[0], pos[1]-0.5, f"|G| = {props['size']}", 
                   ha='center', va='center', fontsize=8)
        
        # Draw connections
        connections = [
            ('S₅', 'A₅', 'contains'),
            ('A₅', 'Rubik', 'embeds in'),
            ('Rubik', 'Monster', 'path to')
        ]
        
        for start, end, label in connections:
            start_pos = positions[start]
            end_pos = positions[end]
            ax.annotate('', xy=end_pos, xytext=start_pos,
                       arrowprops=dict(arrowstyle='->', lw=1.5, color='gray'))
            mid_x = (start_pos[0] + end_pos[0]) / 2
            mid_y = (start_pos[1] + end_pos[1]) / 2
            ax.text(mid_x, mid_y + 0.2, label, ha='center', va='center',
                   fontsize=8, style='italic', color='gray')
        
        # Add title and labels
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 7)
        ax.set_title('The Group Theory Journey: From Polynomials to the Monster', 
                    fontsize=14, fontweight='bold')
        
        # Add legend
        legend_elements = [
            patches.Patch(color='lightgreen', label='Solvable'),
            patches.Patch(color='lightcoral', label='Non-solvable (polynomials)'),
            patches.Patch(color='lightyellow', label='Finite but vast'),
            patches.Patch(color='lightblue', label='Mathematical sublime')
        ]
        ax.legend(handles=legend_elements, loc='upper right')
        
        ax.set_aspect('equal')
        ax.axis('off')
        
        plt.tight_layout()
        plt.savefig('/workspace/notebooks/galois_theory_diagram.png', dpi=150, bbox_inches='tight')
        plt.show()

# Example usage
if __name__ == "__main__":
    print("🧮 DSKYpoly Mathematical Analysis")
    print("=" * 40)
    
    analyzer = DSKYpolyAnalyzer()
    
    # Run performance analysis
    print("📊 Performance Analysis:")
    perf_results = analyzer.performance_analysis()
    for solver, metrics in perf_results.items():
        print(f"  {solver}: {metrics}")
    
    print("\n📈 Generating visualizations...")
    
    # Create visualizations
    analyzer.complexity_visualization()
    analyzer.polynomial_visualization() 
    analyzer.galois_theory_diagram()
    
    print("✅ Analysis complete! Check /workspace/notebooks/ for output files.")
