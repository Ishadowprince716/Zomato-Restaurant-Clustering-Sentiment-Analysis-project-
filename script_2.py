
# Create CONTRIBUTING.md
contributing_content = '''# Contributing to Zomato Restaurant Clustering Project

Thank you for your interest in contributing to this project! This document provides guidelines and instructions for contributing.

## 🤝 How to Contribute

### Reporting Issues

If you find a bug or have a suggestion for improvement:

1. **Check existing issues** to avoid duplicates
2. **Create a new issue** with a clear title and description
3. **Include steps to reproduce** (for bugs)
4. **Add relevant labels** (bug, enhancement, documentation, etc.)

### Submitting Changes

1. **Fork the repository**
   ```bash
   git clone https://github.com/your-username/zomato-ml-clustering.git
   cd zomato-ml-clustering
   ```

2. **Create a new branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Write clean, readable code
   - Follow existing code style
   - Add comments where necessary
   - Update documentation if needed

4. **Test your changes**
   - Ensure all existing tests pass
   - Add new tests for new features
   - Run the Streamlit app to verify functionality

5. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add: brief description of your changes"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your branch
   - Provide a clear description of changes
   - Link related issues

## 📝 Coding Standards

### Python Code Style

- Follow **PEP 8** style guide
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions focused and modular
- Maximum line length: 100 characters

Example:
```python
def calculate_silhouette_score(X, labels):
    """
    Calculate silhouette score for clustering evaluation.
    
    Parameters:
    - X: Feature matrix
    - labels: Cluster labels
    
    Returns:
    - float: Silhouette score
    """
    from sklearn.metrics import silhouette_score
    return silhouette_score(X, labels)
```

### Commit Message Format

Use clear, descriptive commit messages:

- **Add:** New feature or file
- **Update:** Modify existing functionality
- **Fix:** Bug fix
- **Remove:** Delete code or files
- **Refactor:** Code restructuring without changing functionality
- **Docs:** Documentation changes

Examples:
```
Add: K-Means clustering visualization
Fix: Handle missing values in cost column
Update: Improve sentiment analysis accuracy
Docs: Add installation instructions
```

## 🧪 Testing

Before submitting a pull request:

1. **Test the Streamlit app**
   ```bash
   streamlit run streamlit_app.py
   ```

2. **Test Python modules**
   ```python
   python data_processing.py
   python clustering.py
   python sentiment_analysis.py
   ```

3. **Check for errors** in all tabs and features

## 📚 Documentation

When adding new features:

- Update README.md if necessary
- Add docstrings to new functions
- Update requirements.txt for new dependencies
- Add comments for complex logic

## 🐛 Bug Reports

A good bug report should include:

- **Clear title** describing the issue
- **Steps to reproduce** the bug
- **Expected behavior** vs **actual behavior**
- **Screenshots** (if applicable)
- **Environment details** (OS, Python version, package versions)
- **Error messages** or stack traces

## 💡 Feature Requests

When suggesting new features:

- **Describe the feature** clearly
- **Explain the use case** and benefits
- **Provide examples** of how it would work
- **Consider impact** on existing functionality

## 🎯 Areas for Contribution

We welcome contributions in these areas:

### Features
- Additional clustering algorithms
- More sentiment analysis methods
- Advanced visualizations
- Restaurant recommendation system
- User authentication
- Database integration

### Improvements
- Performance optimization
- Error handling
- Code refactoring
- UI/UX enhancements
- Mobile responsiveness

### Documentation
- Tutorial notebooks
- API documentation
- Video guides
- Code examples
- Translation to other languages

### Testing
- Unit tests
- Integration tests
- Performance benchmarks

## 🔄 Review Process

1. **Code review** by maintainers
2. **Testing** on different environments
3. **Feedback** and requested changes
4. **Approval** and merge

## 📞 Getting Help

If you need help:

- **Open an issue** for questions
- **Check documentation** in README.md
- **Review existing code** for examples

## 🌟 Recognition

Contributors will be:

- Listed in CONTRIBUTORS.md
- Mentioned in release notes
- Acknowledged in documentation

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for helping improve this project! 🙏
'''

with open('CONTRIBUTING.md', 'w', encoding='utf-8') as f:
    f.write(contributing_content)

print("✅ CONTRIBUTING.md created successfully!")
