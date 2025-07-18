#!/usr/bin/env python3
"""
Quick test for Flatpak Ghidra integration
"""

import subprocess
from pathlib import Path

def test_flatpak_ghidra():
    print("🔍 Testing Flatpak Ghidra Integration")
    print("=" * 50)
    
    # Check if Flatpak is available
    try:
        result = subprocess.run(["flatpak", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Flatpak version: {result.stdout.strip()}")
        else:
            print("❌ Flatpak not available")
            return False
    except FileNotFoundError:
        print("❌ Flatpak command not found")
        return False
    
    # Check if Ghidra Flatpak is installed
    try:
        result = subprocess.run(["flatpak", "list", "--app"], capture_output=True, text=True)
        if result.returncode == 0 and "org.ghidra_sre.Ghidra" in result.stdout:
            print("✅ Ghidra Flatpak detected")
            
            # Extract version info
            for line in result.stdout.split('\n'):
                if "org.ghidra_sre.Ghidra" in line:
                    parts = line.split('\t')
                    if len(parts) >= 3:
                        print(f"   Version: {parts[2]}")
                    break
            
            return True
        else:
            print("❌ Ghidra Flatpak not found")
            return False
    except Exception as e:
        print(f"❌ Error checking Flatpak apps: {e}")
        return False

def test_ghidra_headless():
    print("\n🔧 Testing Ghidra Headless Access")
    print("=" * 50)
    
    try:
        # Try to get Ghidra help output
        result = subprocess.run([
            "flatpak", "run", "org.ghidra_sre.Ghidra", 
            "--headless", "--help"
        ], capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            print("✅ Ghidra headless mode accessible")
            print("📋 Available options confirmed")
            return True
        else:
            print(f"⚠️  Ghidra headless returned exit code: {result.returncode}")
            print(f"Stderr: {result.stderr[:200]}...")
            return False
            
    except subprocess.TimeoutExpired:
        print("⚠️  Ghidra headless test timed out")
        return False
    except Exception as e:
        print(f"❌ Error testing Ghidra headless: {e}")
        return False

def test_basic_tools():
    print("\n🛠️  Testing Fallback Unix Tools")
    print("=" * 50)
    
    tools = ["objdump", "nm", "strings", "file"]
    all_available = True
    
    for tool in tools:
        try:
            result = subprocess.run([tool, "--version"], capture_output=True, text=True)
            if result.returncode == 0:
                print(f"✅ {tool}: Available")
            else:
                print(f"⚠️  {tool}: Issues detected")
                all_available = False
        except FileNotFoundError:
            print(f"❌ {tool}: Not found")
            all_available = False
        except Exception as e:
            print(f"⚠️  {tool}: Error - {e}")
            all_available = False
    
    return all_available

if __name__ == "__main__":
    print("🔍 DSKYpoly Reverse Engineering Environment Test")
    print("=" * 60)
    
    flatpak_ok = test_flatpak_ghidra()
    tools_ok = test_basic_tools()
    
    if flatpak_ok:
        ghidra_ok = test_ghidra_headless()
    else:
        ghidra_ok = False
    
    print("\n📊 Summary")
    print("=" * 30)
    print(f"Flatpak Ghidra: {'✅ Ready' if flatpak_ok else '❌ Not Available'}")
    print(f"Ghidra Headless: {'✅ Working' if ghidra_ok else '⚠️  Issues'}")
    print(f"Unix Tools: {'✅ Ready' if tools_ok else '⚠️  Issues'}")
    
    if ghidra_ok:
        print("\n🎉 Your system is ready for advanced Ghidra-powered reverse engineering!")
    elif tools_ok:
        print("\n🔧 Your system is ready for Unix tools-based reverse engineering!")
    else:
        print("\n⚠️  Some issues detected. The toolkit may have limited functionality.")
