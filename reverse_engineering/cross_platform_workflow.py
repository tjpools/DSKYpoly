"""
DSKYpoly Cross-Platform Reverse Engineering Workflow
====================================================

Integrates Windows IDA Pro analysis with Fedora Ghidra analysis to create
a comprehensive reverse engineering workflow for mathematical software.

This module implements the "construction-based understanding" philosophy
by enabling deep analysis of polynomial solver implementations.
"""

import os
import json
import subprocess
from pathlib import Path
from typing import Dict, List, Optional, Any
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from dataclasses import dataclass
from datetime import datetime

@dataclass
class AnalysisSession:
    """Represents a complete analysis session across platforms."""
    binary_name: str
    windows_analysis: Optional[Dict] = None
    linux_analysis: Optional[Dict] = None
    combined_insights: Optional[Dict] = None
    timestamp: str = ""
    
    def __post_init__(self):
        if not self.timestamp:
            self.timestamp = datetime.now().isoformat()

class CrossPlatformAnalyzer:
    """
    Orchestrates reverse engineering analysis across Windows (IDA) and Linux (Ghidra).
    
    Features:
    - Import IDA Pro analysis results from Windows
    - Perform Ghidra analysis on Linux
    - Cross-validate findings between platforms
    - Generate unified reports combining both analyses
    - Educational framework for understanding assembly optimization
    """
    
    def __init__(self, workspace_path=None):
        """
        Initialize cross-platform analyzer.
        
        Parameters:
        -----------
        workspace_path : str
            Path to workspace for analysis results
        """
        self.workspace_path = Path(workspace_path) if workspace_path else Path.cwd()
        self.sessions_path = self.workspace_path / "reverse_engineering" / "sessions"
        self.sessions_path.mkdir(parents=True, exist_ok=True)
        
        # Analysis storage
        self.sessions = {}
        self.comparative_results = {}
        
        # Initialize component analyzers
        from .ghidra_analyzer import GhidraAnalyzer
        self.ghidra_analyzer = GhidraAnalyzer()
        
    def import_ida_analysis(self, binary_name: str, ida_export_path: str) -> Dict[str, Any]:
        """
        Import analysis results from IDA Pro (Windows).
        
        Parameters:
        -----------
        binary_name : str
            Name of the binary that was analyzed
        ida_export_path : str
            Path to IDA analysis export file (JSON/CSV)
            
        Returns:
        --------
        dict : Imported IDA analysis data
        """
        ida_path = Path(ida_export_path)
        if not ida_path.exists():
            raise FileNotFoundError(f"IDA export file not found: {ida_path}")
        
        print(f"📥 Importing IDA analysis for {binary_name}")
        
        try:
            if ida_path.suffix.lower() == '.json':
                with open(ida_path, 'r') as f:
                    ida_data = json.load(f)
            else:
                # Try to parse as structured text export
                ida_data = self._parse_ida_text_export(ida_path)
            
            # Normalize IDA data structure
            normalized_data = self._normalize_ida_data(ida_data)
            
            # Store in session
            if binary_name not in self.sessions:
                self.sessions[binary_name] = AnalysisSession(binary_name)
            
            self.sessions[binary_name].windows_analysis = normalized_data
            
            print(f"✅ IDA analysis imported: {len(normalized_data.get('functions', []))} functions")
            return normalized_data
            
        except Exception as e:
            print(f"❌ Failed to import IDA analysis: {e}")
            raise
    
    def _parse_ida_text_export(self, file_path: Path) -> Dict[str, Any]:
        """Parse IDA text export format."""
        # Placeholder for IDA text parsing
        # This would parse specific IDA export formats
        return {
            'functions': [],
            'imports': [],
            'exports': [],
            'analysis_method': 'ida_pro_import',
            'source_file': str(file_path)
        }
    
    def _normalize_ida_data(self, ida_data: Dict) -> Dict[str, Any]:
        """Normalize IDA data to common format."""
        normalized = {
            'analysis_method': 'ida_pro',
            'platform': 'windows',
            'functions': [],
            'imports': [],
            'exports': [],
            'segments': [],
            'cross_references': [],
            'comments': [],
            'ida_specific': ida_data
        }
        
        # Extract function information if available
        if 'functions' in ida_data:
            for func in ida_data['functions']:
                normalized_func = {
                    'name': func.get('name', 'unknown'),
                    'address': func.get('start_ea', func.get('address', '0')),
                    'size': func.get('size', 0),
                    'instructions': [],
                    'ida_metadata': func
                }
                normalized['functions'].append(normalized_func)
        
        return normalized
    
    def run_ghidra_analysis(self, binary_path: str) -> Dict[str, Any]:
        """
        Run Ghidra analysis on Linux and store results.
        
        Parameters:
        -----------
        binary_path : str
            Path to binary file to analyze
            
        Returns:
        --------
        dict : Ghidra analysis results
        """
        binary_name = Path(binary_path).name
        print(f"🔍 Running Ghidra analysis for {binary_name}")
        
        # Use the Ghidra analyzer
        ghidra_results = self.ghidra_analyzer.analyze_binary(binary_path)
        math_patterns = self.ghidra_analyzer.analyze_mathematical_patterns(binary_name)
        
        # Combine results
        combined_results = {
            **ghidra_results,
            'mathematical_patterns': math_patterns,
            'platform': 'linux',
            'analysis_method': 'ghidra'
        }
        
        # Store in session
        if binary_name not in self.sessions:
            self.sessions[binary_name] = AnalysisSession(binary_name)
        
        self.sessions[binary_name].linux_analysis = combined_results
        
        print(f"✅ Ghidra analysis completed")
        return combined_results
    
    def cross_validate_analysis(self, binary_name: str) -> Dict[str, Any]:
        """
        Cross-validate findings between IDA and Ghidra analyses.
        
        Parameters:
        -----------
        binary_name : str
            Name of binary to cross-validate
            
        Returns:
        --------
        dict : Cross-validation results
        """
        if binary_name not in self.sessions:
            raise ValueError(f"No analysis session found for {binary_name}")
        
        session = self.sessions[binary_name]
        
        if not (session.windows_analysis and session.linux_analysis):
            print("⚠️  Both IDA and Ghidra analyses required for cross-validation")
            return {}
        
        print(f"🔬 Cross-validating analysis for {binary_name}")
        
        validation_results = {
            'binary_name': binary_name,
            'validation_timestamp': datetime.now().isoformat(),
            'function_comparison': {},
            'disagreements': [],
            'consensus_findings': [],
            'confidence_metrics': {},
            'recommendations': []
        }
        
        # Compare function discoveries
        ida_functions = {f['name']: f for f in session.windows_analysis.get('functions', [])}
        ghidra_functions = {f['name']: f for f in session.linux_analysis.get('functions', [])}
        
        # Functions found by both tools
        common_functions = set(ida_functions.keys()) & set(ghidra_functions.keys())
        ida_only = set(ida_functions.keys()) - set(ghidra_functions.keys())
        ghidra_only = set(ghidra_functions.keys()) - set(ida_functions.keys())
        
        validation_results['function_comparison'] = {
            'common_functions': list(common_functions),
            'ida_exclusive': list(ida_only),
            'ghidra_exclusive': list(ghidra_only),
            'total_ida': len(ida_functions),
            'total_ghidra': len(ghidra_functions),
            'agreement_ratio': len(common_functions) / max(len(ida_functions), len(ghidra_functions), 1)
        }
        
        # Analyze disagreements
        if ida_only:
            validation_results['disagreements'].append({
                'type': 'function_detection',
                'description': f'IDA found {len(ida_only)} functions not detected by Ghidra',
                'functions': list(ida_only)[:10],  # Limit for readability
                'impact': 'medium'
            })
        
        if ghidra_only:
            validation_results['disagreements'].append({
                'type': 'function_detection',
                'description': f'Ghidra found {len(ghidra_only)} functions not detected by IDA',
                'functions': list(ghidra_only)[:10],
                'impact': 'medium'
            })
        
        # Mathematical pattern consensus
        ghidra_math = session.linux_analysis.get('mathematical_patterns', {})
        if ghidra_math:
            validation_results['consensus_findings'].append({
                'type': 'mathematical_patterns',
                'description': 'Mathematical operation patterns detected',
                'details': {
                    'floating_point_ops': ghidra_math.get('floating_point_ops', 0),
                    'polynomial_indicators': len(ghidra_math.get('polynomial_indicators', [])),
                    'loop_structures': ghidra_math.get('loop_structures', 0)
                }
            })
        
        # Calculate confidence metrics
        validation_results['confidence_metrics'] = {
            'function_detection_confidence': validation_results['function_comparison']['agreement_ratio'],
            'overall_confidence': self._calculate_overall_confidence(validation_results),
            'analysis_completeness': self._assess_analysis_completeness(session)
        }
        
        # Generate recommendations
        validation_results['recommendations'] = self._generate_analysis_recommendations(validation_results)
        
        # Store combined insights
        session.combined_insights = validation_results
        
        print(f"✅ Cross-validation completed")
        print(f"  Function agreement: {validation_results['function_comparison']['agreement_ratio']:.2%}")
        print(f"  Overall confidence: {validation_results['confidence_metrics']['overall_confidence']:.2%}")
        
        return validation_results
    
    def _calculate_overall_confidence(self, validation_results: Dict) -> float:
        """Calculate overall confidence score for the analysis."""
        function_confidence = validation_results['function_comparison']['agreement_ratio']
        
        # Weight different factors
        weights = {
            'function_agreement': 0.7,
            'disagreement_severity': 0.2,
            'data_completeness': 0.1
        }
        
        # Simple confidence calculation
        disagreement_penalty = len(validation_results['disagreements']) * 0.1
        confidence = function_confidence * weights['function_agreement']
        confidence -= min(disagreement_penalty, 0.3)  # Cap penalty
        
        return max(0.0, min(1.0, confidence))
    
    def _assess_analysis_completeness(self, session: AnalysisSession) -> float:
        """Assess how complete the analysis appears to be."""
        completeness_factors = []
        
        # Check IDA analysis completeness
        if session.windows_analysis:
            ida_functions = len(session.windows_analysis.get('functions', []))
            if ida_functions > 0:
                completeness_factors.append(0.5)
        
        # Check Ghidra analysis completeness
        if session.linux_analysis:
            ghidra_functions = len(session.linux_analysis.get('functions', []))
            if ghidra_functions > 0:
                completeness_factors.append(0.5)
        
        return sum(completeness_factors)
    
    def _generate_analysis_recommendations(self, validation_results: Dict) -> List[str]:
        """Generate recommendations based on validation results."""
        recommendations = []
        
        agreement_ratio = validation_results['function_comparison']['agreement_ratio']
        
        if agreement_ratio < 0.5:
            recommendations.append(
                "Low function detection agreement suggests binary may have anti-analysis features or "
                "one tool may need different analysis settings"
            )
        
        if agreement_ratio > 0.9:
            recommendations.append(
                "High agreement between tools increases confidence in analysis results"
            )
        
        ida_exclusive = len(validation_results['function_comparison']['ida_exclusive'])
        ghidra_exclusive = len(validation_results['function_comparison']['ghidra_exclusive'])
        
        if ida_exclusive > ghidra_exclusive * 2:
            recommendations.append(
                "IDA detected significantly more functions - consider reviewing Ghidra analysis settings"
            )
        elif ghidra_exclusive > ida_exclusive * 2:
            recommendations.append(
                "Ghidra detected significantly more functions - consider reviewing IDA analysis completeness"
            )
        
        recommendations.append(
            "For mathematical software analysis, focus on floating-point operations and loop structures"
        )
        
        return recommendations
    
    def generate_unified_report(self, binary_name: str, output_format="html") -> str:
        """
        Generate unified report combining IDA and Ghidra analyses.
        
        Parameters:
        -----------
        binary_name : str
            Name of binary to generate report for
        output_format : str
            Output format ('html', 'markdown', 'json')
            
        Returns:
        --------
        str : Path to generated report
        """
        if binary_name not in self.sessions:
            raise ValueError(f"No analysis session found for {binary_name}")
        
        session = self.sessions[binary_name]
        
        if output_format == "html":
            return self._generate_unified_html_report(binary_name, session)
        elif output_format == "markdown":
            return self._generate_unified_markdown_report(binary_name, session)
        elif output_format == "json":
            return self._generate_unified_json_report(binary_name, session)
        else:
            raise ValueError(f"Unsupported output format: {output_format}")
    
    def _generate_unified_html_report(self, binary_name: str, session: AnalysisSession) -> str:
        """Generate unified HTML report."""
        html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>DSKYpoly Cross-Platform Analysis Report - {binary_name}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }}
        .header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                  color: white; padding: 30px; border-radius: 15px; text-align: center; }}
        .platform-section {{ margin: 30px 0; padding: 20px; border-radius: 10px; }}
        .ida-section {{ background-color: #e8f4fd; border-left: 5px solid #2196F3; }}
        .ghidra-section {{ background-color: #e8f5e8; border-left: 5px solid #4CAF50; }}
        .validation-section {{ background-color: #fff3e0; border-left: 5px solid #FF9800; }}
        .metric {{ display: inline-block; margin: 10px; padding: 15px; 
                  background-color: white; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
        .agreement-high {{ color: #4CAF50; font-weight: bold; }}
        .agreement-medium {{ color: #FF9800; font-weight: bold; }}
        .agreement-low {{ color: #f44336; font-weight: bold; }}
        table {{ border-collapse: collapse; width: 100%; margin: 15px 0; }}
        th, td {{ border: 1px solid #ddd; padding: 12px; text-align: left; }}
        th {{ background-color: #f8f9fa; font-weight: bold; }}
        .code {{ font-family: 'Courier New', monospace; background-color: #f5f5f5; padding: 3px 6px; }}
        .recommendation {{ background-color: #f0f7ff; padding: 15px; margin: 10px 0; 
                          border-left: 4px solid #007acc; border-radius: 5px; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🔍 Cross-Platform Binary Analysis Report</h1>
        <h2>{binary_name}</h2>
        <p>Comprehensive analysis combining Windows IDA Pro and Linux Ghidra</p>
        <p><em>Session: {session.timestamp}</em></p>
    </div>
"""
        
        # Analysis overview
        ida_available = session.windows_analysis is not None
        ghidra_available = session.linux_analysis is not None
        validation_available = session.combined_insights is not None
        
        html_content += f"""
    <div class="platform-section">
        <h3>📊 Analysis Overview</h3>
        <div class="metric">
            <strong>IDA Pro (Windows)</strong><br>
            Status: {"✅ Available" if ida_available else "❌ Not Available"}
        </div>
        <div class="metric">
            <strong>Ghidra (Linux)</strong><br>
            Status: {"✅ Available" if ghidra_available else "❌ Not Available"}
        </div>
        <div class="metric">
            <strong>Cross-Validation</strong><br>
            Status: {"✅ Complete" if validation_available else "❌ Pending"}
        </div>
    </div>
"""
        
        # IDA Analysis Section
        if ida_available:
            ida_data = session.windows_analysis
            html_content += f"""
    <div class="platform-section ida-section">
        <h3>🪟 IDA Pro Analysis (Windows)</h3>
        <table>
            <tr><th>Metric</th><th>Value</th></tr>
            <tr><td>Analysis Method</td><td>{ida_data.get('analysis_method', 'Unknown')}</td></tr>
            <tr><td>Functions Detected</td><td>{len(ida_data.get('functions', []))}</td></tr>
            <tr><td>Imports</td><td>{len(ida_data.get('imports', []))}</td></tr>
            <tr><td>Exports</td><td>{len(ida_data.get('exports', []))}</td></tr>
        </table>
    </div>
"""
        
        # Ghidra Analysis Section
        if ghidra_available:
            ghidra_data = session.linux_analysis
            math_patterns = ghidra_data.get('mathematical_patterns', {})
            
            html_content += f"""
    <div class="platform-section ghidra-section">
        <h3>🐉 Ghidra Analysis (Linux)</h3>
        <table>
            <tr><th>Metric</th><th>Value</th></tr>
            <tr><td>Analysis Method</td><td>{ghidra_data.get('analysis_method', 'Unknown')}</td></tr>
            <tr><td>Functions Detected</td><td>{len(ghidra_data.get('functions', []))}</td></tr>
            <tr><td>File Size</td><td>{ghidra_data.get('file_size', 0):,} bytes</td></tr>
            <tr><td>Symbols</td><td>{len(ghidra_data.get('symbols', []))}</td></tr>
        </table>
        
        <h4>🧮 Mathematical Pattern Analysis</h4>
        <table>
            <tr><th>Pattern Type</th><th>Count</th></tr>
            <tr><td>Floating Point Operations</td><td>{math_patterns.get('floating_point_ops', 0)}</td></tr>
            <tr><td>Loop Structures</td><td>{math_patterns.get('loop_structures', 0)}</td></tr>
            <tr><td>Function Calls</td><td>{math_patterns.get('function_calls', 0)}</td></tr>
            <tr><td>Polynomial Indicators</td><td>{len(math_patterns.get('polynomial_indicators', []))}</td></tr>
        </table>
    </div>
"""
        
        # Cross-Validation Section
        if validation_available:
            validation = session.combined_insights
            func_comparison = validation.get('function_comparison', {})
            confidence_metrics = validation.get('confidence_metrics', {})
            
            agreement_ratio = func_comparison.get('agreement_ratio', 0)
            agreement_class = ('agreement-high' if agreement_ratio > 0.8 else 
                             'agreement-medium' if agreement_ratio > 0.5 else 'agreement-low')
            
            html_content += f"""
    <div class="platform-section validation-section">
        <h3>🔬 Cross-Platform Validation</h3>
        
        <div class="metric">
            <strong>Function Agreement</strong><br>
            <span class="{agreement_class}">{agreement_ratio:.1%}</span>
        </div>
        <div class="metric">
            <strong>Overall Confidence</strong><br>
            <span class="agreement-medium">{confidence_metrics.get('overall_confidence', 0):.1%}</span>
        </div>
        
        <h4>Function Detection Comparison</h4>
        <table>
            <tr><th>Category</th><th>Count</th><th>Details</th></tr>
            <tr><td>Common Functions</td><td>{len(func_comparison.get('common_functions', []))}</td>
                <td>Functions detected by both IDA and Ghidra</td></tr>
            <tr><td>IDA Exclusive</td><td>{len(func_comparison.get('ida_exclusive', []))}</td>
                <td>Functions only detected by IDA Pro</td></tr>
            <tr><td>Ghidra Exclusive</td><td>{len(func_comparison.get('ghidra_exclusive', []))}</td>
                <td>Functions only detected by Ghidra</td></tr>
        </table>
        
        <h4>📋 Recommendations</h4>
"""
            
            for recommendation in validation.get('recommendations', []):
                html_content += f'<div class="recommendation">💡 {recommendation}</div>'
            
            html_content += "</div>"
        
        # Educational insights
        html_content += f"""
    <div class="platform-section">
        <h3>🎓 Educational Insights</h3>
        <div class="recommendation">
            <strong>Construction-Based Understanding:</strong> This analysis demonstrates how different tools 
            can reveal different aspects of the same binary. IDA Pro excels at interactive analysis and 
            has mature disassembly engines, while Ghidra provides excellent headless automation and 
            open-source flexibility.
        </div>
        <div class="recommendation">
            <strong>Mathematical Software Analysis:</strong> For polynomial solvers like DSKYpoly, 
            focus on floating-point operations, loop structures, and function call patterns that 
            indicate numerical computation algorithms.
        </div>
        <div class="recommendation">
            <strong>Cross-Platform Benefits:</strong> Using both Windows IDA and Linux Ghidra provides 
            redundancy and different perspectives, increasing confidence in analysis results and 
            revealing tool-specific insights.
        </div>
    </div>

    <div style="text-align: center; margin-top: 40px; color: #666;">
        <p><em>Generated by DSKYpoly Cross-Platform Reverse Engineering Toolkit</em></p>
        <p><em>"Understanding through Construction" Philosophy</em></p>
    </div>
</body>
</html>
"""
        
        # Save report
        report_path = self.sessions_path / f"{binary_name}_unified_report.html"
        with open(report_path, 'w') as f:
            f.write(html_content)
        
        return str(report_path)
    
    def _generate_unified_markdown_report(self, binary_name: str, session: AnalysisSession) -> str:
        """Generate unified Markdown report."""
        # Implementation for markdown report
        report_path = self.sessions_path / f"{binary_name}_unified_report.md"
        # ... markdown generation code ...
        return str(report_path)
    
    def _generate_unified_json_report(self, binary_name: str, session: AnalysisSession) -> str:
        """Generate unified JSON report."""
        report_path = self.sessions_path / f"{binary_name}_unified_report.json"
        
        report_data = {
            'binary_name': binary_name,
            'session_timestamp': session.timestamp,
            'windows_analysis': session.windows_analysis,
            'linux_analysis': session.linux_analysis,
            'combined_insights': session.combined_insights
        }
        
        with open(report_path, 'w') as f:
            json.dump(report_data, f, indent=2)
        
        return str(report_path)
    
    def create_analysis_workflow_guide(self) -> str:
        """Create educational guide for cross-platform reverse engineering workflow."""
        guide_content = """
# DSKYpoly Cross-Platform Reverse Engineering Workflow

## Overview
This workflow integrates Windows IDA Pro analysis with Linux Ghidra analysis to provide
comprehensive understanding of mathematical software implementations.

## Prerequisites

### Windows Environment
- Visual Studio 2022 (Community Edition or higher)
- IDA Freeware or IDA Pro
- Git for Windows
- Windows Subsystem for Linux (WSL) optional

### Linux Environment (Fedora)
- Ghidra installation: `sudo dnf install ghidra`
- Development tools: `sudo dnf groupinstall "Development Tools"`
- Python 3 with analysis libraries
- Git

## Workflow Steps

### Phase 1: Windows Analysis with IDA Pro

1. **Binary Preparation**
   ```batch
   # Build DSKYpoly binaries
   cd DSKYpoly
   nmake
   ```

2. **IDA Pro Analysis**
   - Open binary in IDA Pro
   - Perform initial auto-analysis
   - Identify key functions (solve_poly_*, main, etc.)
   - Document function signatures and calling conventions
   - Export analysis results (File → Produce file → Create LST file)

3. **Data Export**
   - Export function list: View → Open subviews → Functions
   - Export cross-references
   - Save IDA database (.idb/.i64)

### Phase 2: Linux Analysis with Ghidra

1. **Environment Setup**
   ```bash
   # Ensure Ghidra is installed
   which ghidra
   
   # Set up Python environment
   cd DSKYpoly/reverse_engineering
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Ghidra Analysis**
   ```python
   from ghidra_analyzer import GhidraAnalyzer
   from cross_platform_workflow import CrossPlatformAnalyzer
   
   # Initialize analyzers
   analyzer = CrossPlatformAnalyzer()
   
   # Analyze with Ghidra
   ghidra_results = analyzer.run_ghidra_analysis("../build/dskypoly")
   ```

3. **Pattern Analysis**
   - Mathematical operation detection
   - Loop structure analysis
   - Function calling patterns
   - Assembly optimization identification

### Phase 3: Cross-Platform Validation

1. **Import IDA Results**
   ```python
   # Import IDA analysis from Windows
   ida_results = analyzer.import_ida_analysis(
       "dskypoly", 
       "/path/to/ida/export.json"
   )
   ```

2. **Cross-Validation**
   ```python
   # Perform cross-validation
   validation = analyzer.cross_validate_analysis("dskypoly")
   
   # Generate unified report
   report_path = analyzer.generate_unified_report("dskypoly", "html")
   ```

3. **Analysis Integration**
   - Compare function detection between tools
   - Validate mathematical pattern identification
   - Assess analysis confidence
   - Generate recommendations

## Educational Objectives

### Understanding Assembly Optimization
- Compare different compiler optimizations
- Identify mathematical computation patterns
- Understand calling conventions across platforms

### Tool Capabilities
- Learn IDA Pro's interactive analysis strengths
- Understand Ghidra's automated analysis capabilities
- Compare disassembly engines and analysis accuracy

### Mathematical Software Analysis
- Polynomial evaluation algorithm identification
- Numerical computation pattern recognition
- Performance optimization analysis

## Best Practices

### Data Management
- Keep analysis sessions organized by binary and timestamp
- Export IDA databases before major changes
- Version control analysis scripts and results

### Analysis Validation
- Always cross-validate between multiple tools
- Document disagreements and investigate causes
- Maintain confidence metrics for analysis quality

### Educational Documentation
- Document learning objectives for each analysis
- Create comparative studies between different binaries
- Build knowledge base of mathematical software patterns

## Advanced Techniques

### Differential Analysis
- Compare optimized vs. unoptimized builds
- Analyze different polynomial degree implementations
- Study cross-platform compilation differences

### Pattern Recognition
- Build signature databases for mathematical operations
- Create automated pattern detection systems
- Develop educational exercises based on findings

## Troubleshooting

### Common Issues
- IDA analysis incomplete: Check auto-analysis settings
- Ghidra headless failures: Verify installation and permissions
- Cross-validation low agreement: Review analysis parameters

### Performance Optimization
- Use targeted analysis for large binaries
- Cache analysis results for repeated studies
- Optimize report generation for large datasets

## Conclusion
This workflow embodies the "construction-based understanding" philosophy by providing
hands-on experience with professional reverse engineering tools while building deep
understanding of mathematical software implementation.
"""
        
        guide_path = self.sessions_path / "cross_platform_workflow_guide.md"
        with open(guide_path, 'w') as f:
            f.write(guide_content)
        
        return str(guide_path)


def demo_cross_platform_workflow():
    """Demonstrate cross-platform reverse engineering workflow."""
    print("🔍 DSKYpoly Cross-Platform Reverse Engineering Workflow Demo")
    print("=" * 70)
    
    # Initialize analyzer
    analyzer = CrossPlatformAnalyzer()
    
    # Create workflow guide
    guide_path = analyzer.create_analysis_workflow_guide()
    print(f"📚 Workflow guide created: {guide_path}")
    
    # Find available binaries
    binary_paths = []
    search_paths = [
        Path.cwd() / "build",
        Path.cwd() / "cubic" / "build", 
        Path.cwd() / "quartic" / "build",
        Path.cwd() / "quintic" / "build"
    ]
    
    for search_path in search_paths:
        if search_path.exists():
            for binary in search_path.glob("dskypoly*"):
                if binary.is_file() and binary.stat().st_size > 0:
                    binary_paths.append(binary)
    
    if not binary_paths:
        print("⚠️  No DSKYpoly binaries found for demonstration")
        print("💡 Build some binaries first with: make")
        return analyzer
    
    # Demonstrate with first available binary
    test_binary = binary_paths[0]
    binary_name = test_binary.name
    
    print(f"\n🔬 Demonstrating workflow with: {binary_name}")
    
    try:
        # Run Ghidra analysis (Linux side)
        print("🐉 Running Ghidra analysis...")
        ghidra_results = analyzer.run_ghidra_analysis(str(test_binary))
        
        # Simulate IDA import (would normally come from Windows)
        print("📥 Simulating IDA analysis import...")
        mock_ida_data = {
            'functions': [
                {'name': 'main', 'start_ea': '0x1000', 'size': 100},
                {'name': 'solve_poly_2', 'start_ea': '0x1100', 'size': 200},
                {'name': '_start', 'start_ea': '0x1200', 'size': 50}
            ],
            'analysis_method': 'ida_pro_mock'
        }
        
        # Create temporary IDA export file for demo
        import tempfile
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump(mock_ida_data, f)
            temp_ida_file = f.name
        
        try:
            analyzer.import_ida_analysis(binary_name, temp_ida_file)
            
            # Perform cross-validation
            print("🔬 Performing cross-validation...")
            validation_results = analyzer.cross_validate_analysis(binary_name)
            
            # Generate unified report
            print("📄 Generating unified report...")
            report_path = analyzer.generate_unified_report(binary_name, "html")
            
            print(f"\n✅ Demo completed successfully!")
            print(f"📊 Unified report: {report_path}")
            print(f"📚 Workflow guide: {guide_path}")
            print(f"🎯 Function agreement: {validation_results['function_comparison']['agreement_ratio']:.1%}")
            
        finally:
            # Clean up temporary file
            os.unlink(temp_ida_file)
            
    except Exception as e:
        print(f"❌ Demo failed: {e}")
        import traceback
        traceback.print_exc()
    
    return analyzer

if __name__ == "__main__":
    demo_cross_platform_workflow()
