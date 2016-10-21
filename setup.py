#!/usr/bin/env python
"""Mocky installer."""
from setuptools import find_packages, setup

setup(
    name='mocky',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    entry_points={'console_scripts': ['mocky = mocky.__main__:main'], }, )
