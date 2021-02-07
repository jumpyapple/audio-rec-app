from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="rec_app",
    version="0.1.0",
    description="Audio Recording Application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
    ],
    author="Jumpyapple",
    author_email="70656949+jumpyapple@users.noreply.github.com",
    license="MIT",
    url="https://github.com/jumpyapple",
    python_requires=">=3.8",
    packages=["rec_app"],
    install_requires=[
        "click>=7.1.2",
        "flask>=1.1.2",
        "flask-cors>=3.0.10",
        "requests>=2.25.1",
    ],
    include_package_data=True,
    zip_safe=False,
)
