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
from yzh_py import __version__

requirements = [
    'requests>=2.19.1',
    'pycryptodome==3.10.1',
]

long_description = """
云账户综合服务平台官方 SDK For Python，基于 Python3 开发，支持 Python3.0 及以上版本。
Copyright © 2013 - 2023 云账户技术（天津）有限公司 版权所有
云账户开放平台：https://open.yunzhanghu.com

"""

packages = [
    'yzh_py',
    'yzh_py.client',
    'yzh_py.client.api',
    'yzh_py.client.api.model',
]

setup(
    name='yzh_py',
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
