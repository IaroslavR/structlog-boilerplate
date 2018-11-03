from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="structlog-boilerplate",
    version="0.2",
    description="Simple wrapper for CLI script which can use all advantages of structlog",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
    ],
    url="https://github.com/IaroslavR/structlog-boilerplate",
    author="Iaroslav Russkikh",
    author_email="iarruss@ya.ru",
    license="MIT",
    packages=["structlog_boilerplate"],
    install_requires=["colorama", "Pigments", "structlog"],
    include_package_data=True,
    zip_safe=False,
)
