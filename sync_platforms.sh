#!/bin/bash
# DSKYpoly Cross-Platform Sync Script
# Optimized for Fedora → Windows/WSL → iPhone workflow

echo "🔄 DSKYpoly Cross-Platform Sync"
echo "==============================="
echo ""

# Function to detect current environment
detect_environment() {
    if [ -f /etc/fedora-release ]; then
        echo "fedora"
    elif grep -q Microsoft /proc/version 2>/dev/null; then
        echo "wsl"
    elif [ "$(uname)" = "Linux" ]; then
        echo "linux"
    elif [ "$(uname)" = "Darwin" ]; then
        echo "macos"
    else
        echo "unknown"
    fi
}

ENV=$(detect_environment)
echo "🖥️  Detected environment: $ENV"
echo ""

case $ENV in
    "fedora")
        echo "🔴 Fedora Development Workflow"
        echo "=============================="
        echo ""
        
        # Show current status
        echo "📊 Current Status:"
        git status --short
        echo ""
        
        # Show active branches
        echo "🌿 Branches:"
        git branch -v
        echo ""
        
        # Offer sync options
        echo "🚀 Sync Options:"
        echo "1. Push current work to remote"
        echo "2. Create mobile-friendly commit"
        echo "3. Prepare for Windows/WSL testing"
        echo "4. Show recent changes for iPhone monitoring"
        echo ""
        
        read -p "Choose option (1-4): " choice
        
        case $choice in
            1)
                echo "Pushing current branch..."
                current_branch=$(git branch --show-current)
                git push origin "$current_branch"
                echo "✅ Pushed to origin/$current_branch"
                ;;
            2)
                echo "Creating mobile-friendly commit..."
                git add -A
                echo "Enter commit message:"
                read -r commit_msg
                git commit -m "📱 $commit_msg

Mobile-friendly update for iPhone monitoring
Cross-platform compatibility ensured"
                echo "✅ Commit created"
                ;;
            3)
                echo "Preparing for Windows/WSL..."
                git push origin quintic-hypergeometric
                git push origin reverse-engineering-analysis
                echo "✅ Branches synced for Windows/WSL testing"
                echo ""
                echo "📝 Windows/WSL Commands:"
                echo "git pull origin quintic-hypergeometric"
                echo "conda env create -f environment.yml"
                echo "conda activate dskypoly"
                ;;
            4)
                echo "📱 Recent changes (iPhone-friendly):"
                git log --oneline -10
                echo ""
                echo "📊 Modified files:"
                git diff --name-only HEAD~5..HEAD
                ;;
        esac
        ;;
        
    "wsl"|"linux")
        echo "🪟 Windows/WSL Workflow"
        echo "======================="
        echo ""
        
        # Check if conda is available
        if command -v conda >/dev/null 2>&1; then
            echo "🐍 Conda available"
            
            # Check if dskypoly environment exists
            if conda env list | grep -q dskypoly; then
                echo "✅ DSKYpoly environment ready"
                echo "To activate: conda activate dskypoly"
            else
                echo "📦 Setting up DSKYpoly environment..."
                if [ -f environment.yml ]; then
                    conda env create -f environment.yml
                    echo "✅ Environment created"
                else
                    echo "❌ environment.yml not found. Please pull latest changes."
                fi
            fi
        else
            echo "⚠️  Conda not found. Please install Anaconda/Miniconda"
        fi
        
        echo ""
        echo "🔄 Pull latest changes:"
        git pull origin quintic-hypergeometric
        git pull origin reverse-engineering-analysis
        ;;
        
    *)
        echo "🌐 General Cross-Platform Info"
        echo "==============================="
        echo ""
        echo "📱 For iPhone monitoring:"
        echo "- Check MOBILE.md for quick overview"
        echo "- Use git log --oneline for recent changes"
        echo "- Monitor branch status with git branch -v"
        echo ""
        echo "💻 For development environments:"
        echo "- Fedora: Primary development"
        echo "- Windows/WSL: Testing and Anaconda exploration"
        echo "- Mobile: Monitoring and documentation reading"
        ;;
esac

echo ""
echo "📚 Quick Reference:"
echo "- 📱 Mobile docs: MOBILE.md"
echo "- 🐍 Anaconda setup: ANACONDA.md" 
echo "- 🔍 RE analysis: analysis/README.md"
echo "- 📖 Main docs: README.md"
