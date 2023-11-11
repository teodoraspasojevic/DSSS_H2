from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='math-quiz',
    version='0.1.0',
    author='Teodora Spasojevic',
    author_email='spasojevic.teodora@gmail.com',
    description='Math Quiz Implementation',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/teodoraspasojevic/DSSS_H2.git',
    packages=find_packages(),
    install_requires=[
    ],
    classifiers=[
        "Programming Language :: Python :: 3.7.16",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)