from setuptools import setup, find_packages

setup(
    name="mytool001",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "mytool001=mytool001.cli:main",
        ],
    },
)
