"""
DSKYpoly Data Science Toolkit
============================

Advanced polynomial-based data science tools leveraging the mathematical
foundation of DSKYpoly for practical data analysis applications.

This module bridges the gap between pure polynomial mathematics and
real-world data science applications.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from scipy import optimize
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error, r2_score
import warnings
warnings.filterwarnings('ignore')

class PolynomialAnalyzer:
    """
    Advanced polynomial analysis toolkit for data science applications.
    
    Features:
    - Optimal degree selection with cross-validation
    - Regularization techniques (Ridge/Lasso)
    - Interactive visualizations
    - Performance benchmarking
    - Financial time series modeling
    """
    
    def __init__(self, max_degree=10, regularization='none', alpha=1.0):
        """
        Initialize the polynomial analyzer.
        
        Parameters:
        -----------
        max_degree : int
            Maximum polynomial degree to consider
        regularization : str
            Type of regularization ('none', 'ridge', 'lasso')
        alpha : float
            Regularization strength
        """
        self.max_degree = max_degree
        self.regularization = regularization
        self.alpha = alpha
        self.models = {}
        self.cv_scores = {}
        self.best_degree = None
        
    def find_optimal_degree(self, X, y, cv_folds=5):
        """
        Find optimal polynomial degree using cross-validation.
        
        Parameters:
        -----------
        X : array-like
            Input features
        y : array-like
            Target values
        cv_folds : int
            Number of cross-validation folds
            
        Returns:
        --------
        dict : Cross-validation results for each degree
        """
        X = np.array(X).reshape(-1, 1) if X.ndim == 1 else X
        
        for degree in range(1, self.max_degree + 1):
            # Create polynomial pipeline
            if self.regularization == 'ridge':
                model = Pipeline([
                    ('poly', PolynomialFeatures(degree)),
                    ('regressor', Ridge(alpha=self.alpha))
                ])
            elif self.regularization == 'lasso':
                model = Pipeline([
                    ('poly', PolynomialFeatures(degree)),
                    ('regressor', Lasso(alpha=self.alpha))
                ])
            else:
                model = Pipeline([
                    ('poly', PolynomialFeatures(degree)),
                    ('regressor', LinearRegression())
                ])
            
            # Cross-validation
            cv_scores = cross_val_score(model, X, y, cv=cv_folds, 
                                      scoring='neg_mean_squared_error')
            
            self.models[degree] = model
            self.cv_scores[degree] = {
                'mean': -cv_scores.mean(),
                'std': cv_scores.std(),
                'scores': -cv_scores
            }
        
        # Find best degree
        self.best_degree = min(self.cv_scores.keys(), 
                              key=lambda d: self.cv_scores[d]['mean'])
        
        return self.cv_scores
    
    def fit_best_model(self, X, y):
        """
        Fit the best polynomial model based on cross-validation.
        
        Parameters:
        -----------
        X : array-like
            Input features
        y : array-like
            Target values
            
        Returns:
        --------
        fitted model
        """
        if self.best_degree is None:
            self.find_optimal_degree(X, y)
        
        X = np.array(X).reshape(-1, 1) if X.ndim == 1 else X
        self.best_model = self.models[self.best_degree]
        self.best_model.fit(X, y)
        
        return self.best_model
    
    def predict_with_confidence(self, X_new, confidence_level=0.95):
        """
        Make predictions with confidence intervals.
        
        Parameters:
        -----------
        X_new : array-like
            New input values
        confidence_level : float
            Confidence level for intervals
            
        Returns:
        --------
        dict : Predictions with confidence intervals
        """
        X_new = np.array(X_new).reshape(-1, 1) if X_new.ndim == 1 else X_new
        
        predictions = self.best_model.predict(X_new)
        
        # Estimate prediction intervals using cross-validation scores
        mse = self.cv_scores[self.best_degree]['mean']
        std_error = np.sqrt(mse)
        
        # Approximate confidence intervals
        from scipy.stats import t
        alpha = 1 - confidence_level
        t_value = t.ppf(1 - alpha/2, df=len(X_new) - 1)
        margin = t_value * std_error
        
        return {
            'predictions': predictions,
            'lower_bound': predictions - margin,
            'upper_bound': predictions + margin,
            'std_error': std_error
        }
    
    def plot_model_comparison(self, X, y):
        """
        Create interactive plot comparing different polynomial degrees.
        
        Parameters:
        -----------
        X : array-like
            Input features
        y : array-like
            Target values
            
        Returns:
        --------
        plotly figure
        """
        X = np.array(X).reshape(-1, 1) if X.ndim == 1 else X
        X_flat = X.flatten() if X.ndim > 1 else X
        
        # Create subplot
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Data & Model Fits', 'Cross-Validation Scores',
                          'Model Complexity', 'Residual Analysis'),
            specs=[[{"secondary_y": False}, {"secondary_y": False}],
                   [{"secondary_y": False}, {"secondary_y": False}]]
        )
        
        # Plot 1: Data and model fits
        fig.add_trace(
            go.Scatter(x=X_flat, y=y, mode='markers', name='Data',
                      marker=dict(color='blue', size=6)),
            row=1, col=1
        )
        
        # Generate smooth curve for predictions
        X_smooth = np.linspace(X_flat.min(), X_flat.max(), 200).reshape(-1, 1)
        
        colors = px.colors.qualitative.Set1
        for i, degree in enumerate([1, 2, 3, self.best_degree]):
            if degree in self.models:
                model = self.models[degree]
                model.fit(X, y)
                y_pred = model.predict(X_smooth)
                
                fig.add_trace(
                    go.Scatter(x=X_smooth.flatten(), y=y_pred,
                             mode='lines', name=f'Degree {degree}',
                             line=dict(color=colors[i % len(colors)])),
                    row=1, col=1
                )
        
        # Plot 2: Cross-validation scores
        degrees = list(self.cv_scores.keys())
        cv_means = [self.cv_scores[d]['mean'] for d in degrees]
        cv_stds = [self.cv_scores[d]['std'] for d in degrees]
        
        fig.add_trace(
            go.Scatter(x=degrees, y=cv_means,
                     error_y=dict(type='data', array=cv_stds),
                     mode='lines+markers', name='CV Score',
                     line=dict(color='red')),
            row=1, col=2
        )
        
        # Highlight best degree
        best_score = self.cv_scores[self.best_degree]['mean']
        fig.add_trace(
            go.Scatter(x=[self.best_degree], y=[best_score],
                     mode='markers', name='Best Degree',
                     marker=dict(color='green', size=12, symbol='star')),
            row=1, col=2
        )
        
        # Plot 3: Model complexity (number of coefficients)
        complexities = [sum(range(degree + 2)) for degree in degrees]  # For polynomial features
        fig.add_trace(
            go.Scatter(x=degrees, y=complexities,
                     mode='lines+markers', name='Model Complexity',
                     line=dict(color='purple')),
            row=2, col=1
        )
        
        # Plot 4: Residual analysis for best model
        self.best_model.fit(X, y)
        y_pred = self.best_model.predict(X)
        residuals = y - y_pred
        
        fig.add_trace(
            go.Scatter(x=y_pred, y=residuals,
                     mode='markers', name='Residuals',
                     marker=dict(color='orange')),
            row=2, col=2
        )
        
        # Add horizontal line at y=0 for residuals
        fig.add_hline(y=0, line_dash="dash", line_color="gray", row=2, col=2)
        
        # Update layout
        fig.update_layout(
            title=f'Polynomial Analysis (Best Degree: {self.best_degree})',
            height=800,
            showlegend=True
        )
        
        # Update axis labels
        fig.update_xaxes(title_text="X", row=1, col=1)
        fig.update_yaxes(title_text="Y", row=1, col=1)
        fig.update_xaxes(title_text="Degree", row=1, col=2)
        fig.update_yaxes(title_text="CV Score (MSE)", row=1, col=2)
        fig.update_xaxes(title_text="Degree", row=2, col=1)
        fig.update_yaxes(title_text="Coefficients", row=2, col=1)
        fig.update_xaxes(title_text="Predicted", row=2, col=2)
        fig.update_yaxes(title_text="Residuals", row=2, col=2)
        
        return fig
    
    def generate_performance_report(self, X_train, y_train, X_test=None, y_test=None):
        """
        Generate comprehensive performance report.
        
        Parameters:
        -----------
        X_train, y_train : array-like
            Training data
        X_test, y_test : array-like, optional
            Test data for validation
            
        Returns:
        --------
        dict : Performance metrics and statistics
        """
        X_train = np.array(X_train).reshape(-1, 1) if X_train.ndim == 1 else X_train
        
        # Fit the best model
        self.fit_best_model(X_train, y_train)
        
        # Training performance
        y_train_pred = self.best_model.predict(X_train)
        train_mse = mean_squared_error(y_train, y_train_pred)
        train_r2 = r2_score(y_train, y_train_pred)
        
        report = {
            'best_degree': self.best_degree,
            'regularization': self.regularization,
            'alpha': self.alpha,
            'train_mse': train_mse,
            'train_r2': train_r2,
            'cross_validation': self.cv_scores[self.best_degree]
        }
        
        # Test performance if available
        if X_test is not None and y_test is not None:
            X_test = np.array(X_test).reshape(-1, 1) if X_test.ndim == 1 else X_test
            y_test_pred = self.best_model.predict(X_test)
            test_mse = mean_squared_error(y_test, y_test_pred)
            test_r2 = r2_score(y_test, y_test_pred)
            
            report.update({
                'test_mse': test_mse,
                'test_r2': test_r2,
                'generalization_gap': test_mse - train_mse
            })
        
        return report


class FinancialPolynomialAnalyzer(PolynomialAnalyzer):
    """
    Specialized polynomial analyzer for financial time series data.
    
    Features:
    - Stock price trend analysis
    - Volatility modeling
    - Risk metrics calculation
    - Financial performance visualization
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.returns = None
        self.volatility = None
        
    def analyze_price_trend(self, prices, dates=None):
        """
        Analyze stock price trends using polynomial regression.
        
        Parameters:
        -----------
        prices : array-like
            Stock prices
        dates : array-like, optional
            Date information
            
        Returns:
        --------
        dict : Trend analysis results
        """
        prices = np.array(prices)
        X = np.arange(len(prices))  # Use index as time variable
        
        # Fit polynomial model
        self.find_optimal_degree(X, prices)
        self.fit_best_model(X, prices)
        
        # Calculate returns and volatility
        self.returns = np.diff(np.log(prices))
        self.volatility = np.std(self.returns) * np.sqrt(252)  # Annualized
        
        # Generate predictions
        trend_predictions = self.best_model.predict(X.reshape(-1, 1))
        
        # Calculate trend metrics
        trend_direction = 'upward' if trend_predictions[-1] > trend_predictions[0] else 'downward'
        total_return = (prices[-1] - prices[0]) / prices[0]
        
        return {
            'trend_direction': trend_direction,
            'total_return': total_return,
            'annualized_volatility': self.volatility,
            'best_degree': self.best_degree,
            'trend_predictions': trend_predictions,
            'sharpe_ratio': np.mean(self.returns) / np.std(self.returns) * np.sqrt(252)
        }
    
    def plot_financial_analysis(self, prices, dates=None, symbol='Stock'):
        """
        Create comprehensive financial analysis visualization.
        
        Parameters:
        -----------
        prices : array-like
            Stock prices
        dates : array-like, optional
            Date information
        symbol : str
            Stock symbol for labeling
            
        Returns:
        --------
        plotly figure
        """
        prices = np.array(prices)
        X = np.arange(len(prices))
        
        if dates is None:
            dates = pd.date_range(start='2023-01-01', periods=len(prices), freq='D')
        
        # Analyze trend
        trend_analysis = self.analyze_price_trend(prices, dates)
        
        # Create subplots
        fig = make_subplots(
            rows=3, cols=2,
            subplot_titles=(f'{symbol} Price & Trend', 'Returns Distribution',
                          'Volatility Analysis', 'Model Performance',
                          'Risk Metrics', 'Prediction Confidence'),
            specs=[[{"secondary_y": False}, {"secondary_y": False}],
                   [{"secondary_y": False}, {"secondary_y": False}],
                   [{"secondary_y": False}, {"secondary_y": False}]]
        )
        
        # Plot 1: Price and trend
        fig.add_trace(
            go.Scatter(x=dates, y=prices, mode='lines', name='Price',
                      line=dict(color='blue')),
            row=1, col=1
        )
        
        fig.add_trace(
            go.Scatter(x=dates, y=trend_analysis['trend_predictions'],
                      mode='lines', name='Polynomial Trend',
                      line=dict(color='red', dash='dash')),
            row=1, col=1
        )
        
        # Plot 2: Returns distribution
        fig.add_trace(
            go.Histogram(x=self.returns, nbinsx=30, name='Returns',
                        marker=dict(color='green', opacity=0.7)),
            row=1, col=2
        )
        
        # Plot 3: Volatility analysis (rolling)
        if len(prices) > 30:
            rolling_vol = pd.Series(self.returns).rolling(30).std() * np.sqrt(252)
            fig.add_trace(
                go.Scatter(x=dates[1:], y=rolling_vol, mode='lines',
                          name='Rolling Volatility',
                          line=dict(color='orange')),
                row=2, col=1
            )
        
        # Plot 4: Model performance metrics
        degrees = list(self.cv_scores.keys())
        cv_scores = [self.cv_scores[d]['mean'] for d in degrees]
        
        fig.add_trace(
            go.Bar(x=degrees, y=cv_scores, name='CV Scores',
                  marker=dict(color='purple')),
            row=2, col=2
        )
        
        # Plot 5: Risk metrics
        risk_metrics = ['Total Return', 'Volatility', 'Sharpe Ratio']
        risk_values = [
            trend_analysis['total_return'],
            trend_analysis['annualized_volatility'],
            trend_analysis['sharpe_ratio']
        ]
        
        fig.add_trace(
            go.Bar(x=risk_metrics, y=risk_values, name='Risk Metrics',
                  marker=dict(color='red')),
            row=3, col=1
        )
        
        # Plot 6: Prediction confidence
        future_X = np.arange(len(prices), len(prices) + 30)
        future_pred = self.predict_with_confidence(future_X)
        
        future_dates = pd.date_range(start=dates[-1], periods=31, freq='D')[1:]
        
        fig.add_trace(
            go.Scatter(x=future_dates, y=future_pred['predictions'],
                      mode='lines', name='Future Prediction',
                      line=dict(color='green')),
            row=3, col=2
        )
        
        fig.add_trace(
            go.Scatter(
                x=np.concatenate([future_dates, future_dates[::-1]]),
                y=np.concatenate([future_pred['upper_bound'], 
                                future_pred['lower_bound'][::-1]]),
                fill='toself', fillcolor='rgba(0,255,0,0.2)',
                line=dict(color='rgba(255,255,255,0)'),
                name='Confidence Interval'
            ),
            row=3, col=2
        )
        
        # Update layout
        fig.update_layout(
            title=f'{symbol} Financial Analysis - Polynomial Degree {self.best_degree}',
            height=900,
            showlegend=True
        )
        
        return fig


# Example usage and demonstration functions
def demo_basic_polynomial_analysis():
    """Demonstrate basic polynomial analysis capabilities."""
    # Generate sample data
    np.random.seed(42)
    X = np.linspace(0, 10, 100)
    y = 2*X**3 - 15*X**2 + 30*X + 5 + np.random.normal(0, 10, 100)
    
    # Create analyzer
    analyzer = PolynomialAnalyzer(max_degree=8, regularization='ridge', alpha=1.0)
    
    # Find optimal degree
    cv_results = analyzer.find_optimal_degree(X, y)
    print(f"Optimal degree: {analyzer.best_degree}")
    
    # Fit best model
    analyzer.fit_best_model(X, y)
    
    # Generate report
    report = analyzer.generate_performance_report(X, y)
    print("Performance Report:")
    for key, value in report.items():
        print(f"  {key}: {value}")
    
    # Create visualization
    fig = analyzer.plot_model_comparison(X, y)
    fig.show()
    
    return analyzer, fig

def demo_financial_analysis():
    """Demonstrate financial time series analysis."""
    # Generate sample stock price data
    np.random.seed(42)
    days = 252  # One trading year
    dates = pd.date_range(start='2023-01-01', periods=days, freq='D')
    
    # Simulate stock price with trend and noise
    trend = np.linspace(100, 120, days)
    noise = np.cumsum(np.random.normal(0, 2, days))
    prices = trend + noise
    
    # Create financial analyzer
    fin_analyzer = FinancialPolynomialAnalyzer(max_degree=6, regularization='ridge')
    
    # Analyze trend
    trend_analysis = fin_analyzer.analyze_price_trend(prices, dates)
    print("Financial Analysis Results:")
    for key, value in trend_analysis.items():
        if key != 'trend_predictions':
            print(f"  {key}: {value}")
    
    # Create visualization
    fig = fin_analyzer.plot_financial_analysis(prices, dates, 'DEMO')
    fig.show()
    
    return fin_analyzer, fig

if __name__ == "__main__":
    print("🔬 DSKYpoly Data Science Toolkit")
    print("=" * 50)
    print("\nRunning demonstrations...")
    
    print("\n1. Basic Polynomial Analysis Demo")
    analyzer, fig1 = demo_basic_polynomial_analysis()
    
    print("\n2. Financial Analysis Demo")
    fin_analyzer, fig2 = demo_financial_analysis()
    
    print("\nDemonstrations complete! Check the generated plots.")
