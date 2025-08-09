#!/usr/bin/env python3
"""
DSKYpoly Quintic Solver - iOS Pythonista Version
===============================================

A native iOS application for solving quintic polynomial equations using Pythonista 3.
Demonstrates the journey from ancient mathematical impossibility to modern iPhone accessibility.

Educational Focus:
- Abel-Ruffini theorem and the impossibility of general radical solutions
- 2500-year mathematical lineage from ancient China to iPhone
- Numerical methods for practical solving on mobile devices
- Touch-optimized interface for mathematical exploration

This mobile application embodies the DSKYpoly philosophy:
"Understanding over black boxes" - bringing mathematical concepts
to students' fingertips anywhere, anytime.

Author: DSKYpoly Project  
Date: July 13, 2025
Platform: iOS Pythonista 3
"""

import ui
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
import io
import base64
import cmath
from typing import List, Tuple, Optional

# Configure matplotlib for iOS
matplotlib.use('Agg')
plt.style.use('default')

class QuinticSolverIOS:
    """
    iOS native quintic polynomial solver using Pythonista 3 framework.
    
    Provides touch-optimized interface for:
    - Coefficient input with iOS numeric keyboard
    - Educational content about quintic impossibility  
    - Numerical solving with matplotlib visualization
    - Historical context accessible on mobile device
    """
    
    def __init__(self):
        self.coefficients = {'a': 1, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0}
        self.current_roots = None
        self.setup_ui()
        
    def setup_ui(self):
        """Create the iOS native interface using Pythonista ui framework."""
        # Main view - optimized for iPhone screen
        self.view = ui.View(frame=(0, 0, 375, 812))  # iPhone 13 dimensions
        self.view.name = 'DSKYpoly Quintic Solver'
        self.view.background_color = '#f0f0f0'
        
        # Create tabbed interface using SegmentedControl
        self.tab_control = ui.SegmentedControl(frame=(10, 60, 355, 30))
        self.tab_control.segments = ['Solver', 'Theory', 'History', 'About']
        self.tab_control.selected_index = 0
        self.tab_control.action = self.tab_changed
        self.view.add_subview(self.tab_control)
        
        # Container for tab content
        self.content_view = ui.View(frame=(10, 100, 355, 700))
        self.content_view.background_color = 'white'
        self.content_view.corner_radius = 8
        self.view.add_subview(self.content_view)
        
        # Create all tab contents
        self.create_solver_tab()
        self.create_education_tabs()
        
        # Show solver tab by default
        self.show_solver_tab()
        
    def create_solver_tab(self):
        """Create the main solver interface optimized for touch input."""
        # Title
        title = ui.Label(frame=(10, 10, 335, 30))
        title.text = 'ax⁵ + bx⁴ + cx³ + dx² + ex + f = 0'
        title.font = ('Helvetica-Bold', 18)
        title.text_color = '#333333'
        title.alignment = ui.ALIGN_CENTER
        
        # Coefficient inputs with iOS-friendly layout
        self.coeff_inputs = {}
        coeff_names = [('a', 'x⁵'), ('b', 'x⁴'), ('c', 'x³'), ('d', 'x²'), ('e', 'x¹'), ('f', 'constant')]
        
        y_pos = 50
        for coeff, term in coeff_names:
            # Label
            label = ui.Label(frame=(10, y_pos, 100, 30))
            label.text = f'{coeff} ({term}):'
            label.font = ('Helvetica', 14)
            
            # Input field with numeric keyboard
            input_field = ui.TextField(frame=(120, y_pos, 200, 30))
            input_field.placeholder = f'Enter {coeff}'
            input_field.keyboard_type = ui.KEYBOARD_DECIMAL_PAD
            input_field.text = '1' if coeff == 'a' else '0'
            input_field.border_width = 1
            input_field.border_color = '#cccccc'
            input_field.corner_radius = 4
            
            self.coeff_inputs[coeff] = input_field
            y_pos += 40
        
        # Solve button with iOS styling
        solve_button = ui.Button(frame=(10, y_pos + 20, 335, 44))
        solve_button.title = 'Solve Quintic Polynomial'
        solve_button.background_color = '#007AFF'  # iOS blue
        solve_button.tint_color = 'white'
        solve_button.corner_radius = 8
        solve_button.font = ('Helvetica-Bold', 16)
        solve_button.action = self.solve_quintic
        
        # Results display
        results_label = ui.Label(frame=(10, y_pos + 80, 335, 20))
        results_label.text = 'Solutions:'
        results_label.font = ('Helvetica-Bold', 14)
        
        self.results_view = ui.TextView(frame=(10, y_pos + 105, 335, 150))
        self.results_view.font = ('Courier', 12)
        self.results_view.editable = False
        self.results_view.background_color = '#f8f8f8'
        self.results_view.border_width = 1
        self.results_view.border_color = '#cccccc'
        
        # Visualization area placeholder
        viz_label = ui.Label(frame=(10, y_pos + 270, 335, 20))
        viz_label.text = 'Polynomial Visualization:'
        viz_label.font = ('Helvetica-Bold', 14)
        
        self.viz_view = ui.ImageView(frame=(10, y_pos + 295, 335, 200))
        self.viz_view.background_color = '#f8f8f8'
        self.viz_view.border_width = 1
        self.viz_view.border_color = '#cccccc'
        
        # Store solver tab components
        self.solver_components = [title] + list(self.coeff_inputs.values()) + \
                               [solve_button, results_label, self.results_view, viz_label, self.viz_view]
        
        # Add labels for coefficient inputs
        for i, (coeff, term) in enumerate(coeff_names):
            label = ui.Label(frame=(10, 50 + i * 40, 100, 30))
            label.text = f'{coeff} ({term}):'
            label.font = ('Helvetica', 14)
            self.solver_components.insert(1 + i, label)
    
    def create_education_tabs(self):
        """Create educational content tabs optimized for iPhone reading."""
        # Mathematical Theory content
        self.theory_text = """
🧮 THE QUINTIC IMPOSSIBILITY

The quintic polynomial represents one of mathematics' most profound boundaries - the limit of algebraic solvability.

📚 KEY CONCEPTS:

Abel-Ruffini Theorem:
"General quintic equations CANNOT be solved using radicals alone."

Why Quintics Are Special:
• Degrees 1-2: Ancient solutions
• Degree 3: Cardano (1540s)  
• Degree 4: Ferrari (1540s)
• Degree 5+: IMPOSSIBLE with radicals

🔬 Modern Solutions:
• Numerical methods (like this app)
• Special functions (hypergeometric)
• Group theory explanations

The beauty: Understanding WHY something is impossible often matters more than finding the solution itself.

🤖 DSKYpoly Connection:
This iPhone app demonstrates how 2500 years of mathematical discovery becomes accessible computational power in your pocket.
        """
        
        # Historical Context content  
        self.history_text = """
🏛️ MATHEMATICAL GIANTS' SHOULDERS

Your iPhone connects you to 2500 years of discovery:

🏺 Ancient Foundations:
• Babylonians: First systematic algebra
• Chinese: Cognitive extension methods
• Pattern that continues to iPhone apps

🎨 Renaissance Breakthrough:
• Cardano & Ferrari: Cubic/quartic solutions
• Mathematical optimism about solvability
• Setting stage for quintic challenge

⚡ Impossibility Revolution:
• Abel (1826): Quintic impossibility proof
• Galois (1832): Group theory explanation
• Hermite: Solutions via special functions

🔬 Modern Era:
• von Neumann: Computer architecture
• MIT DSKY: Space-age mathematics
• iPhone: Democratized mathematical tools

🚀 The Continuity:
Ancient systematic thinking → Renaissance confidence → Impossibility proofs → iPhone mathematical education

Every coefficient you enter connects you to this entire lineage of human mathematical achievement.
        """
        
        # About content
        self.about_text = """
🚀 DSKYPOLY QUINTIC SOLVER
iOS Pythonista Version 1.0

📱 MOBILE MATHEMATICAL EDUCATION:

This iPhone app embodies DSKYpoly philosophy:
• "Standing on large shoulders"
• Mathematical accessibility without compromise  
• Understanding over black boxes
• Ancient wisdom meets modern mobility

🛠️ TECHNICAL IMPLEMENTATION:
• Native iOS Python with Pythonista 3
• NumPy numerical computation
• Matplotlib mathematical visualization
• Touch-optimized interface design
• Offline mathematical capability

🎯 EDUCATIONAL MISSION:
Making 2500 years of mathematical discovery accessible to students anywhere, anytime.

From Kennedy's moonshot to iPhone mathematical tools - the democratization of computational power continues.

🏛️ STANDING ON SHOULDERS:
• Ancient Chinese mathematicians
• Renaissance Italian school
• Abel & Galois impossibility proofs
• MIT educational excellence
• Open source Python ecosystem

DSKYpoly Project - Where Ancient Math Meets Modern AI
        """
    
    def tab_changed(self, sender):
        """Handle tab selection changes."""
        if sender.selected_index == 0:
            self.show_solver_tab()
        elif sender.selected_index == 1:
            self.show_text_tab(self.theory_text, "Mathematical Theory")
        elif sender.selected_index == 2:
            self.show_text_tab(self.history_text, "Historical Context")
        elif sender.selected_index == 3:
            self.show_text_tab(self.about_text, "About DSKYpoly")
    
    def show_solver_tab(self):
        """Display the solver interface."""
        # Clear content view
        for subview in self.content_view.subviews:
            subview.remove_from_superview()
        
        # Add solver components
        for component in self.solver_components:
            self.content_view.add_subview(component)
    
    def show_text_tab(self, text_content, title):
        """Display educational text content."""
        # Clear content view
        for subview in self.content_view.subviews:
            subview.remove_from_superview()
        
        # Title
        title_label = ui.Label(frame=(10, 10, 335, 30))
        title_label.text = title
        title_label.font = ('Helvetica-Bold', 18)
        title_label.text_color = '#333333'
        title_label.alignment = ui.ALIGN_CENTER
        self.content_view.add_subview(title_label)
        
        # Content text view
        text_view = ui.TextView(frame=(10, 50, 335, 640))
        text_view.text = text_content
        text_view.font = ('Helvetica', 14)
        text_view.editable = False
        text_view.background_color = 'white'
        self.content_view.add_subview(text_view)
    
    def solve_quintic(self, sender):
        """Solve the quintic polynomial with touch-friendly feedback."""
        try:
            # Get coefficients from input fields
            coeffs = []
            for coeff in ['a', 'b', 'c', 'd', 'e', 'f']:
                value = float(self.coeff_inputs[coeff].text or '0')
                coeffs.append(value)
            
            # Validate quintic
            if coeffs[0] == 0:
                self.show_alert("Error", "Leading coefficient 'a' cannot be zero for quintic equation.")
                return
            
            # Solve using NumPy
            roots = np.roots(coeffs)
            self.current_roots = roots
            
            # Format results for mobile display
            equation = self.format_equation(coeffs)
            results_text = f"Equation: {equation}\n\n"
            results_text += "NUMERICAL SOLUTIONS:\n"
            results_text += "=" * 25 + "\n\n"
            
            for i, root in enumerate(roots, 1):
                if abs(root.imag) < 1e-10:
                    results_text += f"Root {i}: {root.real:.6f}\n"
                else:
                    results_text += f"Root {i}: {root.real:.6f} + {root.imag:.6f}i\n"
            
            results_text += "\n" + "=" * 25 + "\n"
            results_text += "NOTE: Solutions found using numerical methods.\n"
            results_text += "Abel-Ruffini theorem: quintics cannot be solved using radicals alone."
            
            self.results_view.text = results_text
            
            # Generate and display plot
            self.create_mobile_plot(coeffs, roots)
            
        except ValueError:
            self.show_alert("Error", "Please enter valid numbers for all coefficients.")
        except Exception as e:
            self.show_alert("Error", f"Solving error: {str(e)}")
    
    def format_equation(self, coeffs):
        """Format polynomial equation for mobile display."""
        terms = []
        variables = ['x⁵', 'x⁴', 'x³', 'x²', 'x', '']
        
        for i, (coeff, var) in enumerate(zip(coeffs, variables)):
            if coeff == 0:
                continue
            
            if i == 0:
                if coeff == 1 and var:
                    terms.append(var)
                elif coeff == -1 and var:
                    terms.append(f"-{var}")
                else:
                    terms.append(f"{coeff}{var}")
            else:
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
    
    def create_mobile_plot(self, coeffs, roots):
        """Create matplotlib visualization optimized for iPhone display."""
        # Create figure with mobile-friendly dimensions
        fig = Figure(figsize=(6, 4), dpi=80)
        ax = fig.add_subplot(111)
        
        # Determine plot range based on real roots
        real_roots = [r.real for r in roots if abs(r.imag) < 1e-10]
        if real_roots:
            x_min = min(real_roots) - 1
            x_max = max(real_roots) + 1
        else:
            x_min, x_max = -2, 2
        
        # Generate points for smooth curve
        x = np.linspace(x_min, x_max, 500)
        y = np.polyval(coeffs, x)
        
        # Plot polynomial with mobile-friendly styling
        ax.plot(x, y, 'b-', linewidth=2, label='f(x)')
        ax.axhline(y=0, color='k', linestyle='-', alpha=0.3, linewidth=1)
        ax.axvline(x=0, color='k', linestyle='-', alpha=0.3, linewidth=1)
        
        # Mark real roots with touch-friendly markers
        for root in roots:
            if abs(root.imag) < 1e-10:
                ax.plot(root.real, 0, 'ro', markersize=8)
        
        # Mobile-friendly formatting
        ax.set_xlabel('x', fontsize=12)
        ax.set_ylabel('f(x)', fontsize=12)
        ax.set_title('Quintic Visualization', fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3, linewidth=0.5)
        
        # Adjust layout for mobile screen
        fig.tight_layout(pad=1.0)
        
        # Convert to image for display in ui.ImageView
        buf = io.BytesIO()
        fig.savefig(buf, format='png', bbox_inches='tight', facecolor='white')
        buf.seek(0)
        
        # Create ui.Image from buffer
        import PIL.Image
        pil_image = PIL.Image.open(buf)
        self.viz_view.image = ui.Image.from_pil(pil_image)
        
        plt.close(fig)  # Clean up memory
    
    def show_alert(self, title, message):
        """Display iOS-style alert dialog."""
        import console
        console.alert(title, message, 'OK', hide_cancel_button=True)
    
    def present(self):
        """Present the application in full screen."""
        self.view.present('fullscreen')

def main():
    """Main application entry point for iOS."""
    app = QuinticSolverIOS()
    app.present()

if __name__ == "__main__":
    main()
