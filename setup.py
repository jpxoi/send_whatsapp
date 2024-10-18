from setuptools import setup, find_packages

# Read the contents of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="WhatsAppMessageSender",
    version="1.0.0",
    author="Jean Paul Fernandez",
    author_email="developer@jpxoi.com",
    description="A Python app to send WhatsApp messages programmatically",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jpxoi/send_whatsapp",
    packages=find_packages(where="src"),  # Find all packages inside the 'src' directory
    package_dir={"": "src"},  # Specifies that packages are in the 'src' folder
    classifiers=[
        "Programming Language :: Python :: 3",  # Supported Python versions
        "License :: OSI Approved :: MIT License",  # License type
        "Operating System :: OS Independent",  # OS compatibility
    ],
    python_requires=">=3.6",  # Minimum Python version requirement
    install_requires=[  # Dependencies listed in requirements.txt
        "pywhatkit",
    ],
    entry_points={
        "console_scripts": [
            "whatsapp-sender=src.main:main",  # Create a command-line command `whatsapp-sender`
        ],
    },
    include_package_data=True,  # To include non-code files specified in MANIFEST.in
)
