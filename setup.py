#!/usr/bin/env python3

import os.path
from setuptools import setup, find_packages

setup(
    name='md5hash',
    version='0.0.6',
    packages=find_packages(),
    requires=['Python (>= 3.5)'],
    description='Fast and simple md5 hash generator for files and directories',
    long_description=(open('README.rst').read() if os.path.exists('README.rst') else ''),
    author='Val Saven',
    author_email='val.saven@gmail.com',
    url='https://github.com/valsaven/md5hash/',
    license='MIT License',
    keywords='md5',
)
