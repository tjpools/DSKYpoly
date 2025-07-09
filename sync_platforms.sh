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
        echo "6. Configure git for cross-platform development"
        echo "7. 🚫 Remove Tabnine completely"
        echo ""
        
        read -p "Choose option (1-7): " choice
        
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
                echo "git pull origin reverse-engineering-analysis"
                echo "conda env create -f environment.yml"
                echo "conda activate dskypoly"
                echo "jupyter lab notebooks/quintic_exploration.ipynb"
                echo ""
                echo "📖 Windows Setup Guides:"
                echo "- WINDOWS_TESTING.md (Anaconda Navigator setup)"
                echo "- WINDOWS_ANACONDA.md (GUI workflow)"
                echo "- VISUAL_STUDIO.md (Professional development)"
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
            6)
                echo "🔧 Git Configuration for Cross-Platform Development"
                echo "=================================================="
                echo ""
                echo "Choose your preferred development environment:"
                echo "1. VS Code (recommended for general development)"
                echo "2. Visual Studio (for C/Assembly + Python)"
                echo "3. Basic (Notepad/nano editors)"
                echo ""
                read -p "Choose option (1-3): " editor_choice
                
                case $editor_choice in
                    1)
                        echo "🔧 Configuring for VS Code..."
                        git config --global core.editor "code --wait"
                        git config --global merge.tool vscode
                        git config --global mergetool.vscode.cmd 'code --wait $MERGED'
                        git config --global diff.tool vscode
                        git config --global difftool.vscode.cmd 'code --wait --diff $LOCAL $REMOTE'
                        echo "✅ VS Code configured as git editor"
                        ;;
                    2)
                        echo "🔧 Configuring for Visual Studio..."
                        # Check if Visual Studio is available
                        if command -v devenv >/dev/null 2>&1; then
                            git config --global core.editor "devenv /edit"
                            git config --global merge.tool vsdiffmerge
                            echo "✅ Visual Studio configured as git editor"
                        else
                            echo "⚠️  Visual Studio not found in PATH"
                            echo "💡 Using VS Code as fallback..."
                            git config --global core.editor "code --wait"
                        fi
                        ;;
                    3)
                        echo "🔧 Configuring basic editors..."
                        if [ "$ENV" = "wsl" ] || [ "$ENV" = "linux" ]; then
                            git config --global core.editor "nano"
                            echo "✅ Nano configured for Linux/WSL"
                        else
                            git config --global core.editor "notepad"
                            echo "✅ Notepad configured for Windows"
                        fi
                        ;;
                esac
                
                # Common cross-platform settings
                echo "� Applying cross-platform settings..."
                git config --global core.autocrlf input
                git config --global pull.rebase true
                git config --global merge.ff only
                git config --global branch.autosetupmerge always
                git config --global branch.autosetuprebase always
                
                echo "✅ Line ending handling configured"
                echo "✅ Rebase-first pull strategy set"
                echo "✅ Fast-forward merges configured"
                
                echo ""
                echo "🎉 Git configured for cross-platform development!"
                echo "💡 No more vim editor interruptions"
                echo "💡 See GIT_VSCODE.md and VISUAL_STUDIO.md for details"
                ;;
            7)
                echo "🚫 Removing Tabnine Completely"
                echo "==============================="
                echo ""
                
                # Stop processes
                echo "🛑 Stopping Tabnine processes..."
                sudo pkill -9 -f TabNine 2>/dev/null || true
                sudo pkill -9 -f tabnine 2>/dev/null || true
                echo "✅ Processes stopped"
                
                # Remove directories
                echo "📁 Removing Tabnine directories..."
                rm -rf ~/.config/Code/User/globalStorage/tabnine.tabnine-vscode 2>/dev/null || true
                rm -rf ~/.tabnine 2>/dev/null || true
                rm -rf ~/.TabNine 2>/dev/null || true
                rm -rf ~/.local/share/tabnine 2>/dev/null || true
                rm -rf ~/.local/share/TabNine 2>/dev/null || true
                find ~/.vscode* -name "*tabnine*" -exec rm -rf {} + 2>/dev/null || true
                find ~/.config/Code -name "*tabnine*" -exec rm -rf {} + 2>/dev/null || true
                echo "✅ Directories cleaned"
                
                # Try to uninstall extension
                echo "🔧 Removing VS Code extension..."
                code --uninstall-extension tabnine.tabnine-vscode 2>/dev/null || true
                code --uninstall-extension TabNine.tabnine-vscode 2>/dev/null || true
                echo "✅ Extension removal attempted"
                
                echo ""
                echo "🎉 Tabnine removal complete!"
                echo "💡 You may need to restart VS Code"
                echo "💡 See REMOVE_TABNINE.md for more detailed instructions"
                ;;
        esac
        ;;
        
    "wsl"|"linux")
        echo "🪟 Windows/WSL Development Workflow"
        echo "===================================="
        echo ""
        
        # Detect Visual Studio
        VS_DETECTED=false
        if command -v devenv >/dev/null 2>&1; then
            VS_DETECTED=true
            echo "🎯 Visual Studio detected"
        fi
        
        echo "🔧 Development Environment Options:"
        echo "1. 🐍 Anaconda + Jupyter (mathematical exploration)"
        echo "2. 🏗️  Visual Studio development workflow"
        echo "3. 💻 VS Code lightweight development"
        echo "4. 🔄 Sync latest changes"
        echo "5. 🛠️  Configure git editor (fix vim issues)"
        echo ""
        
        read -p "Choose option (1-5): " wsl_choice
        
        case $wsl_choice in
            1)
                echo "🐍 Setting up Anaconda workflow..."
                # Check if conda is available
                if command -v conda >/dev/null 2>&1; then
                    echo "✅ Conda available"
                    
                    # Check if dskypoly environment exists
                    if conda env list | grep -q dskypoly; then
                        echo "✅ DSKYpoly environment ready"
                        echo ""
                        echo "🚀 Launch Options:"
                        echo "📱 Terminal: conda activate dskypoly && jupyter lab"
                        echo "🖱️  GUI: Open Anaconda Navigator → dskypoly environment"
                        echo ""
                        echo "🎯 Jupyter Notebook Targets:"
                        echo "- notebooks/quintic_exploration.ipynb (mathematical exploration)"
                        echo "- analysis/ (reverse engineering notebooks)"
                    else
                        echo "� Creating DSKYpoly environment..."
                        if [ -f environment.yml ]; then
                            conda env create -f environment.yml
                            echo "✅ Environment created successfully"
                        else
                            echo "❌ environment.yml not found"
                        fi
                    fi
                else
                    echo "⚠️  Conda not found. Install Anaconda or Miniconda"
                    echo "💡 See ANACONDA.md for setup instructions"
                fi
                ;;
            2)
                if [ "$VS_DETECTED" = true ]; then
                    echo "🏗️  Visual Studio Development Workflow"
                    echo "======================================"
                    echo ""
                    echo "� Quick Setup Checklist:"
                    echo "✅ Visual Studio with C++ and Python workloads"
                    echo "✅ WSL Extension installed"
                    echo "✅ Git configured for Visual Studio"
                    echo ""
                    echo "🔄 Build Commands (WSL verification):"
                    echo "make clean && make all"
                    echo ""
                    echo "🧪 Test Commands:"
                    echo "./build/dskypoly (quadratic solver)"
                    echo "./quintic/build/dskypoly5 (quintic solver)"
                    echo "python quintic/test_roots_of_unity.py"
                    echo ""
                    echo "📖 See VISUAL_STUDIO.md for complete setup guide"
                else
                    echo "⚠️  Visual Studio not detected in PATH"
                    echo "💡 Install Visual Studio with C++ workload"
                    echo "💡 Or use option 3 for VS Code development"
                fi
                ;;
            3)
                echo "💻 VS Code Development Setup"
                echo "============================"
                echo ""
                echo "� Recommended VS Code Extensions:"
                echo "- ms-python.python (Python development)"
                echo "- ms-toolsai.jupyter (Jupyter notebooks)"
                echo "- 13xforever.language-x86-64-assembly (Assembly syntax)"
                echo "- eamodio.gitlens (Git visualization)"
                echo "- ms-vscode-remote.remote-wsl (WSL integration)"
                echo ""
                echo "💡 See GIT_VSCODE.md for complete VS Code setup"
                ;;
            4)
                echo "🔄 Syncing latest changes..."
                echo ""
                echo "⚠️  Note: If vim editor opens during git operations:"
                echo "   Type ':wq' and press Enter to exit"
                echo "   Or run option 5 to fix this permanently"
                echo ""
                
                branches=("quintic-hypergeometric" "reverse-engineering-analysis")
                for branch in "${branches[@]}"; do
                    echo "📥 Pulling $branch..."
                    if git pull origin "$branch"; then
                        echo "✅ $branch updated successfully"
                    else
                        echo "⚠️  Issue pulling $branch"
                    fi
                    echo ""
                done
                ;;
            5)
                echo "🛠️  Git Editor Configuration"
                echo "============================"
                echo ""
                echo "Choose your preferred git editor:"
                echo "1. VS Code (recommended)"
                echo "2. Visual Studio (if available)"
                echo "3. Nano (simple terminal editor)"
                echo ""
                read -p "Choose (1-3): " git_editor_choice
                
                case $git_editor_choice in
                    1)
                        git config --global core.editor "code --wait"
                        echo "✅ VS Code configured as git editor"
                        ;;
                    2)
                        if command -v devenv >/dev/null 2>&1; then
                            git config --global core.editor "devenv /edit"
                            echo "✅ Visual Studio configured as git editor"
                        else
                            echo "⚠️  Visual Studio not found, using VS Code"
                            git config --global core.editor "code --wait"
                        fi
                        ;;
                    3)
                        git config --global core.editor "nano"
                        echo "✅ Nano configured as git editor"
                        ;;
                esac
                
                # Apply cross-platform settings
                git config --global core.autocrlf input
                git config --global pull.rebase true
                echo "✅ Cross-platform line endings configured"
                echo "✅ Rebase-first pull strategy set"
                echo ""
                echo "🎉 No more vim interruptions during git operations!"
                ;;
        esac
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
echo "- 🪟 Windows testing: WINDOWS_TESTING.md"
echo "- 🏗️  Visual Studio: VISUAL_STUDIO.md"
echo "- 💻 VS Code setup: GIT_VSCODE.md"
echo "- 🔍 RE analysis: analysis/README.md"
echo "- 📖 Main docs: README.md"
