import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nqueens", # Replace with your own username
    version="1.0.3",
    author="Athul Mathew Konoor",
    author_email="athulmathewkonoor@gmail.com",
    description="A package to get nqueens.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/toshihiroryuu/nqueens---PyPI-Package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
       "gtts >= 2.2.0"
   ],
    python_requires='>=3.6',
)