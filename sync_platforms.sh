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
        echo "5. Diagnose git/remote issues"
        echo ""
        
        read -p "Choose option (1-5): " choice
        
        case $choice in
            1)
                echo "Pushing current branch..."
                current_branch=$(git branch --show-current)
                
                # Check if we need to pull first
                git fetch origin
                
                # Check if remote is ahead
                LOCAL=$(git rev-parse @)
                REMOTE=$(git rev-parse @{u} 2>/dev/null)
                BASE=$(git merge-base @ @{u} 2>/dev/null)
                
                if [ "$LOCAL" = "$REMOTE" ]; then
                    echo "📍 Branch is up-to-date"
                elif [ "$LOCAL" = "$BASE" ]; then
                    echo "⚠️  Remote is ahead. Pulling first..."
                    git pull origin "$current_branch"
                elif [ "$REMOTE" = "$BASE" ]; then
                    echo "🚀 Local is ahead. Pushing..."
                else
                    echo "⚠️  Branches have diverged. Manual merge may be required."
                    echo "Run: git pull origin $current_branch"
                    exit 1
                fi
                
                # Attempt push with error handling
                if git push origin "$current_branch"; then
                    echo "✅ Successfully pushed to origin/$current_branch"
                else
                    echo "❌ Push failed. Common solutions:"
                    echo "1. Check internet connection"
                    echo "2. Verify GitHub authentication (token/SSH)"
                    echo "3. Try: git pull origin $current_branch && git push origin $current_branch"
                    echo "4. Check if branch exists on remote: git ls-remote origin"
                fi
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
                
                # Push with error handling
                branches_to_push=("quintic-hypergeometric" "reverse-engineering-analysis")
                for branch in "${branches_to_push[@]}"; do
                    echo "📤 Pushing $branch..."
                    if git push origin "$branch"; then
                        echo "✅ $branch pushed successfully"
                    else
                        echo "❌ Failed to push $branch"
                        echo "💡 Try manually: git push origin $branch"
                    fi
                done
                
                echo ""
                echo "📝 Windows/WSL Commands:"
                echo "git pull origin quintic-hypergeometric"
                echo "conda env create -f environment.yml"
                echo "conda activate dskypoly"
                echo "jupyter lab notebooks/quintic_exploration.ipynb"
                ;;
            4)
                echo "📱 Recent changes (iPhone-friendly):"
                git log --oneline -10
                echo ""
                echo "📊 Modified files:"
                git diff --name-only HEAD~5..HEAD
                ;;
            5)
                echo "🔍 Git/Remote Diagnostics"
                echo "========================="
                echo ""
                echo "📡 Remote configuration:"
                git remote -v
                echo ""
                echo "🌐 Remote branch status:"
                git ls-remote origin
                echo ""
                echo "📊 Local vs Remote comparison:"
                git fetch origin
                for branch in $(git branch -r | grep -v HEAD | sed 's/origin\///'); do
                    echo "Branch: $branch"
                    LOCAL=$(git rev-parse "$branch" 2>/dev/null || echo "local-missing")
                    REMOTE=$(git rev-parse "origin/$branch" 2>/dev/null || echo "remote-missing")
                    if [ "$LOCAL" = "$REMOTE" ]; then
                        echo "  ✅ In sync"
                    else
                        echo "  ⚠️  Out of sync"
                    fi
                done
                echo ""
                echo "🔑 Authentication test:"
                if git ls-remote origin > /dev/null 2>&1; then
                    echo "✅ Can connect to remote repository"
                else
                    echo "❌ Cannot connect to remote repository"
                    echo "💡 Check:"
                    echo "  - Internet connection"
                    echo "  - GitHub authentication (token/SSH key)"
                    echo "  - Repository URL: $(git remote get-url origin)"
                fi
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
