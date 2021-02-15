import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="soft7-pkg-quaat", # Replace with your own username
    version="0.0.1",
    author="Quaat",
    author_email="nims@quaat.com",
    description="SOFT7 semantic interoperability framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/quaat/soft7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.7',
)
