
# Create Git setup and deployment guide
git_guide = '''# 🚀 Git Repository Setup & Deployment Guide

## Complete Guide for Setting Up Your Zomato ML Clustering Repository

---

## 📋 Table of Contents
1. [Initial Git Setup](#initial-git-setup)
2. [Creating GitHub Repository](#creating-github-repository)
3. [First Commit & Push](#first-commit--push)
4. [Repository Organization](#repository-organization)
5. [GitHub Features Setup](#github-features-setup)
6. [Deployment Options](#deployment-options)
7. [Maintenance & Updates](#maintenance--updates)

---

## 🔧 Initial Git Setup

### 1. Install Git
```bash
# Windows: Download from https://git-scm.com/downloads
# macOS:
brew install git

# Linux (Ubuntu/Debian):
sudo apt-get install git

# Verify installation
git --version
```

### 2. Configure Git
```bash
# Set your name
git config --global user.name "Rahul Singh Kushwah"

# Set your email
git config --global user.email "patelmrrahul199@gmail.com"

# Verify configuration
git config --list
```

---

## 🌐 Creating GitHub Repository

### Option 1: Via GitHub Website

1. **Go to GitHub**: https://github.com/new
2. **Fill in details**:
   - Repository name: `zomato-ml-clustering`
   - Description: `Unsupervised ML project for restaurant clustering and sentiment analysis using Python, Streamlit, and Azure ML`
   - Visibility: Public ✅
   - Do NOT initialize with README (we have one)
3. **Click "Create repository"**

### Option 2: Via GitHub CLI

```bash
# Install GitHub CLI
# macOS: brew install gh
# Windows: Download from https://cli.github.com/

# Login to GitHub
gh auth login

# Create repository
gh repo create zomato-ml-clustering --public --description "Unsupervised ML project for restaurant clustering and sentiment analysis"
```

---

## 📦 First Commit & Push

### 1. Navigate to Your Project Directory
```bash
cd /path/to/your/project
# Or create new directory
mkdir zomato-ml-clustering
cd zomato-ml-clustering
```

### 2. Initialize Git Repository
```bash
# Initialize Git
git init

# Check status
git status
```

### 3. Create Directory Structure
```bash
# Create all required directories
mkdir -p data/raw data/processed results/figures results/models notebooks src tests docs

# Create .gitkeep files for empty directories
touch data/raw/.gitkeep
touch data/processed/.gitkeep
touch results/.gitkeep
touch notebooks/.gitkeep
touch models/.gitkeep
```

### 4. Add All Project Files

Place all the created files in the repository:
- streamlit_app.py (root)
- requirements.txt (root)
- README.md (root)
- Dockerfile (root)
- .gitignore (root)
- LICENSE (root)
- data_processing.py → src/
- clustering.py → src/
- sentiment_analysis.py → src/

### 5. Stage All Files
```bash
# Add all files
git add .

# Or add specific files
git add README.md
git add streamlit_app.py
git add requirements.txt
# ... etc

# Check what will be committed
git status
```

### 6. Make First Commit
```bash
git commit -m "Initial commit: Add complete Zomato ML clustering project structure

- Add Streamlit web application with multi-tab interface
- Add data processing, clustering, and sentiment analysis modules
- Add Docker configuration for containerization
- Add comprehensive documentation (README, CONTRIBUTING, PROJECT_STRUCTURE)
- Add requirements.txt with all dependencies
- Add MIT License
- Configure .gitignore for Python projects"
```

### 7. Connect to GitHub Remote
```bash
# Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/Ishadowprince716/zomato-ml-clustering.git

# Verify remote
git remote -v
```

### 8. Push to GitHub
```bash
# Push to main branch
git branch -M main
git push -u origin main

# If you encounter authentication issues, use Personal Access Token
# Generate token at: https://github.com/settings/tokens
```

---

## 📁 Repository Organization

### Recommended Branch Strategy

```bash
# Main branch (production-ready code)
main

# Development branch
git checkout -b develop

# Feature branches
git checkout -b feature/add-hierarchical-clustering
git checkout -b feature/improve-ui
git checkout -b feature/add-tests

# Bug fix branches
git checkout -b fix/sentiment-analysis-error
git checkout -b fix/missing-value-handling

# Release branches
git checkout -b release/v1.0.0
```

### Typical Workflow
```bash
# 1. Create feature branch from develop
git checkout develop
git pull origin develop
git checkout -b feature/new-feature

# 2. Make changes and commit
git add .
git commit -m "Add: new feature description"

# 3. Push feature branch
git push origin feature/new-feature

# 4. Create Pull Request on GitHub

# 5. After merge, update local main
git checkout main
git pull origin main

# 6. Delete feature branch
git branch -d feature/new-feature
git push origin --delete feature/new-feature
```

---

## ⚙️ GitHub Features Setup

### 1. Add Repository Topics
On GitHub repository page → About → Settings (gear icon):
- machine-learning
- unsupervised-learning
- clustering
- sentiment-analysis
- streamlit
- python
- data-science
- zomato
- nlp
- restaurant-analytics
- azure-ml

### 2. Create GitHub Actions (Optional CI/CD)

Create `.github/workflows/main.yml`:

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    
    - name: Lint with flake8
      run: |
        pip install flake8
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
    
    - name: Run tests
      run: |
        pip install pytest
        pytest tests/ -v

  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Deploy to Streamlit Cloud
      run: echo "Deployment configured via Streamlit Cloud"
```

### 3. Add README Badges

Add to top of README.md:
```markdown
![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-orange.svg)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](your-app-url)
```

### 4. Create Issue Templates

`.github/ISSUE_TEMPLATE/bug_report.md`:
```markdown
---
name: Bug Report
about: Create a report to help us improve
---

**Describe the bug**
A clear description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. See error

**Expected behavior**
What you expected to happen.

**Screenshots**
If applicable, add screenshots.

**Environment:**
 - OS: [e.g. Windows 10]
 - Python Version: [e.g. 3.9]
 - Browser: [e.g. Chrome]
```

### 5. Add Pull Request Template

`.github/pull_request_template.md`:
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] Tests added/updated
- [ ] All tests pass

## Related Issues
Closes #(issue number)
```

---

## 🚀 Deployment Options

### 1. Streamlit Cloud (Recommended - Free)

```bash
# 1. Push code to GitHub
git push origin main

# 2. Go to https://share.streamlit.io
# 3. Click "New app"
# 4. Connect GitHub repository
# 5. Select:
#    - Repository: Ishadowprince716/zomato-ml-clustering
#    - Branch: main
#    - Main file: streamlit_app.py
# 6. Add secrets (if using Gemini API):
#    - Click "Advanced settings"
#    - Add secrets in TOML format:

[secrets]
GOOGLE_API_KEY = "your_api_key_here"

# 7. Click "Deploy"
```

### 2. Heroku Deployment

```bash
# Install Heroku CLI
# Create Procfile
echo "web: streamlit run streamlit_app.py --server.port=$PORT --server.address=0.0.0.0" > Procfile

# Create runtime.txt
echo "python-3.9.16" > runtime.txt

# Create setup.sh
cat > setup.sh << EOF
mkdir -p ~/.streamlit/
echo "[server]
headless = true
port = \$PORT
enableCORS = false
" > ~/.streamlit/config.toml
EOF

# Login to Heroku
heroku login

# Create app
heroku create zomato-ml-clustering

# Add buildpack
heroku buildpacks:add --index 1 heroku/python

# Deploy
git push heroku main

# Open app
heroku open
```

### 3. Docker Hub (For Container Distribution)

```bash
# Build image
docker build -t ishadowprince716/zomato-ml-clustering:latest .

# Login to Docker Hub
docker login

# Push image
docker push ishadowprince716/zomato-ml-clustering:latest

# Others can now pull and run:
docker pull ishadowprince716/zomato-ml-clustering:latest
docker run -p 8501:8501 ishadowprince716/zomato-ml-clustering:latest
```

---

## 🔄 Maintenance & Updates

### Regular Updates
```bash
# Update dependencies
pip list --outdated
pip install --upgrade package_name

# Update requirements.txt
pip freeze > requirements.txt

# Commit updates
git add requirements.txt
git commit -m "Update: Upgrade dependencies to latest versions"
git push origin main
```

### Tagging Releases
```bash
# Create annotated tag
git tag -a v1.0.0 -m "Release version 1.0.0 - Initial public release"

# Push tag to GitHub
git push origin v1.0.0

# Create release on GitHub
gh release create v1.0.0 --title "v1.0.0 - Initial Release" --notes "First stable release"
```

### Syncing Forks (For Contributors)
```bash
# Add upstream remote
git remote add upstream https://github.com/Ishadowprince716/zomato-ml-clustering.git

# Fetch upstream changes
git fetch upstream

# Merge upstream/main into your main
git checkout main
git merge upstream/main

# Push to your fork
git push origin main
```

---

## 📊 Repository Statistics & Analytics

Enable on GitHub:
- **Insights** → Track commits, contributors, traffic
- **Actions** → Monitor CI/CD workflows
- **Security** → Dependabot alerts
- **Projects** → Kanban boards for task management

---

## 🎯 Best Practices

1. **Commit Often**: Small, focused commits
2. **Write Clear Messages**: Descriptive commit messages
3. **Use Branches**: Never commit directly to main
4. **Review PRs**: Code review before merging
5. **Keep Updated**: Regular dependency updates
6. **Document Changes**: Update CHANGELOG.md
7. **Tag Releases**: Version your releases properly
8. **Secure Secrets**: Never commit API keys

---

## 📞 Troubleshooting

### Common Issues

**Authentication Failed:**
```bash
# Use Personal Access Token instead of password
# Generate at: https://github.com/settings/tokens
# Use token as password when prompted
```

**Large File Warning:**
```bash
# Remove large files from history
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch path/to/large/file" \
  --prune-empty --tag-name-filter cat -- --all
```

**Merge Conflicts:**
```bash
# View conflicts
git status

# Resolve manually in files
# Then:
git add resolved_file.py
git commit -m "Fix: Resolve merge conflicts"
```

---

## ✅ Verification Checklist

After setup, verify:
- [ ] Repository is public/private as intended
- [ ] README displays correctly
- [ ] All files are committed
- [ ] .gitignore working (no unwanted files)
- [ ] Badges display correctly
- [ ] Topics added
- [ ] License visible
- [ ] Description added
- [ ] Website link (if deployed)
- [ ] Issues enabled
- [ ] Discussions enabled (optional)

---

**Your repository is now ready! 🎉**

Repository URL: https://github.com/Ishadowprince716/zomato-ml-clustering

Share it on:
- LinkedIn
- Twitter
- GeeksforGeeks Profile
- Portfolio Website
'''

with open('GIT_SETUP_GUIDE.md', 'w', encoding='utf-8') as f:
    f.write(git_guide)

print("✅ GIT_SETUP_GUIDE.md created successfully!")
print("\n" + "="*80)
print("📚 Complete Git Repository Package Ready!")
print("="*80)
