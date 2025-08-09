#!/usr/bin/env python3
"""
DSKYpoly Data Science Simple Demo
================================

Basic demonstration using only NumPy, Matplotlib, and Plotly
to show the foundation for data science expansion.
"""

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

class SimplePolynomialAnalyzer:
    """
    Simplified polynomial analyzer using only NumPy.
    This demonstrates the core concepts without heavy dependencies.
    """
    
    def __init__(self, max_degree=10):
        self.max_degree = max_degree
        self.best_degree = None
        self.best_model = None
        self.mse_scores = {}
        
    def fit_polynomial(self, X, y, degree):
        """Fit a polynomial of given degree."""
        # Use numpy's polyfit
        coeffs = np.polyfit(X, y, degree)
        return coeffs
    
    def predict_polynomial(self, coeffs, X):
        """Make predictions using polynomial coefficients."""
        return np.polyval(coeffs, X)
    
    def calculate_mse(self, y_true, y_pred):
        """Calculate mean squared error."""
        return np.mean((y_true - y_pred) ** 2)
    
    def find_optimal_degree(self, X, y, validation_split=0.3):
        """
        Find optimal polynomial degree using train/validation split.
        """
        # Simple train/validation split
        n_val = int(len(X) * validation_split)
        indices = np.arange(len(X))
        np.random.shuffle(indices)
        
        val_indices = indices[:n_val]
        train_indices = indices[n_val:]
        
        X_train, y_train = X[train_indices], y[train_indices]
        X_val, y_val = X[val_indices], y[val_indices]
        
        # Test different degrees
        for degree in range(1, self.max_degree + 1):
            try:
                # Fit on training data
                coeffs = self.fit_polynomial(X_train, y_train, degree)
                
                # Predict on validation data
                y_pred = self.predict_polynomial(coeffs, X_val)
                
                # Calculate validation MSE
                mse = self.calculate_mse(y_val, y_pred)
                self.mse_scores[degree] = mse
                
            except np.linalg.LinAlgError:
                # Handle numerical instability for high degrees
                self.mse_scores[degree] = float('inf')
        
        # Find best degree
        self.best_degree = min(self.mse_scores.keys(), 
                              key=lambda d: self.mse_scores[d])
        
        # Fit best model on full data
        self.best_model = self.fit_polynomial(X, y, self.best_degree)
        
        return self.mse_scores
    
    def predict(self, X):
        """Make predictions using the best model."""
        if self.best_model is None:
            raise ValueError("Model not fitted yet. Call find_optimal_degree first.")
        return self.predict_polynomial(self.best_model, X)
    
    def plot_analysis(self, X, y, title="Polynomial Analysis"):
        """Create comprehensive analysis plots."""
        
        # Create subplots
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Data & Model Fits', 'Model Selection Curve',
                          'Predictions vs Actual', 'Residual Analysis'),
            specs=[[{"secondary_y": False}, {"secondary_y": False}],
                   [{"secondary_y": False}, {"secondary_y": False}]]
        )
        
        # Plot 1: Data and model fits
        fig.add_trace(
            go.Scatter(x=X, y=y, mode='markers', name='Data',
                      marker=dict(color='blue', size=6)),
            row=1, col=1
        )
        
        # Show fits for different degrees
        X_smooth = np.linspace(X.min(), X.max(), 200)
        degrees_to_show = [1, 3, self.best_degree]
        colors = ['red', 'green', 'purple']
        
        for i, degree in enumerate(degrees_to_show):
            if degree <= self.max_degree:
                coeffs = self.fit_polynomial(X, y, degree)
                y_pred_smooth = self.predict_polynomial(coeffs, X_smooth)
                
                fig.add_trace(
                    go.Scatter(x=X_smooth, y=y_pred_smooth,
                             mode='lines', name=f'Degree {degree}',
                             line=dict(color=colors[i])),
                    row=1, col=1
                )
        
        # Plot 2: Model selection curve
        degrees = list(self.mse_scores.keys())
        mse_values = list(self.mse_scores.values())
        
        fig.add_trace(
            go.Scatter(x=degrees, y=mse_values,
                     mode='lines+markers', name='Validation MSE',
                     line=dict(color='orange')),
            row=1, col=2
        )
        
        # Highlight best degree
        best_mse = self.mse_scores[self.best_degree]
        fig.add_trace(
            go.Scatter(x=[self.best_degree], y=[best_mse],
                     mode='markers', name='Best Degree',
                     marker=dict(color='red', size=12, symbol='star')),
            row=1, col=2
        )
        
        # Plot 3: Predictions vs actual
        y_pred = self.predict(X)
        fig.add_trace(
            go.Scatter(x=y, y=y_pred, mode='markers', name='Predictions',
                     marker=dict(color='green')),
            row=2, col=1
        )
        
        # Add perfect prediction line
        min_val, max_val = min(y.min(), y_pred.min()), max(y.max(), y_pred.max())
        fig.add_trace(
            go.Scatter(x=[min_val, max_val], y=[min_val, max_val],
                     mode='lines', name='Perfect Prediction',
                     line=dict(color='red', dash='dash')),
            row=2, col=1
        )
        
        # Plot 4: Residuals
        residuals = y - y_pred
        fig.add_trace(
            go.Scatter(x=y_pred, y=residuals, mode='markers', name='Residuals',
                     marker=dict(color='purple')),
            row=2, col=2
        )
        
        # Add horizontal line at y=0
        fig.add_hline(y=0, line_dash="dash", line_color="gray", row=2, col=2)
        
        # Update layout
        fig.update_layout(
            title=f'{title} (Best Degree: {self.best_degree})',
            height=800,
            showlegend=True
        )
        
        return fig

def demo_basic_analysis():
    """Demonstrate basic polynomial analysis."""
    print("🔬 DSKYpoly Basic Data Science Demo")
    print("=" * 50)
    
    # Generate sample data
    np.random.seed(42)
    X = np.linspace(0, 10, 100)
    
    # Complex function with noise
    true_function = 2*X**3 - 15*X**2 + 30*X + 5
    noise = np.random.normal(0, 50, len(X))
    y = true_function + noise
    
    print(f"📊 Generated dataset with {len(X)} samples")
    print(f"🎯 True function: 2x³ - 15x² + 30x + 5 + noise")
    
    # Create analyzer
    analyzer = SimplePolynomialAnalyzer(max_degree=8)
    
    # Find optimal degree
    print(f"\n🔍 Finding optimal polynomial degree...")
    mse_scores = analyzer.find_optimal_degree(X, y)
    
    print(f"✅ Optimal degree found: {analyzer.best_degree}")
    print(f"📊 Validation MSE: {mse_scores[analyzer.best_degree]:.2f}")
    
    # Show MSE for all degrees
    print(f"\n📈 MSE by degree:")
    for degree, mse in sorted(mse_scores.items()):
        marker = " ⭐" if degree == analyzer.best_degree else ""
        print(f"  Degree {degree}: {mse:.2f}{marker}")
    
    # Create visualization
    print(f"\n📊 Creating interactive visualization...")
    fig = analyzer.plot_analysis(X, y, "DSKYpoly Basic Analysis Demo")
    
    # Save as HTML
    fig.write_html("dskypoly_basic_demo.html")
    print(f"💾 Interactive plot saved as 'dskypoly_basic_demo.html'")
    
    # Also create a simple matplotlib version
    create_matplotlib_summary(X, y, analyzer)
    
    return analyzer

def create_matplotlib_summary(X, y, analyzer):
    """Create a summary plot using matplotlib."""
    plt.figure(figsize=(12, 8))
    
    # Data and best fit
    plt.subplot(2, 2, 1)
    plt.scatter(X, y, alpha=0.6, label='Data')
    y_pred = analyzer.predict(X)
    plt.plot(X, y_pred, 'r-', linewidth=2, label=f'Degree {analyzer.best_degree} Fit')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Data & Best Polynomial Fit')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Model selection
    plt.subplot(2, 2, 2)
    degrees = list(analyzer.mse_scores.keys())
    mse_values = list(analyzer.mse_scores.values())
    plt.plot(degrees, mse_values, 'o-', color='orange')
    plt.scatter([analyzer.best_degree], [analyzer.mse_scores[analyzer.best_degree]], 
                color='red', s=100, marker='*', label='Best')
    plt.xlabel('Polynomial Degree')
    plt.ylabel('Validation MSE')
    plt.title('Model Selection')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Predictions vs actual
    plt.subplot(2, 2, 3)
    plt.scatter(y, y_pred, alpha=0.6)
    min_val, max_val = min(y.min(), y_pred.min()), max(y.max(), y_pred.max())
    plt.plot([min_val, max_val], [min_val, max_val], 'r--', label='Perfect')
    plt.xlabel('Actual')
    plt.ylabel('Predicted')
    plt.title('Predictions vs Actual')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Residuals
    plt.subplot(2, 2, 4)
    residuals = y - y_pred
    plt.scatter(y_pred, residuals, alpha=0.6, color='purple')
    plt.axhline(y=0, color='gray', linestyle='--')
    plt.xlabel('Predicted')
    plt.ylabel('Residuals')
    plt.title('Residual Analysis')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('dskypoly_basic_demo.png', dpi=150, bbox_inches='tight')
    print(f"💾 Static plot saved as 'dskypoly_basic_demo.png'")
    
    # Don't show in non-interactive environment
    try:
        plt.show()
    except:
        print("📊 Plot created (display may not be available)")

def demo_financial_simulation():
    """Demonstrate financial time series simulation."""
    print(f"\n💰 Financial Time Series Simulation")
    print("=" * 40)
    
    # Generate realistic stock price data
    np.random.seed(123)
    n_days = 252  # One trading year
    
    # Create time series
    t = np.arange(n_days)
    
    # Trend component (polynomial)
    trend = 100 + 0.1*t + 0.0001*t**2
    
    # Seasonal component
    seasonal = 5 * np.sin(2*np.pi*t/50)
    
    # Random walk
    returns = np.random.normal(0.001, 0.02, n_days)  # Daily returns
    random_component = np.cumsum(returns)
    
    # Combine components
    log_prices = np.log(trend) + seasonal/100 + random_component
    prices = np.exp(log_prices)
    
    print(f"📊 Generated {n_days} days of stock price data")
    print(f"💰 Price range: ${prices.min():.2f} - ${prices.max():.2f}")
    print(f"📈 Total return: {((prices[-1]/prices[0]) - 1)*100:.2f}%")
    
    # Analyze trend
    analyzer = SimplePolynomialAnalyzer(max_degree=6)
    analyzer.find_optimal_degree(t, prices)
    
    print(f"🔍 Optimal polynomial degree for trend: {analyzer.best_degree}")
    
    # Create financial visualization
    fig = go.Figure()
    
    # Price data
    fig.add_trace(go.Scatter(x=t, y=prices, mode='lines', name='Stock Price',
                           line=dict(color='blue')))
    
    # Polynomial trend
    trend_pred = analyzer.predict(t)
    fig.add_trace(go.Scatter(x=t, y=trend_pred, mode='lines', name='Polynomial Trend',
                           line=dict(color='red', dash='dash')))
    
    fig.update_layout(
        title=f'Stock Price Analysis (Degree {analyzer.best_degree} Polynomial)',
        xaxis_title='Trading Days',
        yaxis_title='Price ($)',
        height=500
    )
    
    fig.write_html("dskypoly_financial_demo.html")
    print(f"💾 Financial demo saved as 'dskypoly_financial_demo.html'")
    
    return analyzer

def main():
    """Main demonstration function."""
    print("🚀 DSKYpoly Data Science Foundation Demo")
    print("Using NumPy, Matplotlib, and Plotly")
    print("=" * 60)
    
    # Basic polynomial analysis
    analyzer1 = demo_basic_analysis()
    
    # Financial simulation
    analyzer2 = demo_financial_simulation()
    
    print(f"\n🎉 Demo Complete!")
    print(f"📊 Generated files:")
    print(f"  • dskypoly_basic_demo.html (interactive)")
    print(f"  • dskypoly_basic_demo.png (static)")
    print(f"  • dskypoly_financial_demo.html (financial analysis)")
    
    print(f"\n🔬 This demonstrates the foundation for DSKYpoly data science:")
    print(f"  ✅ Polynomial model selection and validation")
    print(f"  ✅ Interactive visualizations with Plotly")
    print(f"  ✅ Financial time series trend analysis")
    print(f"  ✅ Statistical analysis and residual checking")
    
    print(f"\n🚀 Next steps:")
    print(f"  1. Install full data science environment:")
    print(f"     conda env create -f environment_datascience.yml")
    print(f"  2. Run advanced demos with scikit-learn and pandas")
    print(f"  3. Explore the Jupyter notebooks for interactive analysis")
    
    print(f"\n🎯 DSKYpoly: From polynomial mathematics to data science!")

if __name__ == "__main__":
    main()
