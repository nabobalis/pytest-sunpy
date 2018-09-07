#!/usr/bin/env python
# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- encoding: utf-8 -*-

import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext
from setuptools import setup, find_packages


def readme():
    with open('README.rst') as ff:
        return ff.read()


setup(
    name='pytest-sunpy',
    version='1.0.0',
    license='BSD',
    description='Meta-package containing dependencies for testing SunPy',
    long_description=readme(),
    author='The SunPy Developers',
    url='https://sunpy.org',
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
    ],
    python_requires='>=3.6',
    install_requires=[
        'pytest-astropy',
        'hypothesis',
        'mock',
        'pytest-cov',
        'pytest-mock',
        'pytest-rerunfailures'
    ]
)
