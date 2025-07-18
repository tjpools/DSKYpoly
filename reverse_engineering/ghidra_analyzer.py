"""
DSKYpoly Reverse Engineering Toolkit
====================================

Advanced binary analysis and reverse engineering tools specifically designed
for mathematical software analysis, with focus on polynomial solvers and
numerical computation algorithms.

This module bridges the gap between high-level mathematical concepts and
low-level assembly implementation analysis.
"""

import os
import sys
import subprocess
import json
import re
import struct
from pathlib import Path
import tempfile
import hashlib
from typing import Dict, List, Optional, Tuple, Any
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

class GhidraAnalyzer:
    """
    Wrapper for Ghidra headless analysis with focus on mathematical software.
    
    Features:
    - Automated binary analysis with Ghidra
    - Function extraction and signature analysis
    - Assembly pattern recognition for mathematical operations
    - Cross-reference analysis for polynomial solvers
    - Performance characteristic analysis
    """
    
    def __init__(self, ghidra_path="/opt/ghidra", project_path=None):
        """
        Initialize Ghidra analyzer.
        
        Parameters:
        -----------
        ghidra_path : str
            Path to Ghidra installation
        project_path : str
            Path for Ghidra project files
        """
        self.ghidra_path = Path(ghidra_path)
        self.project_path = Path(project_path) if project_path else Path.cwd() / "ghidra_projects"
        self.project_path.mkdir(exist_ok=True)
        
        # Check if Ghidra is available
        self.ghidra_available = self._check_ghidra_installation()
        
        # Analysis results storage
        self.analysis_results = {}
        self.function_signatures = {}
        self.assembly_patterns = {}
        
    def _check_ghidra_installation(self) -> bool:
        """Check if Ghidra is properly installed and accessible."""
        # Check for Flatpak Ghidra first
        try:
            result = subprocess.run(["flatpak", "list", "--app"], capture_output=True, text=True)
            if result.returncode == 0 and "org.ghidra_sre.Ghidra" in result.stdout:
                # Set up Flatpak command
                self.ghidra_headless = "flatpak_ghidra"
                print("✅ Found Ghidra Flatpak installation")
                return True
        except:
            pass
        
        # Check traditional installation paths
        possible_paths = [
            self.ghidra_path / "support" / "analyzeHeadless",
            Path("/usr/bin/ghidra"),
            Path("/opt/ghidra/support/analyzeHeadless"),
            Path("/usr/share/ghidra/support/analyzeHeadless")
        ]
        
        for path in possible_paths:
            if path.exists():
                self.ghidra_headless = path
                
                return True
        
        # Try to find ghidra in PATH
        try:
            result = subprocess.run(["which", "ghidra"], capture_output=True, text=True)
            if result.returncode == 0:
                ghidra_bin = Path(result.stdout.strip())
                self.ghidra_headless = ghidra_bin.parent / "support" / "analyzeHeadless"
                if self.ghidra_headless.exists():
                    return True
        except:
            pass
        
        print("⚠️  Ghidra not found. Install with: sudo dnf install ghidra or flatpak install flathub org.ghidra_sre.Ghidra")
        return False
    
    def analyze_binary(self, binary_path: str, output_format="json") -> Dict[str, Any]:
        """
        Perform comprehensive binary analysis using Ghidra.
        
        Parameters:
        -----------
        binary_path : str
            Path to binary file to analyze
        output_format : str
            Output format ('json', 'xml', 'csv')
            
        Returns:
        --------
        dict : Analysis results
        """
        binary_path = Path(binary_path)
        if not binary_path.exists():
            raise FileNotFoundError(f"Binary not found: {binary_path}")
        
        print(f"🔍 Analyzing binary: {binary_path.name}")
        
        # Create unique project name
        binary_hash = self._calculate_file_hash(binary_path)
        project_name = f"dskypoly_{binary_path.stem}_{binary_hash[:8]}"
        
        # Prepare analysis
        analysis_result = {
            'binary_path': str(binary_path),
            'binary_name': binary_path.name,
            'file_hash': binary_hash,
            'file_size': binary_path.stat().st_size,
            'analysis_timestamp': None,
            'functions': [],
            'imports': [],
            'exports': [],
            'strings': [],
            'assembly_patterns': {},
            'mathematical_indicators': {}
        }
        
        if self.ghidra_available:
            analysis_result = self._run_ghidra_analysis(binary_path, project_name, analysis_result)
        else:
            analysis_result = self._fallback_analysis(binary_path, analysis_result)
        
        # Store results
        self.analysis_results[binary_path.name] = analysis_result
        
        return analysis_result
    
    def _run_ghidra_analysis(self, binary_path: Path, project_name: str, analysis_result: Dict) -> Dict:
        """Run Ghidra headless analysis."""
        # Create Ghidra project command
        if str(self.ghidra_headless) == "flatpak_ghidra":
            # Use Flatpak command for Ghidra
            cmd = [
                "flatpak", "run", "org.ghidra_sre.Ghidra",
                "--headless",
                str(self.project_path),
                project_name,
                "-import", str(binary_path),
                "-postScript", "ListFunctionsScript.java",
                "-deleteProject"  # Clean up after analysis
            ]
        else:
            # Use traditional Ghidra installation
            cmd = [
                str(self.ghidra_headless),
                str(self.project_path),
                project_name,
                "-import", str(binary_path),
                "-postScript", "ListFunctionsScript.java",
                "-deleteProject"  # Clean up after analysis
            ]
        
        print(f"🔧 Running Ghidra analysis...")
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            
            if result.returncode == 0:
                analysis_result = self._parse_ghidra_output(result.stdout, analysis_result)
                analysis_result['analysis_method'] = 'ghidra_headless'
                print(f"✅ Ghidra analysis completed successfully")
                return analysis_result
            else:
                print(f"⚠️  Ghidra analysis failed (exit code {result.returncode}), using fallback method")
                
        except subprocess.TimeoutExpired:
            print(f"⚠️  Ghidra analysis timed out after 300 seconds, using fallback method")
        except Exception as e:
            print(f"⚠️  Ghidra analysis error: {e}, using fallback method")
        
        # Single fallback call for all failure cases
        return self._fallback_analysis(binary_path, analysis_result)
    
    def _fallback_analysis(self, binary_path: Path, analysis_result: Dict) -> Dict:
        """Fallback analysis using basic Unix tools."""
        print(f"🔧 Running fallback analysis with Unix tools...")
        
        try:
            # Use objdump for disassembly with Intel syntax
            objdump_result = subprocess.run(
                ["objdump", "-d", "-M", "intel", str(binary_path)], 
                capture_output=True, text=True
            )
            if objdump_result.returncode == 0:
                analysis_result['disassembly'] = objdump_result.stdout
                analysis_result = self._parse_objdump_output(objdump_result.stdout, analysis_result)
            
            # Use nm for symbols
            nm_result = subprocess.run(
                ["nm", "-D", str(binary_path)], 
                capture_output=True, text=True
            )
            if nm_result.returncode == 0:
                analysis_result = self._parse_nm_output(nm_result.stdout, analysis_result)
            
            # Use strings for string analysis
            strings_result = subprocess.run(
                ["strings", str(binary_path)], 
                capture_output=True, text=True
            )
            if strings_result.returncode == 0:
                analysis_result['strings'] = strings_result.stdout.split('\n')[:100]  # Limit output
            
            # Use file command for basic info
            file_result = subprocess.run(
                ["file", str(binary_path)], 
                capture_output=True, text=True
            )
            if file_result.returncode == 0:
                analysis_result['file_type'] = file_result.stdout.strip()
            
            analysis_result['analysis_method'] = 'unix_tools_fallback'
            print(f"✅ Fallback analysis completed")
            
        except Exception as e:
            print(f"❌ Fallback analysis failed: {e}")
            analysis_result['analysis_method'] = 'basic_only'
            analysis_result['error'] = str(e)
        
        return analysis_result
    
    def _parse_objdump_output(self, objdump_output: str, analysis_result: Dict) -> Dict:
        """Parse objdump output to extract function information."""
        functions = []
        current_function = None
        
        for line in objdump_output.split('\n'):
            # Look for function start (address followed by <function_name>:)
            func_match = re.match(r'^([0-9a-f]+)\s+<(.+?)>:', line)
            if func_match:
                if current_function:
                    functions.append(current_function)
                
                current_function = {
                    'address': func_match.group(1),
                    'name': func_match.group(2),
                    'instructions': [],
                    'size_estimate': 0
                }
            
            # Look for instructions
            inst_match = re.match(r'^\s+([0-9a-f]+):\s+([0-9a-f\s]+)\s+(.+)', line)
            if inst_match and current_function:
                instruction = {
                    'address': inst_match.group(1),
                    'bytes': inst_match.group(2).strip(),
                    'assembly': inst_match.group(3)
                }
                current_function['instructions'].append(instruction)
                current_function['size_estimate'] += 1
        
        if current_function:
            functions.append(current_function)
        
        analysis_result['functions'] = functions
        return analysis_result
    
    def _parse_nm_output(self, nm_output: str, analysis_result: Dict) -> Dict:
        """Parse nm output to extract symbol information."""
        symbols = []
        
        for line in nm_output.split('\n'):
            if line.strip():
                parts = line.split()
                if len(parts) >= 3:
                    symbol = {
                        'address': parts[0] if parts[0] != 'U' else 'undefined',
                        'type': parts[1],
                        'name': ' '.join(parts[2:])
                    }
                    symbols.append(symbol)
        
        analysis_result['symbols'] = symbols
        return analysis_result
    
    def _parse_ghidra_output(self, ghidra_output: str, analysis_result: Dict) -> Dict:
        """Parse Ghidra analysis output."""
        # This would parse actual Ghidra script output
        # For now, we'll add placeholder parsing
        analysis_result['ghidra_raw_output'] = ghidra_output
        return analysis_result
    
    def _calculate_file_hash(self, file_path: Path) -> str:
        """Calculate SHA256 hash of file."""
        hash_sha256 = hashlib.sha256()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_sha256.update(chunk)
        return hash_sha256.hexdigest()
    
    def analyze_mathematical_patterns(self, binary_name: str) -> Dict[str, Any]:
        """
        Analyze assembly patterns that indicate mathematical operations.
        
        Parameters:
        -----------
        binary_name : str
            Name of previously analyzed binary
            
        Returns:
        --------
        dict : Mathematical pattern analysis
        """
        if binary_name not in self.analysis_results:
            raise ValueError(f"Binary {binary_name} not yet analyzed")
        
        analysis = self.analysis_results[binary_name]
        math_patterns = {
            'floating_point_ops': 0,
            'polynomial_indicators': [],
            'loop_structures': 0,
            'function_calls': 0,
            'memory_patterns': [],
            'optimization_indicators': []
        }
        
        # Analyze functions for mathematical patterns
        for func in analysis.get('functions', []):
            math_patterns = self._analyze_function_math_patterns(func, math_patterns)
        
        analysis['mathematical_patterns'] = math_patterns
        return math_patterns
    
    def _analyze_function_math_patterns(self, function: Dict, math_patterns: Dict) -> Dict:
        """Analyze a single function for mathematical patterns."""
        func_name = function.get('name', '')
        instructions = function.get('instructions', [])
        
        # Check for polynomial-related function names
        polynomial_indicators = [
            'poly', 'eval', 'root', 'solve', 'newton', 'horner',
            'coefficient', 'degree', 'cubic', 'quartic', 'quintic'
        ]
        
        for indicator in polynomial_indicators:
            if indicator.lower() in func_name.lower():
                math_patterns['polynomial_indicators'].append({
                    'function': func_name,
                    'indicator': indicator,
                    'confidence': 0.8
                })
        
        # Analyze instructions for mathematical operations
        for inst in instructions:
            assembly = inst.get('assembly', '').lower()
            
            # Floating point operations
            fp_ops = ['fmul', 'fadd', 'fsub', 'fdiv', 'fld', 'fst', 'movss', 'movsd', 'mulss', 'addss']
            for op in fp_ops:
                if op in assembly:
                    math_patterns['floating_point_ops'] += 1
            
            # Loop indicators
            if any(op in assembly for op in ['loop', 'jmp', 'je', 'jne', 'jl', 'jg']):
                math_patterns['loop_structures'] += 1
            
            # Function calls
            if 'call' in assembly:
                math_patterns['function_calls'] += 1
        
        return math_patterns
    
    def compare_binaries(self, binary_names: List[str]) -> Dict[str, Any]:
        """
        Compare multiple analyzed binaries for similarities and differences.
        
        Parameters:
        -----------
        binary_names : list
            Names of binaries to compare
            
        Returns:
        --------
        dict : Comparison results
        """
        comparison = {
            'binaries': binary_names,
            'function_overlap': {},
            'size_comparison': {},
            'pattern_comparison': {},
            'similarity_score': 0.0
        }
        
        # Compare function names and patterns
        all_functions = {}
        for binary in binary_names:
            if binary in self.analysis_results:
                analysis = self.analysis_results[binary]
                functions = [f.get('name', '') for f in analysis.get('functions', [])]
                all_functions[binary] = set(functions)
                
                comparison['size_comparison'][binary] = {
                    'file_size': analysis.get('file_size', 0),
                    'function_count': len(functions)
                }
        
        # Calculate function overlap
        if len(all_functions) >= 2:
            binaries = list(all_functions.keys())
            for i, binary1 in enumerate(binaries):
                for binary2 in binaries[i+1:]:
                    overlap = all_functions[binary1] & all_functions[binary2]
                    total = all_functions[binary1] | all_functions[binary2]
                    similarity = len(overlap) / len(total) if total else 0
                    
                    comparison['function_overlap'][f"{binary1}_vs_{binary2}"] = {
                        'common_functions': list(overlap),
                        'similarity_ratio': similarity,
                        'unique_to_first': list(all_functions[binary1] - all_functions[binary2]),
                        'unique_to_second': list(all_functions[binary2] - all_functions[binary1])
                    }
        
        return comparison
    
    def generate_analysis_report(self, binary_name: str, output_format="html") -> str:
        """
        Generate comprehensive analysis report.
        
        Parameters:
        -----------
        binary_name : str
            Name of analyzed binary
        output_format : str
            Output format ('html', 'markdown', 'json')
            
        Returns:
        --------
        str : Path to generated report
        """
        if binary_name not in self.analysis_results:
            raise ValueError(f"Binary {binary_name} not yet analyzed")
        
        analysis = self.analysis_results[binary_name]
        
        if output_format == "html":
            return self._generate_html_report(binary_name, analysis)
        elif output_format == "markdown":
            return self._generate_markdown_report(binary_name, analysis)
        elif output_format == "json":
            return self._generate_json_report(binary_name, analysis)
        else:
            raise ValueError(f"Unsupported output format: {output_format}")
    
    def _generate_html_report(self, binary_name: str, analysis: Dict) -> str:
        """Generate HTML analysis report."""
        html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>DSKYpoly Binary Analysis Report - {binary_name}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; }}
        .header {{ background-color: #f0f8ff; padding: 20px; border-radius: 10px; }}
        .section {{ margin: 20px 0; padding: 15px; border-left: 3px solid #007acc; }}
        .function {{ background-color: #f9f9f9; margin: 10px 0; padding: 10px; }}
        .code {{ font-family: monospace; background-color: #f5f5f5; padding: 5px; }}
        table {{ border-collapse: collapse; width: 100%; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #f2f2f2; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🔍 DSKYpoly Binary Analysis Report</h1>
        <h2>{binary_name}</h2>
        <p><strong>Analysis Method:</strong> {analysis.get('analysis_method', 'unknown')}</p>
        <p><strong>File Size:</strong> {analysis.get('file_size', 0):,} bytes</p>
        <p><strong>File Hash:</strong> {analysis.get('file_hash', 'unknown')[:16]}...</p>
    </div>
    
    <div class="section">
        <h3>📊 Overview</h3>
        <table>
            <tr><th>Metric</th><th>Value</th></tr>
            <tr><td>Functions Found</td><td>{len(analysis.get('functions', []))}</td></tr>
            <tr><td>Symbols</td><td>{len(analysis.get('symbols', []))}</td></tr>
            <tr><td>Strings</td><td>{len(analysis.get('strings', []))}</td></tr>
        </table>
    </div>
    
    <div class="section">
        <h3>🔧 Functions</h3>
"""
        
        for func in analysis.get('functions', [])[:10]:  # Limit to first 10 functions
            html_content += f"""
        <div class="function">
            <h4>{func.get('name', 'unnamed')}</h4>
            <p><strong>Address:</strong> <span class="code">0x{func.get('address', 'unknown')}</span></p>
            <p><strong>Instructions:</strong> {func.get('size_estimate', 0)}</p>
        </div>
"""
        
        # Mathematical patterns section
        math_patterns = analysis.get('mathematical_patterns', {})
        if math_patterns:
            html_content += f"""
    </div>
    
    <div class="section">
        <h3>🧮 Mathematical Analysis</h3>
        <table>
            <tr><th>Pattern</th><th>Count/Details</th></tr>
            <tr><td>Floating Point Operations</td><td>{math_patterns.get('floating_point_ops', 0)}</td></tr>
            <tr><td>Loop Structures</td><td>{math_patterns.get('loop_structures', 0)}</td></tr>
            <tr><td>Function Calls</td><td>{math_patterns.get('function_calls', 0)}</td></tr>
            <tr><td>Polynomial Indicators</td><td>{len(math_patterns.get('polynomial_indicators', []))}</td></tr>
        </table>
    </div>
"""
        
        html_content += """
</body>
</html>
"""
        
        # Save report
        report_path = f"reverse_engineering/{binary_name}_analysis_report.html"
        with open(report_path, 'w') as f:
            f.write(html_content)
        
        return report_path
    
    def _generate_markdown_report(self, binary_name: str, analysis: Dict) -> str:
        """Generate Markdown analysis report."""
        # Implementation for markdown report
        report_path = f"reverse_engineering/{binary_name}_analysis_report.md"
        # ... markdown generation code ...
        return report_path
    
    def _generate_json_report(self, binary_name: str, analysis: Dict) -> str:
        """Generate JSON analysis report."""
        report_path = f"reverse_engineering/{binary_name}_analysis_report.json"
        with open(report_path, 'w') as f:
            json.dump(analysis, f, indent=2)
        return report_path
    
    def visualize_analysis(self, binary_name: str) -> go.Figure:
        """
        Create interactive visualization of binary analysis results.
        
        Parameters:
        -----------
        binary_name : str
            Name of analyzed binary
            
        Returns:
        --------
        plotly.graph_objects.Figure : Interactive visualization
        """
        if binary_name not in self.analysis_results:
            raise ValueError(f"Binary {binary_name} not yet analyzed")
        
        analysis = self.analysis_results[binary_name]
        
        # Create subplots
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Function Size Distribution', 'Mathematical Patterns',
                          'Memory Layout', 'Assembly Instruction Types'),
            specs=[[{"secondary_y": False}, {"secondary_y": False}],
                   [{"secondary_y": False}, {"secondary_y": False}]]
        )
        
        # Plot 1: Function size distribution
        functions = analysis.get('functions', [])
        if functions:
            sizes = [f.get('size_estimate', 0) for f in functions]
            fig.add_trace(
                go.Histogram(x=sizes, nbinsx=20, name='Function Sizes',
                           marker=dict(color='blue', opacity=0.7)),
                row=1, col=1
            )
        
        # Plot 2: Mathematical patterns
        math_patterns = analysis.get('mathematical_patterns', {})
        if math_patterns:
            pattern_names = ['FP Ops', 'Loops', 'Calls']
            pattern_values = [
                math_patterns.get('floating_point_ops', 0),
                math_patterns.get('loop_structures', 0),
                math_patterns.get('function_calls', 0)
            ]
            
            fig.add_trace(
                go.Bar(x=pattern_names, y=pattern_values, name='Math Patterns',
                      marker=dict(color='green')),
                row=1, col=2
            )
        
        # Plot 3: Function addresses (memory layout approximation)
        if functions:
            addresses = []
            names = []
            for f in functions:
                try:
                    addr = int(f.get('address', '0'), 16)
                    addresses.append(addr)
                    names.append(f.get('name', 'unknown')[:20])  # Truncate long names
                except:
                    continue
            
            if addresses:
                fig.add_trace(
                    go.Scatter(x=addresses, y=list(range(len(addresses))),
                             mode='markers', name='Function Addresses',
                             text=names, marker=dict(color='red', size=8)),
                    row=2, col=1
                )
        
        # Plot 4: Instruction type analysis (simplified)
        if functions:
            instruction_types = {'mov': 0, 'add': 0, 'mul': 0, 'call': 0, 'jmp': 0, 'other': 0}
            
            for func in functions:
                for inst in func.get('instructions', []):
                    assembly = inst.get('assembly', '').lower()
                    categorized = False
                    for inst_type in instruction_types:
                        if inst_type in assembly:
                            instruction_types[inst_type] += 1
                            categorized = True
                            break
                    if not categorized:
                        instruction_types['other'] += 1
            
            fig.add_trace(
                go.Pie(labels=list(instruction_types.keys()),
                      values=list(instruction_types.values()),
                      name='Instruction Types'),
                row=2, col=2
            )
        
        # Update layout
        fig.update_layout(
            title=f'🔍 Binary Analysis Visualization: {binary_name}',
            height=800,
            showlegend=True
        )
        
        return fig


def demo_reverse_engineering():
    """Demonstrate reverse engineering capabilities."""
    print("🔍 DSKYpoly Reverse Engineering Toolkit Demo")
    print("=" * 60)
    
    # Initialize analyzer
    analyzer = GhidraAnalyzer()
    
    # Find DSKYpoly binaries to analyze
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
        print("⚠️  No DSKYpoly binaries found for analysis")
        print("💡 Try building some binaries first with: make")
        return None
    
    print(f"📁 Found {len(binary_paths)} binaries to analyze:")
    for bp in binary_paths:
        print(f"  • {bp}")
    
    # Analyze first binary as example
    if binary_paths:
        test_binary = binary_paths[0]
        print(f"\n🔬 Analyzing: {test_binary.name}")
        
        try:
            # Perform analysis
            analysis_result = analyzer.analyze_binary(str(test_binary))
            
            # Analyze mathematical patterns
            math_patterns = analyzer.analyze_mathematical_patterns(test_binary.name)
            
            # Generate report
            report_path = analyzer.generate_analysis_report(test_binary.name, "html")
            print(f"📄 Analysis report saved: {report_path}")
            
            # Create visualization
            fig = analyzer.visualize_analysis(test_binary.name)
            fig.write_html(f"reverse_engineering/{test_binary.name}_visualization.html")
            print(f"📊 Visualization saved: reverse_engineering/{test_binary.name}_visualization.html")
            
            # Print summary
            print(f"\n📋 Analysis Summary:")
            print(f"  Functions found: {len(analysis_result.get('functions', []))}")
            print(f"  Symbols found: {len(analysis_result.get('symbols', []))}")
            print(f"  Analysis method: {analysis_result.get('analysis_method', 'unknown')}")
            print(f"  Mathematical patterns: {len(math_patterns.get('polynomial_indicators', []))} polynomial indicators")
            
            return analyzer, analysis_result
            
        except Exception as e:
            print(f"❌ Analysis failed: {e}")
            return None
    
    return analyzer

if __name__ == "__main__":
    demo_reverse_engineering()
