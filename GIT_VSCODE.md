# Git Configuration for Visual Studio Code

*Optimize git workflow with VS Code on Windows and WSL Ubuntu*

## 🔧 **Configure Git Editor**

### **For Windows:**
```cmd
# Set VS Code as default git editor
git config --global core.editor "code --wait"

# Optional: Configure merge tool
git config --global merge.tool vscode
git config --global mergetool.vscode.cmd 'code --wait $MERGED'

# Configure diff tool
git config --global diff.tool vscode
git config --global difftool.vscode.cmd 'code --wait --diff $LOCAL $REMOTE'
```

### **For WSL Ubuntu:**
```bash
# Set VS Code as default git editor
git config --global core.editor "code --wait"

# Alternative: Use VS Code from WSL
git config --global core.editor "/mnt/c/Users/$USER/AppData/Local/Programs/Microsoft\ VS\ Code/bin/code --wait"
```

## 🚀 **Better: Avoid Merge Commits Entirely**

### **Configure Git to Use Rebase Instead of Merge:**
```bash
# Set rebase as default for pulls (prevents merge commits)
git config --global pull.rebase true

# Set fast-forward only for merges
git config --global merge.ff only

# Auto-setup tracking branches
git config --global branch.autosetupmerge always
git config --global branch.autosetuprebase always
```

## 🎯 **DSKYpoly-Specific Git Workflow**

### **Recommended .gitconfig additions:**
```ini
[core]
    editor = code --wait
    autocrlf = input  # Consistent line endings across platforms
    
[pull]
    rebase = true     # Use rebase instead of merge
    
[merge]
    tool = vscode
    ff = only
    
[diff]
    tool = vscode
    
[alias]
    # DSKYpoly-specific aliases
    sync-all = "!f() { git pull --rebase origin quintic-hypergeometric && git pull --rebase origin reverse-engineering-analysis; }; f"
    push-all = "!f() { git push origin quintic-hypergeometric && git push origin reverse-engineering-analysis; }; f"
    status-all = "!f() { git status --short && echo '\n--- Branches ---' && git branch -v; }; f"
```

## 🔄 **Cross-Platform Sync Commands**

### **Windows (PowerShell/CMD):**
```cmd
# Quick sync without merge commits
git pull --rebase origin quintic-hypergeometric
git pull --rebase origin reverse-engineering-analysis

# Or use alias
git sync-all
```

### **WSL Ubuntu:**
```bash
# Same commands work in WSL
git pull --rebase origin quintic-hypergeometric
git sync-all
```

## 🛠️ **VS Code Integration Benefits**

### **For DSKYpoly Development:**
- **Assembly syntax highlighting** for .asm files
- **Python IntelliSense** for quintic solver
- **Integrated terminal** for git commands
- **Git lens extension** for better git visualization
- **Jupyter extension** for notebook editing
- **Cross-platform consistency** between Windows and WSL

### **Recommended VS Code Extensions:**
```json
{
    "recommendations": [
        "ms-vscode.vscode-json",
        "ms-python.python",
        "ms-toolsai.jupyter",
        "eamodio.gitlens",
        "ms-vscode.hexeditor",
        "13xforever.language-x86-64-assembly",
        "ms-vscode-remote.remote-wsl"
    ]
}
```

## 🎯 **No More Vim Editor Issues!**

With this configuration:
- ✅ **VS Code opens** instead of vim for commit messages
- ✅ **Rebase instead of merge** eliminates most commit message prompts
- ✅ **Cross-platform consistency** between Windows and WSL
- ✅ **Better conflict resolution** with VS Code merge tools
- ✅ **Integrated workflow** for DSKYpoly development

---

*Say goodbye to vim editor interruptions!* 🎉
