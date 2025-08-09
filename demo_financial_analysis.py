#!/usr/bin/env python3
"""
DSKYpoly Financial Data Science Demo
===================================

Quick demonstration of financial analysis capabilities using
real market data with polynomial trend analysis.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime, timedelta
import sys
import os

# Add the data science module to the path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'data_science'))

try:
    from polynomial_toolkit import FinancialPolynomialAnalyzer
    print("✅ DSKYpoly Financial Toolkit imported successfully")
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Make sure you're running from the DSKYpoly root directory")
    sys.exit(1)

def fetch_stock_data(symbol, period='1y'):
    """Fetch real stock data using yfinance."""
    try:
        ticker = yf.Ticker(symbol)
        data = ticker.history(period=period)
        return data['Close'].values, data.index
    except Exception as e:
        print(f"⚠️  Could not fetch {symbol} data: {e}")
        return None, None

def generate_demo_data():
    """Generate synthetic stock data if real data unavailable."""
    print("📊 Generating synthetic stock data for demonstration...")
    
    np.random.seed(42)
    n_days = 252  # One trading year
    dates = pd.date_range(start='2023-01-01', periods=n_days, freq='D')
    
    # Realistic stock price simulation
    base_price = 100
    drift = 0.0001  # Daily drift
    volatility = 0.02  # Daily volatility
    
    returns = np.random.normal(drift, volatility, n_days)
    prices = base_price * np.exp(np.cumsum(returns))
    
    # Add some trending behavior
    trend = np.linspace(0, 20, n_days)
    prices += trend
    
    return prices, dates

def analyze_stock(symbol='AAPL'):
    """Perform comprehensive stock analysis."""
    print(f"\n🔍 Analyzing {symbol} with DSKYpoly Financial Toolkit")
    print("=" * 60)
    
    # Try to fetch real data first
    prices, dates = fetch_stock_data(symbol, period='1y')
    
    if prices is None:
        print("Using synthetic data for demonstration...")
        prices, dates = generate_demo_data()
        symbol = 'DEMO'
    else:
        print(f"✅ Fetched {len(prices)} days of {symbol} data")
    
    # Create financial analyzer
    analyzer = FinancialPolynomialAnalyzer(
        max_degree=8, 
        regularization='ridge', 
        alpha=0.1
    )
    
    # Perform analysis
    print(f"\n📈 Performing polynomial trend analysis...")
    trend_analysis = analyzer.analyze_price_trend(prices, dates)
    
    # Display results
    print(f"\n🎯 Analysis Results for {symbol}:")
    print(f"  📊 Price Range: ${prices.min():.2f} - ${prices.max():.2f}")
    print(f"  📈 Trend Direction: {trend_analysis['trend_direction'].title()}")
    print(f"  💰 Total Return: {trend_analysis['total_return']*100:.2f}%")
    print(f"  📊 Annualized Volatility: {trend_analysis['annualized_volatility']*100:.2f}%")
    print(f"  📈 Sharpe Ratio: {trend_analysis['sharpe_ratio']:.3f}")
    print(f"  🔢 Optimal Polynomial Degree: {trend_analysis['best_degree']}")
    
    # Risk assessment
    vol = trend_analysis['annualized_volatility']
    if vol < 0.15:
        risk_level = "Low"
    elif vol < 0.25:
        risk_level = "Moderate"
    else:
        risk_level = "High"
    
    print(f"  ⚠️  Risk Level: {risk_level}")
    
    # Future price prediction
    print(f"\n🔮 Generating future price predictions...")
    future_days = 30
    X_current = np.arange(len(prices))
    X_future = np.arange(len(prices), len(prices) + future_days)
    
    # Get current model predictions
    analyzer.fit_best_model(X_current, prices)
    future_pred = analyzer.predict_with_confidence(X_future)
    
    current_price = prices[-1]
    predicted_price = future_pred['predictions'][-1]
    price_change = (predicted_price - current_price) / current_price * 100
    
    print(f"  📅 Current Price: ${current_price:.2f}")
    print(f"  📅 30-day Prediction: ${predicted_price:.2f}")
    print(f"  📊 Expected Change: {price_change:+.2f}%")
    print(f"  📊 Confidence Range: ${future_pred['lower_bound'][-1]:.2f} - ${future_pred['upper_bound'][-1]:.2f}")
    
    # Create a simple matplotlib visualization
    create_simple_plot(dates, prices, trend_analysis, symbol)
    
    return analyzer, trend_analysis

def create_simple_plot(dates, prices, trend_analysis, symbol):
    """Create a simple matplotlib plot of the analysis."""
    plt.figure(figsize=(12, 8))
    
    # Main price plot
    plt.subplot(2, 2, 1)
    plt.plot(dates, prices, 'b-', alpha=0.7, label='Price')
    plt.plot(dates, trend_analysis['trend_predictions'], 'r--', linewidth=2, label='Polynomial Trend')
    plt.title(f'{symbol} Price & Polynomial Trend')
    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Returns distribution
    plt.subplot(2, 2, 2)
    returns = np.diff(np.log(prices))
    plt.hist(returns, bins=30, alpha=0.7, color='green', edgecolor='black')
    plt.title('Daily Returns Distribution')
    plt.xlabel('Log Returns')
    plt.ylabel('Frequency')
    plt.grid(True, alpha=0.3)
    
    # Cumulative returns
    plt.subplot(2, 2, 3)
    cumulative_returns = np.cumprod(1 + returns) - 1
    plt.plot(dates[1:], cumulative_returns * 100, 'purple', linewidth=2)
    plt.title('Cumulative Returns')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Return (%)')
    plt.grid(True, alpha=0.3)
    
    # Risk metrics
    plt.subplot(2, 2, 4)
    metrics = ['Total Return', 'Volatility', 'Sharpe Ratio']
    values = [
        trend_analysis['total_return'] * 100,
        trend_analysis['annualized_volatility'] * 100,
        trend_analysis['sharpe_ratio']
    ]
    colors = ['green' if v > 0 else 'red' for v in values]
    plt.bar(metrics, values, color=colors, alpha=0.7)
    plt.title('Risk Metrics')
    plt.ylabel('Value')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f'DSKYpoly_{symbol}_analysis.png', dpi=150, bbox_inches='tight')
    print(f"📊 Chart saved as 'DSKYpoly_{symbol}_analysis.png'")
    
    # Show plot if in interactive environment
    try:
        plt.show()
    except:
        print("📊 Plot created (display may not be available in this environment)")

def main():
    """Main demonstration function."""
    print("🚀 DSKYpoly Financial Data Science Demo")
    print("=" * 50)
    print("Leveraging polynomial mathematics for financial analysis")
    
    # List of stocks to analyze
    stocks = ['AAPL', 'GOOGL', 'MSFT', 'TSLA']
    
    print(f"\nAvailable stocks for analysis: {', '.join(stocks)}")
    print("Note: Will use synthetic data if real data unavailable")
    
    # Analyze one stock in detail
    analyzer, results = analyze_stock('AAPL')
    
    print(f"\n🎉 Analysis Complete!")
    print(f"📊 DSKYpoly successfully applied polynomial mathematics")
    print(f"   to financial time series analysis!")
    
    print(f"\n🔬 Technical Details:")
    print(f"  • Used {results['best_degree']}-degree polynomial for trend modeling")
    print(f"  • Applied Ridge regularization for overfitting prevention")
    print(f"  • Cross-validation for optimal model selection")
    print(f"  • Statistical confidence intervals for predictions")
    
    print(f"\n🎯 This demonstrates how DSKYpoly's mathematical foundation")
    print(f"   can power sophisticated data science applications!")

if __name__ == "__main__":
    main()
