#!/usr/bin/env python
"""Mocky installer."""
from setuptools import find_packages, setup

setup(
    name='mocky',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=['coloredlogs'],
    entry_points={
        'console_scripts': [
            'mocky = mocky.__main__:main',
            'rm = mocky.__main__:debug',
            'cp = mocky.__main__:info',
            'install = mocky.__main__:error',
            'gcc = mocky.__main__:critical',
        ],
    }, )
