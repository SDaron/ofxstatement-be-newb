#!/usr/bin/python3
"""Setup
"""
from setuptools import find_packages
from distutils.core import setup

version = "0.0.3"

with open("README.rst") as f:
    long_description = f.read()

setup(
    name="ofxstatement-newb",
    version=version,
    author="Simon Daron",
    #author_email="",
    url="https://github.com/SDaron/ofxstatement-be-newb",
    description=("NewB plugin for ofxstatement"),
    long_description=long_description,
    license="GPLv3",
    keywords=["ofx", "banking", "statement"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Natural Language :: English",
        "Topic :: Office/Business :: Financial :: Accounting",
        "Topic :: Utilities",
        "Environment :: Console",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    packages=find_packages("src"),
    package_dir={"": "src"},
    namespace_packages=["ofxstatement", "ofxstatement.plugins"],
    entry_points={
        "ofxstatement": ["newb = ofxstatement.plugins.newb:NewBPlugin"]
    },
    install_requires=["ofxstatement"],
    include_package_data=True,
    zip_safe=True,
)
