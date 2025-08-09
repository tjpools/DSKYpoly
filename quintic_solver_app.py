#!/usr/bin/env python3
"""
DSKYpoly Quintic Solver App
==========================

A cross-platform desktop application for solving quintic polynomial equations.
Demonstrates the journey from ancient mathematical impossibility to modern
numerical solutions.

Educational Focus:
- Abel-Ruffini theorem and the impossibility of general radical solutions
- Galois theory and group theory foundations
- Numerical methods for practical solving
- Visualization of polynomial behavior and roots

This application embodies the DSKYpoly philosophy:
"Understanding over black boxes" - showing how mathematical concepts
become computational reality.

Author: DSKYpoly Project  
Date: July 13, 2025
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import cmath
from typing import List, Tuple, Optional
import sys
import os

# Import our existing quintic solver if available
try:
    from quintic_hypergeometric import QuinticHypergeometricSolver
    ADVANCED_SOLVER_AVAILABLE = True
except ImportError:
    ADVANCED_SOLVER_AVAILABLE = False

class QuinticSolverApp:
    """
    Main application class for the DSKYpoly Quintic Solver.
    
    This GUI application provides:
    - Coefficient input for quintic polynomials
    - Educational content about quintic impossibility
    - Numerical solving with visualization
    - Historical context and mathematical foundations
    """
    
    def __init__(self, root):
        self.root = root
        self.root.title("DSKYpoly Quintic Solver - Ancient Math Meets Modern Computing")
        self.root.geometry("1200x800")
        
        # Configure style
        self.setup_styles()
        
        # Create main notebook for tabbed interface
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create tabs
        self.create_solver_tab()
        self.create_education_tab()
        self.create_history_tab()
        self.create_about_tab()
        
    def setup_styles(self):
        """Configure the visual style of the application."""
        style = ttk.Style()
        style.theme_use('clam')  # Professional look
        
        # Configure custom styles
        style.configure('Title.TLabel', font=('Arial', 16, 'bold'))
        style.configure('Heading.TLabel', font=('Arial', 12, 'bold'))
        style.configure('Math.TLabel', font=('Courier', 10))
    
    def create_solver_tab(self):
        """Create the main solver interface tab."""
        solver_frame = ttk.Frame(self.notebook)
        self.notebook.add(solver_frame, text="Quintic Solver")
        
        # Left panel for input
        input_frame = ttk.LabelFrame(solver_frame, text="Polynomial Coefficients", padding=10)
        input_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 5))
        
        # Title
        title_label = ttk.Label(input_frame, text="ax⁵ + bx⁴ + cx³ + dx² + ex + f = 0", 
                               style='Title.TLabel')
        title_label.pack(pady=(0, 20))
        
        # Coefficient inputs
        self.coefficients = {}
        coeff_names = [('a', 'x⁵'), ('b', 'x⁴'), ('c', 'x³'), ('d', 'x²'), ('e', 'x¹'), ('f', 'constant')]
        
        for coeff, term in coeff_names:
            frame = ttk.Frame(input_frame)
            frame.pack(fill=tk.X, pady=2)
            
            ttk.Label(frame, text=f"{coeff} ({term}):", width=12).pack(side=tk.LEFT)
            entry = ttk.Entry(frame, width=15)
            entry.pack(side=tk.LEFT, padx=(5, 0))
            entry.insert(0, "1" if coeff == 'a' else "0")  # Default values
            self.coefficients[coeff] = entry
        
        # Solve button
        solve_btn = ttk.Button(input_frame, text="Solve Quintic", command=self.solve_quintic)
        solve_btn.pack(pady=20)
        
        # Results area
        results_frame = ttk.LabelFrame(input_frame, text="Solutions", padding=10)
        results_frame.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
        
        self.results_text = scrolledtext.ScrolledText(results_frame, width=40, height=15, 
                                                     font=('Courier', 9))
        self.results_text.pack(fill=tk.BOTH, expand=True)
        
        # Right panel for visualization
        viz_frame = ttk.Frame(solver_frame)
        viz_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))
        
        # Create matplotlib figure
        self.fig = Figure(figsize=(8, 6), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, viz_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Initial plot
        self.plot_example_quintic()
    
    def create_education_tab(self):
        """Create the educational content tab."""
        edu_frame = ttk.Frame(self.notebook)
        self.notebook.add(edu_frame, text="Mathematical Theory")
        
        # Create scrolled text with educational content
        text_widget = scrolledtext.ScrolledText(edu_frame, wrap=tk.WORD, font=('Arial', 11))
        text_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        educational_content = """
THE QUINTIC IMPOSSIBILITY: A Mathematical Boundary

The quintic polynomial equation represents one of the most profound boundaries in mathematics - the limit of what can be solved using algebraic radicals.

🏛️ HISTORICAL TIMELINE:

1500s - Renaissance Breakthrough:
• Gerolamo Cardano solved cubic equations using radicals
• Ludovico Ferrari solved quartic equations
• Mathematicians believed quintics would follow

1824-1826 - The Impossible Truth:
• Niels Henrik Abel proved that general quintic equations CANNOT be solved using radicals
• Paolo Ruffini had earlier work pointing to this impossibility
• This shattered the Renaissance optimism about algebraic solvability

1832 - Group Theory Revolution:
• Évariste Galois developed group theory to explain WHY quintics are unsolvable
• The symmetric group S₅ contains the alternating group A₅
• A₅ is not a solvable group, proving the impossibility rigorously

🧮 THE MATHEMATICAL ESSENCE:

What Makes Quintics Special?
• Degrees 1-2: Solvable since ancient times
• Degree 3: Solved by Cardano (complex but doable)  
• Degree 4: Solved by Ferrari (very complex)
• Degree 5+: IMPOSSIBLE using radicals alone

The Abel-Ruffini Theorem:
"There is no general solution in radicals to polynomial equations of degree five or higher."

Galois Theory Explanation:
The symmetries of the quintic equation (described by the symmetric group S₅) cannot be "broken down" into the simple symmetries that correspond to radical operations.

🔧 MODERN SOLUTIONS:

While general radical solutions are impossible, quintics CAN be solved using:

1. Numerical Methods:
   • Newton-Raphson iteration
   • Durand-Kerner algorithm  
   • Aberth method

2. Special Functions:
   • Hypergeometric functions
   • Elliptic functions (Hermite's approach)
   • Jacobi theta functions

3. Special Cases:
   • Some quintics ARE solvable by radicals
   • Monomial forms: x⁵ - a = 0
   • Certain symmetric patterns

🤖 THE DSKYPOLY APPROACH:

This application demonstrates:
• Respect for mathematical impossibility
• Practical numerical solutions
• Connection from theory to silicon implementation
• "Understanding over black boxes" philosophy

The journey from ancient radical-seeking to modern numerical methods parallels the broader theme of human cognitive extension through systematic methods - the same pattern we see from Chinese mathematical breakthroughs 2500 years ago to today's AI systems.

Understanding WHY something is impossible is often more valuable than finding the solution itself.
        """
        
        text_widget.insert(tk.END, educational_content)
        text_widget.config(state=tk.DISABLED)  # Make read-only
    
    def create_history_tab(self):
        """Create the historical context tab."""
        history_frame = ttk.Frame(self.notebook)
        self.notebook.add(history_frame, text="Historical Context")
        
        text_widget = scrolledtext.ScrolledText(history_frame, wrap=tk.WORD, font=('Arial', 11))
        text_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        historical_content = """
STANDING ON THE SHOULDERS OF MATHEMATICAL GIANTS

The quintic polynomial represents a convergence of 2500 years of mathematical discovery, connecting ancient systematic thinking to modern computational power.

🏺 ANCIENT FOUNDATIONS (2000 BCE - 500 CE):

Babylonian Mathematicians:
• First systematic solutions to quadratic equations
• Recognition that mathematical problems could have systematic, repeatable solutions
• Introduction of algebraic thinking beyond arithmetic

Chinese Mathematical Revolution (500 BCE):
• Systematic methods for solving "3 equations in 3 unknowns"
• First cognitive extension through mechanical mathematical processes
• The pattern that continues through quintic solving today

🏛️ CLASSICAL PERIOD (500 CE - 1500 CE):

Islamic Golden Age:
• Al-Khwarizmi's systematic algebra (algorithm = "al-Khwarizmi")
• Preservation and extension of Greek and Indian mathematical knowledge
• Translation and transmission to European scholars

Medieval European Synthesis:
• Integration of classical knowledge with new discoveries
• Setting the stage for Renaissance breakthroughs

🎨 RENAISSANCE EXPLOSION (1500s):

The Italian School:
• Scipione del Ferro (first cubic solutions, kept secret)
• Niccolò Tartaglia (rediscovered cubic solutions)
• Gerolamo Cardano (published cubic solutions, solved quartics with Ferrari)
• Ludovico Ferrari (quartic reduction to cubic)

The Optimistic Era:
• Belief that ALL polynomial equations would eventually yield to algebraic methods
• Mathematical confidence in human rational power
• The stage set for the quintic challenge

⚡ THE IMPOSSIBILITY REVOLUTION (1800s):

Niels Henrik Abel (1802-1829):
• Norwegian mathematician who proved quintic impossibility
• Died tragically young in poverty
• His proof changed mathematics forever

Paolo Ruffini (1765-1822):
• Italian mathematician with early impossibility work
• Less rigorous than Abel but pointing in the right direction
• Showed the mathematical courage to challenge optimistic assumptions

Évariste Galois (1811-1832):
• French mathematician killed in duel at age 20
• Developed group theory to explain WHY quintics are impossible
• His work unified algebra, geometry, and logic

Charles Hermite (1822-1901):
• First to solve general quintic using elliptic functions
• Showed that impossibility in radicals ≠ impossibility in general
• Bridge to modern function theory

🔬 MODERN COMPUTATIONAL ERA (1900s-Present):

John von Neumann & Digital Computing:
• Stored-program computer architecture
• Made numerical polynomial solving practical
• Connected mathematical theory to silicon implementation

MIT & Educational Excellence:
• Professor Gilbert Strang's accessible linear algebra
• MIT Instrumentation Laboratory's Apollo DSKY
• Bridge between theoretical mathematics and practical engineering

Open Source & Collaborative Development:
• GNU/Linux environments for mathematical computation
• Python, NumPy, SciPy ecosystem
• Democratization of advanced mathematical tools

🚀 THE DSKYPOLY CONNECTION:

This application honors every link in this chain:

Ancient Systematic Thinking → Renaissance Algebraic Confidence → 
Impossibility Proofs → Modern Numerical Methods → Silicon Implementation

The quintic stands as a perfect symbol of:
• Human mathematical ambition meeting fundamental limits
• The beauty of understanding WHY something is impossible
• The power of numerical methods to transcend algebraic limitations
• The continuous thread from ancient cognitive extension to modern AI

We solve quintics not because we can do it algebraically (we can't), but because we understand the mathematical landscape well enough to navigate it with numerical precision.

Every coefficient you enter into this solver connects you to 2500 years of human mathematical achievement.
        """
        
        text_widget.insert(tk.END, historical_content)
        text_widget.config(state=tk.DISABLED)
    
    def create_about_tab(self):
        """Create the about/credits tab."""
        about_frame = ttk.Frame(self.notebook)
        self.notebook.add(about_frame, text="About DSKYpoly")
        
        text_widget = scrolledtext.ScrolledText(about_frame, wrap=tk.WORD, font=('Arial', 11))
        text_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        about_content = """
🚀 DSKYPOLY QUINTIC SOLVER

Version: 1.0.0
Build Date: July 13, 2025
Platform: Cross-platform Python application

PHILOSOPHICAL FOUNDATIONS:

This application embodies the DSKYpoly project philosophy:

1. "Standing on Large Shoulders"
   Honoring 2500 years of mathematical discovery from ancient Chinese 
   systematic methods to modern computational approaches.

2. "Matrix vs. Understanding Paradigm"
   Rather than providing a black-box solver, this application teaches 
   WHY quintics are special and HOW solutions are found.

3. "Assembly Language as Focusing Discipline"
   Built with attention to computational detail and respect for the 
   craft of programming at multiple abstraction levels.

4. "Complexity as Beauty, Not Obstacle"
   Embracing the mathematical richness of quintic impossibility rather 
   than hiding from it.

5. "Leibnizian Multi-Level Communication"
   Accessible to curious learners while maintaining mathematical rigor 
   for serious students.

6. "Explanation is Essential in Modeling"
   In data science and mathematical modeling, equations and algorithms are only part of the story. The true power of a model comes from the explanation that accompanies it: the context, the assumptions, the limitations, and the interpretation of results. See:
   • data_science/EXPLANATION_AND_MODELS.md

TECHNICAL IMPLEMENTATION:

• Python with tkinter for cross-platform GUI
• NumPy and SciPy for numerical computation
• Matplotlib for mathematical visualization
• Modular design for easy extension and analysis
• Compilable to standalone binary for distribution

EDUCATIONAL MISSION:

This solver serves multiple audiences:
• Students learning about polynomial equations
• Educators teaching algebraic impossibility
• Developers interested in mathematical software
• Anyone curious about the deep history of mathematics

REVERSE ENGINEERING READY:

This application is deliberately designed to be analyzed:
• Clear code structure for educational purposes
• Compilable to binary for reverse engineering study
• Documentation of design decisions
• Integration with DSKYpoly analysis tools

CREDITS & ACKNOWLEDGMENTS:

Standing on the Shoulders of Giants:
• Ancient Chinese mathematicians (systematic methods)
• Babylonian mathematicians (quadratic solutions)
• Gerolamo Cardano & Ludovico Ferrari (Renaissance breakthroughs)
• Niels Henrik Abel & Paolo Ruffini (impossibility proofs)
• Évariste Galois (group theory foundations)
• Charles Hermite (elliptic function solutions)
• MIT Educational Tradition (Gilbert Strang, DSKY legacy)
• Open Source Community (Python, NumPy, Matplotlib ecosystems)

"We are utilizing mechanical machines to convey our thoughts and 
computations" - continuing humanity's 2500-year journey of cognitive 
extension through systematic methods.

This application is part of the DSKYpoly project, bridging ancient 
mathematical wisdom with modern computational power.

For more information: https://github.com/tjpools/DSKYpoly

---
DSKYpoly Project - Where Ancient Math Meets Modern AI
        """
        
        text_widget.insert(tk.END, about_content)
        text_widget.config(state=tk.DISABLED)
    
    def solve_quintic(self):
        """Solve the quintic polynomial with the entered coefficients."""
        try:
            # Get coefficients
            coeffs = []
            for coeff in ['a', 'b', 'c', 'd', 'e', 'f']:
                value = float(self.coefficients[coeff].get())
                coeffs.append(value)
            
            # Check if it's actually a quintic (leading coefficient non-zero)
            if coeffs[0] == 0:
                messagebox.showerror("Error", "Leading coefficient 'a' cannot be zero for a quintic equation.")
                return
            
            # Clear previous results
            self.results_text.delete(1.0, tk.END)
            
            # Display the equation
            equation = self.format_equation(coeffs)
            self.results_text.insert(tk.END, f"Solving: {equation}\n\n")
            
            # Find roots using numpy
            roots = np.roots(coeffs)
            
            # Display results
            self.results_text.insert(tk.END, "NUMERICAL SOLUTIONS:\n")
            self.results_text.insert(tk.END, "=" * 30 + "\n\n")
            
            for i, root in enumerate(roots, 1):
                if abs(root.imag) < 1e-10:  # Essentially real
                    self.results_text.insert(tk.END, f"Root {i}: {root.real:.6f}\n")
                else:
                    self.results_text.insert(tk.END, f"Root {i}: {root.real:.6f} + {root.imag:.6f}i\n")
            
            # Add educational note
            self.results_text.insert(tk.END, "\n" + "=" * 30 + "\n")
            self.results_text.insert(tk.END, "NOTE: These solutions were found using\n")
            self.results_text.insert(tk.END, "numerical methods, not algebraic radicals.\n")
            self.results_text.insert(tk.END, "The Abel-Ruffini theorem proves that\n")
            self.results_text.insert(tk.END, "general quintic equations cannot be\n")
            self.results_text.insert(tk.END, "solved using radicals alone.\n")
            
            # Plot the polynomial and its roots
            self.plot_polynomial(coeffs, roots)
            
        except ValueError as e:
            messagebox.showerror("Error", f"Please enter valid numbers for all coefficients.\n\nError: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while solving:\n\n{str(e)}")
    
    def format_equation(self, coeffs):
        """Format the polynomial equation as a string."""
        terms = []
        variables = ['x⁵', 'x⁴', 'x³', 'x²', 'x', '']
        
        for i, (coeff, var) in enumerate(zip(coeffs, variables)):
            if coeff == 0:
                continue
            
            # Format coefficient
            if i == 0:  # First term
                if coeff == 1 and var:
                    terms.append(var)
                elif coeff == -1 and var:
                    terms.append(f"-{var}")
                else:
                    terms.append(f"{coeff}{var}")
            else:  # Subsequent terms
                if coeff > 0:
                    if coeff == 1 and var:
                        terms.append(f" + {var}")
                    else:
                        terms.append(f" + {coeff}{var}")
                else:
                    if coeff == -1 and var:
                        terms.append(f" - {var}")
                    else:
                        terms.append(f" - {abs(coeff)}{var}")
        
        equation = "".join(terms) if terms else "0"
        return f"{equation} = 0"
    
    def plot_polynomial(self, coeffs, roots):
        """Plot the polynomial function and mark its roots."""
        self.fig.clear()
        ax = self.fig.add_subplot(111)
        
        # Create x values for plotting
        real_roots = [r.real for r in roots if abs(r.imag) < 1e-10]
        if real_roots:
            x_min = min(real_roots) - 2
            x_max = max(real_roots) + 2
        else:
            x_min, x_max = -3, 3
        
        x = np.linspace(x_min, x_max, 1000)
        
        # Evaluate polynomial
        y = np.polyval(coeffs, x)
        
        # Plot the function
        ax.plot(x, y, 'b-', linewidth=2, label='f(x)')
        ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
        ax.axvline(x=0, color='k', linestyle='-', alpha=0.3)
        
        # Mark real roots
        for root in roots:
            if abs(root.imag) < 1e-10:  # Real root
                ax.plot(root.real, 0, 'ro', markersize=8, label=f'Root: {root.real:.3f}')
        
        # Format plot
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.set_title('Quintic Polynomial Visualization')
        ax.grid(True, alpha=0.3)
        ax.legend()
        
        # Refresh canvas
        self.canvas.draw()
    
    def plot_example_quintic(self):
        """Plot an example quintic polynomial on startup."""
        # Example: x^5 - 5x^3 + 4x = 0
        coeffs = [1, 0, -5, 0, 4, 0]
        roots = np.roots(coeffs)
        self.plot_polynomial(coeffs, roots)

def main():
    """Main application entry point."""
    root = tk.Tk()
    app = QuinticSolverApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
