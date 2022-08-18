import setuptools

with open("README.md", "r", encoding="utf-8") as fhand:
    long_description = fhand.read()

setuptools.setup(
    name="repometrics",
    version="0.0.1",
    author="Liu Zheng",
    author_email="zheng@example.com",
    description=("An CLI Tool for Repo metrics."),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/liuzheng1990/python_packaging_demo",
    project_urls={
        "Bug Tracker": "https://github.com/liuzheng1990/python_packaging_demo/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests"],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "repometrics = repometrics.cli:main",
        ]
    }
)