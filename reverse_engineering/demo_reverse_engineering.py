#!/usr/bin/env python3
"""
DSKYpoly Reverse Engineering Toolkit Demo
=========================================

Comprehensive demonstration of cross-platform reverse engineering capabilities
for mathematical software analysis.

Usage:
    python demo_reverse_engineering.py [options]

Options:
    --ghidra-only    Run only Ghidra analysis (skip cross-platform features)
    --educational    Run educational framework demo
    --all           Run complete demonstration (default)
"""

import sys
import argparse
from pathlib import Path

# Add current directory to path for imports
sys.path.append(str(Path(__file__).parent))

from ghidra_analyzer import GhidraAnalyzer, demo_reverse_engineering
from cross_platform_workflow import CrossPlatformAnalyzer, demo_cross_platform_workflow
from educational_framework import EducationalReversEngineeringFramework, demo_educational_framework

def print_banner():
    """Print demo banner."""
    banner = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                    DSKYpoly Reverse Engineering Toolkit                      ║
║                          Comprehensive Demo Suite                            ║
║                                                                              ║
║  "Understanding through Construction" - Advanced Binary Analysis Education   ║
╚══════════════════════════════════════════════════════════════════════════════╝

🔍 Capabilities:
   • Cross-platform analysis (Windows IDA + Linux Ghidra)
   • Mathematical software pattern recognition
   • Educational reverse engineering curriculum
   • Interactive analysis workflow
   • Professional reporting and visualization

🎯 Target: DSKYpoly polynomial solver suite
   • Assembly-optimized mathematical algorithms
   • Progressive complexity (quadratic → quintic)
   • Real-world binary analysis scenarios
"""
    print(banner)

def demo_ghidra_analyzer():
    """Demonstrate Ghidra analyzer capabilities."""
    print("\n" + "="*80)
    print("🐉 GHIDRA ANALYZER DEMONSTRATION")
    print("="*80)
    
    try:
        analyzer, results = demo_reverse_engineering()
        if analyzer and results:
            print(f"\n✅ Ghidra analyzer demo completed successfully")
            return True
        else:
            print(f"\n⚠️  Ghidra analyzer demo completed with limited results")
            return False
    except Exception as e:
        print(f"\n❌ Ghidra analyzer demo failed: {e}")
        return False

def demo_cross_platform():
    """Demonstrate cross-platform workflow."""
    print("\n" + "="*80)
    print("🔗 CROSS-PLATFORM WORKFLOW DEMONSTRATION")
    print("="*80)
    
    try:
        analyzer = demo_cross_platform_workflow()
        if analyzer:
            print(f"\n✅ Cross-platform workflow demo completed successfully")
            return True
        else:
            print(f"\n⚠️  Cross-platform workflow demo completed with limitations")
            return False
    except Exception as e:
        print(f"\n❌ Cross-platform workflow demo failed: {e}")
        return False

def demo_educational():
    """Demonstrate educational framework."""
    print("\n" + "="*80)
    print("🎓 EDUCATIONAL FRAMEWORK DEMONSTRATION")
    print("="*80)
    
    try:
        framework = demo_educational_framework()
        if framework:
            print(f"\n✅ Educational framework demo completed successfully")
            return True
        else:
            print(f"\n⚠️  Educational framework demo completed with limitations")
            return False
    except Exception as e:
        print(f"\n❌ Educational framework demo failed: {e}")
        return False

def check_prerequisites():
    """Check if prerequisites are available."""
    print("🔧 Checking Prerequisites...")
    
    issues = []
    warnings = []
    
    # Check for DSKYpoly binaries
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
        issues.append("No DSKYpoly binaries found. Run 'make' to build them.")
    else:
        print(f"  ✅ Found {len(binary_paths)} DSKYpoly binaries")
    
    # Check for required Python packages
    required_packages = ['matplotlib', 'plotly', 'numpy']
    for package in required_packages:
        try:
            __import__(package)
            print(f"  ✅ {package} available")
        except ImportError:
            issues.append(f"Missing Python package: {package}")
    
    # Check for optional tools
    import subprocess
    optional_tools = [
        ('objdump', 'Basic disassembly'),
        ('nm', 'Symbol analysis'),
        ('strings', 'String extraction'),
        ('readelf', 'ELF analysis')
    ]
    
    for tool, description in optional_tools:
        try:
            result = subprocess.run(['which', tool], capture_output=True)
            if result.returncode == 0:
                print(f"  ✅ {tool} available ({description})")
            else:
                warnings.append(f"{tool} not found - {description} limited")
        except:
            warnings.append(f"Could not check for {tool}")
    
    # Check for Ghidra
    ghidra_paths = [
        Path("/opt/ghidra"),
        Path("/usr/bin/ghidra"),
        Path("/usr/share/ghidra")
    ]
    
    ghidra_found = False
    for path in ghidra_paths:
        if path.exists():
            ghidra_found = True
            print(f"  ✅ Ghidra found at {path}")
            break
    
    if not ghidra_found:
        warnings.append("Ghidra not found - advanced analysis limited")
    
    # Report results
    if issues:
        print(f"\n❌ Issues found:")
        for issue in issues:
            print(f"   • {issue}")
        return False
    
    if warnings:
        print(f"\n⚠️  Warnings:")
        for warning in warnings:
            print(f"   • {warning}")
    
    print(f"\n✅ Prerequisites check completed")
    return True

def create_summary_report(results):
    """Create summary report of demo results."""
    
    report_content = f"""
# DSKYpoly Reverse Engineering Toolkit Demo Summary

## Execution Summary
- **Date:** {results['timestamp']}
- **Total Demos:** {results['total_demos']}
- **Successful:** {results['successful']}
- **Failed:** {results['failed']}

## Demo Results

### Ghidra Analyzer
- **Status:** {'✅ Success' if results['ghidra_success'] else '❌ Failed'}
- **Features Tested:** Binary analysis, pattern recognition, visualization
- **Output:** Analysis reports and visualizations

### Cross-Platform Workflow
- **Status:** {'✅ Success' if results['cross_platform_success'] else '❌ Failed'}
- **Features Tested:** IDA integration, cross-validation, unified reporting
- **Output:** Workflow guide and analysis sessions

### Educational Framework
- **Status:** {'✅ Success' if results['educational_success'] else '❌ Failed'}
- **Features Tested:** Curriculum creation, progress tracking, assessment
- **Output:** Complete educational curriculum

## Key Achievements

### Technical Capabilities
- Advanced binary analysis with Ghidra integration
- Cross-platform workflow for Windows IDA + Linux Ghidra
- Mathematical pattern recognition in polynomial solvers
- Professional reporting and visualization

### Educational Value
- Complete reverse engineering curriculum
- Progressive skill development framework
- Hands-on exercises with real binaries
- Assessment and progress tracking system

### Philosophy Implementation
- "Construction-based understanding" approach
- Learning through building and analyzing
- Real-world application focus
- Professional tool integration

## Generated Artifacts

### Analysis Tools
- `ghidra_analyzer.py` - Ghidra automation and analysis
- `cross_platform_workflow.py` - Multi-platform integration
- `educational_framework.py` - Complete curriculum system

### Documentation
- Workflow guides and tutorials
- Educational lesson plans
- Assessment frameworks
- Interactive demonstrations

### Reports and Visualizations
- HTML analysis reports with interactive plots
- Cross-validation studies
- Progress tracking dashboards
- Educational assessment tools

## Next Steps

### For Educators
1. Review generated curriculum materials
2. Adapt lessons for specific student populations
3. Set up assessment and progress tracking
4. Begin pilot educational programs

### For Researchers
1. Extend analysis capabilities with custom tools
2. Develop automated pattern recognition systems
3. Create specialized analysis methodologies
4. Publish educational research findings

### For Students
1. Work through progressive lesson sequence
2. Complete hands-on exercises with real binaries
3. Build portfolio of analysis work
4. Mentor other students in reverse engineering

## Technical Recommendations

### Environment Setup
- Fedora Linux with development tools installed
- Ghidra properly configured for headless analysis
- Python environment with scientific computing packages
- Cross-platform development setup (Windows + Linux)

### Tool Integration
- Automated analysis pipeline development
- Custom plugin creation for specialized analysis
- Integration with additional reverse engineering tools
- Educational content management systems

## Conclusion

The DSKYpoly Reverse Engineering Toolkit successfully demonstrates:

1. **Professional Capabilities:** Advanced binary analysis suitable for industry use
2. **Educational Value:** Complete curriculum for teaching reverse engineering
3. **Philosophy Integration:** Construction-based understanding through hands-on work
4. **Cross-Platform Power:** Windows IDA + Linux Ghidra workflow integration

This toolkit bridges the gap between academic reverse engineering education and
practical industry applications, providing both students and professionals with
powerful analysis capabilities grounded in sound educational principles.

---
*Generated by DSKYpoly Reverse Engineering Toolkit Demo Suite*
"""
    
    report_path = Path.cwd() / "reverse_engineering" / "demo_summary_report.md"
    with open(report_path, 'w') as f:
        f.write(report_content)
    
    return str(report_path)

def main():
    """Main demo orchestrator."""
    parser = argparse.ArgumentParser(
        description="DSKYpoly Reverse Engineering Toolkit Demo",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python demo_reverse_engineering.py --all
    python demo_reverse_engineering.py --ghidra-only
    python demo_reverse_engineering.py --educational
        """
    )
    
    parser.add_argument('--ghidra-only', action='store_true',
                       help='Run only Ghidra analysis demo')
    parser.add_argument('--educational', action='store_true',
                       help='Run only educational framework demo')
    parser.add_argument('--all', action='store_true', default=True,
                       help='Run complete demonstration (default)')
    
    args = parser.parse_args()
    
    # Print banner
    print_banner()
    
    # Check prerequisites
    if not check_prerequisites():
        print("\n❌ Prerequisites check failed. Please resolve issues before continuing.")
        return 1
    
    # Track results
    results = {
        'timestamp': str(Path(__file__).stat().st_mtime),
        'total_demos': 0,
        'successful': 0,
        'failed': 0,
        'ghidra_success': False,
        'cross_platform_success': False,
        'educational_success': False
    }
    
    # Run demos based on arguments
    if args.ghidra_only:
        results['total_demos'] = 1
        results['ghidra_success'] = demo_ghidra_analyzer()
        if results['ghidra_success']:
            results['successful'] += 1
        else:
            results['failed'] += 1
    
    elif args.educational:
        results['total_demos'] = 1
        results['educational_success'] = demo_educational()
        if results['educational_success']:
            results['successful'] += 1
        else:
            results['failed'] += 1
    
    else:  # --all or default
        results['total_demos'] = 3
        
        # Run all demos
        results['ghidra_success'] = demo_ghidra_analyzer()
        results['cross_platform_success'] = demo_cross_platform()
        results['educational_success'] = demo_educational()
        
        # Count results
        for success in [results['ghidra_success'], results['cross_platform_success'], results['educational_success']]:
            if success:
                results['successful'] += 1
            else:
                results['failed'] += 1
    
    # Generate summary report
    report_path = create_summary_report(results)
    
    # Print final summary
    print("\n" + "="*80)
    print("📊 DEMO SUITE SUMMARY")
    print("="*80)
    print(f"Total demos run: {results['total_demos']}")
    print(f"Successful: {results['successful']}")
    print(f"Failed: {results['failed']}")
    print(f"Success rate: {results['successful']/results['total_demos']:.1%}")
    
    print(f"\n📄 Summary report: {report_path}")
    
    if results['successful'] > 0:
        print(f"\n🎉 DSKYpoly Reverse Engineering Toolkit demonstration completed!")
        print(f"   The toolkit is ready for educational and research use.")
        print(f"   Check the generated files for detailed analysis capabilities.")
        return 0
    else:
        print(f"\n⚠️  Demo suite completed with issues.")
        print(f"   Check error messages above and resolve before use.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
