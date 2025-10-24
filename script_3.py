
# Create setup.py for package installation
setup_content = '''"""
Setup configuration for Zomato Restaurant Clustering package
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="zomato-ml-clustering",
    version="1.0.0",
    author="Rahul Singh Kushwah",
    author_email="patelmrrahul199@gmail.com",
    description="Unsupervised ML project for Zomato restaurant clustering and sentiment analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ishadowprince716/zomato-ml-clustering",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=3.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
            "mypy>=0.950",
        ],
    },
    entry_points={
        "console_scripts": [
            "zomato-app=streamlit_app:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
'''

with open('setup.py', 'w', encoding='utf-8') as f:
    f.write(setup_content)

print("✅ setup.py created successfully!")
