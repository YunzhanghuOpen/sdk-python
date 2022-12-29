#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (C) 云账户
# All rights reserved.

"""
Setup script for log service SDK.
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from src import __version__

requirements = [
    'requests>=2.19.1',
    'pycryptodome==3.10.1',
]

long_description = """
Python SDK for 云账户 
"""

packages = [
    'src',
    'src.base',
    'src.config',
    'src.model',
    'src.util',
]

setup(
    name='yzh-python-sdk',
    version=__version__,
    description='yunzhanghu service Python client SDK',
    author='yunzhanghu',
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    packages=packages,
    long_description=long_description,
)
