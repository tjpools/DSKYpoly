#!/bin/bash

echo "========================================"
echo "DSKYpoly Anaconda Environment Setup"
echo "========================================"
echo ""

echo "Creating conda environment from environment.yml..."
conda env create -f environment.yml

echo ""
echo "Activating environment..."
conda activate dskypoly

echo ""
echo "Installing additional Jupyter extensions..."
jupyter contrib nbextension install --user
jupyter nbextension enable --py widgetsnbextension

echo ""
echo "Testing installation..."
python -c "import numpy, scipy, sympy, matplotlib, plotly, mpmath; print('All packages imported successfully!')"

echo ""
echo "========================================"
echo "Setup Complete!"
echo "========================================"
echo ""
echo "To start Jupyter Lab:"
echo "  conda activate dskypoly"
echo "  jupyter lab"
echo ""
echo "To start Jupyter Notebook:"
echo "  conda activate dskypoly"
echo "  jupyter notebook"
echo ""
echo "Navigate to the notebooks/ directory to explore quintic polynomials!"
echo ""
