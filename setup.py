"""Setup script for dope"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from codecs import open
import sys

if sys.version_info[:3] < (3, 0, 0):
    print("Requires Python 3 to run.")
    sys.exit(1)

with open("README.md", encoding="utf-8") as file:
    readme = file.read()


# This call to setup() does all the work
setup(
    name="dope",
    version="1.0.0",
    description="Read the latest Real Python tutorials",
    # long_description=readme,
    # long_description_content_type="text/markdown",
    url="https://github.com/aditya612/dope",
    author="Aditya Agarwal",
    author_email="naveenagarwal123451@gmail.com",
    license="MIT",
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
        "Topic :: Software Development :: Debuggers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python"
    ],
    packages=["dope"],
    include_package_data=True,

    entry_points={"console_scripts": ["dope = dope.dope:main"]},
    install_requires=["BeautifulSoup4", "requests",
                      "urllib3", "tkinter", "numpy", "pandas"],
    requires=["BeautifulSoup4", "requests",
              "urllib3", "tkinter", "numpy", "pandas"],
)
