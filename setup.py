import os
from setuptools import setup

setup(
    name = "datatransporttools",
    version = "0.1.1",
    author = "Zakir Durumeric",
    author_email = "zakird@gmail.com",
    description = "A light-weight python framework for transforming datasets between common sources/destinations.",
    license = "BSD",
    keywords = "python data conversion data transfer",
    packages=['datatransporttools'],
    long_description="long description",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: BSD License",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Topic :: Database",
        "Topic :: Text Processing"
    ],
)
