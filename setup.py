from setuptools import setup, find_packages

setup(
    name="calculatorz",
    version="0.1.0",
    author="frozin01",
    author_email="fauzanrozin01@gmail.com",
    description="Calculator python module.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/frozin01/calculatorz",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10.11',
)
