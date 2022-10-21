import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fullask-rest-framework",
    version="0.0.1",
    author="TGoddessna",
    author_email="twicegoddessana1229@gmail.com",
    description="A full-supported flask extension for build REST API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TGoddessana/fullask-rest-framework",
    packages=setuptools.find_packages(),
    python_requires='>=3.8',
    install_requires=[
        "flask",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
