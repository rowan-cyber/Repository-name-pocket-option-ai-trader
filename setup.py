"""
Setup script for Pocket Option Telegram Bot
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pocket-option-telegram-bot",
    version="1.0.0",
    author="rowan-cyber",
    description="Telegram bot for automated binary options trading on Pocket Option",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rowan-cyber/Repository-name-pocket-option-ai-trader",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "python-telegram-bot>=20.0",
        "python-dotenv>=1.0.0",
        "requests>=2.28.0",
        "SQLAlchemy>=2.0.0",
    ],
)
