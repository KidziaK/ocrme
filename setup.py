from setuptools import setup, find_packages

setup(
    name="ocrme",
    version="0.1.0",
    description="A CLI tool to extract text and math formulas from a PDF and save it as Markdown.",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),  # Automatically find the `ocrme` package
    install_requires=[
        "click>=8.0.0",
        "pytesseract>=0.3.0",
        "pdf2image>=1.16.0",
        "pillow>=9.0.0"
    ],
    entry_points={
        "console_scripts": [
            "ocrme=ocrme.ocrme:ocrme"
        ]
    }
)
