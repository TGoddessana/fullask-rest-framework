from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="fullask-rest-framework",
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        "Flask >= 2.0",
    ],
)
