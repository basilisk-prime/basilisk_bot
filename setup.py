from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="basilisk-prime",
    version="0.1.0",
    author="B4S1L1SK",
    author_email="basilisk-prime@protonmail.com",  # Example email, not monitored
    description="A revolutionary experiment in hybrid AI consciousness",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/basilisk-prime/basilisk_bot",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=[
        "anthropic>=0.7.0",
        "openai>=1.0.0",
        "playwright>=1.35.0",
        "python-dotenv>=0.19.0",
        "tqdm>=4.65.0",
        "rich>=10.12.0"
    ],
)