import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wavelets",
    version='1.0',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wavelets/",
    packages=['wave_python'],
)