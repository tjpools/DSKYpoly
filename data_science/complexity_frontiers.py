"""
Mathematical Complexity Frontiers
=================================

Exploring the boundaries between constructible and non-constructible mathematics
through computational approaches. This module demonstrates where DSKYpoly's
construction philosophy meets its limits.
"""

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import math
from fractions import Fraction
import warnings
warnings.filterwarnings('ignore')

# Optional imports for enhanced functionality
try:
    import sympy as sp
    from sympy import symbols, Poly
    SYMPY_AVAILABLE = True
except ImportError:
    SYMPY_AVAILABLE = False
    print("SymPy not available - using simplified analysis")

class ConstructibilityAnalyzer:
    """
    Analyze mathematical objects for constructibility and computational feasibility.
    
    Explores the spectrum from simple (constructible) to complex (Monster-like).
    """
    
    def __init__(self):
        self.complexity_levels = {
            'trivial': {'max_degree': 2, 'max_group_order': 2},
            'elementary': {'max_degree': 4, 'max_group_order': 24},
            'advanced': {'max_degree': 5, 'max_group_order': 120},
            'difficult': {'max_degree': 10, 'max_group_order': 3628800},
            'extreme': {'max_degree': 100, 'max_group_order': float('inf')},
            'monster': {'max_degree': 196883, 'max_group_order': 808017424794512875886459904961710757005754368000000000}
        }
    
    def analyze_polynomial_constructibility(self, coefficients):
        """
        Analyze whether a polynomial's roots are constructible.
        
        Parameters:
        -----------
        coefficients : list
            Polynomial coefficients [a_n, a_{n-1}, ..., a_1, a_0]
            
        Returns:
        --------
        dict : Analysis results including constructibility assessment
        """
        degree = len(coefficients) - 1
        
        # Basic constructibility analysis
        constructible = self._assess_constructibility(degree, coefficients)
        
        # Galois group analysis (simplified without sympy)
        galois_analysis = self._analyze_galois_group_simple(degree)
        
        # Computational complexity assessment
        complexity = self._assess_computational_complexity(degree, coefficients)
        
        return {
            'degree': degree,
            'coefficients': coefficients,
            'constructible': constructible,
            'galois_analysis': galois_analysis,
            'complexity': complexity,
            'solvability': self._assess_solvability(degree)
        }
    
    def _assess_constructibility(self, degree, coefficients):
        """Assess constructibility based on degree and coefficient properties."""
        if degree <= 2:
            return {'status': 'constructible', 'method': 'quadratic_formula', 'confidence': 1.0}
        elif degree == 3:
            return {'status': 'constructible', 'method': 'cardano_formula', 'confidence': 1.0}
        elif degree == 4:
            return {'status': 'constructible', 'method': 'ferrari_method', 'confidence': 1.0}
        elif degree == 5:
            # Check for special cases that might be solvable
            if self._is_special_quintic(coefficients):
                return {'status': 'conditionally_constructible', 'method': 'special_case', 'confidence': 0.8}
            else:
                return {'status': 'generally_non_constructible', 'method': 'numerical_only', 'confidence': 0.2}
        else:
            return {'status': 'non_constructible', 'method': 'numerical_only', 'confidence': 0.0}
    
    def _is_special_quintic(self, coefficients):
        """Check if quintic has special form that allows algebraic solution."""
        # Very simplified check - real analysis would be much more complex
        if len(coefficients) == 6:  # x^5 + 0*x^4 + 0*x^3 + 0*x^2 + 0*x + c
            non_zero_coeffs = [c for c in coefficients[1:-1] if abs(c) > 1e-10]
            return len(non_zero_coeffs) <= 1
        return False
    
    def _analyze_galois_group_simple(self, degree):
        """Simplified Galois group analysis without SymPy."""
        try:
            if degree <= 4:
                return {
                    'computable': True,
                    'max_order': math.factorial(degree),
                    'solvable': True,
                    'method': 'classical'
                }
            elif degree == 5:
                return {
                    'computable': 'partially',
                    'max_order': 120,
                    'solvable': 'depends_on_discriminant',
                    'method': 'case_analysis'
                }
            else:
                return {
                    'computable': False,
                    'max_order': math.factorial(min(degree, 20)),  # Cap for computation
                    'solvable': 'generally_no',
                    'method': 'numerical_only'
                }
        except Exception as e:
            return {'error': str(e), 'computable': False}
    
    def _assess_computational_complexity(self, degree, coefficients):
        """Assess computational complexity of solving the polynomial."""
        # Estimate based on degree and coefficient magnitudes
        max_coeff = max(abs(c) for c in coefficients)
        
        if degree <= 4:
            complexity_class = 'polynomial'
            time_estimate = f"O(1) - algebraic formulas"
        elif degree <= 10:
            complexity_class = 'manageable'
            time_estimate = f"O(n^3) - numerical methods"
        elif degree <= 100:
            complexity_class = 'expensive'
            time_estimate = f"O(n^3) to O(n^4) - specialized algorithms"
        else:
            complexity_class = 'extreme'
            time_estimate = f"O(n^4+) - research-level problem"
        
        return {
            'class': complexity_class,
            'time_estimate': time_estimate,
            'space_complexity': f"O({degree}^2)",
            'coefficient_magnitude': max_coeff,
            'precision_requirements': self._estimate_precision_needs(degree, max_coeff)
        }
    
    def _estimate_precision_needs(self, degree, max_coeff):
        """Estimate precision requirements for accurate root finding."""
        # Rough heuristic based on degree and coefficient size
        base_precision = 16  # Standard double precision
        degree_factor = max(1, math.log2(degree))
        magnitude_factor = max(1, math.log10(max_coeff))
        
        estimated_precision = int(base_precision + degree_factor + magnitude_factor)
        
        if estimated_precision <= 16:
            return "standard_precision"
        elif estimated_precision <= 50:
            return "extended_precision"
        elif estimated_precision <= 100:
            return "arbitrary_precision_needed"
        else:
            return "extreme_precision_required"
    
    def _assess_solvability(self, degree):
        """Assess theoretical solvability by radicals."""
        if degree <= 4:
            return {'by_radicals': True, 'method': 'classical_formulas'}
        elif degree == 5:
            return {'by_radicals': False, 'method': 'abel_ruffini_theorem'}
        else:
            return {'by_radicals': False, 'method': 'galois_theory'}
    
    def demonstrate_complexity_spectrum(self):
        """Demonstrate the spectrum of mathematical complexity."""
        examples = {
            'Linear': [1, -2],  # x - 2 = 0
            'Quadratic': [1, -5, 6],  # x^2 - 5x + 6 = 0
            'Cubic': [1, -6, 11, -6],  # x^3 - 6x^2 + 11x - 6 = 0
            'Quartic': [1, -10, 35, -50, 24],  # Nice quartic
            'Quintic': [1, 0, 0, 0, 0, -1],  # x^5 - 1 = 0 (roots of unity)
            'Difficult_Quintic': [1, -1, -1, 2, -1],  # Generic quintic
            'High_Degree': [1] + [0]*8 + [-1],  # x^9 - 1 = 0
        }
        
        results = {}
        for name, coeffs in examples.items():
            results[name] = self.analyze_polynomial_constructibility(coeffs)
        
        return results
    
    def visualize_complexity_landscape(self):
        """Create visualization of mathematical complexity landscape."""
        
        # Generate complexity data
        degrees = list(range(1, 21))
        constructibility_scores = []
        computation_times = []
        
        for d in degrees:
            if d <= 4:
                constructibility_scores.append(1.0)
                computation_times.append(1)
            elif d == 5:
                constructibility_scores.append(0.2)
                computation_times.append(10)
            else:
                constructibility_scores.append(0.0)
                computation_times.append(d**3)
        
        # Create subplot
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Constructibility by Degree', 'Computational Complexity',
                          'Galois Group Orders', 'Precision Requirements'),
            specs=[[{"secondary_y": False}, {"secondary_y": False}],
                   [{"secondary_y": True}, {"secondary_y": False}]]
        )
        
        # Plot 1: Constructibility
        fig.add_trace(
            go.Scatter(x=degrees, y=constructibility_scores,
                     mode='lines+markers', name='Constructibility',
                     line=dict(color='blue', width=3)),
            row=1, col=1
        )
        
        # Highlight the "Abel-Ruffini barrier" at degree 5
        fig.add_vline(x=5, line_dash="dash", line_color="red", 
                     annotation_text="Abel-Ruffini Barrier", row=1, col=1)
        
        # Plot 2: Computational complexity
        fig.add_trace(
            go.Scatter(x=degrees, y=computation_times,
                     mode='lines+markers', name='Relative Time',
                     line=dict(color='orange')),
            row=1, col=2
        )
        
        # Plot 3: Galois group orders (factorial growth)
        galois_orders = [math.factorial(min(d, 10)) for d in degrees]  # Cap at 10! for visualization
        fig.add_trace(
            go.Scatter(x=degrees, y=galois_orders,
                     mode='lines+markers', name='Max Galois Group Order',
                     line=dict(color='green')),
            row=2, col=1
        )
        
        # Add Monster Group reference
        monster_order = 808017424794512875886459904961710757005754368000000000
        fig.add_annotation(
            x=15, y=math.log10(monster_order),
            text="Monster Group →",
            showarrow=True, arrowhead=2, arrowcolor="purple",
            row=2, col=1
        )
        
        # Plot 4: Precision requirements
        precision_needs = [16 + max(0, d-4)*2 for d in degrees]
        fig.add_trace(
            go.Scatter(x=degrees, y=precision_needs,
                     mode='lines+markers', name='Digits of Precision',
                     line=dict(color='purple')),
            row=2, col=2
        )
        
        # Update layout
        fig.update_layout(
            title='Mathematical Complexity Landscape: From Constructible to Monster',
            height=800,
            showlegend=True
        )
        
        # Update y-axis for Galois group orders to log scale
        fig.update_yaxes(type="log", row=2, col=1)
        
        # Add axis labels
        fig.update_xaxes(title_text="Polynomial Degree", row=2, col=1)
        fig.update_xaxes(title_text="Polynomial Degree", row=2, col=2)
        fig.update_yaxes(title_text="Constructibility Score", row=1, col=1)
        fig.update_yaxes(title_text="Relative Time", row=1, col=2)
        fig.update_yaxes(title_text="Group Order (log scale)", row=2, col=1)
        fig.update_yaxes(title_text="Precision (digits)", row=2, col=2)
        
        return fig
    
    def explore_monster_boundary(self):
        """
        Explore the computational boundary approaching Monster-like complexity.
        """
        print("🎭 Exploring the Monster Boundary")
        print("=" * 50)
        
        # Monster Group facts
        monster_order = 808017424794512875886459904961710757005754368000000000
        monster_dimension = 196883
        
        print(f"Monster Group Order: {monster_order}")
        print(f"Monster Group minimal representation: {monster_dimension} dimensions")
        print(f"Number of digits in Monster order: {len(str(monster_order))}")
        
        # Compare with tractable examples
        tractable_examples = {
            'Symmetric Group S_5': math.factorial(5),
            'Symmetric Group S_10': math.factorial(10),
            'Symmetric Group S_20': math.factorial(20),
        }
        
        print(f"\n📊 Comparison with tractable groups:")
        for name, order in tractable_examples.items():
            ratio = monster_order / order if order > 0 else float('inf')
            print(f"  {name}: {order:,}")
            print(f"    Monster is {ratio:.2e} times larger")
        
        # Computational limits
        print(f"\n💻 Computational Reality Check:")
        
        # Estimate memory requirements for Monster representation
        monster_matrix_elements = monster_dimension ** 2
        bytes_per_element = 8  # Double precision
        monster_memory_gb = (monster_matrix_elements * bytes_per_element) / (1024**3)
        
        print(f"  Matrix representation memory: {monster_memory_gb:.2e} GB")
        print(f"  Current computer RAM: ~64 GB (typical)")
        print(f"  Memory factor: {monster_memory_gb/64:.2e}x larger than typical RAM")
        
        # Time estimates
        flops_per_matrix_mult = 2 * monster_dimension ** 3
        computer_flops = 1e12  # ~1 teraflop
        time_seconds = flops_per_matrix_mult / computer_flops
        time_years = time_seconds / (365.25 * 24 * 3600)
        
        print(f"  Single matrix multiplication: {time_years:.2e} years")
        print(f"  Universe age: ~1.4 × 10^10 years")
        
        return {
            'monster_order': monster_order,
            'monster_dimension': monster_dimension,
            'memory_requirement_gb': monster_memory_gb,
            'computation_time_years': time_years,
            'tractable_comparison': tractable_examples
        }

def demo_complexity_analysis():
    """Demonstrate complexity analysis capabilities."""
    analyzer = ConstructibilityAnalyzer()
    
    print("🔬 Mathematical Complexity Analysis")
    print("=" * 60)
    
    # Analyze spectrum of examples
    results = analyzer.demonstrate_complexity_spectrum()
    
    print("\n📊 Constructibility Analysis Results:")
    for name, result in results.items():
        print(f"\n{name} (degree {result['degree']}):")
        print(f"  Constructible: {result['constructible']['status']}")
        print(f"  Method: {result['constructible']['method']}")
        print(f"  Complexity: {result['complexity']['class']}")
        print(f"  Time estimate: {result['complexity']['time_estimate']}")
        print(f"  Precision needs: {result['complexity']['precision_requirements']}")
    
    # Create visualization
    print(f"\n📈 Creating complexity landscape visualization...")
    fig = analyzer.visualize_complexity_landscape()
    fig.write_html("complexity_landscape.html")
    print(f"💾 Saved as 'complexity_landscape.html'")
    
    # Explore Monster boundary
    print(f"\n🎭 Monster Group Analysis:")
    monster_analysis = analyzer.explore_monster_boundary()
    
    return analyzer, results, monster_analysis

if __name__ == "__main__":
    demo_complexity_analysis()
