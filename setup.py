import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "mast.plugins",
    version = "2.2.0",
    author = "Clifford Bressette",
    author_email = "cliffordbressette@mcindi.com",
    description = ("A set of utilities to help with creating plugins for MAST."),
    license = "GPLv3",
    keywords = "DataPower plugin",
    url = "http://github.com/mcindi/mast.plugins",
    namespace_packages=["mast"],
    packages=['mast', 'mast.plugins'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
        "License :: OSI Approved :: GPLv3",
    ],
)
