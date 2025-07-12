#!/usr/bin/env python3
"""
Simple DSKYpoly Reverse Engineering Demo
=======================================

Direct demonstration of reverse engineering capabilities without complex imports.
"""

import subprocess
import os
from pathlib import Path

def analyze_dskypoly_binaries():
    """Analyze DSKYpoly binaries with basic tools."""
    print("🔍 DSKYpoly Reverse Engineering Demonstration")
    print("=" * 60)
    
    # Find DSKYpoly binaries
    base_path = Path("/home/tjpools/assembly-projects/DSKYpoly")
    binaries = [
        base_path / "build/dskypoly",
        base_path / "cubic/build/dskypoly3", 
        base_path / "quartic/build/dskypoly4",
        base_path / "quintic/build/dskypoly5"
    ]
    
    available_binaries = [b for b in binaries if b.exists() and b.stat().st_size > 0]
    
    if not available_binaries:
        print("❌ No DSKYpoly binaries found!")
        return
    
    print(f"📁 Found {len(available_binaries)} binaries:")
    for binary in available_binaries:
        print(f"  • {binary.name}: {binary.stat().st_size:,} bytes")
    
    # Analyze first binary in detail
    target_binary = available_binaries[0]
    print(f"\n🔬 Detailed Analysis: {target_binary.name}")
    print("-" * 40)
    
    # Basic file information
    print("📋 Basic Information:")
    try:
        result = subprocess.run(["file", str(target_binary)], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"  File type: {result.stdout.strip()}")
    except:
        print("  File command failed")
    
    # String analysis
    print("\n📝 String Analysis:")
    try:
        result = subprocess.run(["strings", str(target_binary)], capture_output=True, text=True)
        if result.returncode == 0:
            strings = result.stdout.split('\n')
            math_strings = [s for s in strings if any(term in s.lower() for term in ['poly', 'solve', 'root', 'coefficient'])]
            print(f"  Total strings: {len(strings)}")
            print(f"  Mathematical strings: {len(math_strings)}")
            if math_strings:
                print("  Mathematical terms found:")
                for s in math_strings[:5]:  # Show first 5
                    print(f"    - {s}")
    except:
        print("  Strings analysis failed")
    
    # Function analysis
    print("\n🔧 Function Analysis:")
    try:
        result = subprocess.run(["nm", "-D", str(target_binary)], capture_output=True, text=True)
        if result.returncode == 0:
            symbols = result.stdout.split('\n')
            functions = [s for s in symbols if ' T ' in s or ' t ' in s]  # Text symbols (functions)
            print(f"  Total symbols: {len(symbols)}")
            print(f"  Function symbols: {len(functions)}")
            
            # Look for mathematical function names
            math_funcs = [f for f in functions if any(term in f.lower() for term in ['solve', 'poly', 'eval', 'newton'])]
            if math_funcs:
                print("  Mathematical functions:")
                for f in math_funcs[:3]:  # Show first 3
                    print(f"    - {f}")
    except:
        print("  Symbol analysis failed")
    
    # Assembly analysis
    print("\n⚙️  Assembly Analysis:")
    try:
        result = subprocess.run(["objdump", "-d", "-M", "intel", str(target_binary)], capture_output=True, text=True)
        if result.returncode == 0:
            disasm = result.stdout
            
            # Count mathematical operations
            fp_ops = len([line for line in disasm.split('\n') if any(op in line for op in ['movsd', 'movss', 'mulsd', 'addsd', 'subsd'])])
            loops = len([line for line in disasm.split('\n') if any(op in line for op in ['jmp', 'je', 'jne', 'jl', 'jg'])])
            calls = len([line for line in disasm.split('\n') if 'call' in line])
            
            print(f"  Floating point operations: {fp_ops}")
            print(f"  Jump/loop instructions: {loops}")
            print(f"  Function calls: {calls}")
            
            # Look for main solving function
            if 'solve_poly' in disasm:
                print("  ✅ Found polynomial solving function")
            else:
                print("  ❓ Polynomial solving function not clearly identified")
                
    except:
        print("  Assembly analysis failed")
    
    # Comparative analysis
    if len(available_binaries) > 1:
        print(f"\n📊 Comparative Analysis:")
        print("-" * 40)
        
        for binary in available_binaries:
            try:
                # Get basic metrics for each binary
                size = binary.stat().st_size
                
                # Count functions
                result = subprocess.run(["nm", "-D", str(binary)], capture_output=True, text=True)
                func_count = 0
                if result.returncode == 0:
                    symbols = result.stdout.split('\n')
                    func_count = len([s for s in symbols if ' T ' in s or ' t ' in s])
                
                print(f"  {binary.name:12}: {size:6,} bytes, {func_count:3} functions")
                
            except:
                print(f"  {binary.name:12}: Analysis failed")
    
    # Educational insights
    print(f"\n🎓 Educational Insights:")
    print("-" * 40)
    print("  • Polynomial solvers show increasing complexity from quadratic to quintic")
    print("  • Assembly code reveals mathematical optimization techniques")
    print("  • Function symbols help identify algorithmic structure")
    print("  • String analysis reveals debugging and user interface elements")
    print("  • Comparative analysis shows scaling of algorithmic complexity")
    
    print(f"\n✅ Basic reverse engineering analysis completed!")
    print("   This demonstrates the foundation for advanced binary analysis.")
    print("   Next steps: Use professional tools like Ghidra for deeper analysis.")

if __name__ == "__main__":
    analyze_dskypoly_binaries()
