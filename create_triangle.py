#!/usr/bin/env python3
"""
DSKYpoly Triangle Visualization Generator
Creates the elegant equilateral triangle showing the synchronized development environment
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def create_dskypoly_triangle():
    """Create the elegant DSKYpoly development triangle"""
    fig, ax = plt.subplots(1, 1, figsize=(12, 10))
    
    # Define triangle vertices (equilateral triangle)
    github_x, github_y = 0, np.sqrt(3)/2  # Top vertex
    fedora_x, fedora_y = -0.5, 0          # Bottom left
    wsl_x, wsl_y = 0.5, 0                 # Bottom right
    
    # Draw the triangle
    triangle = patches.Polygon([(github_x, github_y), (fedora_x, fedora_y), (wsl_x, wsl_y)], 
                              linewidth=3, edgecolor='blue', facecolor='lightblue', alpha=0.3)
    ax.add_patch(triangle)
    
    # Add vertices with enhanced styling
    ax.plot(github_x, github_y, 'o', markersize=20, color='gold', markeredgecolor='orange', markeredgewidth=3)
    ax.plot(fedora_x, fedora_y, 'o', markersize=20, color='red', markeredgecolor='darkred', markeredgewidth=3)
    ax.plot(wsl_x, wsl_y, 'o', markersize=20, color='green', markeredgecolor='darkgreen', markeredgewidth=3)
    
    # Add labels with better positioning
    ax.text(github_x, github_y + 0.15, 'GitHub\n(origin)', ha='center', va='bottom', 
            fontsize=14, fontweight='bold', color='darkblue')
    ax.text(fedora_x - 0.15, fedora_y - 0.05, 'Fedora\n(development)', ha='center', va='top', 
            fontsize=14, fontweight='bold', color='darkred')
    ax.text(wsl_x + 0.15, wsl_y - 0.05, 'WSL Ubuntu\n(current)', ha='center', va='top', 
            fontsize=14, fontweight='bold', color='darkgreen')
    
    # Add synchronization arrows
    # GitHub to Fedora
    ax.annotate('', xy=(fedora_x + 0.1, fedora_y + 0.1), xytext=(github_x - 0.1, github_y - 0.1),
                arrowprops=dict(arrowstyle='<->', color='purple', lw=2))
    # GitHub to WSL
    ax.annotate('', xy=(wsl_x - 0.1, wsl_y + 0.1), xytext=(github_x + 0.1, github_y - 0.1),
                arrowprops=dict(arrowstyle='<->', color='purple', lw=2))
    # Fedora to WSL
    ax.annotate('', xy=(wsl_x - 0.1, wsl_y), xytext=(fedora_x + 0.1, fedora_y),
                arrowprops=dict(arrowstyle='<->', color='purple', lw=2))
    
    # Add center synchronization indicator
    center_x = (github_x + fedora_x + wsl_x) / 3
    center_y = (github_y + fedora_y + wsl_y) / 3
    ax.plot(center_x, center_y, '*', markersize=15, color='purple')
    ax.text(center_x, center_y - 0.1, 'synchronized', ha='center', va='top', 
            fontsize=12, style='italic', color='purple')
    
    # Add title and enhance the plot
    ax.set_title('DSKYpoly Development Triangle\nEquilateral Synchronization', 
                fontsize=18, fontweight='bold', pad=20)
    
    # Set equal aspect ratio and clean axes
    ax.set_aspect('equal')
    ax.set_xlim(-0.8, 0.8)
    ax.set_ylim(-0.3, 1.0)
    ax.axis('off')
    
    # Add subtitle with current status
    ax.text(0, -0.25, '✅ All vertices synchronized with latest mathematical sophistication', 
            ha='center', va='center', fontsize=12, 
            bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgreen", alpha=0.7))
    
    plt.tight_layout()
    return fig

if __name__ == "__main__":
    # Create and save the triangle
    print("🔺 Creating DSKYpoly Triangle visualization...")
    triangle_fig = create_dskypoly_triangle()
    
    # Save in multiple formats
    triangle_fig.savefig('DSKYpoly_Triangle.png', dpi=300, bbox_inches='tight', 
                        facecolor='white', edgecolor='none')
    triangle_fig.savefig('DSKYpoly_Triangle.svg', format='svg', bbox_inches='tight', 
                        facecolor='white', edgecolor='none')
    
    print("✅ DSKYpoly Triangle saved as:")
    print("📁 DSKYpoly_Triangle.png (high-resolution)")
    print("📁 DSKYpoly_Triangle.svg (vector graphics)")
    print("\n✨ Your perfect equilateral triangle of computational sophistication!")
    
    # Display the plot
    plt.show()
