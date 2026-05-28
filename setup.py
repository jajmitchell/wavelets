import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wavelets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ct6502/wavelets.git",
    packages=setuptools.find_packages(),
)