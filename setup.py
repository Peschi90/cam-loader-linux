#!/usr/bin/env python3
"""
Setup script for CamLoader
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README file
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

# Read requirements
requirements_file = Path(__file__).parent / "requirements.txt"
if requirements_file.exists():
    with open(requirements_file, 'r') as f:
        requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]
else:
    requirements = [
        "Pillow>=8.0.0",
        "opencv-python>=4.5.0",
        "psutil>=5.8.0"
    ]

setup(
    name="camloader",
    version="0.0.0.1",
    author="Your Name",
    author_email="your.email@example.com",
    description="A GUI application for controlling V4L2 camera parameters",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/cam-loader-linux",
    
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Multimedia :: Video :: Capture",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: POSIX :: Linux",
    ],
    
    python_requires=">=3.8",
    install_requires=requirements,
    
    entry_points={
        "console_scripts": [
            "camloader=main:main",
        ],
    },
    
    include_package_data=True,
    package_data={
        "": ["*.json", "*.txt", "*.md"],
    },
    
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "black>=21.0.0",
            "flake8>=3.8.0",
            "pyinstaller>=6.0.0",
        ],
        "build": [
            "pyinstaller>=6.0.0",
            "wheel>=0.37.0",
            "build>=0.8.0",
        ],
    },
    
    keywords="camera v4l2 gui linux video parameters control",
)